from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.booking import (
    BookingCreate, BookingResponse, BookingStatusUpdate, AssignTechnicianPayload
)
from app.services.booking_service import BookingService
from app.models.user import User, UserRole
from app.api.deps import get_current_user, require_roles

router = APIRouter()


@router.post("/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
def create_booking(
    booking_in: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.CUSTOMER]))
):
    """Create a new service booking (Customer only)."""
    return BookingService.create_booking(
        db=db, customer_id=current_user.id, booking_in=booking_in
    )


@router.get("/my", response_model=List[BookingResponse])
def list_my_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Fetch bookings relevant to currently authenticated user."""
    return BookingService.get_user_bookings(db=db, user=current_user)


@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Fetch single booking details."""
    return BookingService.get_booking_by_id(db=db, booking_id=booking_id)


@router.patch("/{booking_id}/status", response_model=BookingResponse)
def update_booking_status(
    booking_id: int,
    status_in: BookingStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update status of booking (Technician / Customer / Admin)."""
    return BookingService.update_booking_status(
        db=db, booking_id=booking_id, new_status=status_in.status, current_user=current_user
    )


@router.patch(
    "/{booking_id}/assign",
    response_model=BookingResponse,
    dependencies=[Depends(require_roles([UserRole.ADMIN]))]
)
def assign_technician(
    booking_id: int,
    payload: AssignTechnicianPayload,
    db: Session = Depends(get_db)
):
    """Manually assign/re-assign technician to booking (Admin only)."""
    return BookingService.assign_technician(
        db=db, booking_id=booking_id, technician_id=payload.technician_id
    )
