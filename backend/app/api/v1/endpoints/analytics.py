from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.analytics import AnalyticsStatus
from app.schemas.analytics import (
    AnalyticsMasterEntityCreate, AnalyticsMasterEntityUpdate, AnalyticsMasterEntityResponse,
    AnalyticsRelationalComponent1Create, AnalyticsRelationalComponent1Response ,AnalyticsRelationalComponent2Create, AnalyticsRelationalComponent2Response ,AnalyticsRelationalComponent3Create, AnalyticsRelationalComponent3Response ,AnalyticsRelationalComponent4Create, AnalyticsRelationalComponent4Response ,AnalyticsRelationalComponent5Create, AnalyticsRelationalComponent5Response ,AnalyticsRelationalComponent6Create, AnalyticsRelationalComponent6Response ,AnalyticsRelationalComponent7Create, AnalyticsRelationalComponent7Response ,AnalyticsRelationalComponent8Create, AnalyticsRelationalComponent8Response ,AnalyticsRelationalComponent9Create, AnalyticsRelationalComponent9Response ,AnalyticsRelationalComponent10Create, AnalyticsRelationalComponent10Response ,AnalyticsRelationalComponent11Create, AnalyticsRelationalComponent11Response ,AnalyticsRelationalComponent12Create, AnalyticsRelationalComponent12Response ,AnalyticsRelationalComponent13Create, AnalyticsRelationalComponent13Response ,AnalyticsRelationalComponent14Create, AnalyticsRelationalComponent14Response ,AnalyticsRelationalComponent15Create, AnalyticsRelationalComponent15Response ,AnalyticsRelationalComponent16Create, AnalyticsRelationalComponent16Response ,AnalyticsRelationalComponent17Create, AnalyticsRelationalComponent17Response ,AnalyticsRelationalComponent18Create, AnalyticsRelationalComponent18Response ,AnalyticsRelationalComponent19Create, AnalyticsRelationalComponent19Response ,AnalyticsRelationalComponent20Create, AnalyticsRelationalComponent20Response ,AnalyticsRelationalComponent21Create, AnalyticsRelationalComponent21Response ,AnalyticsRelationalComponent22Create, AnalyticsRelationalComponent22Response ,AnalyticsRelationalComponent23Create, AnalyticsRelationalComponent23Response ,AnalyticsRelationalComponent24Create, AnalyticsRelationalComponent24Response ,AnalyticsRelationalComponent25Create, AnalyticsRelationalComponent25Response
)
from app.services.analytics_service import AnalyticsService

router = APIRouter()

@router.post("/master", response_model=AnalyticsMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: AnalyticsMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[AnalyticsMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[AnalyticsStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=AnalyticsMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=AnalyticsMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: AnalyticsMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    AnalyticsService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=AnalyticsRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: AnalyticsRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[AnalyticsRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=AnalyticsRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: AnalyticsRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[AnalyticsRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=AnalyticsRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: AnalyticsRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[AnalyticsRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=AnalyticsRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: AnalyticsRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[AnalyticsRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=AnalyticsRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: AnalyticsRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[AnalyticsRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=AnalyticsRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: AnalyticsRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[AnalyticsRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=AnalyticsRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: AnalyticsRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[AnalyticsRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=AnalyticsRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: AnalyticsRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[AnalyticsRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=AnalyticsRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: AnalyticsRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[AnalyticsRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=AnalyticsRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: AnalyticsRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[AnalyticsRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=AnalyticsRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: AnalyticsRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[AnalyticsRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=AnalyticsRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: AnalyticsRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[AnalyticsRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=AnalyticsRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: AnalyticsRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[AnalyticsRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=AnalyticsRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: AnalyticsRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[AnalyticsRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=AnalyticsRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: AnalyticsRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[AnalyticsRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=AnalyticsRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: AnalyticsRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[AnalyticsRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=AnalyticsRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: AnalyticsRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[AnalyticsRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=AnalyticsRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: AnalyticsRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[AnalyticsRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=AnalyticsRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: AnalyticsRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[AnalyticsRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=AnalyticsRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: AnalyticsRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[AnalyticsRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=AnalyticsRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: AnalyticsRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[AnalyticsRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=AnalyticsRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: AnalyticsRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[AnalyticsRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=AnalyticsRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: AnalyticsRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[AnalyticsRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=AnalyticsRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: AnalyticsRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[AnalyticsRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=AnalyticsRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: AnalyticsRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[AnalyticsRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AnalyticsService.list_components_25(db, master_entity_id)
