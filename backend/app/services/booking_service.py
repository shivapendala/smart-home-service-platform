from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.booking import Booking, BookingStatus
from app.models.service import Service, Category
from app.models.user import User, UserRole
from app.schemas.booking import BookingCreate


class BookingService:

    @staticmethod
    def create_booking(db: Session, customer_id: int, booking_in: BookingCreate) -> Booking:
        """Create a new service booking and attempt smart auto-assignment of technician."""
        service = db.query(Service).filter(Service.id == booking_in.service_id).first()
        if not service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Service item not found."
            )
        if not service.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This service is currently unavailable."
            )

        # Smart technician auto-assignment search
        category = db.query(Category).filter(Category.id == service.category_id).first()
        cat_name = category.name if category else ""

        # Find active technicians matching category specialization
        assigned_tech = db.query(User).filter(
            User.role == UserRole.TECHNICIAN,
            User.is_active == True,
            User.specialization.ilike(f"%{cat_name[:6]}%")
        ).first()

        if not assigned_tech:
            # Fallback to any active technician
            assigned_tech = db.query(User).filter(
                User.role == UserRole.TECHNICIAN,
                User.is_active == True
            ).first()

        initial_status = BookingStatus.ASSIGNED if assigned_tech else BookingStatus.PENDING

        booking = Booking(
            customer_id=customer_id,
            technician_id=assigned_tech.id if assigned_tech else None,
            service_id=service.id,
            scheduled_date=booking_in.scheduled_date,
            scheduled_time_slot=booking_in.scheduled_time_slot,
            address_line=booking_in.address_line,
            city=booking_in.city,
            zip_code=booking_in.zip_code,
            notes=booking_in.notes,
            status=initial_status,
            total_amount=service.base_price
        )
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking

    @staticmethod
    def get_booking_by_id(db: Session, booking_id: int) -> Booking:
        """Fetch single booking by ID."""
        booking = db.query(Booking).filter(Booking.id == booking_id).first()
        if not booking:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Booking not found."
            )
        return booking

    @staticmethod
    def get_user_bookings(db: Session, user: User) -> List[Booking]:
        """Fetch bookings relevant to user role."""
        if user.role == UserRole.ADMIN:
            return db.query(Booking).order_by(Booking.created_at.desc()).all()
        elif user.role == UserRole.TECHNICIAN:
            return db.query(Booking).filter(
                (Booking.technician_id == user.id) | (Booking.status == BookingStatus.PENDING)
            ).order_by(Booking.created_at.desc()).all()
        else:
            return db.query(Booking).filter(
                Booking.customer_id == user.id
            ).order_by(Booking.created_at.desc()).all()

    @staticmethod
    def update_booking_status(db: Session, booking_id: int, new_status: BookingStatus, current_user: User) -> Booking:
        """Transition booking status with permission checks."""
        booking = BookingService.get_booking_by_id(db, booking_id)

        # Validate authorization
        if current_user.role == UserRole.CUSTOMER and booking.customer_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied.")
        if current_user.role == UserRole.TECHNICIAN and booking.technician_id not in (current_user.id, None):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied.")

        # If technician accepts a pending booking
        if current_user.role == UserRole.TECHNICIAN and booking.technician_id is None:
            booking.technician_id = current_user.id

        booking.status = new_status
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking

    @staticmethod
    def assign_technician(db: Session, booking_id: int, technician_id: int) -> Booking:
        """Manually assign technician to booking (Admin endpoint)."""
        booking = BookingService.get_booking_by_id(db, booking_id)
        tech = db.query(User).filter(User.id == technician_id, User.role == UserRole.TECHNICIAN).first()
        if not tech:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Technician not found."
            )
        booking.technician_id = tech.id
        booking.status = BookingStatus.ASSIGNED
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking
