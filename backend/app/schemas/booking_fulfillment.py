from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.booking_fulfillment import BookingFulfillmentStatus

class BookingFulfillmentMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: BookingFulfillmentStatus = BookingFulfillmentStatus.ACTIVE
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    is_active: bool = True

class BookingFulfillmentMasterEntityCreate(BookingFulfillmentMasterEntityBase):
    pass

class BookingFulfillmentMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[BookingFulfillmentStatus] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class BookingFulfillmentMasterEntityResponse(BookingFulfillmentMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent1Create(BookingFulfillmentRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent1Response(BookingFulfillmentRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent2Create(BookingFulfillmentRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent2Response(BookingFulfillmentRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent3Create(BookingFulfillmentRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent3Response(BookingFulfillmentRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent4Create(BookingFulfillmentRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent4Response(BookingFulfillmentRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent5Create(BookingFulfillmentRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent5Response(BookingFulfillmentRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent6Create(BookingFulfillmentRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent6Response(BookingFulfillmentRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent7Create(BookingFulfillmentRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent7Response(BookingFulfillmentRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent8Create(BookingFulfillmentRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent8Response(BookingFulfillmentRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent9Create(BookingFulfillmentRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent9Response(BookingFulfillmentRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent10Create(BookingFulfillmentRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent10Response(BookingFulfillmentRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent11Create(BookingFulfillmentRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent11Response(BookingFulfillmentRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent12Create(BookingFulfillmentRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent12Response(BookingFulfillmentRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent13Create(BookingFulfillmentRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent13Response(BookingFulfillmentRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent14Create(BookingFulfillmentRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent14Response(BookingFulfillmentRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent15Create(BookingFulfillmentRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent15Response(BookingFulfillmentRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent16Create(BookingFulfillmentRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent16Response(BookingFulfillmentRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent17Create(BookingFulfillmentRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent17Response(BookingFulfillmentRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent18Create(BookingFulfillmentRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent18Response(BookingFulfillmentRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent19Create(BookingFulfillmentRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent19Response(BookingFulfillmentRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent20Create(BookingFulfillmentRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent20Response(BookingFulfillmentRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent21Create(BookingFulfillmentRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent21Response(BookingFulfillmentRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent22Create(BookingFulfillmentRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent22Response(BookingFulfillmentRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent23Create(BookingFulfillmentRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent23Response(BookingFulfillmentRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent24Create(BookingFulfillmentRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent24Response(BookingFulfillmentRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingFulfillmentRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingFulfillmentRelationalComponent25Create(BookingFulfillmentRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class BookingFulfillmentRelationalComponent25Response(BookingFulfillmentRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
