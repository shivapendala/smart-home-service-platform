from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.user_management import UserManagementStatus

class UserManagementMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: UserManagementStatus = UserManagementStatus.ACTIVE
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    is_active: bool = True

class UserManagementMasterEntityCreate(UserManagementMasterEntityBase):
    pass

class UserManagementMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[UserManagementStatus] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class UserManagementMasterEntityResponse(UserManagementMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent1Create(UserManagementRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent1Response(UserManagementRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent2Create(UserManagementRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent2Response(UserManagementRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent3Create(UserManagementRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent3Response(UserManagementRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent4Create(UserManagementRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent4Response(UserManagementRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent5Create(UserManagementRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent5Response(UserManagementRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent6Create(UserManagementRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent6Response(UserManagementRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent7Create(UserManagementRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent7Response(UserManagementRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent8Create(UserManagementRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent8Response(UserManagementRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent9Create(UserManagementRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent9Response(UserManagementRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent10Create(UserManagementRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent10Response(UserManagementRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent11Create(UserManagementRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent11Response(UserManagementRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent12Create(UserManagementRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent12Response(UserManagementRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent13Create(UserManagementRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent13Response(UserManagementRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent14Create(UserManagementRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent14Response(UserManagementRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent15Create(UserManagementRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent15Response(UserManagementRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent16Create(UserManagementRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent16Response(UserManagementRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent17Create(UserManagementRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent17Response(UserManagementRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent18Create(UserManagementRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent18Response(UserManagementRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent19Create(UserManagementRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent19Response(UserManagementRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent20Create(UserManagementRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent20Response(UserManagementRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent21Create(UserManagementRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent21Response(UserManagementRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent22Create(UserManagementRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent22Response(UserManagementRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent23Create(UserManagementRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent23Response(UserManagementRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent24Create(UserManagementRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent24Response(UserManagementRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserManagementRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class UserManagementRelationalComponent25Create(UserManagementRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class UserManagementRelationalComponent25Response(UserManagementRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
