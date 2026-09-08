from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.admin_oversight import AdminOversightStatus
from app.schemas.admin_oversight import (
    AdminOversightMasterEntityCreate, AdminOversightMasterEntityUpdate, AdminOversightMasterEntityResponse,
    AdminOversightRelationalComponent1Create, AdminOversightRelationalComponent1Response ,AdminOversightRelationalComponent2Create, AdminOversightRelationalComponent2Response ,AdminOversightRelationalComponent3Create, AdminOversightRelationalComponent3Response ,AdminOversightRelationalComponent4Create, AdminOversightRelationalComponent4Response ,AdminOversightRelationalComponent5Create, AdminOversightRelationalComponent5Response ,AdminOversightRelationalComponent6Create, AdminOversightRelationalComponent6Response ,AdminOversightRelationalComponent7Create, AdminOversightRelationalComponent7Response ,AdminOversightRelationalComponent8Create, AdminOversightRelationalComponent8Response ,AdminOversightRelationalComponent9Create, AdminOversightRelationalComponent9Response ,AdminOversightRelationalComponent10Create, AdminOversightRelationalComponent10Response ,AdminOversightRelationalComponent11Create, AdminOversightRelationalComponent11Response ,AdminOversightRelationalComponent12Create, AdminOversightRelationalComponent12Response ,AdminOversightRelationalComponent13Create, AdminOversightRelationalComponent13Response ,AdminOversightRelationalComponent14Create, AdminOversightRelationalComponent14Response ,AdminOversightRelationalComponent15Create, AdminOversightRelationalComponent15Response ,AdminOversightRelationalComponent16Create, AdminOversightRelationalComponent16Response ,AdminOversightRelationalComponent17Create, AdminOversightRelationalComponent17Response ,AdminOversightRelationalComponent18Create, AdminOversightRelationalComponent18Response ,AdminOversightRelationalComponent19Create, AdminOversightRelationalComponent19Response ,AdminOversightRelationalComponent20Create, AdminOversightRelationalComponent20Response ,AdminOversightRelationalComponent21Create, AdminOversightRelationalComponent21Response ,AdminOversightRelationalComponent22Create, AdminOversightRelationalComponent22Response ,AdminOversightRelationalComponent23Create, AdminOversightRelationalComponent23Response ,AdminOversightRelationalComponent24Create, AdminOversightRelationalComponent24Response ,AdminOversightRelationalComponent25Create, AdminOversightRelationalComponent25Response
)
from app.services.admin_oversight_service import AdminOversightService

router = APIRouter()

@router.post("/master", response_model=AdminOversightMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: AdminOversightMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[AdminOversightMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[AdminOversightStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=AdminOversightMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=AdminOversightMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: AdminOversightMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    AdminOversightService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=AdminOversightRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: AdminOversightRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[AdminOversightRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=AdminOversightRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: AdminOversightRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[AdminOversightRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=AdminOversightRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: AdminOversightRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[AdminOversightRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=AdminOversightRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: AdminOversightRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[AdminOversightRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=AdminOversightRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: AdminOversightRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[AdminOversightRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=AdminOversightRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: AdminOversightRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[AdminOversightRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=AdminOversightRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: AdminOversightRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[AdminOversightRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=AdminOversightRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: AdminOversightRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[AdminOversightRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=AdminOversightRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: AdminOversightRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[AdminOversightRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=AdminOversightRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: AdminOversightRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[AdminOversightRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=AdminOversightRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: AdminOversightRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[AdminOversightRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=AdminOversightRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: AdminOversightRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[AdminOversightRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=AdminOversightRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: AdminOversightRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[AdminOversightRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=AdminOversightRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: AdminOversightRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[AdminOversightRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=AdminOversightRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: AdminOversightRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[AdminOversightRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=AdminOversightRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: AdminOversightRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[AdminOversightRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=AdminOversightRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: AdminOversightRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[AdminOversightRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=AdminOversightRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: AdminOversightRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[AdminOversightRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=AdminOversightRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: AdminOversightRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[AdminOversightRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=AdminOversightRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: AdminOversightRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[AdminOversightRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=AdminOversightRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: AdminOversightRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[AdminOversightRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=AdminOversightRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: AdminOversightRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[AdminOversightRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=AdminOversightRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: AdminOversightRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[AdminOversightRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=AdminOversightRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: AdminOversightRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[AdminOversightRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=AdminOversightRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: AdminOversightRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[AdminOversightRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AdminOversightService.list_components_25(db, master_entity_id)

