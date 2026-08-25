from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.payments_billing import PaymentsBillingStatus, PaymentsBillingPriority, PaymentsBillingCategoryType

class PaymentsBillingMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: PaymentsBillingStatus = PaymentsBillingStatus.ACTIVE
    priority: PaymentsBillingPriority = PaymentsBillingPriority.NORMAL
    category_type: PaymentsBillingCategoryType = PaymentsBillingCategoryType.PRIMARY
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    score: float = 100.0
    is_active: bool = True
    is_flagged: bool = False

class PaymentsBillingMasterEntityCreate(PaymentsBillingMasterEntityBase):
    pass

class PaymentsBillingMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[PaymentsBillingStatus] = None
    priority: Optional[PaymentsBillingPriority] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class PaymentsBillingMasterEntityResponse(PaymentsBillingMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent1Create(PaymentsBillingRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent1Response(PaymentsBillingRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent2Create(PaymentsBillingRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent2Response(PaymentsBillingRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent3Create(PaymentsBillingRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent3Response(PaymentsBillingRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent4Create(PaymentsBillingRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent4Response(PaymentsBillingRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent5Create(PaymentsBillingRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent5Response(PaymentsBillingRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent6Create(PaymentsBillingRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent6Response(PaymentsBillingRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent7Create(PaymentsBillingRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent7Response(PaymentsBillingRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent8Create(PaymentsBillingRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent8Response(PaymentsBillingRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent9Create(PaymentsBillingRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent9Response(PaymentsBillingRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent10Create(PaymentsBillingRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent10Response(PaymentsBillingRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent11Create(PaymentsBillingRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent11Response(PaymentsBillingRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent12Create(PaymentsBillingRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent12Response(PaymentsBillingRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent13Create(PaymentsBillingRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent13Response(PaymentsBillingRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent14Create(PaymentsBillingRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent14Response(PaymentsBillingRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent15Create(PaymentsBillingRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent15Response(PaymentsBillingRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent16Create(PaymentsBillingRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent16Response(PaymentsBillingRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent17Create(PaymentsBillingRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent17Response(PaymentsBillingRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent18Create(PaymentsBillingRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent18Response(PaymentsBillingRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent19Create(PaymentsBillingRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent19Response(PaymentsBillingRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent20Create(PaymentsBillingRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent20Response(PaymentsBillingRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent21Create(PaymentsBillingRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent21Response(PaymentsBillingRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent22Create(PaymentsBillingRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent22Response(PaymentsBillingRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent23Create(PaymentsBillingRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent23Response(PaymentsBillingRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent24Create(PaymentsBillingRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent24Response(PaymentsBillingRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentsBillingRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PaymentsBillingRelationalComponent25Create(PaymentsBillingRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class PaymentsBillingRelationalComponent25Response(PaymentsBillingRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
