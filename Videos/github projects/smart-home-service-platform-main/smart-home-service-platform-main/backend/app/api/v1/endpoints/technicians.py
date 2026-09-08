from typing import List, Optional
from fastapi import APIRouter, Depends, status, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.technician import (
    TechnicianProfileResponse, TechnicianAvailabilityUpdate,
    ServicePhotoResponse, ServiceNoteCreate, ServiceNoteResponse
)
from app.schemas.booking import BookingResponse
from app.models.technician import PhotoType
from app.models.user import User, UserRole
from app.services.technician_service import TechnicianService
from app.services.booking_service import BookingService
from app.api.deps import get_current_user, require_roles

router = APIRouter()


@router.get("/dashboard")
def get_technician_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.TECHNICIAN]))
):
    """Retrieve technician dashboard metrics & job queues."""
    return TechnicianService.get_technician_jobs(db=db, technician_id=current_user.id)


@router.patch("/availability", response_model=TechnicianProfileResponse)
def update_availability(
    payload: TechnicianAvailabilityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.TECHNICIAN]))
):
    """Toggle technician online availability status."""
    return TechnicianService.update_availability(db=db, user=current_user, is_available=payload.is_available)


@router.post("/jobs/{booking_id}/action", response_model=BookingResponse)
def execute_job_action(
    booking_id: int,
    action: str = Form(..., description="Action: ACCEPT, REJECT, ON_THE_WAY, START, COMPLETE"),
    notes: Optional[str] = Form(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.TECHNICIAN]))
):
    """Execute technician workflow state transition with security assignment check."""
    return TechnicianService.execute_job_action(
        db=db, booking_id=booking_id, action=action, technician=current_user, notes=notes
    )


@router.post("/jobs/{booking_id}/notes", response_model=ServiceNoteResponse, status_code=status.HTTP_201_CREATED)
def add_service_note(
    booking_id: int,
    note_in: ServiceNoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Add service diagnostic or job progress note."""
    return TechnicianService.add_service_note(
        db=db, booking_id=booking_id, note_in=note_in, author=current_user
    )


@router.post("/jobs/{booking_id}/photos", response_model=ServicePhotoResponse, status_code=status.HTTP_201_CREATED)
async def upload_service_photo(
    booking_id: int,
    photo_type: PhotoType = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Upload validated before/after service photo to local storage."""
    return await TechnicianService.upload_service_photo(
        db=db, booking_id=booking_id, photo_type=photo_type, file=file, uploader=current_user
    )


@router.get("/profile/{user_id}", response_model=TechnicianProfileResponse)
def get_technician_profile(user_id: int, db: Session = Depends(get_db)):
    """Retrieve technician profile details."""
    tech_user = db.query(User).filter(User.id == user_id, User.role == UserRole.TECHNICIAN).first()
    if not tech_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Technician not found.")
    return TechnicianService.get_or_create_profile(db=db, user=tech_user)
