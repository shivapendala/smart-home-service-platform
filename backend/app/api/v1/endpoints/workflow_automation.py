from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.workflow_automation import WorkflowAutomationStatus
from app.schemas.workflow_automation import (
    WorkflowAutomationMasterEntityCreate, WorkflowAutomationMasterEntityUpdate, WorkflowAutomationMasterEntityResponse,
    WorkflowAutomationRelationalComponent1Create, WorkflowAutomationRelationalComponent1Response ,WorkflowAutomationRelationalComponent2Create, WorkflowAutomationRelationalComponent2Response ,WorkflowAutomationRelationalComponent3Create, WorkflowAutomationRelationalComponent3Response ,WorkflowAutomationRelationalComponent4Create, WorkflowAutomationRelationalComponent4Response ,WorkflowAutomationRelationalComponent5Create, WorkflowAutomationRelationalComponent5Response ,WorkflowAutomationRelationalComponent6Create, WorkflowAutomationRelationalComponent6Response ,WorkflowAutomationRelationalComponent7Create, WorkflowAutomationRelationalComponent7Response ,WorkflowAutomationRelationalComponent8Create, WorkflowAutomationRelationalComponent8Response ,WorkflowAutomationRelationalComponent9Create, WorkflowAutomationRelationalComponent9Response ,WorkflowAutomationRelationalComponent10Create, WorkflowAutomationRelationalComponent10Response ,WorkflowAutomationRelationalComponent11Create, WorkflowAutomationRelationalComponent11Response ,WorkflowAutomationRelationalComponent12Create, WorkflowAutomationRelationalComponent12Response ,WorkflowAutomationRelationalComponent13Create, WorkflowAutomationRelationalComponent13Response ,WorkflowAutomationRelationalComponent14Create, WorkflowAutomationRelationalComponent14Response ,WorkflowAutomationRelationalComponent15Create, WorkflowAutomationRelationalComponent15Response ,WorkflowAutomationRelationalComponent16Create, WorkflowAutomationRelationalComponent16Response ,WorkflowAutomationRelationalComponent17Create, WorkflowAutomationRelationalComponent17Response ,WorkflowAutomationRelationalComponent18Create, WorkflowAutomationRelationalComponent18Response ,WorkflowAutomationRelationalComponent19Create, WorkflowAutomationRelationalComponent19Response ,WorkflowAutomationRelationalComponent20Create, WorkflowAutomationRelationalComponent20Response ,WorkflowAutomationRelationalComponent21Create, WorkflowAutomationRelationalComponent21Response ,WorkflowAutomationRelationalComponent22Create, WorkflowAutomationRelationalComponent22Response ,WorkflowAutomationRelationalComponent23Create, WorkflowAutomationRelationalComponent23Response ,WorkflowAutomationRelationalComponent24Create, WorkflowAutomationRelationalComponent24Response ,WorkflowAutomationRelationalComponent25Create, WorkflowAutomationRelationalComponent25Response
)
from app.services.workflow_automation_service import WorkflowAutomationService

router = APIRouter()

@router.post("/master", response_model=WorkflowAutomationMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: WorkflowAutomationMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[WorkflowAutomationMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[WorkflowAutomationStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=WorkflowAutomationMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=WorkflowAutomationMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: WorkflowAutomationMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    WorkflowAutomationService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=WorkflowAutomationRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: WorkflowAutomationRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[WorkflowAutomationRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=WorkflowAutomationRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: WorkflowAutomationRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[WorkflowAutomationRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=WorkflowAutomationRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: WorkflowAutomationRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[WorkflowAutomationRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=WorkflowAutomationRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: WorkflowAutomationRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[WorkflowAutomationRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=WorkflowAutomationRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: WorkflowAutomationRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[WorkflowAutomationRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=WorkflowAutomationRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: WorkflowAutomationRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[WorkflowAutomationRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=WorkflowAutomationRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: WorkflowAutomationRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[WorkflowAutomationRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=WorkflowAutomationRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: WorkflowAutomationRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[WorkflowAutomationRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=WorkflowAutomationRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: WorkflowAutomationRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[WorkflowAutomationRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=WorkflowAutomationRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: WorkflowAutomationRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[WorkflowAutomationRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=WorkflowAutomationRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: WorkflowAutomationRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[WorkflowAutomationRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=WorkflowAutomationRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: WorkflowAutomationRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[WorkflowAutomationRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=WorkflowAutomationRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: WorkflowAutomationRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[WorkflowAutomationRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=WorkflowAutomationRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: WorkflowAutomationRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[WorkflowAutomationRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=WorkflowAutomationRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: WorkflowAutomationRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[WorkflowAutomationRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=WorkflowAutomationRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: WorkflowAutomationRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[WorkflowAutomationRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=WorkflowAutomationRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: WorkflowAutomationRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[WorkflowAutomationRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=WorkflowAutomationRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: WorkflowAutomationRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[WorkflowAutomationRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=WorkflowAutomationRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: WorkflowAutomationRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[WorkflowAutomationRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=WorkflowAutomationRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: WorkflowAutomationRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[WorkflowAutomationRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=WorkflowAutomationRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: WorkflowAutomationRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[WorkflowAutomationRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=WorkflowAutomationRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: WorkflowAutomationRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[WorkflowAutomationRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=WorkflowAutomationRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: WorkflowAutomationRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[WorkflowAutomationRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=WorkflowAutomationRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: WorkflowAutomationRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[WorkflowAutomationRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=WorkflowAutomationRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: WorkflowAutomationRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[WorkflowAutomationRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return WorkflowAutomationService.list_components_25(db, master_entity_id)

