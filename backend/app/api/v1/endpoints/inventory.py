from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.inventory import InventoryStatus
from app.schemas.inventory import (
    InventoryMasterEntityCreate, InventoryMasterEntityUpdate, InventoryMasterEntityResponse,
    InventoryRelationalComponent1Create, InventoryRelationalComponent1Response ,InventoryRelationalComponent2Create, InventoryRelationalComponent2Response ,InventoryRelationalComponent3Create, InventoryRelationalComponent3Response ,InventoryRelationalComponent4Create, InventoryRelationalComponent4Response ,InventoryRelationalComponent5Create, InventoryRelationalComponent5Response ,InventoryRelationalComponent6Create, InventoryRelationalComponent6Response ,InventoryRelationalComponent7Create, InventoryRelationalComponent7Response ,InventoryRelationalComponent8Create, InventoryRelationalComponent8Response ,InventoryRelationalComponent9Create, InventoryRelationalComponent9Response ,InventoryRelationalComponent10Create, InventoryRelationalComponent10Response ,InventoryRelationalComponent11Create, InventoryRelationalComponent11Response ,InventoryRelationalComponent12Create, InventoryRelationalComponent12Response ,InventoryRelationalComponent13Create, InventoryRelationalComponent13Response ,InventoryRelationalComponent14Create, InventoryRelationalComponent14Response ,InventoryRelationalComponent15Create, InventoryRelationalComponent15Response ,InventoryRelationalComponent16Create, InventoryRelationalComponent16Response ,InventoryRelationalComponent17Create, InventoryRelationalComponent17Response ,InventoryRelationalComponent18Create, InventoryRelationalComponent18Response ,InventoryRelationalComponent19Create, InventoryRelationalComponent19Response ,InventoryRelationalComponent20Create, InventoryRelationalComponent20Response ,InventoryRelationalComponent21Create, InventoryRelationalComponent21Response ,InventoryRelationalComponent22Create, InventoryRelationalComponent22Response ,InventoryRelationalComponent23Create, InventoryRelationalComponent23Response ,InventoryRelationalComponent24Create, InventoryRelationalComponent24Response ,InventoryRelationalComponent25Create, InventoryRelationalComponent25Response
)
from app.services.inventory_service import InventoryService

router = APIRouter()

@router.post("/master", response_model=InventoryMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: InventoryMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[InventoryMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[InventoryStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=InventoryMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=InventoryMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: InventoryMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    InventoryService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=InventoryRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: InventoryRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[InventoryRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=InventoryRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: InventoryRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[InventoryRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=InventoryRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: InventoryRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[InventoryRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=InventoryRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: InventoryRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[InventoryRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=InventoryRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: InventoryRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[InventoryRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=InventoryRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: InventoryRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[InventoryRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=InventoryRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: InventoryRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[InventoryRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=InventoryRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: InventoryRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[InventoryRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=InventoryRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: InventoryRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[InventoryRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=InventoryRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: InventoryRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[InventoryRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=InventoryRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: InventoryRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[InventoryRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=InventoryRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: InventoryRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[InventoryRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=InventoryRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: InventoryRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[InventoryRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=InventoryRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: InventoryRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[InventoryRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=InventoryRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: InventoryRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[InventoryRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=InventoryRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: InventoryRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[InventoryRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=InventoryRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: InventoryRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[InventoryRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=InventoryRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: InventoryRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[InventoryRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=InventoryRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: InventoryRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[InventoryRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=InventoryRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: InventoryRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[InventoryRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=InventoryRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: InventoryRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[InventoryRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=InventoryRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: InventoryRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[InventoryRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=InventoryRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: InventoryRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[InventoryRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=InventoryRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: InventoryRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[InventoryRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=InventoryRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: InventoryRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[InventoryRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return InventoryService.list_components_25(db, master_entity_id)
