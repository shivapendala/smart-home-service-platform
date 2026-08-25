from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.financial_reporting import FinancialReportingStatus

class FinancialReportingMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: FinancialReportingStatus = FinancialReportingStatus.ACTIVE
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    is_active: bool = True

class FinancialReportingMasterEntityCreate(FinancialReportingMasterEntityBase):
    pass

class FinancialReportingMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[FinancialReportingStatus] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class FinancialReportingMasterEntityResponse(FinancialReportingMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent1Create(FinancialReportingRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent1Response(FinancialReportingRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent2Create(FinancialReportingRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent2Response(FinancialReportingRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent3Create(FinancialReportingRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent3Response(FinancialReportingRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent4Create(FinancialReportingRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent4Response(FinancialReportingRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent5Create(FinancialReportingRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent5Response(FinancialReportingRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent6Create(FinancialReportingRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent6Response(FinancialReportingRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent7Create(FinancialReportingRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent7Response(FinancialReportingRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent8Create(FinancialReportingRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent8Response(FinancialReportingRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent9Create(FinancialReportingRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent9Response(FinancialReportingRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent10Create(FinancialReportingRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent10Response(FinancialReportingRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent11Create(FinancialReportingRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent11Response(FinancialReportingRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent12Create(FinancialReportingRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent12Response(FinancialReportingRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent13Create(FinancialReportingRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent13Response(FinancialReportingRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent14Create(FinancialReportingRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent14Response(FinancialReportingRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent15Create(FinancialReportingRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent15Response(FinancialReportingRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent16Create(FinancialReportingRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent16Response(FinancialReportingRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent17Create(FinancialReportingRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent17Response(FinancialReportingRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent18Create(FinancialReportingRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent18Response(FinancialReportingRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent19Create(FinancialReportingRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent19Response(FinancialReportingRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent20Create(FinancialReportingRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent20Response(FinancialReportingRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent21Create(FinancialReportingRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent21Response(FinancialReportingRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent22Create(FinancialReportingRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent22Response(FinancialReportingRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent23Create(FinancialReportingRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent23Response(FinancialReportingRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent24Create(FinancialReportingRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent24Response(FinancialReportingRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent25Create(FinancialReportingRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent25Response(FinancialReportingRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent26Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent26Create(FinancialReportingRelationalComponent26Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent26Response(FinancialReportingRelationalComponent26Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent27Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent27Create(FinancialReportingRelationalComponent27Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent27Response(FinancialReportingRelationalComponent27Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent28Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent28Create(FinancialReportingRelationalComponent28Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent28Response(FinancialReportingRelationalComponent28Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent29Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent29Create(FinancialReportingRelationalComponent29Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent29Response(FinancialReportingRelationalComponent29Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialReportingRelationalComponent30Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FinancialReportingRelationalComponent30Create(FinancialReportingRelationalComponent30Base):
    master_entity_id: Optional[int] = None

class FinancialReportingRelationalComponent30Response(FinancialReportingRelationalComponent30Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
