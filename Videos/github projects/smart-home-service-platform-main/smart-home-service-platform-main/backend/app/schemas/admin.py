from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field
from app.models.payment import PaymentStatus
from app.models.review import ComplaintStatus
from app.schemas.user import UserResponse
from app.schemas.booking import BookingResponse


class AdminDashboardStats(BaseModel):
    total_customers: int
    total_technicians: int
    todays_bookings: int
    pending_bookings: int
    active_bookings: int
    completed_services: int
    cancelled_services: int
    revenue_summary: float


class PaymentCreate(BaseModel):
    booking_id: int
    amount: float
    payment_method: str = "CARD"


class PaymentResponse(BaseModel):
    id: int
    booking_id: int
    customer_id: int
    amount: float
    currency: str
    payment_method: str
    status: PaymentStatus
    transaction_id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ReviewCreate(BaseModel):
    booking_id: int
    rating: int = Field(..., ge=1, le=5, description="Rating from 1 to 5 stars")
    comment: Optional[str] = None


class ReviewResponse(BaseModel):
    id: int
    booking_id: int
    customer_id: int
    technician_id: Optional[int] = None
    rating: int
    comment: Optional[str] = None
    customer: Optional[UserResponse] = None
    technician: Optional[UserResponse] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ComplaintCreate(BaseModel):
    booking_id: int
    subject: str
    description: str


class ComplaintUpdate(BaseModel):
    status: Optional[ComplaintStatus] = None
    assigned_to_admin_id: Optional[int] = None
    resolution_notes: Optional[str] = None


class ComplaintResponse(BaseModel):
    id: int
    booking_id: int
    customer_id: int
    assigned_to_admin_id: Optional[int] = None
    subject: str
    description: str
    status: ComplaintStatus
    resolution_notes: Optional[str] = None
    customer: Optional[UserResponse] = None
    assigned_admin: Optional[UserResponse] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
