from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.technician_dispatch import TechnicianDispatchStatus

class TechnicianDispatchMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: TechnicianDispatchStatus = TechnicianDispatchStatus.ACTIVE
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    is_active: bool = True

class TechnicianDispatchMasterEntityCreate(TechnicianDispatchMasterEntityBase):
    pass

class TechnicianDispatchMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TechnicianDispatchStatus] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class TechnicianDispatchMasterEntityResponse(TechnicianDispatchMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent1Create(TechnicianDispatchRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent1Response(TechnicianDispatchRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent2Create(TechnicianDispatchRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent2Response(TechnicianDispatchRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent3Create(TechnicianDispatchRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent3Response(TechnicianDispatchRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent4Create(TechnicianDispatchRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent4Response(TechnicianDispatchRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent5Create(TechnicianDispatchRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent5Response(TechnicianDispatchRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent6Create(TechnicianDispatchRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent6Response(TechnicianDispatchRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent7Create(TechnicianDispatchRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent7Response(TechnicianDispatchRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent8Create(TechnicianDispatchRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent8Response(TechnicianDispatchRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent9Create(TechnicianDispatchRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent9Response(TechnicianDispatchRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent10Create(TechnicianDispatchRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent10Response(TechnicianDispatchRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent11Create(TechnicianDispatchRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent11Response(TechnicianDispatchRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent12Create(TechnicianDispatchRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent12Response(TechnicianDispatchRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent13Create(TechnicianDispatchRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent13Response(TechnicianDispatchRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent14Create(TechnicianDispatchRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent14Response(TechnicianDispatchRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent15Create(TechnicianDispatchRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent15Response(TechnicianDispatchRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent16Create(TechnicianDispatchRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent16Response(TechnicianDispatchRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent17Create(TechnicianDispatchRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent17Response(TechnicianDispatchRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent18Create(TechnicianDispatchRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent18Response(TechnicianDispatchRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent19Create(TechnicianDispatchRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent19Response(TechnicianDispatchRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent20Create(TechnicianDispatchRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent20Response(TechnicianDispatchRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent21Create(TechnicianDispatchRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent21Response(TechnicianDispatchRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent22Create(TechnicianDispatchRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent22Response(TechnicianDispatchRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent23Create(TechnicianDispatchRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent23Response(TechnicianDispatchRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent24Create(TechnicianDispatchRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent24Response(TechnicianDispatchRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent25Create(TechnicianDispatchRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent25Response(TechnicianDispatchRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent26Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent26Create(TechnicianDispatchRelationalComponent26Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent26Response(TechnicianDispatchRelationalComponent26Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent27Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent27Create(TechnicianDispatchRelationalComponent27Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent27Response(TechnicianDispatchRelationalComponent27Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent28Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent28Create(TechnicianDispatchRelationalComponent28Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent28Response(TechnicianDispatchRelationalComponent28Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent29Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent29Create(TechnicianDispatchRelationalComponent29Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent29Response(TechnicianDispatchRelationalComponent29Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianDispatchRelationalComponent30Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianDispatchRelationalComponent30Create(TechnicianDispatchRelationalComponent30Base):
    master_entity_id: Optional[int] = None

class TechnicianDispatchRelationalComponent30Response(TechnicianDispatchRelationalComponent30Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
