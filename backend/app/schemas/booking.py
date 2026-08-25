from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, ConfigDict, field_validator, model_validator
from app.models.booking import BookingStatus
from app.schemas.user import UserResponse
from app.schemas.service import ServiceResponse


class AddressBase(BaseModel):
    street_address: str
    city: str
    state: str = "CA"
    zip_code: str
    is_default: bool = False

    @model_validator(mode="before")
    @classmethod
    def normalize_address(cls, data):
        if isinstance(data, dict):
            if "address_line" in data and "street_address" not in data:
                data["street_address"] = data["address_line"]
            if "postal_code" in data and "zip_code" not in data:
                data["zip_code"] = data["postal_code"]
        return data


class AddressCreate(AddressBase):
    pass


class AddressResponse(AddressBase):
    id: int
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class BookingBase(BaseModel):
    service_id: int
    problem_description: Optional[str] = None
    scheduled_date: date
    scheduled_time: Optional[str] = None
    scheduled_time_slot: Optional[str] = None
    notes: Optional[str] = None
    address_id: Optional[int] = None
    new_address: Optional[AddressCreate] = None

    # Top-level address fields fallback from frontend
    address_line: Optional[str] = None
    street_address: Optional[str] = None
    city: Optional[str] = None
    zip_code: Optional[str] = None
    postal_code: Optional[str] = None
    state: Optional[str] = "CA"

    @model_validator(mode="before")
    @classmethod
    def normalize_booking_inputs(cls, data):
        if isinstance(data, dict):
            # 1. Normalize scheduled_time vs scheduled_time_slot
            if not data.get("scheduled_time") and data.get("scheduled_time_slot"):
                data["scheduled_time"] = data["scheduled_time_slot"]
            elif not data.get("scheduled_time_slot") and data.get("scheduled_time"):
                data["scheduled_time_slot"] = data["scheduled_time"]
            if not data.get("scheduled_time"):
                data["scheduled_time"] = "10:00 AM - 12:00 PM"
                data["scheduled_time_slot"] = "10:00 AM - 12:00 PM"

            # 2. Normalize problem_description vs notes
            if not data.get("problem_description") and data.get("notes"):
                data["problem_description"] = data["notes"]
            elif not data.get("notes") and data.get("problem_description"):
                data["notes"] = data["problem_description"]
            if not data.get("problem_description"):
                data["problem_description"] = "General home service request"
                data["notes"] = "General home service request"

            # 3. Build new_address if top-level address fields are provided
            street = data.get("street_address") or data.get("address_line")
            city = data.get("city")
            zip_code = data.get("zip_code") or data.get("postal_code")
            if street and city and zip_code and not data.get("new_address") and not data.get("address_id"):
                data["new_address"] = {
                    "street_address": street,
                    "city": city,
                    "state": data.get("state", "CA"),
                    "zip_code": zip_code
                }
        return data

    @field_validator("scheduled_date", mode="before")
    @classmethod
    def parse_and_validate_date(cls, v):
        if isinstance(v, str):
            if "T" in v:
                v = v.split("T")[0]
            v = date.fromisoformat(v)
        if isinstance(v, date) and v < date.today():
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

    # Aliases / Computed fields expected by frontend
    scheduled_time_slot: Optional[str] = None
    notes: Optional[str] = None
    total_amount: Optional[float] = None
    address_line: Optional[str] = None
    city: Optional[str] = None
    zip_code: Optional[str] = None

    customer: Optional[UserResponse] = None
    technician: Optional[UserResponse] = None
    service: Optional[ServiceResponse] = None
    address: Optional[AddressResponse] = None
    status_history: List[BookingStatusHistoryResponse] = []

    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode="after")
    def populate_frontend_aliases(self):
        if not self.scheduled_time_slot:
            self.scheduled_time_slot = self.scheduled_time
        if not self.notes:
            self.notes = self.problem_description
        if self.total_amount is None:
            self.total_amount = self.final_price if self.final_price else self.estimated_price
        if self.address:
            if not self.address_line:
                self.address_line = self.address.street_address
            if not self.city:
                self.city = self.address.city
            if not self.zip_code:
                self.zip_code = self.address.zip_code
        return self

