from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.enterprise_integration import EnterpriseIntegrationStatus
from app.schemas.enterprise_integration import (
    EnterpriseIntegrationMasterEntityCreate, EnterpriseIntegrationMasterEntityUpdate, EnterpriseIntegrationMasterEntityResponse,
    EnterpriseIntegrationRelationalComponent1Create, EnterpriseIntegrationRelationalComponent1Response ,EnterpriseIntegrationRelationalComponent2Create, EnterpriseIntegrationRelationalComponent2Response ,EnterpriseIntegrationRelationalComponent3Create, EnterpriseIntegrationRelationalComponent3Response ,EnterpriseIntegrationRelationalComponent4Create, EnterpriseIntegrationRelationalComponent4Response ,EnterpriseIntegrationRelationalComponent5Create, EnterpriseIntegrationRelationalComponent5Response ,EnterpriseIntegrationRelationalComponent6Create, EnterpriseIntegrationRelationalComponent6Response ,EnterpriseIntegrationRelationalComponent7Create, EnterpriseIntegrationRelationalComponent7Response ,EnterpriseIntegrationRelationalComponent8Create, EnterpriseIntegrationRelationalComponent8Response ,EnterpriseIntegrationRelationalComponent9Create, EnterpriseIntegrationRelationalComponent9Response ,EnterpriseIntegrationRelationalComponent10Create, EnterpriseIntegrationRelationalComponent10Response ,EnterpriseIntegrationRelationalComponent11Create, EnterpriseIntegrationRelationalComponent11Response ,EnterpriseIntegrationRelationalComponent12Create, EnterpriseIntegrationRelationalComponent12Response ,EnterpriseIntegrationRelationalComponent13Create, EnterpriseIntegrationRelationalComponent13Response ,EnterpriseIntegrationRelationalComponent14Create, EnterpriseIntegrationRelationalComponent14Response ,EnterpriseIntegrationRelationalComponent15Create, EnterpriseIntegrationRelationalComponent15Response ,EnterpriseIntegrationRelationalComponent16Create, EnterpriseIntegrationRelationalComponent16Response ,EnterpriseIntegrationRelationalComponent17Create, EnterpriseIntegrationRelationalComponent17Response ,EnterpriseIntegrationRelationalComponent18Create, EnterpriseIntegrationRelationalComponent18Response ,EnterpriseIntegrationRelationalComponent19Create, EnterpriseIntegrationRelationalComponent19Response ,EnterpriseIntegrationRelationalComponent20Create, EnterpriseIntegrationRelationalComponent20Response ,EnterpriseIntegrationRelationalComponent21Create, EnterpriseIntegrationRelationalComponent21Response ,EnterpriseIntegrationRelationalComponent22Create, EnterpriseIntegrationRelationalComponent22Response ,EnterpriseIntegrationRelationalComponent23Create, EnterpriseIntegrationRelationalComponent23Response ,EnterpriseIntegrationRelationalComponent24Create, EnterpriseIntegrationRelationalComponent24Response ,EnterpriseIntegrationRelationalComponent25Create, EnterpriseIntegrationRelationalComponent25Response
)
from app.services.enterprise_integration_service import EnterpriseIntegrationService

router = APIRouter()

@router.post("/master", response_model=EnterpriseIntegrationMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: EnterpriseIntegrationMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[EnterpriseIntegrationMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[EnterpriseIntegrationStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=EnterpriseIntegrationMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=EnterpriseIntegrationMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: EnterpriseIntegrationMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    EnterpriseIntegrationService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=EnterpriseIntegrationRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: EnterpriseIntegrationRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[EnterpriseIntegrationRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=EnterpriseIntegrationRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: EnterpriseIntegrationRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[EnterpriseIntegrationRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=EnterpriseIntegrationRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: EnterpriseIntegrationRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[EnterpriseIntegrationRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=EnterpriseIntegrationRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: EnterpriseIntegrationRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[EnterpriseIntegrationRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=EnterpriseIntegrationRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: EnterpriseIntegrationRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[EnterpriseIntegrationRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=EnterpriseIntegrationRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: EnterpriseIntegrationRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[EnterpriseIntegrationRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=EnterpriseIntegrationRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: EnterpriseIntegrationRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[EnterpriseIntegrationRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=EnterpriseIntegrationRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: EnterpriseIntegrationRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[EnterpriseIntegrationRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=EnterpriseIntegrationRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: EnterpriseIntegrationRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[EnterpriseIntegrationRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=EnterpriseIntegrationRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: EnterpriseIntegrationRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[EnterpriseIntegrationRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=EnterpriseIntegrationRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: EnterpriseIntegrationRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[EnterpriseIntegrationRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=EnterpriseIntegrationRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: EnterpriseIntegrationRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[EnterpriseIntegrationRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=EnterpriseIntegrationRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: EnterpriseIntegrationRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[EnterpriseIntegrationRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=EnterpriseIntegrationRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: EnterpriseIntegrationRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[EnterpriseIntegrationRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=EnterpriseIntegrationRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: EnterpriseIntegrationRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[EnterpriseIntegrationRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=EnterpriseIntegrationRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: EnterpriseIntegrationRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[EnterpriseIntegrationRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=EnterpriseIntegrationRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: EnterpriseIntegrationRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[EnterpriseIntegrationRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=EnterpriseIntegrationRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: EnterpriseIntegrationRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[EnterpriseIntegrationRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=EnterpriseIntegrationRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: EnterpriseIntegrationRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[EnterpriseIntegrationRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=EnterpriseIntegrationRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: EnterpriseIntegrationRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[EnterpriseIntegrationRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=EnterpriseIntegrationRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: EnterpriseIntegrationRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[EnterpriseIntegrationRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=EnterpriseIntegrationRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: EnterpriseIntegrationRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[EnterpriseIntegrationRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=EnterpriseIntegrationRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: EnterpriseIntegrationRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[EnterpriseIntegrationRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=EnterpriseIntegrationRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: EnterpriseIntegrationRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[EnterpriseIntegrationRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=EnterpriseIntegrationRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: EnterpriseIntegrationRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[EnterpriseIntegrationRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return EnterpriseIntegrationService.list_components_25(db, master_entity_id)
