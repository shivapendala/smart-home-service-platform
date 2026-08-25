from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, ConfigDict, field_validator
from app.models.booking import BookingStatus
from app.schemas.user import UserResponse
from app.schemas.service import ServiceResponse


class AddressBase(BaseModel):
    street_address: str
    city: str
    state: str = "CA"
    zip_code: str
    is_default: bool = False


class AddressCreate(AddressBase):
    pass


class AddressResponse(AddressBase):
    id: int
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class BookingBase(BaseModel):
    service_id: int
    problem_description: str
    scheduled_date: date
    scheduled_time: str
    address_id: Optional[int] = None
    new_address: Optional[AddressCreate] = None

    @field_validator("scheduled_date")
    @classmethod
    def date_must_not_be_in_past(cls, v: date) -> date:
        if v < date.today():
            raise ValueError("Scheduled date cannot be in the past.")
        return v


class BookingCreate(BookingBase):
    pass


class BookingStatusUpdate(BaseModel):
    status: BookingStatus
    notes: Optional[str] = None


class BookingStatusHistoryResponse(BaseModel):
    id: int
    booking_id: int
    old_status: str
    new_status: str
    notes: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class BookingResponse(BaseModel):
    id: int
    customer_id: int
    technician_id: Optional[int] = None
    service_id: int
    address_id: int
    problem_description: str
    scheduled_date: date
    scheduled_time: str
    status: BookingStatus
    estimated_price: float
    final_price: float
    created_at: datetime
    updated_at: datetime

    customer: Optional[UserResponse] = None
    technician: Optional[UserResponse] = None
    service: Optional[ServiceResponse] = None
    address: Optional[AddressResponse] = None
    status_history: List[BookingStatusHistoryResponse] = []

    model_config = ConfigDict(from_attributes=True)
