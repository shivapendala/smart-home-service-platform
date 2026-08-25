from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.workflow_automation import WorkflowAutomationStatus

class WorkflowAutomationMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: WorkflowAutomationStatus = WorkflowAutomationStatus.ACTIVE
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    is_active: bool = True

class WorkflowAutomationMasterEntityCreate(WorkflowAutomationMasterEntityBase):
    pass

class WorkflowAutomationMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[WorkflowAutomationStatus] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class WorkflowAutomationMasterEntityResponse(WorkflowAutomationMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent1Create(WorkflowAutomationRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent1Response(WorkflowAutomationRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent2Create(WorkflowAutomationRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent2Response(WorkflowAutomationRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent3Create(WorkflowAutomationRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent3Response(WorkflowAutomationRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent4Create(WorkflowAutomationRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent4Response(WorkflowAutomationRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent5Create(WorkflowAutomationRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent5Response(WorkflowAutomationRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent6Create(WorkflowAutomationRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent6Response(WorkflowAutomationRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent7Create(WorkflowAutomationRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent7Response(WorkflowAutomationRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent8Create(WorkflowAutomationRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent8Response(WorkflowAutomationRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent9Create(WorkflowAutomationRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent9Response(WorkflowAutomationRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent10Create(WorkflowAutomationRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent10Response(WorkflowAutomationRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent11Create(WorkflowAutomationRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent11Response(WorkflowAutomationRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent12Create(WorkflowAutomationRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent12Response(WorkflowAutomationRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent13Create(WorkflowAutomationRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent13Response(WorkflowAutomationRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent14Create(WorkflowAutomationRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent14Response(WorkflowAutomationRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent15Create(WorkflowAutomationRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent15Response(WorkflowAutomationRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent16Create(WorkflowAutomationRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent16Response(WorkflowAutomationRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent17Create(WorkflowAutomationRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent17Response(WorkflowAutomationRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent18Create(WorkflowAutomationRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent18Response(WorkflowAutomationRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent19Create(WorkflowAutomationRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent19Response(WorkflowAutomationRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent20Create(WorkflowAutomationRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent20Response(WorkflowAutomationRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent21Create(WorkflowAutomationRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent21Response(WorkflowAutomationRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent22Create(WorkflowAutomationRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent22Response(WorkflowAutomationRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent23Create(WorkflowAutomationRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent23Response(WorkflowAutomationRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent24Create(WorkflowAutomationRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent24Response(WorkflowAutomationRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent25Create(WorkflowAutomationRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent25Response(WorkflowAutomationRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent26Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent26Create(WorkflowAutomationRelationalComponent26Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent26Response(WorkflowAutomationRelationalComponent26Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent27Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent27Create(WorkflowAutomationRelationalComponent27Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent27Response(WorkflowAutomationRelationalComponent27Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent28Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent28Create(WorkflowAutomationRelationalComponent28Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent28Response(WorkflowAutomationRelationalComponent28Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent29Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent29Create(WorkflowAutomationRelationalComponent29Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent29Response(WorkflowAutomationRelationalComponent29Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WorkflowAutomationRelationalComponent30Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WorkflowAutomationRelationalComponent30Create(WorkflowAutomationRelationalComponent30Base):
    master_entity_id: Optional[int] = None

class WorkflowAutomationRelationalComponent30Response(WorkflowAutomationRelationalComponent30Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
