from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.ai_recommendations import AiRecommendationsStatus, AiRecommendationsPriority, AiRecommendationsCategoryType

class AiRecommendationsMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: AiRecommendationsStatus = AiRecommendationsStatus.ACTIVE
    priority: AiRecommendationsPriority = AiRecommendationsPriority.NORMAL
    category_type: AiRecommendationsCategoryType = AiRecommendationsCategoryType.PRIMARY
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    score: float = 100.0
    is_active: bool = True
    is_flagged: bool = False

class AiRecommendationsMasterEntityCreate(AiRecommendationsMasterEntityBase):
    pass

class AiRecommendationsMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[AiRecommendationsStatus] = None
    priority: Optional[AiRecommendationsPriority] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class AiRecommendationsMasterEntityResponse(AiRecommendationsMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent1Create(AiRecommendationsRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent1Response(AiRecommendationsRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent2Create(AiRecommendationsRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent2Response(AiRecommendationsRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent3Create(AiRecommendationsRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent3Response(AiRecommendationsRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent4Create(AiRecommendationsRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent4Response(AiRecommendationsRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent5Create(AiRecommendationsRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent5Response(AiRecommendationsRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent6Create(AiRecommendationsRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent6Response(AiRecommendationsRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent7Create(AiRecommendationsRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent7Response(AiRecommendationsRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent8Create(AiRecommendationsRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent8Response(AiRecommendationsRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent9Create(AiRecommendationsRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent9Response(AiRecommendationsRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent10Create(AiRecommendationsRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent10Response(AiRecommendationsRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent11Create(AiRecommendationsRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent11Response(AiRecommendationsRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent12Create(AiRecommendationsRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent12Response(AiRecommendationsRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent13Create(AiRecommendationsRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent13Response(AiRecommendationsRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent14Create(AiRecommendationsRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent14Response(AiRecommendationsRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent15Create(AiRecommendationsRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent15Response(AiRecommendationsRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent16Create(AiRecommendationsRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent16Response(AiRecommendationsRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent17Create(AiRecommendationsRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent17Response(AiRecommendationsRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent18Create(AiRecommendationsRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent18Response(AiRecommendationsRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent19Create(AiRecommendationsRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent19Response(AiRecommendationsRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent20Create(AiRecommendationsRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent20Response(AiRecommendationsRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent21Create(AiRecommendationsRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent21Response(AiRecommendationsRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent22Create(AiRecommendationsRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent22Response(AiRecommendationsRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent23Create(AiRecommendationsRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent23Response(AiRecommendationsRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent24Create(AiRecommendationsRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent24Response(AiRecommendationsRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AiRecommendationsRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class AiRecommendationsRelationalComponent25Create(AiRecommendationsRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class AiRecommendationsRelationalComponent25Response(AiRecommendationsRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
