from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.models.booking import BookingStatus
from app.schemas.user import UserResponse
from app.schemas.service import ServiceResponse


class BookingBase(BaseModel):
    service_id: int
    scheduled_date: date
    scheduled_time_slot: str
    address_line: str
    city: str
    zip_code: str
    notes: Optional[str] = None


class BookingCreate(BookingBase):
    pass


class BookingStatusUpdate(BaseModel):
    status: BookingStatus


class AssignTechnicianPayload(BaseModel):
    technician_id: int


class BookingResponse(BookingBase):
    id: int
    customer_id: int
    technician_id: Optional[int] = None
    status: BookingStatus
    total_amount: float
    created_at: datetime
    updated_at: datetime

    customer: Optional[UserResponse] = None
    technician: Optional[UserResponse] = None
    service: Optional[ServiceResponse] = None

    model_config = ConfigDict(from_attributes=True)
