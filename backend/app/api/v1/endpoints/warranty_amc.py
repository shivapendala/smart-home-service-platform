from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.warranty_amc import WarrantyAmcStatus
from app.schemas.warranty_amc import (
    WarrantyAmcMasterEntityCreate, WarrantyAmcMasterEntityUpdate, WarrantyAmcMasterEntityResponse,
    WarrantyAmcRelationalComponent1Create, WarrantyAmcRelationalComponent1Response ,WarrantyAmcRelationalComponent2Create, WarrantyAmcRelationalComponent2Response ,WarrantyAmcRelationalComponent3Create, WarrantyAmcRelationalComponent3Response ,WarrantyAmcRelationalComponent4Create, WarrantyAmcRelationalComponent4Response ,WarrantyAmcRelationalComponent5Create, WarrantyAmcRelationalComponent5Response ,WarrantyAmcRelationalComponent6Create, WarrantyAmcRelationalComponent6Response ,WarrantyAmcRelationalComponent7Create, WarrantyAmcRelationalComponent7Response ,WarrantyAmcRelationalComponent8Create, WarrantyAmcRelationalComponent8Response ,WarrantyAmcRelationalComponent9Create, WarrantyAmcRelationalComponent9Response ,WarrantyAmcRelationalComponent10Create, WarrantyAmcRelationalComponent10Response ,WarrantyAmcRelationalComponent11Create, WarrantyAmcRelationalComponent11Response ,WarrantyAmcRelationalComponent12Create, WarrantyAmcRelationalComponent12Response ,WarrantyAmcRelationalComponent13Create, WarrantyAmcRelationalComponent13Response ,WarrantyAmcRelationalComponent14Create, WarrantyAmcRelationalComponent14Response ,WarrantyAmcRelationalComponent15Create, WarrantyAmcRelationalComponent15Response ,WarrantyAmcRelationalComponent16Create, WarrantyAmcRelationalComponent16Response ,WarrantyAmcRelationalComponent17Create, WarrantyAmcRelationalComponent17Response ,WarrantyAmcRelationalComponent18Create, WarrantyAmcRelationalComponent18Response ,WarrantyAmcRelationalComponent19Create, WarrantyAmcRelationalComponent19Response ,WarrantyAmcRelationalComponent20Create, WarrantyAmcRelationalComponent20Response ,WarrantyAmcRelationalComponent21Create, WarrantyAmcRelationalComponent21Response ,WarrantyAmcRelationalComponent22Create, WarrantyAmcRelationalComponent22Response ,WarrantyAmcRelationalComponent23Create, WarrantyAmcRelationalComponent23Response ,WarrantyAmcRelationalComponent24Create, WarrantyAmcRelationalComponent24Response ,WarrantyAmcRelationalComponent25Create, WarrantyAmcRelationalComponent25Response
)
from app.services.warranty_amc_service import WarrantyAmcService

router = APIRouter()

@router.post("/master", response_model=WarrantyAmcMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: WarrantyAmcMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[WarrantyAmcMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[WarrantyAmcStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=WarrantyAmcMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=WarrantyAmcMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: WarrantyAmcMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    WarrantyAmcService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=WarrantyAmcRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: WarrantyAmcRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[WarrantyAmcRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=WarrantyAmcRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: WarrantyAmcRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[WarrantyAmcRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=WarrantyAmcRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: WarrantyAmcRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[WarrantyAmcRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=WarrantyAmcRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: WarrantyAmcRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[WarrantyAmcRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=WarrantyAmcRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: WarrantyAmcRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[WarrantyAmcRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=WarrantyAmcRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: WarrantyAmcRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[WarrantyAmcRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=WarrantyAmcRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: WarrantyAmcRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[WarrantyAmcRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=WarrantyAmcRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: WarrantyAmcRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[WarrantyAmcRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=WarrantyAmcRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: WarrantyAmcRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[WarrantyAmcRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=WarrantyAmcRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: WarrantyAmcRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[WarrantyAmcRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=WarrantyAmcRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: WarrantyAmcRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[WarrantyAmcRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=WarrantyAmcRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: WarrantyAmcRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[WarrantyAmcRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=WarrantyAmcRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: WarrantyAmcRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[WarrantyAmcRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=WarrantyAmcRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: WarrantyAmcRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[WarrantyAmcRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=WarrantyAmcRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: WarrantyAmcRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[WarrantyAmcRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=WarrantyAmcRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: WarrantyAmcRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[WarrantyAmcRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=WarrantyAmcRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: WarrantyAmcRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[WarrantyAmcRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=WarrantyAmcRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: WarrantyAmcRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[WarrantyAmcRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=WarrantyAmcRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: WarrantyAmcRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[WarrantyAmcRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=WarrantyAmcRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: WarrantyAmcRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[WarrantyAmcRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=WarrantyAmcRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: WarrantyAmcRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[WarrantyAmcRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=WarrantyAmcRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: WarrantyAmcRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[WarrantyAmcRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=WarrantyAmcRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: WarrantyAmcRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[WarrantyAmcRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=WarrantyAmcRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: WarrantyAmcRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[WarrantyAmcRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=WarrantyAmcRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: WarrantyAmcRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[WarrantyAmcRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WarrantyAmcService.list_components_25(db, master_entity_id)
