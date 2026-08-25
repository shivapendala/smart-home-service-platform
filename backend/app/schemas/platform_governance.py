from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.platform_governance import PlatformGovernanceStatus

class PlatformGovernanceMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: PlatformGovernanceStatus = PlatformGovernanceStatus.ACTIVE
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    is_active: bool = True

class PlatformGovernanceMasterEntityCreate(PlatformGovernanceMasterEntityBase):
    pass

class PlatformGovernanceMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[PlatformGovernanceStatus] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class PlatformGovernanceMasterEntityResponse(PlatformGovernanceMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent1Create(PlatformGovernanceRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent1Response(PlatformGovernanceRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent2Create(PlatformGovernanceRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent2Response(PlatformGovernanceRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent3Create(PlatformGovernanceRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent3Response(PlatformGovernanceRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent4Create(PlatformGovernanceRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent4Response(PlatformGovernanceRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent5Create(PlatformGovernanceRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent5Response(PlatformGovernanceRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent6Create(PlatformGovernanceRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent6Response(PlatformGovernanceRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent7Create(PlatformGovernanceRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent7Response(PlatformGovernanceRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent8Create(PlatformGovernanceRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent8Response(PlatformGovernanceRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent9Create(PlatformGovernanceRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent9Response(PlatformGovernanceRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent10Create(PlatformGovernanceRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent10Response(PlatformGovernanceRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent11Create(PlatformGovernanceRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent11Response(PlatformGovernanceRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent12Create(PlatformGovernanceRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent12Response(PlatformGovernanceRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent13Create(PlatformGovernanceRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent13Response(PlatformGovernanceRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent14Create(PlatformGovernanceRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent14Response(PlatformGovernanceRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent15Create(PlatformGovernanceRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent15Response(PlatformGovernanceRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent16Create(PlatformGovernanceRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent16Response(PlatformGovernanceRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent17Create(PlatformGovernanceRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent17Response(PlatformGovernanceRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent18Create(PlatformGovernanceRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent18Response(PlatformGovernanceRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent19Create(PlatformGovernanceRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent19Response(PlatformGovernanceRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent20Create(PlatformGovernanceRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent20Response(PlatformGovernanceRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent21Create(PlatformGovernanceRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent21Response(PlatformGovernanceRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent22Create(PlatformGovernanceRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent22Response(PlatformGovernanceRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent23Create(PlatformGovernanceRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent23Response(PlatformGovernanceRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent24Create(PlatformGovernanceRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent24Response(PlatformGovernanceRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PlatformGovernanceRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class PlatformGovernanceRelationalComponent25Create(PlatformGovernanceRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class PlatformGovernanceRelationalComponent25Response(PlatformGovernanceRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
