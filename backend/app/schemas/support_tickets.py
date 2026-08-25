from datetime import datetime, date, time
from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from app.models.support_tickets import TicketPriority, TicketStatus

class SupportTicketCreate(BaseModel):
    booking_id: Optional[int] = None
    subject: str = Field(..., max_length=200)
    category: str = "GENERAL_INQUIRY"
    priority: TicketPriority = TicketPriority.MEDIUM

class TicketCommentCreate(BaseModel):
    comment_text: str
    is_internal_note: bool = False

class SatisfactionSurveyCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    feedback_notes: Optional[str] = None


from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.support_tickets import SupportTicketsStatus, SupportTicketsPriority, SupportTicketsCategoryType

class SupportTicketsMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: SupportTicketsStatus = SupportTicketsStatus.ACTIVE
    priority: SupportTicketsPriority = SupportTicketsPriority.NORMAL
    category_type: SupportTicketsCategoryType = SupportTicketsCategoryType.PRIMARY
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    score: float = 100.0
    is_active: bool = True
    is_flagged: bool = False

class SupportTicketsMasterEntityCreate(SupportTicketsMasterEntityBase):
    pass

class SupportTicketsMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[SupportTicketsStatus] = None
    priority: Optional[SupportTicketsPriority] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class SupportTicketsMasterEntityResponse(SupportTicketsMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent1Create(SupportTicketsRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent1Response(SupportTicketsRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent2Create(SupportTicketsRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent2Response(SupportTicketsRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent3Create(SupportTicketsRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent3Response(SupportTicketsRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent4Create(SupportTicketsRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent4Response(SupportTicketsRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent5Create(SupportTicketsRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent5Response(SupportTicketsRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent6Create(SupportTicketsRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent6Response(SupportTicketsRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent7Create(SupportTicketsRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent7Response(SupportTicketsRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent8Create(SupportTicketsRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent8Response(SupportTicketsRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent9Create(SupportTicketsRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent9Response(SupportTicketsRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent10Create(SupportTicketsRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent10Response(SupportTicketsRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent11Create(SupportTicketsRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent11Response(SupportTicketsRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent12Create(SupportTicketsRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent12Response(SupportTicketsRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent13Create(SupportTicketsRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent13Response(SupportTicketsRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent14Create(SupportTicketsRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent14Response(SupportTicketsRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent15Create(SupportTicketsRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent15Response(SupportTicketsRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent16Create(SupportTicketsRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent16Response(SupportTicketsRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent17Create(SupportTicketsRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent17Response(SupportTicketsRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent18Create(SupportTicketsRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent18Response(SupportTicketsRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent19Create(SupportTicketsRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent19Response(SupportTicketsRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent20Create(SupportTicketsRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent20Response(SupportTicketsRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent21Create(SupportTicketsRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent21Response(SupportTicketsRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent22Create(SupportTicketsRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent22Response(SupportTicketsRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent23Create(SupportTicketsRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent23Response(SupportTicketsRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent24Create(SupportTicketsRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent24Response(SupportTicketsRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupportTicketsRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class SupportTicketsRelationalComponent25Create(SupportTicketsRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class SupportTicketsRelationalComponent25Response(SupportTicketsRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
