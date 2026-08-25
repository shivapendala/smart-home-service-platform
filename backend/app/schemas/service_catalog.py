from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.service_catalog import ServiceCatalogStatus

class ServiceCatalogMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: ServiceCatalogStatus = ServiceCatalogStatus.ACTIVE
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    is_active: bool = True

class ServiceCatalogMasterEntityCreate(ServiceCatalogMasterEntityBase):
    pass

class ServiceCatalogMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ServiceCatalogStatus] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class ServiceCatalogMasterEntityResponse(ServiceCatalogMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent1Create(ServiceCatalogRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent1Response(ServiceCatalogRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent2Create(ServiceCatalogRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent2Response(ServiceCatalogRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent3Create(ServiceCatalogRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent3Response(ServiceCatalogRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent4Create(ServiceCatalogRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent4Response(ServiceCatalogRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent5Create(ServiceCatalogRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent5Response(ServiceCatalogRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent6Create(ServiceCatalogRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent6Response(ServiceCatalogRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent7Create(ServiceCatalogRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent7Response(ServiceCatalogRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent8Create(ServiceCatalogRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent8Response(ServiceCatalogRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent9Create(ServiceCatalogRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent9Response(ServiceCatalogRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent10Create(ServiceCatalogRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent10Response(ServiceCatalogRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent11Create(ServiceCatalogRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent11Response(ServiceCatalogRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent12Create(ServiceCatalogRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent12Response(ServiceCatalogRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent13Create(ServiceCatalogRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent13Response(ServiceCatalogRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent14Create(ServiceCatalogRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent14Response(ServiceCatalogRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent15Create(ServiceCatalogRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent15Response(ServiceCatalogRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent16Create(ServiceCatalogRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent16Response(ServiceCatalogRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent17Create(ServiceCatalogRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent17Response(ServiceCatalogRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent18Create(ServiceCatalogRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent18Response(ServiceCatalogRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent19Create(ServiceCatalogRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent19Response(ServiceCatalogRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent20Create(ServiceCatalogRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent20Response(ServiceCatalogRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent21Create(ServiceCatalogRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent21Response(ServiceCatalogRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent22Create(ServiceCatalogRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent22Response(ServiceCatalogRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent23Create(ServiceCatalogRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent23Response(ServiceCatalogRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent24Create(ServiceCatalogRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent24Response(ServiceCatalogRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ServiceCatalogRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ServiceCatalogRelationalComponent25Create(ServiceCatalogRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class ServiceCatalogRelationalComponent25Response(ServiceCatalogRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
