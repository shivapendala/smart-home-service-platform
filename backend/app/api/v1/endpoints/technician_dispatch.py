from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.technician_dispatch import TechnicianDispatchStatus
from app.schemas.technician_dispatch import (
    TechnicianDispatchMasterEntityCreate, TechnicianDispatchMasterEntityUpdate, TechnicianDispatchMasterEntityResponse,
    TechnicianDispatchRelationalComponent1Create, TechnicianDispatchRelationalComponent1Response ,TechnicianDispatchRelationalComponent2Create, TechnicianDispatchRelationalComponent2Response ,TechnicianDispatchRelationalComponent3Create, TechnicianDispatchRelationalComponent3Response ,TechnicianDispatchRelationalComponent4Create, TechnicianDispatchRelationalComponent4Response ,TechnicianDispatchRelationalComponent5Create, TechnicianDispatchRelationalComponent5Response ,TechnicianDispatchRelationalComponent6Create, TechnicianDispatchRelationalComponent6Response ,TechnicianDispatchRelationalComponent7Create, TechnicianDispatchRelationalComponent7Response ,TechnicianDispatchRelationalComponent8Create, TechnicianDispatchRelationalComponent8Response ,TechnicianDispatchRelationalComponent9Create, TechnicianDispatchRelationalComponent9Response ,TechnicianDispatchRelationalComponent10Create, TechnicianDispatchRelationalComponent10Response ,TechnicianDispatchRelationalComponent11Create, TechnicianDispatchRelationalComponent11Response ,TechnicianDispatchRelationalComponent12Create, TechnicianDispatchRelationalComponent12Response ,TechnicianDispatchRelationalComponent13Create, TechnicianDispatchRelationalComponent13Response ,TechnicianDispatchRelationalComponent14Create, TechnicianDispatchRelationalComponent14Response ,TechnicianDispatchRelationalComponent15Create, TechnicianDispatchRelationalComponent15Response ,TechnicianDispatchRelationalComponent16Create, TechnicianDispatchRelationalComponent16Response ,TechnicianDispatchRelationalComponent17Create, TechnicianDispatchRelationalComponent17Response ,TechnicianDispatchRelationalComponent18Create, TechnicianDispatchRelationalComponent18Response ,TechnicianDispatchRelationalComponent19Create, TechnicianDispatchRelationalComponent19Response ,TechnicianDispatchRelationalComponent20Create, TechnicianDispatchRelationalComponent20Response ,TechnicianDispatchRelationalComponent21Create, TechnicianDispatchRelationalComponent21Response ,TechnicianDispatchRelationalComponent22Create, TechnicianDispatchRelationalComponent22Response ,TechnicianDispatchRelationalComponent23Create, TechnicianDispatchRelationalComponent23Response ,TechnicianDispatchRelationalComponent24Create, TechnicianDispatchRelationalComponent24Response ,TechnicianDispatchRelationalComponent25Create, TechnicianDispatchRelationalComponent25Response
)
from app.services.technician_dispatch_service import TechnicianDispatchService

router = APIRouter()

@router.post("/master", response_model=TechnicianDispatchMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: TechnicianDispatchMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[TechnicianDispatchMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[TechnicianDispatchStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=TechnicianDispatchMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=TechnicianDispatchMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: TechnicianDispatchMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    TechnicianDispatchService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=TechnicianDispatchRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: TechnicianDispatchRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[TechnicianDispatchRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=TechnicianDispatchRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: TechnicianDispatchRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[TechnicianDispatchRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=TechnicianDispatchRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: TechnicianDispatchRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[TechnicianDispatchRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=TechnicianDispatchRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: TechnicianDispatchRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[TechnicianDispatchRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=TechnicianDispatchRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: TechnicianDispatchRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[TechnicianDispatchRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=TechnicianDispatchRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: TechnicianDispatchRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[TechnicianDispatchRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=TechnicianDispatchRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: TechnicianDispatchRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[TechnicianDispatchRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=TechnicianDispatchRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: TechnicianDispatchRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[TechnicianDispatchRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=TechnicianDispatchRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: TechnicianDispatchRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[TechnicianDispatchRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=TechnicianDispatchRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: TechnicianDispatchRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[TechnicianDispatchRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=TechnicianDispatchRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: TechnicianDispatchRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[TechnicianDispatchRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=TechnicianDispatchRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: TechnicianDispatchRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[TechnicianDispatchRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=TechnicianDispatchRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: TechnicianDispatchRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[TechnicianDispatchRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=TechnicianDispatchRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: TechnicianDispatchRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[TechnicianDispatchRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=TechnicianDispatchRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: TechnicianDispatchRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[TechnicianDispatchRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=TechnicianDispatchRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: TechnicianDispatchRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[TechnicianDispatchRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=TechnicianDispatchRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: TechnicianDispatchRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[TechnicianDispatchRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=TechnicianDispatchRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: TechnicianDispatchRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[TechnicianDispatchRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=TechnicianDispatchRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: TechnicianDispatchRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[TechnicianDispatchRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=TechnicianDispatchRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: TechnicianDispatchRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[TechnicianDispatchRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=TechnicianDispatchRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: TechnicianDispatchRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[TechnicianDispatchRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=TechnicianDispatchRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: TechnicianDispatchRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[TechnicianDispatchRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=TechnicianDispatchRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: TechnicianDispatchRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[TechnicianDispatchRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=TechnicianDispatchRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: TechnicianDispatchRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[TechnicianDispatchRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=TechnicianDispatchRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: TechnicianDispatchRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[TechnicianDispatchRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianDispatchService.list_components_25(db, master_entity_id)

