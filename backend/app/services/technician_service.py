import os
import uuid
from typing import List, Optional, BinaryIO
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, UploadFile
from app.models.technician import TechnicianProfile, ServicePhoto, ServiceNote, PhotoType
from app.models.booking import Booking, BookingStatus, BookingStatusHistory, ALLOWED_TRANSITIONS
from app.models.user import User, UserRole
from app.core.storage import get_storage_provider
from app.schemas.technician import ServiceNoteCreate

ALLOWED_PHOTO_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
ALLOWED_MIME_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_FILE_SIZE_BYTES = 5 * 1024 * 1024  # 5MB max


class TechnicianService:

    @staticmethod
    def get_or_create_profile(db: Session, user: User) -> TechnicianProfile:
        """Fetch or initialize technician profile."""
        profile = db.query(TechnicianProfile).filter(TechnicianProfile.user_id == user.id).first()
        if not profile:
            profile = TechnicianProfile(
                user_id=user.id,
                specialization=user.specialization or "General Repair",
                experience_years=user.experience_years or 2,
                bio=user.bio or "Certified home service technician.",
                is_available=True
            )
            db.add(profile)
            db.commit()
            db.refresh(profile)
        return profile

    @staticmethod
    def update_availability(db: Session, user: User, is_available: bool) -> TechnicianProfile:
        """Toggle technician online availability status."""
        profile = TechnicianService.get_or_create_profile(db, user)
        profile.is_available = is_available
        db.add(profile)
        db.commit()
        db.refresh(profile)
        return profile

    @staticmethod
    def get_technician_jobs(db: Session, technician_id: int) -> dict:
        """Categorize jobs for technician dashboard (Assigned, Today's, Active, Completed)."""
        all_jobs = db.query(Booking).filter(
            (Booking.technician_id == technician_id) | (Booking.status == BookingStatus.PENDING)
        ).order_by(Booking.created_at.desc()).all()

        today = datetime.now().date()

        assigned_jobs = [j for j in all_jobs if j.status in (BookingStatus.ASSIGNED, BookingStatus.PENDING) and j.technician_id in (technician_id, None)]
        todays_jobs = [j for j in all_jobs if j.scheduled_date == today and j.technician_id == technician_id and j.status != BookingStatus.CANCELLED]
        active_job = next((j for j in all_jobs if j.technician_id == technician_id and j.status in (BookingStatus.ACCEPTED, BookingStatus.ON_THE_WAY, BookingStatus.IN_PROGRESS)), None)
        completed_jobs = [j for j in all_jobs if j.technician_id == technician_id and j.status == BookingStatus.COMPLETED]

        return {
            "assigned_jobs": assigned_jobs,
            "todays_jobs": todays_jobs,
            "active_job": active_job,
            "completed_jobs": completed_jobs,
            "all_jobs": [j for j in all_jobs if j.technician_id == technician_id]
        }

    @staticmethod
    def verify_technician_assignment(booking: Booking, technician: User):
        """Security check: Technician may ONLY access bookings assigned to them."""
        if booking.technician_id is not None and booking.technician_id != technician.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Security Violation: Technicians may only view or modify bookings assigned to them."
            )

    @classmethod
    def execute_job_action(cls, db: Session, booking_id: int, action: str, technician: User, notes: Optional[str] = None) -> Booking:
        """Execute technician workflow actions with strict status validation and security isolation."""
        booking = db.query(Booking).filter(Booking.id == booking_id).first()
        if not booking:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")

        cls.verify_technician_assignment(booking, technician)

        old_status = booking.status
        action = action.upper()

        if action == "ACCEPT":
            if booking.status not in (BookingStatus.ASSIGNED, BookingStatus.PENDING):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Cannot accept job in status {booking.status.value}.")
            booking.technician_id = technician.id
            booking.status = BookingStatus.ACCEPTED

        elif action == "REJECT":
            if booking.status not in (BookingStatus.ASSIGNED, BookingStatus.PENDING, BookingStatus.ACCEPTED):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Cannot reject job in status {booking.status.value}.")
            booking.technician_id = None
            booking.status = BookingStatus.PENDING

        elif action == "ON_THE_WAY":
            if booking.status != BookingStatus.ACCEPTED:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Job must be ACCEPTED before marking ON_THE_WAY. Current: {booking.status.value}.")
            booking.status = BookingStatus.ON_THE_WAY

        elif action == "START":
            if booking.status != BookingStatus.ON_THE_WAY:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Technician must be ON_THE_WAY before starting service. Current: {booking.status.value}.")
            booking.status = BookingStatus.IN_PROGRESS

        elif action == "COMPLETE":
            if booking.status != BookingStatus.IN_PROGRESS:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Service must be IN_PROGRESS before completing. Current: {booking.status.value}.")
            booking.status = BookingStatus.COMPLETED

        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid action '{action}'.")

        # Record audit history
        history = BookingStatusHistory(
            booking_id=booking.id,
            old_status=old_status.value,
            new_status=booking.status.value,
            changed_by_user_id=technician.id,
            notes=notes or f"Technician performed action: {action}"
        )
        db.add(history)
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking

    @classmethod
    def add_service_note(cls, db: Session, booking_id: int, note_in: ServiceNoteCreate, author: User) -> ServiceNote:
        """Add service note to booking with assignment verification."""
        booking = db.query(Booking).filter(Booking.id == booking_id).first()
        if not booking:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")

        if author.role == UserRole.TECHNICIAN:
            cls.verify_technician_assignment(booking, author)

        note = ServiceNote(
            booking_id=booking.id,
            note_text=note_in.note_text,
            author_id=author.id
        )
        db.add(note)
        db.commit()
        db.refresh(note)
        return note

    @classmethod
    async def upload_service_photo(cls, db: Session, booking_id: int, photo_type: PhotoType, file: UploadFile, uploader: User) -> ServicePhoto:
        """Safe file upload validation & local storage provider saving."""
        booking = db.query(Booking).filter(Booking.id == booking_id).first()
        if not booking:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")

        if uploader.role == UserRole.TECHNICIAN:
            cls.verify_technician_assignment(booking, uploader)

        # 1. Validate file extension & content type
        filename = file.filename or "upload.jpg"
        ext = os.path.splitext(filename)[1].lower()
        if ext not in ALLOWED_PHOTO_EXTENSIONS or file.content_type not in ALLOWED_MIME_TYPES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid file type '{ext}'. Only JPG, PNG, and WEBP images are supported."
            )

        # 2. Read content & validate file size limit (max 5MB)
        contents = await file.read()
        if len(contents) > MAX_FILE_SIZE_BYTES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="File size exceeds maximum allowed limit of 5MB."
            )

        # 3. Generate sanitized filename & save via StorageProvider
        safe_filename = f"{uuid.uuid4().hex}{ext}"
        storage = get_storage_provider()
        import io
        rel_path = storage.save_file(io.BytesIO(contents), filename=safe_filename, folder=f"bookings/{booking_id}")
        photo_url = storage.get_file_url(rel_path)

        # 4. Save record in database
        photo = ServicePhoto(
            booking_id=booking.id,
            photo_url=photo_url,
            photo_type=photo_type,
            uploaded_by_user_id=uploader.id
        )
        db.add(photo)
        db.commit()
        db.refresh(photo)
        return photo
