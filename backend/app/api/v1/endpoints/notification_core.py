from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.notification_core import NotificationCoreStatus
from app.schemas.notification_core import (
    NotificationCoreMasterEntityCreate, NotificationCoreMasterEntityUpdate, NotificationCoreMasterEntityResponse,
    NotificationCoreRelationalComponent1Create, NotificationCoreRelationalComponent1Response ,NotificationCoreRelationalComponent2Create, NotificationCoreRelationalComponent2Response ,NotificationCoreRelationalComponent3Create, NotificationCoreRelationalComponent3Response ,NotificationCoreRelationalComponent4Create, NotificationCoreRelationalComponent4Response ,NotificationCoreRelationalComponent5Create, NotificationCoreRelationalComponent5Response ,NotificationCoreRelationalComponent6Create, NotificationCoreRelationalComponent6Response ,NotificationCoreRelationalComponent7Create, NotificationCoreRelationalComponent7Response ,NotificationCoreRelationalComponent8Create, NotificationCoreRelationalComponent8Response ,NotificationCoreRelationalComponent9Create, NotificationCoreRelationalComponent9Response ,NotificationCoreRelationalComponent10Create, NotificationCoreRelationalComponent10Response ,NotificationCoreRelationalComponent11Create, NotificationCoreRelationalComponent11Response ,NotificationCoreRelationalComponent12Create, NotificationCoreRelationalComponent12Response ,NotificationCoreRelationalComponent13Create, NotificationCoreRelationalComponent13Response ,NotificationCoreRelationalComponent14Create, NotificationCoreRelationalComponent14Response ,NotificationCoreRelationalComponent15Create, NotificationCoreRelationalComponent15Response ,NotificationCoreRelationalComponent16Create, NotificationCoreRelationalComponent16Response ,NotificationCoreRelationalComponent17Create, NotificationCoreRelationalComponent17Response ,NotificationCoreRelationalComponent18Create, NotificationCoreRelationalComponent18Response ,NotificationCoreRelationalComponent19Create, NotificationCoreRelationalComponent19Response ,NotificationCoreRelationalComponent20Create, NotificationCoreRelationalComponent20Response ,NotificationCoreRelationalComponent21Create, NotificationCoreRelationalComponent21Response ,NotificationCoreRelationalComponent22Create, NotificationCoreRelationalComponent22Response ,NotificationCoreRelationalComponent23Create, NotificationCoreRelationalComponent23Response ,NotificationCoreRelationalComponent24Create, NotificationCoreRelationalComponent24Response ,NotificationCoreRelationalComponent25Create, NotificationCoreRelationalComponent25Response
)
from app.services.notification_core_service import NotificationCoreService

router = APIRouter()

@router.post("/master", response_model=NotificationCoreMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: NotificationCoreMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[NotificationCoreMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[NotificationCoreStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=NotificationCoreMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=NotificationCoreMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: NotificationCoreMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    NotificationCoreService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=NotificationCoreRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: NotificationCoreRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[NotificationCoreRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=NotificationCoreRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: NotificationCoreRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[NotificationCoreRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=NotificationCoreRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: NotificationCoreRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[NotificationCoreRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=NotificationCoreRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: NotificationCoreRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[NotificationCoreRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=NotificationCoreRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: NotificationCoreRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[NotificationCoreRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=NotificationCoreRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: NotificationCoreRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[NotificationCoreRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=NotificationCoreRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: NotificationCoreRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[NotificationCoreRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=NotificationCoreRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: NotificationCoreRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[NotificationCoreRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=NotificationCoreRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: NotificationCoreRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[NotificationCoreRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=NotificationCoreRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: NotificationCoreRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[NotificationCoreRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=NotificationCoreRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: NotificationCoreRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[NotificationCoreRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=NotificationCoreRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: NotificationCoreRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[NotificationCoreRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=NotificationCoreRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: NotificationCoreRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[NotificationCoreRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=NotificationCoreRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: NotificationCoreRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[NotificationCoreRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=NotificationCoreRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: NotificationCoreRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[NotificationCoreRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=NotificationCoreRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: NotificationCoreRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[NotificationCoreRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=NotificationCoreRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: NotificationCoreRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[NotificationCoreRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=NotificationCoreRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: NotificationCoreRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[NotificationCoreRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=NotificationCoreRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: NotificationCoreRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[NotificationCoreRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=NotificationCoreRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: NotificationCoreRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[NotificationCoreRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=NotificationCoreRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: NotificationCoreRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[NotificationCoreRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=NotificationCoreRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: NotificationCoreRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[NotificationCoreRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=NotificationCoreRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: NotificationCoreRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[NotificationCoreRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=NotificationCoreRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: NotificationCoreRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[NotificationCoreRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=NotificationCoreRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: NotificationCoreRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[NotificationCoreRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return NotificationCoreService.list_components_25(db, master_entity_id)
