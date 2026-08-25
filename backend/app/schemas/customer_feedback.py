from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.customer_feedback import CustomerFeedbackStatus

class CustomerFeedbackMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: CustomerFeedbackStatus = CustomerFeedbackStatus.ACTIVE
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    is_active: bool = True

class CustomerFeedbackMasterEntityCreate(CustomerFeedbackMasterEntityBase):
    pass

class CustomerFeedbackMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[CustomerFeedbackStatus] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class CustomerFeedbackMasterEntityResponse(CustomerFeedbackMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent1Create(CustomerFeedbackRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent1Response(CustomerFeedbackRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent2Create(CustomerFeedbackRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent2Response(CustomerFeedbackRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent3Create(CustomerFeedbackRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent3Response(CustomerFeedbackRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent4Create(CustomerFeedbackRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent4Response(CustomerFeedbackRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent5Create(CustomerFeedbackRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent5Response(CustomerFeedbackRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent6Create(CustomerFeedbackRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent6Response(CustomerFeedbackRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent7Create(CustomerFeedbackRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent7Response(CustomerFeedbackRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent8Create(CustomerFeedbackRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent8Response(CustomerFeedbackRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent9Create(CustomerFeedbackRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent9Response(CustomerFeedbackRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent10Create(CustomerFeedbackRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent10Response(CustomerFeedbackRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent11Create(CustomerFeedbackRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent11Response(CustomerFeedbackRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent12Create(CustomerFeedbackRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent12Response(CustomerFeedbackRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent13Create(CustomerFeedbackRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent13Response(CustomerFeedbackRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent14Create(CustomerFeedbackRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent14Response(CustomerFeedbackRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent15Create(CustomerFeedbackRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent15Response(CustomerFeedbackRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent16Create(CustomerFeedbackRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent16Response(CustomerFeedbackRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent17Create(CustomerFeedbackRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent17Response(CustomerFeedbackRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent18Create(CustomerFeedbackRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent18Response(CustomerFeedbackRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent19Create(CustomerFeedbackRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent19Response(CustomerFeedbackRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent20Create(CustomerFeedbackRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent20Response(CustomerFeedbackRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent21Create(CustomerFeedbackRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent21Response(CustomerFeedbackRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent22Create(CustomerFeedbackRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent22Response(CustomerFeedbackRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent23Create(CustomerFeedbackRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent23Response(CustomerFeedbackRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent24Create(CustomerFeedbackRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent24Response(CustomerFeedbackRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent25Create(CustomerFeedbackRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent25Response(CustomerFeedbackRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent26Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent26Create(CustomerFeedbackRelationalComponent26Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent26Response(CustomerFeedbackRelationalComponent26Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent27Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent27Create(CustomerFeedbackRelationalComponent27Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent27Response(CustomerFeedbackRelationalComponent27Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent28Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent28Create(CustomerFeedbackRelationalComponent28Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent28Response(CustomerFeedbackRelationalComponent28Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent29Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent29Create(CustomerFeedbackRelationalComponent29Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent29Response(CustomerFeedbackRelationalComponent29Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CustomerFeedbackRelationalComponent30Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CustomerFeedbackRelationalComponent30Create(CustomerFeedbackRelationalComponent30Base):
    master_entity_id: Optional[int] = None

class CustomerFeedbackRelationalComponent30Response(CustomerFeedbackRelationalComponent30Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
