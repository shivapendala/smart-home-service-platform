from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from app.models.technician import PhotoType
from app.schemas.user import UserResponse


class TechnicianProfileBase(BaseModel):
    specialization: str
    experience_years: int = 0
    bio: Optional[str] = None
    hourly_rate: float = 45.0
    is_available: bool = True


class TechnicianProfileCreate(TechnicianProfileBase):
    user_id: int


class TechnicianAvailabilityUpdate(BaseModel):
    is_available: bool


class TechnicianProfileResponse(TechnicianProfileBase):
    id: int
    user_id: int
    rating: float
    user: Optional[UserResponse] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ServicePhotoResponse(BaseModel):
    id: int
    booking_id: int
    photo_url: str
    photo_type: PhotoType
    uploaded_by_user_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ServiceNoteCreate(BaseModel):
    note_text: str


class ServiceNoteResponse(BaseModel):
    id: int
    booking_id: int
    note_text: str
    author_id: int
    author: Optional[UserResponse] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
