from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.communication import CommunicationStatus
from app.schemas.communication import (
    CommunicationMasterEntityCreate, CommunicationMasterEntityUpdate, CommunicationMasterEntityResponse,
    CommunicationRelationalComponent1Create, CommunicationRelationalComponent1Response ,CommunicationRelationalComponent2Create, CommunicationRelationalComponent2Response ,CommunicationRelationalComponent3Create, CommunicationRelationalComponent3Response ,CommunicationRelationalComponent4Create, CommunicationRelationalComponent4Response ,CommunicationRelationalComponent5Create, CommunicationRelationalComponent5Response ,CommunicationRelationalComponent6Create, CommunicationRelationalComponent6Response ,CommunicationRelationalComponent7Create, CommunicationRelationalComponent7Response ,CommunicationRelationalComponent8Create, CommunicationRelationalComponent8Response ,CommunicationRelationalComponent9Create, CommunicationRelationalComponent9Response ,CommunicationRelationalComponent10Create, CommunicationRelationalComponent10Response ,CommunicationRelationalComponent11Create, CommunicationRelationalComponent11Response ,CommunicationRelationalComponent12Create, CommunicationRelationalComponent12Response ,CommunicationRelationalComponent13Create, CommunicationRelationalComponent13Response ,CommunicationRelationalComponent14Create, CommunicationRelationalComponent14Response ,CommunicationRelationalComponent15Create, CommunicationRelationalComponent15Response ,CommunicationRelationalComponent16Create, CommunicationRelationalComponent16Response ,CommunicationRelationalComponent17Create, CommunicationRelationalComponent17Response ,CommunicationRelationalComponent18Create, CommunicationRelationalComponent18Response ,CommunicationRelationalComponent19Create, CommunicationRelationalComponent19Response ,CommunicationRelationalComponent20Create, CommunicationRelationalComponent20Response ,CommunicationRelationalComponent21Create, CommunicationRelationalComponent21Response ,CommunicationRelationalComponent22Create, CommunicationRelationalComponent22Response ,CommunicationRelationalComponent23Create, CommunicationRelationalComponent23Response ,CommunicationRelationalComponent24Create, CommunicationRelationalComponent24Response ,CommunicationRelationalComponent25Create, CommunicationRelationalComponent25Response
)
from app.services.communication_service import CommunicationService

router = APIRouter()

@router.post("/master", response_model=CommunicationMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: CommunicationMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[CommunicationMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[CommunicationStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=CommunicationMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=CommunicationMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: CommunicationMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    CommunicationService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=CommunicationRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: CommunicationRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[CommunicationRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=CommunicationRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: CommunicationRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[CommunicationRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=CommunicationRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: CommunicationRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[CommunicationRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=CommunicationRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: CommunicationRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[CommunicationRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=CommunicationRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: CommunicationRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[CommunicationRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=CommunicationRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: CommunicationRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[CommunicationRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=CommunicationRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: CommunicationRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[CommunicationRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=CommunicationRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: CommunicationRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[CommunicationRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=CommunicationRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: CommunicationRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[CommunicationRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=CommunicationRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: CommunicationRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[CommunicationRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=CommunicationRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: CommunicationRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[CommunicationRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=CommunicationRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: CommunicationRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[CommunicationRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=CommunicationRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: CommunicationRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[CommunicationRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=CommunicationRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: CommunicationRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[CommunicationRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=CommunicationRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: CommunicationRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[CommunicationRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=CommunicationRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: CommunicationRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[CommunicationRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=CommunicationRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: CommunicationRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[CommunicationRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=CommunicationRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: CommunicationRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[CommunicationRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=CommunicationRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: CommunicationRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[CommunicationRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=CommunicationRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: CommunicationRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[CommunicationRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=CommunicationRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: CommunicationRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[CommunicationRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=CommunicationRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: CommunicationRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[CommunicationRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=CommunicationRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: CommunicationRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[CommunicationRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=CommunicationRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: CommunicationRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[CommunicationRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=CommunicationRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: CommunicationRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[CommunicationRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CommunicationService.list_components_25(db, master_entity_id)
