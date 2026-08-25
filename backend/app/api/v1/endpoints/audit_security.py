from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.audit_security import AuditSecurityStatus
from app.schemas.audit_security import (
    AuditSecurityMasterEntityCreate, AuditSecurityMasterEntityUpdate, AuditSecurityMasterEntityResponse,
    AuditSecurityRelationalComponent1Create, AuditSecurityRelationalComponent1Response ,AuditSecurityRelationalComponent2Create, AuditSecurityRelationalComponent2Response ,AuditSecurityRelationalComponent3Create, AuditSecurityRelationalComponent3Response ,AuditSecurityRelationalComponent4Create, AuditSecurityRelationalComponent4Response ,AuditSecurityRelationalComponent5Create, AuditSecurityRelationalComponent5Response ,AuditSecurityRelationalComponent6Create, AuditSecurityRelationalComponent6Response ,AuditSecurityRelationalComponent7Create, AuditSecurityRelationalComponent7Response ,AuditSecurityRelationalComponent8Create, AuditSecurityRelationalComponent8Response ,AuditSecurityRelationalComponent9Create, AuditSecurityRelationalComponent9Response ,AuditSecurityRelationalComponent10Create, AuditSecurityRelationalComponent10Response ,AuditSecurityRelationalComponent11Create, AuditSecurityRelationalComponent11Response ,AuditSecurityRelationalComponent12Create, AuditSecurityRelationalComponent12Response ,AuditSecurityRelationalComponent13Create, AuditSecurityRelationalComponent13Response ,AuditSecurityRelationalComponent14Create, AuditSecurityRelationalComponent14Response ,AuditSecurityRelationalComponent15Create, AuditSecurityRelationalComponent15Response ,AuditSecurityRelationalComponent16Create, AuditSecurityRelationalComponent16Response ,AuditSecurityRelationalComponent17Create, AuditSecurityRelationalComponent17Response ,AuditSecurityRelationalComponent18Create, AuditSecurityRelationalComponent18Response ,AuditSecurityRelationalComponent19Create, AuditSecurityRelationalComponent19Response ,AuditSecurityRelationalComponent20Create, AuditSecurityRelationalComponent20Response ,AuditSecurityRelationalComponent21Create, AuditSecurityRelationalComponent21Response ,AuditSecurityRelationalComponent22Create, AuditSecurityRelationalComponent22Response ,AuditSecurityRelationalComponent23Create, AuditSecurityRelationalComponent23Response ,AuditSecurityRelationalComponent24Create, AuditSecurityRelationalComponent24Response ,AuditSecurityRelationalComponent25Create, AuditSecurityRelationalComponent25Response
)
from app.services.audit_security_service import AuditSecurityService

router = APIRouter()

@router.post("/master", response_model=AuditSecurityMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: AuditSecurityMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[AuditSecurityMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[AuditSecurityStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=AuditSecurityMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=AuditSecurityMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: AuditSecurityMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    AuditSecurityService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=AuditSecurityRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: AuditSecurityRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[AuditSecurityRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=AuditSecurityRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: AuditSecurityRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[AuditSecurityRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=AuditSecurityRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: AuditSecurityRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[AuditSecurityRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=AuditSecurityRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: AuditSecurityRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[AuditSecurityRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=AuditSecurityRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: AuditSecurityRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[AuditSecurityRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=AuditSecurityRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: AuditSecurityRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[AuditSecurityRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=AuditSecurityRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: AuditSecurityRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[AuditSecurityRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=AuditSecurityRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: AuditSecurityRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[AuditSecurityRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=AuditSecurityRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: AuditSecurityRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[AuditSecurityRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=AuditSecurityRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: AuditSecurityRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[AuditSecurityRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=AuditSecurityRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: AuditSecurityRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[AuditSecurityRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=AuditSecurityRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: AuditSecurityRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[AuditSecurityRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=AuditSecurityRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: AuditSecurityRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[AuditSecurityRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=AuditSecurityRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: AuditSecurityRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[AuditSecurityRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=AuditSecurityRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: AuditSecurityRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[AuditSecurityRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=AuditSecurityRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: AuditSecurityRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[AuditSecurityRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=AuditSecurityRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: AuditSecurityRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[AuditSecurityRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=AuditSecurityRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: AuditSecurityRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[AuditSecurityRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=AuditSecurityRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: AuditSecurityRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[AuditSecurityRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=AuditSecurityRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: AuditSecurityRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[AuditSecurityRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=AuditSecurityRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: AuditSecurityRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[AuditSecurityRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=AuditSecurityRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: AuditSecurityRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[AuditSecurityRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=AuditSecurityRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: AuditSecurityRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[AuditSecurityRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=AuditSecurityRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: AuditSecurityRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[AuditSecurityRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=AuditSecurityRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: AuditSecurityRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[AuditSecurityRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return AuditSecurityService.list_components_25(db, master_entity_id)
