from datetime import datetime, date, time
from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from app.models.technician_mgmt import DayOfWeek, PayoutStatus, DispatchPriority

class TechnicianShiftCreate(BaseModel):
    day_of_week: DayOfWeek
    shift_start: time
    shift_end: time
    break_start: Optional[time] = None
    break_end: Optional[time] = None
    is_active: bool = True
    max_jobs_per_shift: int = 6

class TechnicianShiftResponse(TechnicianShiftCreate):
    id: int
    technician_id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class TechnicianServiceZoneCreate(BaseModel):
    zone_name: str
    zip_code: str
    city: str
    state: str
    latitude_center: Optional[float] = None
    longitude_center: Optional[float] = None
    radius_km: float = 15.0
    is_primary_zone: bool = True

class TechnicianSkillCreate(BaseModel):
    skill_name: str
    category_name: str
    proficiency_level: str = "INTERMEDIATE"
    years_experience: int = 1
    is_certified: bool = False

class TechnicianCertificationCreate(BaseModel):
    certification_title: str
    issuing_authority: str
    license_number: str
    issue_date: date
    expiry_date: Optional[date] = None

class EmergencyDispatchCreate(BaseModel):
    booking_id: int
    priority: DispatchPriority = DispatchPriority.HIGH
    dispatch_reason: str
    response_sla_minutes: int = 30

class TechnicianPayoutCreate(BaseModel):
    technician_id: int
    period_start: date
    period_end: date
    gross_earnings: float
    platform_commission: float
    payout_method: str = "BANK_TRANSFER"


from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.technician_mgmt import TechnicianMgmtStatus, TechnicianMgmtPriority, TechnicianMgmtCategoryType

class TechnicianMgmtMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: TechnicianMgmtStatus = TechnicianMgmtStatus.ACTIVE
    priority: TechnicianMgmtPriority = TechnicianMgmtPriority.NORMAL
    category_type: TechnicianMgmtCategoryType = TechnicianMgmtCategoryType.PRIMARY
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    score: float = 100.0
    is_active: bool = True
    is_flagged: bool = False

class TechnicianMgmtMasterEntityCreate(TechnicianMgmtMasterEntityBase):
    pass

class TechnicianMgmtMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TechnicianMgmtStatus] = None
    priority: Optional[TechnicianMgmtPriority] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class TechnicianMgmtMasterEntityResponse(TechnicianMgmtMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent1Create(TechnicianMgmtRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent1Response(TechnicianMgmtRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent2Create(TechnicianMgmtRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent2Response(TechnicianMgmtRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent3Create(TechnicianMgmtRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent3Response(TechnicianMgmtRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent4Create(TechnicianMgmtRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent4Response(TechnicianMgmtRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent5Create(TechnicianMgmtRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent5Response(TechnicianMgmtRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent6Create(TechnicianMgmtRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent6Response(TechnicianMgmtRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent7Create(TechnicianMgmtRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent7Response(TechnicianMgmtRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent8Create(TechnicianMgmtRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent8Response(TechnicianMgmtRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent9Create(TechnicianMgmtRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent9Response(TechnicianMgmtRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent10Create(TechnicianMgmtRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent10Response(TechnicianMgmtRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent11Create(TechnicianMgmtRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent11Response(TechnicianMgmtRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent12Create(TechnicianMgmtRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent12Response(TechnicianMgmtRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent13Create(TechnicianMgmtRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent13Response(TechnicianMgmtRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent14Create(TechnicianMgmtRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent14Response(TechnicianMgmtRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent15Create(TechnicianMgmtRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent15Response(TechnicianMgmtRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent16Create(TechnicianMgmtRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent16Response(TechnicianMgmtRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent17Create(TechnicianMgmtRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent17Response(TechnicianMgmtRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent18Create(TechnicianMgmtRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent18Response(TechnicianMgmtRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent19Create(TechnicianMgmtRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent19Response(TechnicianMgmtRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent20Create(TechnicianMgmtRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent20Response(TechnicianMgmtRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent21Create(TechnicianMgmtRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent21Response(TechnicianMgmtRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent22Create(TechnicianMgmtRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent22Response(TechnicianMgmtRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent23Create(TechnicianMgmtRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent23Response(TechnicianMgmtRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent24Create(TechnicianMgmtRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent24Response(TechnicianMgmtRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent25Create(TechnicianMgmtRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent25Response(TechnicianMgmtRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent26Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent26Create(TechnicianMgmtRelationalComponent26Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent26Response(TechnicianMgmtRelationalComponent26Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent27Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent27Create(TechnicianMgmtRelationalComponent27Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent27Response(TechnicianMgmtRelationalComponent27Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent28Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent28Create(TechnicianMgmtRelationalComponent28Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent28Response(TechnicianMgmtRelationalComponent28Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent29Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent29Create(TechnicianMgmtRelationalComponent29Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent29Response(TechnicianMgmtRelationalComponent29Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TechnicianMgmtRelationalComponent30Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class TechnicianMgmtRelationalComponent30Create(TechnicianMgmtRelationalComponent30Base):
    master_entity_id: Optional[int] = None

class TechnicianMgmtRelationalComponent30Response(TechnicianMgmtRelationalComponent30Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
