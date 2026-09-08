from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.enterprise_integration import EnterpriseIntegrationStatus

class EnterpriseIntegrationMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: EnterpriseIntegrationStatus = EnterpriseIntegrationStatus.ACTIVE
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    is_active: bool = True

class EnterpriseIntegrationMasterEntityCreate(EnterpriseIntegrationMasterEntityBase):
    pass

class EnterpriseIntegrationMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[EnterpriseIntegrationStatus] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class EnterpriseIntegrationMasterEntityResponse(EnterpriseIntegrationMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent1Create(EnterpriseIntegrationRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent1Response(EnterpriseIntegrationRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent2Create(EnterpriseIntegrationRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent2Response(EnterpriseIntegrationRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent3Create(EnterpriseIntegrationRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent3Response(EnterpriseIntegrationRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent4Create(EnterpriseIntegrationRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent4Response(EnterpriseIntegrationRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent5Create(EnterpriseIntegrationRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent5Response(EnterpriseIntegrationRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent6Create(EnterpriseIntegrationRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent6Response(EnterpriseIntegrationRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent7Create(EnterpriseIntegrationRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent7Response(EnterpriseIntegrationRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent8Create(EnterpriseIntegrationRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent8Response(EnterpriseIntegrationRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent9Create(EnterpriseIntegrationRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent9Response(EnterpriseIntegrationRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent10Create(EnterpriseIntegrationRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent10Response(EnterpriseIntegrationRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent11Create(EnterpriseIntegrationRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent11Response(EnterpriseIntegrationRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent12Create(EnterpriseIntegrationRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent12Response(EnterpriseIntegrationRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent13Create(EnterpriseIntegrationRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent13Response(EnterpriseIntegrationRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent14Create(EnterpriseIntegrationRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent14Response(EnterpriseIntegrationRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent15Create(EnterpriseIntegrationRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent15Response(EnterpriseIntegrationRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent16Create(EnterpriseIntegrationRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent16Response(EnterpriseIntegrationRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent17Create(EnterpriseIntegrationRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent17Response(EnterpriseIntegrationRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent18Create(EnterpriseIntegrationRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent18Response(EnterpriseIntegrationRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent19Create(EnterpriseIntegrationRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent19Response(EnterpriseIntegrationRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent20Create(EnterpriseIntegrationRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent20Response(EnterpriseIntegrationRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent21Create(EnterpriseIntegrationRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent21Response(EnterpriseIntegrationRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent22Create(EnterpriseIntegrationRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent22Response(EnterpriseIntegrationRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent23Create(EnterpriseIntegrationRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent23Response(EnterpriseIntegrationRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent24Create(EnterpriseIntegrationRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent24Response(EnterpriseIntegrationRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent25Create(EnterpriseIntegrationRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent25Response(EnterpriseIntegrationRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent26Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent26Create(EnterpriseIntegrationRelationalComponent26Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent26Response(EnterpriseIntegrationRelationalComponent26Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent27Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent27Create(EnterpriseIntegrationRelationalComponent27Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent27Response(EnterpriseIntegrationRelationalComponent27Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent28Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent28Create(EnterpriseIntegrationRelationalComponent28Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent28Response(EnterpriseIntegrationRelationalComponent28Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent29Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent29Create(EnterpriseIntegrationRelationalComponent29Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent29Response(EnterpriseIntegrationRelationalComponent29Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EnterpriseIntegrationRelationalComponent30Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class EnterpriseIntegrationRelationalComponent30Create(EnterpriseIntegrationRelationalComponent30Base):
    master_entity_id: Optional[int] = None

class EnterpriseIntegrationRelationalComponent30Response(EnterpriseIntegrationRelationalComponent30Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
