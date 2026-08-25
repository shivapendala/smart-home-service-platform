from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.technician_mgmt import TechnicianMgmtStatus
from app.schemas.technician_mgmt import (
    TechnicianMgmtMasterEntityCreate, TechnicianMgmtMasterEntityUpdate, TechnicianMgmtMasterEntityResponse,
    TechnicianMgmtRelationalComponent1Create, TechnicianMgmtRelationalComponent1Response ,TechnicianMgmtRelationalComponent2Create, TechnicianMgmtRelationalComponent2Response ,TechnicianMgmtRelationalComponent3Create, TechnicianMgmtRelationalComponent3Response ,TechnicianMgmtRelationalComponent4Create, TechnicianMgmtRelationalComponent4Response ,TechnicianMgmtRelationalComponent5Create, TechnicianMgmtRelationalComponent5Response ,TechnicianMgmtRelationalComponent6Create, TechnicianMgmtRelationalComponent6Response ,TechnicianMgmtRelationalComponent7Create, TechnicianMgmtRelationalComponent7Response ,TechnicianMgmtRelationalComponent8Create, TechnicianMgmtRelationalComponent8Response ,TechnicianMgmtRelationalComponent9Create, TechnicianMgmtRelationalComponent9Response ,TechnicianMgmtRelationalComponent10Create, TechnicianMgmtRelationalComponent10Response ,TechnicianMgmtRelationalComponent11Create, TechnicianMgmtRelationalComponent11Response ,TechnicianMgmtRelationalComponent12Create, TechnicianMgmtRelationalComponent12Response ,TechnicianMgmtRelationalComponent13Create, TechnicianMgmtRelationalComponent13Response ,TechnicianMgmtRelationalComponent14Create, TechnicianMgmtRelationalComponent14Response ,TechnicianMgmtRelationalComponent15Create, TechnicianMgmtRelationalComponent15Response ,TechnicianMgmtRelationalComponent16Create, TechnicianMgmtRelationalComponent16Response ,TechnicianMgmtRelationalComponent17Create, TechnicianMgmtRelationalComponent17Response ,TechnicianMgmtRelationalComponent18Create, TechnicianMgmtRelationalComponent18Response ,TechnicianMgmtRelationalComponent19Create, TechnicianMgmtRelationalComponent19Response ,TechnicianMgmtRelationalComponent20Create, TechnicianMgmtRelationalComponent20Response ,TechnicianMgmtRelationalComponent21Create, TechnicianMgmtRelationalComponent21Response ,TechnicianMgmtRelationalComponent22Create, TechnicianMgmtRelationalComponent22Response ,TechnicianMgmtRelationalComponent23Create, TechnicianMgmtRelationalComponent23Response ,TechnicianMgmtRelationalComponent24Create, TechnicianMgmtRelationalComponent24Response ,TechnicianMgmtRelationalComponent25Create, TechnicianMgmtRelationalComponent25Response
)
from app.services.technician_mgmt_service import TechnicianMgmtService

router = APIRouter()

@router.post("/master", response_model=TechnicianMgmtMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: TechnicianMgmtMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[TechnicianMgmtMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[TechnicianMgmtStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=TechnicianMgmtMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=TechnicianMgmtMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: TechnicianMgmtMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    TechnicianMgmtService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=TechnicianMgmtRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: TechnicianMgmtRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[TechnicianMgmtRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=TechnicianMgmtRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: TechnicianMgmtRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[TechnicianMgmtRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=TechnicianMgmtRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: TechnicianMgmtRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[TechnicianMgmtRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=TechnicianMgmtRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: TechnicianMgmtRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[TechnicianMgmtRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=TechnicianMgmtRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: TechnicianMgmtRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[TechnicianMgmtRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=TechnicianMgmtRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: TechnicianMgmtRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[TechnicianMgmtRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=TechnicianMgmtRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: TechnicianMgmtRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[TechnicianMgmtRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=TechnicianMgmtRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: TechnicianMgmtRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[TechnicianMgmtRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=TechnicianMgmtRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: TechnicianMgmtRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[TechnicianMgmtRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=TechnicianMgmtRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: TechnicianMgmtRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[TechnicianMgmtRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=TechnicianMgmtRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: TechnicianMgmtRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[TechnicianMgmtRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=TechnicianMgmtRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: TechnicianMgmtRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[TechnicianMgmtRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=TechnicianMgmtRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: TechnicianMgmtRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[TechnicianMgmtRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=TechnicianMgmtRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: TechnicianMgmtRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[TechnicianMgmtRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=TechnicianMgmtRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: TechnicianMgmtRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[TechnicianMgmtRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=TechnicianMgmtRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: TechnicianMgmtRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[TechnicianMgmtRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=TechnicianMgmtRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: TechnicianMgmtRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[TechnicianMgmtRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=TechnicianMgmtRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: TechnicianMgmtRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[TechnicianMgmtRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=TechnicianMgmtRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: TechnicianMgmtRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[TechnicianMgmtRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=TechnicianMgmtRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: TechnicianMgmtRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[TechnicianMgmtRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=TechnicianMgmtRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: TechnicianMgmtRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[TechnicianMgmtRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=TechnicianMgmtRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: TechnicianMgmtRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[TechnicianMgmtRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=TechnicianMgmtRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: TechnicianMgmtRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[TechnicianMgmtRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=TechnicianMgmtRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: TechnicianMgmtRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[TechnicianMgmtRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=TechnicianMgmtRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: TechnicianMgmtRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[TechnicianMgmtRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return TechnicianMgmtService.list_components_25(db, master_entity_id)
