from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.fleet_logistics import FleetLogisticsStatus

class FleetLogisticsMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: FleetLogisticsStatus = FleetLogisticsStatus.ACTIVE
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    is_active: bool = True

class FleetLogisticsMasterEntityCreate(FleetLogisticsMasterEntityBase):
    pass

class FleetLogisticsMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[FleetLogisticsStatus] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class FleetLogisticsMasterEntityResponse(FleetLogisticsMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent1Create(FleetLogisticsRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent1Response(FleetLogisticsRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent2Create(FleetLogisticsRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent2Response(FleetLogisticsRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent3Create(FleetLogisticsRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent3Response(FleetLogisticsRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent4Create(FleetLogisticsRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent4Response(FleetLogisticsRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent5Create(FleetLogisticsRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent5Response(FleetLogisticsRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent6Create(FleetLogisticsRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent6Response(FleetLogisticsRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent7Create(FleetLogisticsRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent7Response(FleetLogisticsRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent8Create(FleetLogisticsRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent8Response(FleetLogisticsRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent9Create(FleetLogisticsRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent9Response(FleetLogisticsRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent10Create(FleetLogisticsRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent10Response(FleetLogisticsRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent11Create(FleetLogisticsRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent11Response(FleetLogisticsRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent12Create(FleetLogisticsRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent12Response(FleetLogisticsRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent13Create(FleetLogisticsRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent13Response(FleetLogisticsRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent14Create(FleetLogisticsRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent14Response(FleetLogisticsRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent15Create(FleetLogisticsRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent15Response(FleetLogisticsRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent16Create(FleetLogisticsRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent16Response(FleetLogisticsRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent17Create(FleetLogisticsRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent17Response(FleetLogisticsRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent18Create(FleetLogisticsRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent18Response(FleetLogisticsRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent19Create(FleetLogisticsRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent19Response(FleetLogisticsRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent20Create(FleetLogisticsRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent20Response(FleetLogisticsRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent21Create(FleetLogisticsRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent21Response(FleetLogisticsRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent22Create(FleetLogisticsRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent22Response(FleetLogisticsRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent23Create(FleetLogisticsRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent23Response(FleetLogisticsRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent24Create(FleetLogisticsRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent24Response(FleetLogisticsRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FleetLogisticsRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class FleetLogisticsRelationalComponent25Create(FleetLogisticsRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class FleetLogisticsRelationalComponent25Response(FleetLogisticsRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
