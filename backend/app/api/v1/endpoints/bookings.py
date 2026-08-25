from typing import List, Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.booking import (
    BookingCreate, BookingResponse, BookingStatusUpdate, AddressCreate, AddressResponse
)
from app.services.booking_service import BookingService
from app.models.user import User, UserRole
from app.api.deps import get_current_user, require_roles

router = APIRouter()


# --- Address API ---

@router.post("/addresses", response_model=AddressResponse, status_code=status.HTTP_201_CREATED)
def create_customer_address(
    address_in: AddressCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.CUSTOMER]))
):
    """Create a new service delivery address for customer."""
    return BookingService.get_or_create_address(
        db=db, customer_id=current_user.id, address_id=None, new_address=address_in
    )


# --- Booking API (/api/bookings and /api/v1/bookings) ---

@router.post("", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
@router.post("/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
def create_booking(
    booking_in: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.CUSTOMER]))
):
    """Customer workflow: Create a new service booking with address, date, and problem description."""
    return BookingService.create_booking(
        db=db, customer_id=current_user.id, booking_in=booking_in
    )


@router.get("", response_model=List[BookingResponse])
@router.get("/", response_model=List[BookingResponse])
@router.get("/my", response_model=List[BookingResponse])
def list_customer_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Fetch bookings scoped strictly to the current customer."""
    return BookingService.get_customer_bookings(db=db, customer_id=current_user.id)


@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking_details(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Fetch details for a single booking (Strict Customer ownership validation)."""
    return BookingService.get_booking_by_id(db=db, booking_id=booking_id, current_user=current_user)


@router.put("/{booking_id}/cancel", response_model=BookingResponse)
@router.patch("/{booking_id}/cancel", response_model=BookingResponse)
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Customer workflow: Cancel an existing booking."""
    return BookingService.cancel_booking(db=db, booking_id=booking_id, current_user=current_user)


@router.patch("/{booking_id}/status", response_model=BookingResponse)
def update_booking_status(
    booking_id: int,
    status_in: BookingStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Transition booking status with strict state-machine validation."""
    return BookingService.update_status(
        db=db, booking_id=booking_id, new_status=status_in.status, current_user=current_user, notes=status_in.notes
    )
