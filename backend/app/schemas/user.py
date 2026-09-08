from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, model_validator
from app.models.user import UserRole

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    phone: Optional[str] = None
    phone_number: Optional[str] = None
    role: UserRole = UserRole.CUSTOMER
    specialization: Optional[str] = None
    experience_years: Optional[int] = 0
    bio: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def normalize_phone(cls, data):
        if isinstance(data, dict):
            if "phone_number" in data and "phone" not in data:
                data["phone"] = data["phone_number"]
            elif "phone" in data and "phone_number" not in data:
                data["phone_number"] = data["phone"]
        return data



class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    avatar_url: Optional[str] = None
    specialization: Optional[str] = None
    experience_years: Optional[int] = None
    bio: Optional[str] = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    avatar_url: Optional[str] = None
    hourly_rate: Optional[str] = None
    rating: Optional[str] = "5.0"
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
