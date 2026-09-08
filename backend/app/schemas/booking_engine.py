from datetime import datetime, date, time
from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from app.models.booking_engine import RecurrenceFrequency, ScheduleStatus

class RecurringScheduleCreate(BaseModel):
    service_id: int
    address_id: int
    frequency: RecurrenceFrequency = RecurrenceFrequency.MONTHLY
    start_date: date
    end_date: Optional[date] = None
    preferred_time_slot: str

class RecurringScheduleResponse(RecurringScheduleCreate):
    id: int
    customer_id: int
    status: ScheduleStatus
    next_execution_date: date
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class MultiTechAssignmentCreate(BaseModel):
    booking_id: int
    technician_id: int
    role_title: str = "ASSISTANT_TECHNICIAN"


from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.booking_engine import BookingEngineStatus, BookingEnginePriority, BookingEngineCategoryType

class BookingEngineMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: BookingEngineStatus = BookingEngineStatus.ACTIVE
    priority: BookingEnginePriority = BookingEnginePriority.NORMAL
    category_type: BookingEngineCategoryType = BookingEngineCategoryType.PRIMARY
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    score: float = 100.0
    is_active: bool = True
    is_flagged: bool = False

class BookingEngineMasterEntityCreate(BookingEngineMasterEntityBase):
    pass

class BookingEngineMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[BookingEngineStatus] = None
    priority: Optional[BookingEnginePriority] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class BookingEngineMasterEntityResponse(BookingEngineMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent1Create(BookingEngineRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent1Response(BookingEngineRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent2Create(BookingEngineRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent2Response(BookingEngineRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent3Create(BookingEngineRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent3Response(BookingEngineRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent4Create(BookingEngineRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent4Response(BookingEngineRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent5Create(BookingEngineRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent5Response(BookingEngineRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent6Create(BookingEngineRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent6Response(BookingEngineRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent7Create(BookingEngineRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent7Response(BookingEngineRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent8Create(BookingEngineRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent8Response(BookingEngineRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent9Create(BookingEngineRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent9Response(BookingEngineRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent10Create(BookingEngineRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent10Response(BookingEngineRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent11Create(BookingEngineRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent11Response(BookingEngineRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent12Create(BookingEngineRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent12Response(BookingEngineRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent13Create(BookingEngineRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent13Response(BookingEngineRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent14Create(BookingEngineRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent14Response(BookingEngineRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent15Create(BookingEngineRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent15Response(BookingEngineRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent16Create(BookingEngineRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent16Response(BookingEngineRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent17Create(BookingEngineRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent17Response(BookingEngineRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent18Create(BookingEngineRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent18Response(BookingEngineRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent19Create(BookingEngineRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent19Response(BookingEngineRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent20Create(BookingEngineRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent20Response(BookingEngineRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent21Create(BookingEngineRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent21Response(BookingEngineRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent22Create(BookingEngineRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent22Response(BookingEngineRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent23Create(BookingEngineRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent23Response(BookingEngineRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent24Create(BookingEngineRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent24Response(BookingEngineRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent25Create(BookingEngineRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent25Response(BookingEngineRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent26Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent26Create(BookingEngineRelationalComponent26Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent26Response(BookingEngineRelationalComponent26Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent27Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent27Create(BookingEngineRelationalComponent27Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent27Response(BookingEngineRelationalComponent27Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent28Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent28Create(BookingEngineRelationalComponent28Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent28Response(BookingEngineRelationalComponent28Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent29Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent29Create(BookingEngineRelationalComponent29Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent29Response(BookingEngineRelationalComponent29Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class BookingEngineRelationalComponent30Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class BookingEngineRelationalComponent30Create(BookingEngineRelationalComponent30Base):
    master_entity_id: Optional[int] = None

class BookingEngineRelationalComponent30Response(BookingEngineRelationalComponent30Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
