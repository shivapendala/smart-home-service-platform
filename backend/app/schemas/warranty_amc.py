from datetime import datetime, date, time
from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from app.models.warranty_amc import AMCPlanTier, WarrantyClaimStatus

class AMCPlanCreate(BaseModel):
    plan_name: str
    tier: AMCPlanTier = AMCPlanTier.GOLD_PREMIUM
    description: str
    annual_price: float
    duration_months: int = 12
    covered_visits_per_year: int = 4
    discount_on_spare_parts: float = 15.0

class AMCPlanResponse(AMCPlanCreate):
    id: int
    is_active: bool
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class AMCSubscriptionCreate(BaseModel):
    amc_plan_id: int
    is_auto_renew: bool = False

class WarrantyClaimCreate(BaseModel):
    booking_id: int
    issue_description: str


from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.warranty_amc import WarrantyAmcStatus, WarrantyAmcPriority, WarrantyAmcCategoryType

class WarrantyAmcMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: WarrantyAmcStatus = WarrantyAmcStatus.ACTIVE
    priority: WarrantyAmcPriority = WarrantyAmcPriority.NORMAL
    category_type: WarrantyAmcCategoryType = WarrantyAmcCategoryType.PRIMARY
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    score: float = 100.0
    is_active: bool = True
    is_flagged: bool = False

class WarrantyAmcMasterEntityCreate(WarrantyAmcMasterEntityBase):
    pass

class WarrantyAmcMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[WarrantyAmcStatus] = None
    priority: Optional[WarrantyAmcPriority] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class WarrantyAmcMasterEntityResponse(WarrantyAmcMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent1Create(WarrantyAmcRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent1Response(WarrantyAmcRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent2Create(WarrantyAmcRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent2Response(WarrantyAmcRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent3Create(WarrantyAmcRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent3Response(WarrantyAmcRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent4Create(WarrantyAmcRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent4Response(WarrantyAmcRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent5Create(WarrantyAmcRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent5Response(WarrantyAmcRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent6Create(WarrantyAmcRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent6Response(WarrantyAmcRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent7Create(WarrantyAmcRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent7Response(WarrantyAmcRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent8Create(WarrantyAmcRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent8Response(WarrantyAmcRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent9Create(WarrantyAmcRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent9Response(WarrantyAmcRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent10Create(WarrantyAmcRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent10Response(WarrantyAmcRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent11Create(WarrantyAmcRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent11Response(WarrantyAmcRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent12Create(WarrantyAmcRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent12Response(WarrantyAmcRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent13Create(WarrantyAmcRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent13Response(WarrantyAmcRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent14Create(WarrantyAmcRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent14Response(WarrantyAmcRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent15Create(WarrantyAmcRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent15Response(WarrantyAmcRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent16Create(WarrantyAmcRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent16Response(WarrantyAmcRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent17Create(WarrantyAmcRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent17Response(WarrantyAmcRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent18Create(WarrantyAmcRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent18Response(WarrantyAmcRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent19Create(WarrantyAmcRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent19Response(WarrantyAmcRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent20Create(WarrantyAmcRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent20Response(WarrantyAmcRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent21Create(WarrantyAmcRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent21Response(WarrantyAmcRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent22Create(WarrantyAmcRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent22Response(WarrantyAmcRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent23Create(WarrantyAmcRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent23Response(WarrantyAmcRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent24Create(WarrantyAmcRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent24Response(WarrantyAmcRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent25Create(WarrantyAmcRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent25Response(WarrantyAmcRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent26Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent26Create(WarrantyAmcRelationalComponent26Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent26Response(WarrantyAmcRelationalComponent26Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent27Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent27Create(WarrantyAmcRelationalComponent27Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent27Response(WarrantyAmcRelationalComponent27Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent28Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent28Create(WarrantyAmcRelationalComponent28Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent28Response(WarrantyAmcRelationalComponent28Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent29Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent29Create(WarrantyAmcRelationalComponent29Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent29Response(WarrantyAmcRelationalComponent29Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class WarrantyAmcRelationalComponent30Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class WarrantyAmcRelationalComponent30Create(WarrantyAmcRelationalComponent30Base):
    master_entity_id: Optional[int] = None

class WarrantyAmcRelationalComponent30Response(WarrantyAmcRelationalComponent30Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
