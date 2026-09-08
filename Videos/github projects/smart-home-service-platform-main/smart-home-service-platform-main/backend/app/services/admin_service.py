from datetime import datetime, date
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException, status
from app.models.user import User, UserRole
from app.models.booking import Booking, BookingStatus
from app.models.payment import Payment, PaymentStatus
from app.models.review import Review, Complaint, ComplaintStatus
from app.schemas.admin import AdminDashboardStats, PaymentCreate, ReviewCreate, ComplaintCreate, ComplaintUpdate
from app.core.payment import get_payment_provider


class AdminService:

    @staticmethod
    def get_dashboard_stats(db: Session) -> AdminDashboardStats:
        """Calculate real-time platform metrics and financial revenue summary."""
        total_customers = db.query(User).filter(User.role == UserRole.CUSTOMER).count()
        total_technicians = db.query(User).filter(User.role == UserRole.TECHNICIAN).count()

        today = date.today()
        todays_bookings = db.query(Booking).filter(Booking.scheduled_date == today).count()

        pending_bookings = db.query(Booking).filter(Booking.status == BookingStatus.PENDING).count()
        active_bookings = db.query(Booking).filter(
            Booking.status.in_([BookingStatus.ASSIGNED, BookingStatus.ACCEPTED, BookingStatus.ON_THE_WAY, BookingStatus.IN_PROGRESS])
        ).count()
        completed_services = db.query(Booking).filter(Booking.status == BookingStatus.COMPLETED).count()
        cancelled_services = db.query(Booking).filter(Booking.status == BookingStatus.CANCELLED).count()

        revenue_res = db.query(func.sum(Payment.amount)).filter(Payment.status == PaymentStatus.PAID).scalar()
        revenue_summary = float(revenue_res or 0.0)

        return AdminDashboardStats(
            total_customers=total_customers,
            total_technicians=total_technicians,
            todays_bookings=todays_bookings,
            pending_bookings=pending_bookings,
            active_bookings=active_bookings,
            completed_services=completed_services,
            cancelled_services=cancelled_services,
            revenue_summary=revenue_summary
        )

    # --- Payments ---

    @staticmethod
    def process_payment(db: Session, payment_in: PaymentCreate, customer: User) -> Payment:
        """Process booking payment via PaymentProvider abstraction."""
        booking = db.query(Booking).filter(Booking.id == payment_in.booking_id).first()
        if not booking:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")

        if customer.role == UserRole.CUSTOMER and booking.customer_id != customer.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied.")

        existing_payment = db.query(Payment).filter(Payment.booking_id == booking.id, Payment.status == PaymentStatus.PAID).first()
        if existing_payment:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Payment already completed for this booking.")

        provider = get_payment_provider()
        res = provider.process_payment(amount=payment_in.amount, currency="USD", payment_method=payment_in.payment_method)

        payment = Payment(
            booking_id=booking.id,
            customer_id=customer.id,
            amount=payment_in.amount,
            currency="USD",
            payment_method=payment_in.payment_method,
            status=PaymentStatus.PAID if res["success"] else PaymentStatus.FAILED,
            transaction_id=res["transaction_id"]
        )
        db.add(payment)
        db.flush()

        if payment.status == PaymentStatus.PAID:
            from app.services.notification_service import NotificationService
            NotificationService.notify_payment_completed(db, payment)

        db.commit()
        db.refresh(payment)
        return payment

    @staticmethod
    def refund_payment(db: Session, payment_id: int, admin: User) -> Payment:
        """Process refund for paid transaction (Admin only)."""
        payment = db.query(Payment).filter(Payment.id == payment_id).first()
        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment record not found.")

        if payment.status != PaymentStatus.PAID:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Cannot refund payment in status {payment.status.value}.")

        provider = get_payment_provider()
        res = provider.refund_payment(transaction_id=payment.transaction_id, amount=payment.amount)

        payment.status = PaymentStatus.REFUNDED
        db.add(payment)
        db.commit()
        db.refresh(payment)
        return payment

    @staticmethod
    def list_payments(db: Session) -> List[Payment]:
        return db.query(Payment).order_by(Payment.created_at.desc()).all()

    # --- Reviews ---

    @staticmethod
    def create_review(db: Session, review_in: ReviewCreate, customer: User) -> Review:
        """Create customer review for COMPLETED booking. Blocks duplicate reviews."""
        booking = db.query(Booking).filter(Booking.id == review_in.booking_id).first()
        if not booking:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")

        if booking.customer_id != customer.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only review your own bookings.")

        if booking.status != BookingStatus.COMPLETED:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Reviews can only be submitted after the service is COMPLETED.")

        existing_review = db.query(Review).filter(Review.booking_id == booking.id).first()
        if existing_review:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You have already submitted a review for this booking.")

        review = Review(
            booking_id=booking.id,
            customer_id=customer.id,
            technician_id=booking.technician_id,
            rating=review_in.rating,
            comment=review_in.comment
        )
        db.add(review)
        db.commit()
        db.refresh(review)
        return review

    @staticmethod
    def list_reviews(db: Session) -> List[Review]:
        return db.query(Review).order_by(Review.created_at.desc()).all()

    # --- Complaints ---

    @staticmethod
    def create_complaint(db: Session, complaint_in: ComplaintCreate, customer: User) -> Complaint:
        """Customer files complaint regarding booking."""
        booking = db.query(Booking).filter(Booking.id == complaint_in.booking_id).first()
        if not booking:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")

        if booking.customer_id != customer.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only file complaints for your own bookings.")

        complaint = Complaint(
            booking_id=booking.id,
            customer_id=customer.id,
            subject=complaint_in.subject,
            description=complaint_in.description,
            status=ComplaintStatus.OPEN
        )
        db.add(complaint)
        db.commit()
        db.refresh(complaint)
        return complaint

    @staticmethod
    def list_complaints(db: Session) -> List[Complaint]:
        return db.query(Complaint).order_by(Complaint.created_at.desc()).all()

    @staticmethod
    def update_complaint(db: Session, complaint_id: int, complaint_in: ComplaintUpdate, admin: User) -> Complaint:
        """Admin views, assigns, updates status, and resolves complaint."""
        complaint = db.query(Complaint).filter(Complaint.id == complaint_id).first()
        if not complaint:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Complaint record not found.")

        if complaint_in.status:
            complaint.status = complaint_in.status
        if complaint_in.assigned_to_admin_id:
            complaint.assigned_to_admin_id = complaint_in.assigned_to_admin_id
        else:
            complaint.assigned_to_admin_id = admin.id
        if complaint_in.resolution_notes:
            complaint.resolution_notes = complaint_in.resolution_notes

        db.add(complaint)

        # Trigger notification
        from app.services.notification_service import NotificationService
        NotificationService.notify_complaint_updated(db, complaint)

        db.commit()
        db.refresh(complaint)
        return complaint
