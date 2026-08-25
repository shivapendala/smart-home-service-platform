from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.notification_core import NotificationCoreStatus

class NotificationCoreMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: NotificationCoreStatus = NotificationCoreStatus.ACTIVE
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    is_active: bool = True

class NotificationCoreMasterEntityCreate(NotificationCoreMasterEntityBase):
    pass

class NotificationCoreMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[NotificationCoreStatus] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class NotificationCoreMasterEntityResponse(NotificationCoreMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent1Create(NotificationCoreRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent1Response(NotificationCoreRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent2Create(NotificationCoreRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent2Response(NotificationCoreRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent3Create(NotificationCoreRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent3Response(NotificationCoreRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent4Create(NotificationCoreRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent4Response(NotificationCoreRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent5Create(NotificationCoreRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent5Response(NotificationCoreRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent6Create(NotificationCoreRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent6Response(NotificationCoreRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent7Create(NotificationCoreRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent7Response(NotificationCoreRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent8Create(NotificationCoreRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent8Response(NotificationCoreRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent9Create(NotificationCoreRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent9Response(NotificationCoreRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent10Create(NotificationCoreRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent10Response(NotificationCoreRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent11Create(NotificationCoreRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent11Response(NotificationCoreRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent12Create(NotificationCoreRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent12Response(NotificationCoreRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent13Create(NotificationCoreRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent13Response(NotificationCoreRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent14Create(NotificationCoreRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent14Response(NotificationCoreRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent15Create(NotificationCoreRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent15Response(NotificationCoreRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent16Create(NotificationCoreRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent16Response(NotificationCoreRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent17Create(NotificationCoreRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent17Response(NotificationCoreRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent18Create(NotificationCoreRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent18Response(NotificationCoreRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent19Create(NotificationCoreRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent19Response(NotificationCoreRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent20Create(NotificationCoreRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent20Response(NotificationCoreRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent21Create(NotificationCoreRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent21Response(NotificationCoreRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent22Create(NotificationCoreRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent22Response(NotificationCoreRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent23Create(NotificationCoreRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent23Response(NotificationCoreRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent24Create(NotificationCoreRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent24Response(NotificationCoreRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationCoreRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class NotificationCoreRelationalComponent25Create(NotificationCoreRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class NotificationCoreRelationalComponent25Response(NotificationCoreRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
