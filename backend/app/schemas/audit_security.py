from datetime import datetime, date, time
from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict

class AuditLogCreate(BaseModel):
    action: str
    entity_name: str
    entity_id: Optional[str] = None
    changes_json: Optional[str] = None

class AuditLogResponse(AuditLogCreate):
    id: int
    user_id: Optional[int]
    ip_address: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class SecurityIpPolicyCreate(BaseModel):
    ip_address_or_cidr: str
    policy_type: str = "WHITELIST"
    reason: Optional[str] = None

class SecurityIpPolicyResponse(SecurityIpPolicyCreate):
    id: int
    is_active: bool
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.audit_security import AuditSecurityStatus, AuditSecurityPriority, AuditSecurityCategoryType

class AuditSecurityMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: AuditSecurityStatus = AuditSecurityStatus.ACTIVE
    priority: AuditSecurityPriority = AuditSecurityPriority.NORMAL
    category_type: AuditSecurityCategoryType = AuditSecurityCategoryType.PRIMARY
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    score: float = 100.0
    is_active: bool = True
    is_flagged: bool = False

class AuditSecurityMasterEntityCreate(AuditSecurityMasterEntityBase):
    pass

class AuditSecurityMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[AuditSecurityStatus] = None
    priority: Optional[AuditSecurityPriority] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class AuditSecurityMasterEntityResponse(AuditSecurityMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent1Create(AuditSecurityRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent1Response(AuditSecurityRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent2Create(AuditSecurityRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent2Response(AuditSecurityRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent3Create(AuditSecurityRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent3Response(AuditSecurityRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent4Create(AuditSecurityRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent4Response(AuditSecurityRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent5Create(AuditSecurityRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent5Response(AuditSecurityRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent6Create(AuditSecurityRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent6Response(AuditSecurityRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent7Create(AuditSecurityRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent7Response(AuditSecurityRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent8Create(AuditSecurityRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent8Response(AuditSecurityRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent9Create(AuditSecurityRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent9Response(AuditSecurityRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent10Create(AuditSecurityRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent10Response(AuditSecurityRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent11Create(AuditSecurityRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent11Response(AuditSecurityRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent12Create(AuditSecurityRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent12Response(AuditSecurityRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent13Create(AuditSecurityRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent13Response(AuditSecurityRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent14Create(AuditSecurityRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent14Response(AuditSecurityRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent15Create(AuditSecurityRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent15Response(AuditSecurityRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent16Create(AuditSecurityRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent16Response(AuditSecurityRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent17Create(AuditSecurityRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent17Response(AuditSecurityRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent18Create(AuditSecurityRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent18Response(AuditSecurityRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent19Create(AuditSecurityRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent19Response(AuditSecurityRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent20Create(AuditSecurityRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent20Response(AuditSecurityRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent21Create(AuditSecurityRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent21Response(AuditSecurityRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent22Create(AuditSecurityRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent22Response(AuditSecurityRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent23Create(AuditSecurityRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent23Response(AuditSecurityRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent24Create(AuditSecurityRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent24Response(AuditSecurityRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent25Create(AuditSecurityRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent25Response(AuditSecurityRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent26Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent26Create(AuditSecurityRelationalComponent26Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent26Response(AuditSecurityRelationalComponent26Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent27Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent27Create(AuditSecurityRelationalComponent27Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent27Response(AuditSecurityRelationalComponent27Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent28Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent28Create(AuditSecurityRelationalComponent28Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent28Response(AuditSecurityRelationalComponent28Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent29Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent29Create(AuditSecurityRelationalComponent29Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent29Response(AuditSecurityRelationalComponent29Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuditSecurityRelationalComponent30Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AuditSecurityRelationalComponent30Create(AuditSecurityRelationalComponent30Base):
    master_entity_id: Optional[int] = None

class AuditSecurityRelationalComponent30Response(AuditSecurityRelationalComponent30Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
