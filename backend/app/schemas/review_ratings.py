from datetime import datetime, date, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.models.review_ratings import ReviewRatingsStatus

class ReviewRatingsMasterEntityBase(BaseModel):
    entity_code: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: ReviewRatingsStatus = ReviewRatingsStatus.ACTIVE
    amount: float = Field(0.0, ge=0.0)
    quantity: int = Field(1, ge=1)
    is_active: bool = True

class ReviewRatingsMasterEntityCreate(ReviewRatingsMasterEntityBase):
    pass

class ReviewRatingsMasterEntityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ReviewRatingsStatus] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None

class ReviewRatingsMasterEntityResponse(ReviewRatingsMasterEntityBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent1Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 1
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent1Create(ReviewRatingsRelationalComponent1Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent1Response(ReviewRatingsRelationalComponent1Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent2Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 2
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent2Create(ReviewRatingsRelationalComponent2Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent2Response(ReviewRatingsRelationalComponent2Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent3Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 3
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent3Create(ReviewRatingsRelationalComponent3Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent3Response(ReviewRatingsRelationalComponent3Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent4Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 4
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent4Create(ReviewRatingsRelationalComponent4Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent4Response(ReviewRatingsRelationalComponent4Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent5Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 5
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent5Create(ReviewRatingsRelationalComponent5Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent5Response(ReviewRatingsRelationalComponent5Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent6Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 6
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent6Create(ReviewRatingsRelationalComponent6Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent6Response(ReviewRatingsRelationalComponent6Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent7Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 7
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent7Create(ReviewRatingsRelationalComponent7Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent7Response(ReviewRatingsRelationalComponent7Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent8Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 8
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent8Create(ReviewRatingsRelationalComponent8Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent8Response(ReviewRatingsRelationalComponent8Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent9Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 9
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent9Create(ReviewRatingsRelationalComponent9Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent9Response(ReviewRatingsRelationalComponent9Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent10Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 10
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent10Create(ReviewRatingsRelationalComponent10Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent10Response(ReviewRatingsRelationalComponent10Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent11Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 11
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent11Create(ReviewRatingsRelationalComponent11Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent11Response(ReviewRatingsRelationalComponent11Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent12Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 12
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent12Create(ReviewRatingsRelationalComponent12Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent12Response(ReviewRatingsRelationalComponent12Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent13Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 13
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent13Create(ReviewRatingsRelationalComponent13Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent13Response(ReviewRatingsRelationalComponent13Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent14Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 14
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent14Create(ReviewRatingsRelationalComponent14Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent14Response(ReviewRatingsRelationalComponent14Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent15Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 15
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent15Create(ReviewRatingsRelationalComponent15Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent15Response(ReviewRatingsRelationalComponent15Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent16Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 16
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent16Create(ReviewRatingsRelationalComponent16Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent16Response(ReviewRatingsRelationalComponent16Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent17Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 17
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent17Create(ReviewRatingsRelationalComponent17Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent17Response(ReviewRatingsRelationalComponent17Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent18Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 18
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent18Create(ReviewRatingsRelationalComponent18Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent18Response(ReviewRatingsRelationalComponent18Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent19Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 19
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent19Create(ReviewRatingsRelationalComponent19Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent19Response(ReviewRatingsRelationalComponent19Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent20Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 20
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent20Create(ReviewRatingsRelationalComponent20Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent20Response(ReviewRatingsRelationalComponent20Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent21Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 21
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent21Create(ReviewRatingsRelationalComponent21Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent21Response(ReviewRatingsRelationalComponent21Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent22Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 22
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent22Create(ReviewRatingsRelationalComponent22Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent22Response(ReviewRatingsRelationalComponent22Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent23Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 23
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent23Create(ReviewRatingsRelationalComponent23Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent23Response(ReviewRatingsRelationalComponent23Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent24Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 24
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent24Create(ReviewRatingsRelationalComponent24Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent24Response(ReviewRatingsRelationalComponent24Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewRatingsRelationalComponent25Base(BaseModel):
    component_name: str = Field(..., max_length=150)
    component_type: str = "STANDARD"
    metric_value: float = 0.0
    cost_factor: float = 1.0
    sequence_order: int = 25
    status_flag: str = "ENABLED"
    notes_text: Optional[str] = None

class ReviewRatingsRelationalComponent25Create(ReviewRatingsRelationalComponent25Base):
    master_entity_id: Optional[int] = None

class ReviewRatingsRelationalComponent25Response(ReviewRatingsRelationalComponent25Base):
    id: int
    master_entity_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
