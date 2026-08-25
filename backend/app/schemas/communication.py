from datetime import datetime, date, time
from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from app.models.communication import CommChannel, CommDeliveryStatus

class ChatMessageCreate(BaseModel):
    booking_id: int
    recipient_id: int
    message_text: str
    attachment_url: Optional[str] = None

class ChatMessageResponse(ChatMessageCreate):
    id: int
    sender_id: int
    is_read: bool
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class NotificationTemplateCreate(BaseModel):
    template_key: str
    channel: CommChannel
    title_template: str
    body_template: str

class CommunicationDispatchCreate(BaseModel):
    recipient_user_id: int
    channel: CommChannel
    destination: str
    template_key: Optional[str] = None
    template_data: Optional[dict] = None


from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.communication import CommunicationStatus, CommunicationPriority, CommunicationCategoryType

class CommunicationMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: CommunicationStatus = CommunicationStatus.ACTIVE
    priority: CommunicationPriority = CommunicationPriority.NORMAL
    category_type: CommunicationCategoryType = CommunicationCategoryType.PRIMARY
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    score: float = 100.0
    is_active: bool = True
    is_flagged: bool = False

class CommunicationMasterEntityCreate(CommunicationMasterEntityBase):
    pass

class CommunicationMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[CommunicationStatus] = None
    priority: Optional[CommunicationPriority] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class CommunicationMasterEntityResponse(CommunicationMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent1Create(CommunicationRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent1Response(CommunicationRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent2Create(CommunicationRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent2Response(CommunicationRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent3Create(CommunicationRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent3Response(CommunicationRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent4Create(CommunicationRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent4Response(CommunicationRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent5Create(CommunicationRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent5Response(CommunicationRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent6Create(CommunicationRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent6Response(CommunicationRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent7Create(CommunicationRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent7Response(CommunicationRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent8Create(CommunicationRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent8Response(CommunicationRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent9Create(CommunicationRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent9Response(CommunicationRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent10Create(CommunicationRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent10Response(CommunicationRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent11Create(CommunicationRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent11Response(CommunicationRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent12Create(CommunicationRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent12Response(CommunicationRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent13Create(CommunicationRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent13Response(CommunicationRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent14Create(CommunicationRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent14Response(CommunicationRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent15Create(CommunicationRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent15Response(CommunicationRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent16Create(CommunicationRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent16Response(CommunicationRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent17Create(CommunicationRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent17Response(CommunicationRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent18Create(CommunicationRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent18Response(CommunicationRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent19Create(CommunicationRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent19Response(CommunicationRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent20Create(CommunicationRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent20Response(CommunicationRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent21Create(CommunicationRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent21Response(CommunicationRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent22Create(CommunicationRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent22Response(CommunicationRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent23Create(CommunicationRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent23Response(CommunicationRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent24Create(CommunicationRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent24Response(CommunicationRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunicationRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class CommunicationRelationalComponent25Create(CommunicationRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class CommunicationRelationalComponent25Response(CommunicationRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
