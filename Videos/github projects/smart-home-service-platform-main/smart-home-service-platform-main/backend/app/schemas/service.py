from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    name: str
    icon: str = "🛠️"
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int
    slug: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ServiceBase(BaseModel):
    category_id: int
    name: str
    description: str
    base_price: float
    duration_minutes: int = 60
    image_url: Optional[str] = None
    is_active: bool = True


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    base_price: Optional[float] = None
    duration_minutes: Optional[int] = None
    image_url: Optional[str] = None
    is_active: Optional[bool] = None
    category_id: Optional[int] = None


class ServiceResponse(ServiceBase):
    id: int
    slug: str
    category: Optional[CategoryResponse] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
