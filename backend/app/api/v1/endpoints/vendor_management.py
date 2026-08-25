from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.vendor_management import VendorManagementStatus
from app.schemas.vendor_management import (
    VendorManagementMasterEntityCreate, VendorManagementMasterEntityUpdate, VendorManagementMasterEntityResponse,
    VendorManagementRelationalComponent1Create, VendorManagementRelationalComponent1Response ,VendorManagementRelationalComponent2Create, VendorManagementRelationalComponent2Response ,VendorManagementRelationalComponent3Create, VendorManagementRelationalComponent3Response ,VendorManagementRelationalComponent4Create, VendorManagementRelationalComponent4Response ,VendorManagementRelationalComponent5Create, VendorManagementRelationalComponent5Response ,VendorManagementRelationalComponent6Create, VendorManagementRelationalComponent6Response ,VendorManagementRelationalComponent7Create, VendorManagementRelationalComponent7Response ,VendorManagementRelationalComponent8Create, VendorManagementRelationalComponent8Response ,VendorManagementRelationalComponent9Create, VendorManagementRelationalComponent9Response ,VendorManagementRelationalComponent10Create, VendorManagementRelationalComponent10Response ,VendorManagementRelationalComponent11Create, VendorManagementRelationalComponent11Response ,VendorManagementRelationalComponent12Create, VendorManagementRelationalComponent12Response ,VendorManagementRelationalComponent13Create, VendorManagementRelationalComponent13Response ,VendorManagementRelationalComponent14Create, VendorManagementRelationalComponent14Response ,VendorManagementRelationalComponent15Create, VendorManagementRelationalComponent15Response ,VendorManagementRelationalComponent16Create, VendorManagementRelationalComponent16Response ,VendorManagementRelationalComponent17Create, VendorManagementRelationalComponent17Response ,VendorManagementRelationalComponent18Create, VendorManagementRelationalComponent18Response ,VendorManagementRelationalComponent19Create, VendorManagementRelationalComponent19Response ,VendorManagementRelationalComponent20Create, VendorManagementRelationalComponent20Response ,VendorManagementRelationalComponent21Create, VendorManagementRelationalComponent21Response ,VendorManagementRelationalComponent22Create, VendorManagementRelationalComponent22Response ,VendorManagementRelationalComponent23Create, VendorManagementRelationalComponent23Response ,VendorManagementRelationalComponent24Create, VendorManagementRelationalComponent24Response ,VendorManagementRelationalComponent25Create, VendorManagementRelationalComponent25Response
)
from app.services.vendor_management_service import VendorManagementService

router = APIRouter()

@router.post("/master", response_model=VendorManagementMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: VendorManagementMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[VendorManagementMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[VendorManagementStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=VendorManagementMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=VendorManagementMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: VendorManagementMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    VendorManagementService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=VendorManagementRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: VendorManagementRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[VendorManagementRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=VendorManagementRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: VendorManagementRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[VendorManagementRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=VendorManagementRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: VendorManagementRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[VendorManagementRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=VendorManagementRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: VendorManagementRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[VendorManagementRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=VendorManagementRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: VendorManagementRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[VendorManagementRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=VendorManagementRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: VendorManagementRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[VendorManagementRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=VendorManagementRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: VendorManagementRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[VendorManagementRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=VendorManagementRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: VendorManagementRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[VendorManagementRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=VendorManagementRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: VendorManagementRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[VendorManagementRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=VendorManagementRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: VendorManagementRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[VendorManagementRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=VendorManagementRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: VendorManagementRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[VendorManagementRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=VendorManagementRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: VendorManagementRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[VendorManagementRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=VendorManagementRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: VendorManagementRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[VendorManagementRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=VendorManagementRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: VendorManagementRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[VendorManagementRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=VendorManagementRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: VendorManagementRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[VendorManagementRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=VendorManagementRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: VendorManagementRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[VendorManagementRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=VendorManagementRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: VendorManagementRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[VendorManagementRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=VendorManagementRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: VendorManagementRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[VendorManagementRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=VendorManagementRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: VendorManagementRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[VendorManagementRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=VendorManagementRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: VendorManagementRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[VendorManagementRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=VendorManagementRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: VendorManagementRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[VendorManagementRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=VendorManagementRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: VendorManagementRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[VendorManagementRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=VendorManagementRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: VendorManagementRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[VendorManagementRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=VendorManagementRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: VendorManagementRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[VendorManagementRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=VendorManagementRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: VendorManagementRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[VendorManagementRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return VendorManagementService.list_components_25(db, master_entity_id)

