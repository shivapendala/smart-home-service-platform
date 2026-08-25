from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.platform_governance import PlatformGovernanceStatus
from app.schemas.platform_governance import (
    PlatformGovernanceMasterEntityCreate, PlatformGovernanceMasterEntityUpdate, PlatformGovernanceMasterEntityResponse,
    PlatformGovernanceRelationalComponent1Create, PlatformGovernanceRelationalComponent1Response ,PlatformGovernanceRelationalComponent2Create, PlatformGovernanceRelationalComponent2Response ,PlatformGovernanceRelationalComponent3Create, PlatformGovernanceRelationalComponent3Response ,PlatformGovernanceRelationalComponent4Create, PlatformGovernanceRelationalComponent4Response ,PlatformGovernanceRelationalComponent5Create, PlatformGovernanceRelationalComponent5Response ,PlatformGovernanceRelationalComponent6Create, PlatformGovernanceRelationalComponent6Response ,PlatformGovernanceRelationalComponent7Create, PlatformGovernanceRelationalComponent7Response ,PlatformGovernanceRelationalComponent8Create, PlatformGovernanceRelationalComponent8Response ,PlatformGovernanceRelationalComponent9Create, PlatformGovernanceRelationalComponent9Response ,PlatformGovernanceRelationalComponent10Create, PlatformGovernanceRelationalComponent10Response ,PlatformGovernanceRelationalComponent11Create, PlatformGovernanceRelationalComponent11Response ,PlatformGovernanceRelationalComponent12Create, PlatformGovernanceRelationalComponent12Response ,PlatformGovernanceRelationalComponent13Create, PlatformGovernanceRelationalComponent13Response ,PlatformGovernanceRelationalComponent14Create, PlatformGovernanceRelationalComponent14Response ,PlatformGovernanceRelationalComponent15Create, PlatformGovernanceRelationalComponent15Response ,PlatformGovernanceRelationalComponent16Create, PlatformGovernanceRelationalComponent16Response ,PlatformGovernanceRelationalComponent17Create, PlatformGovernanceRelationalComponent17Response ,PlatformGovernanceRelationalComponent18Create, PlatformGovernanceRelationalComponent18Response ,PlatformGovernanceRelationalComponent19Create, PlatformGovernanceRelationalComponent19Response ,PlatformGovernanceRelationalComponent20Create, PlatformGovernanceRelationalComponent20Response ,PlatformGovernanceRelationalComponent21Create, PlatformGovernanceRelationalComponent21Response ,PlatformGovernanceRelationalComponent22Create, PlatformGovernanceRelationalComponent22Response ,PlatformGovernanceRelationalComponent23Create, PlatformGovernanceRelationalComponent23Response ,PlatformGovernanceRelationalComponent24Create, PlatformGovernanceRelationalComponent24Response ,PlatformGovernanceRelationalComponent25Create, PlatformGovernanceRelationalComponent25Response
)
from app.services.platform_governance_service import PlatformGovernanceService

router = APIRouter()

@router.post("/master", response_model=PlatformGovernanceMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: PlatformGovernanceMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[PlatformGovernanceMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[PlatformGovernanceStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=PlatformGovernanceMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=PlatformGovernanceMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: PlatformGovernanceMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    PlatformGovernanceService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=PlatformGovernanceRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: PlatformGovernanceRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[PlatformGovernanceRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=PlatformGovernanceRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: PlatformGovernanceRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[PlatformGovernanceRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=PlatformGovernanceRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: PlatformGovernanceRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[PlatformGovernanceRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=PlatformGovernanceRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: PlatformGovernanceRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[PlatformGovernanceRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=PlatformGovernanceRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: PlatformGovernanceRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[PlatformGovernanceRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=PlatformGovernanceRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: PlatformGovernanceRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[PlatformGovernanceRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=PlatformGovernanceRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: PlatformGovernanceRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[PlatformGovernanceRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=PlatformGovernanceRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: PlatformGovernanceRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[PlatformGovernanceRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=PlatformGovernanceRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: PlatformGovernanceRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[PlatformGovernanceRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=PlatformGovernanceRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: PlatformGovernanceRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[PlatformGovernanceRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=PlatformGovernanceRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: PlatformGovernanceRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[PlatformGovernanceRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=PlatformGovernanceRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: PlatformGovernanceRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[PlatformGovernanceRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=PlatformGovernanceRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: PlatformGovernanceRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[PlatformGovernanceRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=PlatformGovernanceRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: PlatformGovernanceRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[PlatformGovernanceRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=PlatformGovernanceRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: PlatformGovernanceRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[PlatformGovernanceRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=PlatformGovernanceRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: PlatformGovernanceRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[PlatformGovernanceRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=PlatformGovernanceRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: PlatformGovernanceRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[PlatformGovernanceRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=PlatformGovernanceRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: PlatformGovernanceRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[PlatformGovernanceRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=PlatformGovernanceRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: PlatformGovernanceRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[PlatformGovernanceRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=PlatformGovernanceRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: PlatformGovernanceRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[PlatformGovernanceRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=PlatformGovernanceRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: PlatformGovernanceRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[PlatformGovernanceRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=PlatformGovernanceRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: PlatformGovernanceRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[PlatformGovernanceRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=PlatformGovernanceRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: PlatformGovernanceRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[PlatformGovernanceRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=PlatformGovernanceRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: PlatformGovernanceRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[PlatformGovernanceRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=PlatformGovernanceRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: PlatformGovernanceRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[PlatformGovernanceRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PlatformGovernanceService.list_components_25(db, master_entity_id)
