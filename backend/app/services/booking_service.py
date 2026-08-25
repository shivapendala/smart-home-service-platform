from datetime import date, datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.booking import Booking, BookingStatus, Address, BookingStatusHistory, ALLOWED_TRANSITIONS
from app.models.service import Service
from app.models.user import User, UserRole
from app.schemas.booking import BookingCreate, AddressCreate


class BookingService:

    @staticmethod
    def get_or_create_address(db: Session, customer_id: int, address_id: Optional[int], new_address: Optional[AddressCreate]) -> Address:
        """Resolve existing address or create new address for customer."""
        if address_id:
            addr = db.query(Address).filter(Address.id == address_id, Address.user_id == customer_id).first()
            if not addr:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Address not found or does not belong to this customer."
                )
            return addr
        
        if new_address:
            addr = Address(
                user_id=customer_id,
                street_address=new_address.street_address,
                city=new_address.city,
                state=new_address.state,
                zip_code=new_address.zip_code,
                is_default=new_address.is_default
            )
            db.add(addr)
            db.flush()
            return addr
            
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Either address_id or new_address must be provided."
        )

    @classmethod
    def create_booking(cls, db: Session, customer_id: int, booking_in: BookingCreate) -> Booking:
        """Customer workflow: Validate service, resolve address, calculate price, and create booking."""
        service = db.query(Service).filter(Service.id == booking_in.service_id).first()
        if not service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invalid service ID. Service not found."
            )
        if not service.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This service is currently inactive."
            )

        if booking_in.scheduled_date < date.today():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Scheduled date cannot be in the past."
            )

        address = cls.get_or_create_address(db, customer_id, booking_in.address_id, booking_in.new_address)

        booking = Booking(
            customer_id=customer_id,
            service_id=service.id,
            address_id=address.id,
            problem_description=booking_in.problem_description,
            scheduled_date=booking_in.scheduled_date,
            scheduled_time=booking_in.scheduled_time,
            status=BookingStatus.PENDING,
            estimated_price=service.base_price,
            final_price=service.base_price
        )
        db.add(booking)
        db.flush()

        # Record initial status history
        history = BookingStatusHistory(
            booking_id=booking.id,
            old_status="NONE",
            new_status=BookingStatus.PENDING.value,
            changed_by_user_id=customer_id,
            notes="Booking created by customer"
        )
        db.add(history)

        db.commit()
        db.refresh(booking)
        return booking

    @staticmethod
    def get_booking_by_id(db: Session, booking_id: int, current_user: Optional[User] = None) -> Booking:
        """Fetch single booking details with strict customer scoping."""
        booking = db.query(Booking).filter(Booking.id == booking_id).first()
        if not booking:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Booking not found."
            )
        
        # Customer scoping: customer can only view their own booking
        if current_user and current_user.role == UserRole.CUSTOMER and booking.customer_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied. Customers can only view their own bookings."
            )
            
        return booking

    @classmethod
    def assign_technician(cls, db: Session, booking_id: int, technician_id: int, admin_user: Optional[User] = None) -> Booking:
        """Admin action: Assign a technician to a booking and transition to ASSIGNED status."""
        booking = cls.get_booking_by_id(db, booking_id, admin_user)
        tech = db.query(User).filter(User.id == technician_id, User.role == UserRole.TECHNICIAN).first()
        if not tech:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Technician not found or user is not a technician."
            )

        old_status = booking.status
        booking.technician_id = tech.id
        booking.status = BookingStatus.ASSIGNED

        history = BookingStatusHistory(
            booking_id=booking.id,
            old_status=old_status.value,
            new_status=BookingStatus.ASSIGNED.value,
            changed_by_user_id=admin_user.id if admin_user else None,
            notes=f"Assigned technician {tech.full_name} (ID: {tech.id})"
        )
        db.add(history)
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking

    @staticmethod
    def get_customer_bookings(db: Session, customer_id: int) -> List[Booking]:
        """Fetch all bookings belonging exclusively to the customer."""
        return db.query(Booking).filter(
            Booking.customer_id == customer_id
        ).order_by(Booking.created_at.desc()).all()

    @classmethod
    def cancel_booking(cls, db: Session, booking_id: int, current_user: User, notes: Optional[str] = None) -> Booking:
        """Customer workflow: Cancel a booking with transition validation and history record."""
        booking = cls.get_booking_by_id(db, booking_id, current_user)

        if current_user.role == UserRole.CUSTOMER and booking.customer_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You cannot cancel another customer's booking."
            )

        if booking.status in (BookingStatus.COMPLETED, BookingStatus.CANCELLED):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Cannot cancel a booking in status {booking.status}."
            )

        old_status = booking.status
        booking.status = BookingStatus.CANCELLED

        # Log status transition
        history = BookingStatusHistory(
            booking_id=booking.id,
            old_status=old_status.value,
            new_status=BookingStatus.CANCELLED.value,
            changed_by_user_id=current_user.id,
            notes=notes or "Cancelled by customer"
        )
        db.add(history)
        db.add(booking)

        db.commit()
        db.refresh(booking)
        return booking

    @classmethod
    def update_status(cls, db: Session, booking_id: int, new_status: BookingStatus, current_user: User, notes: Optional[str] = None) -> Booking:
        """Strict status-transition validation state machine."""
        booking = cls.get_booking_by_id(db, booking_id, current_user)
        old_status = booking.status

        if new_status not in ALLOWED_TRANSITIONS.get(old_status, set()):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid status transition from {old_status.value} to {new_status.value}."
            )

        booking.status = new_status

        # Record history
        history = BookingStatusHistory(
            booking_id=booking.id,
            old_status=old_status.value,
            new_status=new_status.value,
            changed_by_user_id=current_user.id,
            notes=notes or f"Status updated to {new_status.value}"
        )
        db.add(history)
        db.add(booking)

        db.commit()
        db.refresh(booking)
        return booking
