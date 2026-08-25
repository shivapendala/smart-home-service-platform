from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.fleet_logistics import FleetLogisticsStatus
from app.schemas.fleet_logistics import (
    FleetLogisticsMasterEntityCreate, FleetLogisticsMasterEntityUpdate, FleetLogisticsMasterEntityResponse,
    FleetLogisticsRelationalComponent1Create, FleetLogisticsRelationalComponent1Response ,FleetLogisticsRelationalComponent2Create, FleetLogisticsRelationalComponent2Response ,FleetLogisticsRelationalComponent3Create, FleetLogisticsRelationalComponent3Response ,FleetLogisticsRelationalComponent4Create, FleetLogisticsRelationalComponent4Response ,FleetLogisticsRelationalComponent5Create, FleetLogisticsRelationalComponent5Response ,FleetLogisticsRelationalComponent6Create, FleetLogisticsRelationalComponent6Response ,FleetLogisticsRelationalComponent7Create, FleetLogisticsRelationalComponent7Response ,FleetLogisticsRelationalComponent8Create, FleetLogisticsRelationalComponent8Response ,FleetLogisticsRelationalComponent9Create, FleetLogisticsRelationalComponent9Response ,FleetLogisticsRelationalComponent10Create, FleetLogisticsRelationalComponent10Response ,FleetLogisticsRelationalComponent11Create, FleetLogisticsRelationalComponent11Response ,FleetLogisticsRelationalComponent12Create, FleetLogisticsRelationalComponent12Response ,FleetLogisticsRelationalComponent13Create, FleetLogisticsRelationalComponent13Response ,FleetLogisticsRelationalComponent14Create, FleetLogisticsRelationalComponent14Response ,FleetLogisticsRelationalComponent15Create, FleetLogisticsRelationalComponent15Response ,FleetLogisticsRelationalComponent16Create, FleetLogisticsRelationalComponent16Response ,FleetLogisticsRelationalComponent17Create, FleetLogisticsRelationalComponent17Response ,FleetLogisticsRelationalComponent18Create, FleetLogisticsRelationalComponent18Response ,FleetLogisticsRelationalComponent19Create, FleetLogisticsRelationalComponent19Response ,FleetLogisticsRelationalComponent20Create, FleetLogisticsRelationalComponent20Response ,FleetLogisticsRelationalComponent21Create, FleetLogisticsRelationalComponent21Response ,FleetLogisticsRelationalComponent22Create, FleetLogisticsRelationalComponent22Response ,FleetLogisticsRelationalComponent23Create, FleetLogisticsRelationalComponent23Response ,FleetLogisticsRelationalComponent24Create, FleetLogisticsRelationalComponent24Response ,FleetLogisticsRelationalComponent25Create, FleetLogisticsRelationalComponent25Response
)
from app.services.fleet_logistics_service import FleetLogisticsService

router = APIRouter()

@router.post("/master", response_model=FleetLogisticsMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: FleetLogisticsMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[FleetLogisticsMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[FleetLogisticsStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=FleetLogisticsMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=FleetLogisticsMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: FleetLogisticsMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    FleetLogisticsService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=FleetLogisticsRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: FleetLogisticsRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[FleetLogisticsRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=FleetLogisticsRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: FleetLogisticsRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[FleetLogisticsRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=FleetLogisticsRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: FleetLogisticsRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[FleetLogisticsRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=FleetLogisticsRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: FleetLogisticsRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[FleetLogisticsRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=FleetLogisticsRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: FleetLogisticsRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[FleetLogisticsRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=FleetLogisticsRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: FleetLogisticsRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[FleetLogisticsRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=FleetLogisticsRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: FleetLogisticsRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[FleetLogisticsRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=FleetLogisticsRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: FleetLogisticsRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[FleetLogisticsRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=FleetLogisticsRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: FleetLogisticsRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[FleetLogisticsRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=FleetLogisticsRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: FleetLogisticsRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[FleetLogisticsRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=FleetLogisticsRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: FleetLogisticsRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[FleetLogisticsRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=FleetLogisticsRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: FleetLogisticsRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[FleetLogisticsRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=FleetLogisticsRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: FleetLogisticsRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[FleetLogisticsRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=FleetLogisticsRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: FleetLogisticsRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[FleetLogisticsRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=FleetLogisticsRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: FleetLogisticsRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[FleetLogisticsRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=FleetLogisticsRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: FleetLogisticsRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[FleetLogisticsRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=FleetLogisticsRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: FleetLogisticsRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[FleetLogisticsRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=FleetLogisticsRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: FleetLogisticsRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[FleetLogisticsRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=FleetLogisticsRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: FleetLogisticsRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[FleetLogisticsRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=FleetLogisticsRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: FleetLogisticsRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[FleetLogisticsRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=FleetLogisticsRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: FleetLogisticsRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[FleetLogisticsRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=FleetLogisticsRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: FleetLogisticsRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[FleetLogisticsRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=FleetLogisticsRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: FleetLogisticsRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[FleetLogisticsRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=FleetLogisticsRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: FleetLogisticsRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[FleetLogisticsRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=FleetLogisticsRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: FleetLogisticsRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[FleetLogisticsRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FleetLogisticsService.list_components_25(db, master_entity_id)
