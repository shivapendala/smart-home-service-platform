from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.system_health import SystemHealthStatus
from app.schemas.system_health import (
    SystemHealthMasterEntityCreate, SystemHealthMasterEntityUpdate, SystemHealthMasterEntityResponse,
    SystemHealthRelationalComponent1Create, SystemHealthRelationalComponent1Response ,SystemHealthRelationalComponent2Create, SystemHealthRelationalComponent2Response ,SystemHealthRelationalComponent3Create, SystemHealthRelationalComponent3Response ,SystemHealthRelationalComponent4Create, SystemHealthRelationalComponent4Response ,SystemHealthRelationalComponent5Create, SystemHealthRelationalComponent5Response ,SystemHealthRelationalComponent6Create, SystemHealthRelationalComponent6Response ,SystemHealthRelationalComponent7Create, SystemHealthRelationalComponent7Response ,SystemHealthRelationalComponent8Create, SystemHealthRelationalComponent8Response ,SystemHealthRelationalComponent9Create, SystemHealthRelationalComponent9Response ,SystemHealthRelationalComponent10Create, SystemHealthRelationalComponent10Response ,SystemHealthRelationalComponent11Create, SystemHealthRelationalComponent11Response ,SystemHealthRelationalComponent12Create, SystemHealthRelationalComponent12Response ,SystemHealthRelationalComponent13Create, SystemHealthRelationalComponent13Response ,SystemHealthRelationalComponent14Create, SystemHealthRelationalComponent14Response ,SystemHealthRelationalComponent15Create, SystemHealthRelationalComponent15Response ,SystemHealthRelationalComponent16Create, SystemHealthRelationalComponent16Response ,SystemHealthRelationalComponent17Create, SystemHealthRelationalComponent17Response ,SystemHealthRelationalComponent18Create, SystemHealthRelationalComponent18Response ,SystemHealthRelationalComponent19Create, SystemHealthRelationalComponent19Response ,SystemHealthRelationalComponent20Create, SystemHealthRelationalComponent20Response ,SystemHealthRelationalComponent21Create, SystemHealthRelationalComponent21Response ,SystemHealthRelationalComponent22Create, SystemHealthRelationalComponent22Response ,SystemHealthRelationalComponent23Create, SystemHealthRelationalComponent23Response ,SystemHealthRelationalComponent24Create, SystemHealthRelationalComponent24Response ,SystemHealthRelationalComponent25Create, SystemHealthRelationalComponent25Response
)
from app.services.system_health_service import SystemHealthService

router = APIRouter()

@router.post("/master", response_model=SystemHealthMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: SystemHealthMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[SystemHealthMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[SystemHealthStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=SystemHealthMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=SystemHealthMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: SystemHealthMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    SystemHealthService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=SystemHealthRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: SystemHealthRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[SystemHealthRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=SystemHealthRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: SystemHealthRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[SystemHealthRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=SystemHealthRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: SystemHealthRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[SystemHealthRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=SystemHealthRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: SystemHealthRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[SystemHealthRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=SystemHealthRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: SystemHealthRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[SystemHealthRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=SystemHealthRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: SystemHealthRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[SystemHealthRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=SystemHealthRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: SystemHealthRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[SystemHealthRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=SystemHealthRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: SystemHealthRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[SystemHealthRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=SystemHealthRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: SystemHealthRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[SystemHealthRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=SystemHealthRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: SystemHealthRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[SystemHealthRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=SystemHealthRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: SystemHealthRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[SystemHealthRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=SystemHealthRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: SystemHealthRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[SystemHealthRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=SystemHealthRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: SystemHealthRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[SystemHealthRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=SystemHealthRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: SystemHealthRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[SystemHealthRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=SystemHealthRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: SystemHealthRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[SystemHealthRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=SystemHealthRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: SystemHealthRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[SystemHealthRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=SystemHealthRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: SystemHealthRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[SystemHealthRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=SystemHealthRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: SystemHealthRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[SystemHealthRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=SystemHealthRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: SystemHealthRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[SystemHealthRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=SystemHealthRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: SystemHealthRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[SystemHealthRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=SystemHealthRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: SystemHealthRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[SystemHealthRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=SystemHealthRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: SystemHealthRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[SystemHealthRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=SystemHealthRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: SystemHealthRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[SystemHealthRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=SystemHealthRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: SystemHealthRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[SystemHealthRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=SystemHealthRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: SystemHealthRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[SystemHealthRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SystemHealthService.list_components_25(db, master_entity_id)

