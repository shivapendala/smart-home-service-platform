from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.notification import Notification
from app.models.booking import Booking, BookingStatus
from app.models.user import User
from app.models.payment import Payment
from app.models.review import Complaint


class NotificationService:

    @staticmethod
    def send_notification(db: Session, user_id: int, title: str, message: str, notification_type: str = "INFO") -> Notification:
        """Central notification dispatcher. Creates in-app notification record and provides hook for future Email/SMS providers."""
        notif = Notification(
            user_id=user_id,
            title=title,
            message=message,
            type=notification_type,
            is_read=False
        )
        db.add(notif)
        # Flush to generate ID without breaking parent transaction
        db.flush()
        return notif

    # --- Domain Event Triggers ---

    @classmethod
    def notify_booking_created(cls, db: Session, booking: Booking):
        """Event: Booking created by customer."""
        cls.send_notification(
            db=db,
            user_id=booking.customer_id,
            title="Booking Confirmation 📅",
            message=f"Your booking (#{booking.id}) for service has been successfully submitted and is PENDING dispatch.",
            notification_type="BOOKING_CREATED"
        )

    @classmethod
    def notify_technician_assigned(cls, db: Session, booking: Booking, technician_user: User):
        """Event: Admin assigns technician to booking."""
        # Notify Customer
        cls.send_notification(
            db=db,
            user_id=booking.customer_id,
            title="Technician Assigned 👨‍🔧",
            message=f"Technician {technician_user.full_name} has been assigned to your booking (#{booking.id}).",
            notification_type="TECHNICIAN_ASSIGNED"
        )
        # Notify Technician
        cls.send_notification(
            db=db,
            user_id=technician_user.id,
            title="New Job Assigned 🔧",
            message=f"You have been assigned to job #{booking.id} scheduled for {booking.scheduled_date}.",
            notification_type="JOB_DISPATCH"
        )

    @classmethod
    def notify_job_status_change(cls, db: Session, booking: Booking, action: str):
        """Event: Technician accepts, arrives, starts, or completes service."""
        action_messages = {
            "ACCEPT": ("Job Accepted", f"Your technician has accepted booking #{booking.id}."),
            "ON_THE_WAY": ("Technician En Route 🚚", f"Technician is on the way to your address for booking #{booking.id}."),
            "START": ("Service Started 🛠️", f"Technician has started working on booking #{booking.id}."),
            "COMPLETE": ("Service Completed 🎉", f"Service for booking #{booking.id} has been marked COMPLETED. Please review your service.")
        }
        if action in action_messages:
            title, msg = action_messages[action]
            cls.send_notification(
                db=db,
                user_id=booking.customer_id,
                title=title,
                message=msg,
                notification_type=f"STATUS_{action}"
            )

    @classmethod
    def notify_payment_completed(cls, db: Session, payment: Payment):
        """Event: Customer payment completes."""
        cls.send_notification(
            db=db,
            user_id=payment.customer_id,
            title="Payment Received 💳",
            message=f"Payment of ${payment.amount:.2f} for booking #{payment.booking_id} was successful. Transaction ID: {payment.transaction_id}.",
            notification_type="PAYMENT_SUCCESS"
        )

    @classmethod
    def notify_complaint_updated(cls, db: Session, complaint: Complaint):
        """Event: Admin updates complaint status or resolution notes."""
        cls.send_notification(
            db=db,
            user_id=complaint.customer_id,
            title=f"Complaint Update ({complaint.status.value}) 🎫",
            message=f"Your complaint regarding booking #{complaint.booking_id} status is now {complaint.status.value}. Notes: {complaint.resolution_notes or 'Under review'}.",
            notification_type="COMPLAINT_UPDATE"
        )

    # --- User Notification Management ---

    @staticmethod
    def get_user_notifications(db: Session, user_id: int) -> dict:
        """Fetch notifications and unread count for user."""
        notifications = db.query(Notification).filter(
            Notification.user_id == user_id
        ).order_by(Notification.created_at.desc()).all()

        unread_count = sum(1 for n in notifications if not n.is_read)
        return {
            "unread_count": unread_count,
            "notifications": notifications
        }

    @staticmethod
    def mark_as_read(db: Session, notification_id: int, current_user: User) -> Notification:
        """Mark single notification as read (User isolation check)."""
        notif = db.query(Notification).filter(Notification.id == notification_id).first()
        if not notif:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found.")

        if notif.user_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied. Cannot modify another user's notifications.")

        notif.is_read = True
        db.add(notif)
        db.commit()
        db.refresh(notif)
        return notif

    @staticmethod
    def mark_all_as_read(db: Session, user_id: int) -> int:
        """Mark all unread notifications for user as read."""
        unread = db.query(Notification).filter(Notification.user_id == user_id, Notification.is_read == False).all()
        for n in unread:
            n.is_read = True
            db.add(n)
        db.commit()
        return len(unread)
