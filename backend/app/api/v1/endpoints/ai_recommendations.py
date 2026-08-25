from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.ai_recommendations import AiRecommendationsStatus
from app.schemas.ai_recommendations import (
    AiRecommendationsMasterEntityCreate, AiRecommendationsMasterEntityUpdate, AiRecommendationsMasterEntityResponse,
    AiRecommendationsRelationalComponent1Create, AiRecommendationsRelationalComponent1Response ,AiRecommendationsRelationalComponent2Create, AiRecommendationsRelationalComponent2Response ,AiRecommendationsRelationalComponent3Create, AiRecommendationsRelationalComponent3Response ,AiRecommendationsRelationalComponent4Create, AiRecommendationsRelationalComponent4Response ,AiRecommendationsRelationalComponent5Create, AiRecommendationsRelationalComponent5Response ,AiRecommendationsRelationalComponent6Create, AiRecommendationsRelationalComponent6Response ,AiRecommendationsRelationalComponent7Create, AiRecommendationsRelationalComponent7Response ,AiRecommendationsRelationalComponent8Create, AiRecommendationsRelationalComponent8Response ,AiRecommendationsRelationalComponent9Create, AiRecommendationsRelationalComponent9Response ,AiRecommendationsRelationalComponent10Create, AiRecommendationsRelationalComponent10Response ,AiRecommendationsRelationalComponent11Create, AiRecommendationsRelationalComponent11Response ,AiRecommendationsRelationalComponent12Create, AiRecommendationsRelationalComponent12Response ,AiRecommendationsRelationalComponent13Create, AiRecommendationsRelationalComponent13Response ,AiRecommendationsRelationalComponent14Create, AiRecommendationsRelationalComponent14Response ,AiRecommendationsRelationalComponent15Create, AiRecommendationsRelationalComponent15Response ,AiRecommendationsRelationalComponent16Create, AiRecommendationsRelationalComponent16Response ,AiRecommendationsRelationalComponent17Create, AiRecommendationsRelationalComponent17Response ,AiRecommendationsRelationalComponent18Create, AiRecommendationsRelationalComponent18Response ,AiRecommendationsRelationalComponent19Create, AiRecommendationsRelationalComponent19Response ,AiRecommendationsRelationalComponent20Create, AiRecommendationsRelationalComponent20Response ,AiRecommendationsRelationalComponent21Create, AiRecommendationsRelationalComponent21Response ,AiRecommendationsRelationalComponent22Create, AiRecommendationsRelationalComponent22Response ,AiRecommendationsRelationalComponent23Create, AiRecommendationsRelationalComponent23Response ,AiRecommendationsRelationalComponent24Create, AiRecommendationsRelationalComponent24Response ,AiRecommendationsRelationalComponent25Create, AiRecommendationsRelationalComponent25Response
)
from app.services.ai_recommendations_service import AiRecommendationsService

router = APIRouter()

@router.post("/master", response_model=AiRecommendationsMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: AiRecommendationsMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[AiRecommendationsMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[AiRecommendationsStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=AiRecommendationsMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=AiRecommendationsMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: AiRecommendationsMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    AiRecommendationsService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=AiRecommendationsRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: AiRecommendationsRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[AiRecommendationsRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=AiRecommendationsRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: AiRecommendationsRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[AiRecommendationsRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=AiRecommendationsRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: AiRecommendationsRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[AiRecommendationsRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=AiRecommendationsRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: AiRecommendationsRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[AiRecommendationsRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=AiRecommendationsRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: AiRecommendationsRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[AiRecommendationsRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=AiRecommendationsRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: AiRecommendationsRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[AiRecommendationsRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=AiRecommendationsRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: AiRecommendationsRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[AiRecommendationsRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=AiRecommendationsRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: AiRecommendationsRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[AiRecommendationsRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=AiRecommendationsRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: AiRecommendationsRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[AiRecommendationsRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=AiRecommendationsRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: AiRecommendationsRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[AiRecommendationsRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=AiRecommendationsRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: AiRecommendationsRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[AiRecommendationsRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=AiRecommendationsRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: AiRecommendationsRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[AiRecommendationsRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=AiRecommendationsRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: AiRecommendationsRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[AiRecommendationsRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=AiRecommendationsRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: AiRecommendationsRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[AiRecommendationsRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=AiRecommendationsRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: AiRecommendationsRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[AiRecommendationsRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=AiRecommendationsRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: AiRecommendationsRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[AiRecommendationsRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=AiRecommendationsRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: AiRecommendationsRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[AiRecommendationsRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=AiRecommendationsRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: AiRecommendationsRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[AiRecommendationsRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=AiRecommendationsRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: AiRecommendationsRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[AiRecommendationsRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=AiRecommendationsRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: AiRecommendationsRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[AiRecommendationsRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=AiRecommendationsRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: AiRecommendationsRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[AiRecommendationsRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=AiRecommendationsRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: AiRecommendationsRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[AiRecommendationsRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=AiRecommendationsRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: AiRecommendationsRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[AiRecommendationsRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=AiRecommendationsRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: AiRecommendationsRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[AiRecommendationsRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=AiRecommendationsRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: AiRecommendationsRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[AiRecommendationsRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AiRecommendationsService.list_components_25(db, master_entity_id)
