from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.financial_reporting import FinancialReportingStatus
from app.schemas.financial_reporting import (
    FinancialReportingMasterEntityCreate, FinancialReportingMasterEntityUpdate, FinancialReportingMasterEntityResponse,
    FinancialReportingRelationalComponent1Create, FinancialReportingRelationalComponent1Response ,FinancialReportingRelationalComponent2Create, FinancialReportingRelationalComponent2Response ,FinancialReportingRelationalComponent3Create, FinancialReportingRelationalComponent3Response ,FinancialReportingRelationalComponent4Create, FinancialReportingRelationalComponent4Response ,FinancialReportingRelationalComponent5Create, FinancialReportingRelationalComponent5Response ,FinancialReportingRelationalComponent6Create, FinancialReportingRelationalComponent6Response ,FinancialReportingRelationalComponent7Create, FinancialReportingRelationalComponent7Response ,FinancialReportingRelationalComponent8Create, FinancialReportingRelationalComponent8Response ,FinancialReportingRelationalComponent9Create, FinancialReportingRelationalComponent9Response ,FinancialReportingRelationalComponent10Create, FinancialReportingRelationalComponent10Response ,FinancialReportingRelationalComponent11Create, FinancialReportingRelationalComponent11Response ,FinancialReportingRelationalComponent12Create, FinancialReportingRelationalComponent12Response ,FinancialReportingRelationalComponent13Create, FinancialReportingRelationalComponent13Response ,FinancialReportingRelationalComponent14Create, FinancialReportingRelationalComponent14Response ,FinancialReportingRelationalComponent15Create, FinancialReportingRelationalComponent15Response ,FinancialReportingRelationalComponent16Create, FinancialReportingRelationalComponent16Response ,FinancialReportingRelationalComponent17Create, FinancialReportingRelationalComponent17Response ,FinancialReportingRelationalComponent18Create, FinancialReportingRelationalComponent18Response ,FinancialReportingRelationalComponent19Create, FinancialReportingRelationalComponent19Response ,FinancialReportingRelationalComponent20Create, FinancialReportingRelationalComponent20Response ,FinancialReportingRelationalComponent21Create, FinancialReportingRelationalComponent21Response ,FinancialReportingRelationalComponent22Create, FinancialReportingRelationalComponent22Response ,FinancialReportingRelationalComponent23Create, FinancialReportingRelationalComponent23Response ,FinancialReportingRelationalComponent24Create, FinancialReportingRelationalComponent24Response ,FinancialReportingRelationalComponent25Create, FinancialReportingRelationalComponent25Response
)
from app.services.financial_reporting_service import FinancialReportingService

router = APIRouter()

@router.post("/master", response_model=FinancialReportingMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: FinancialReportingMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[FinancialReportingMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[FinancialReportingStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=FinancialReportingMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=FinancialReportingMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: FinancialReportingMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    FinancialReportingService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=FinancialReportingRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: FinancialReportingRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[FinancialReportingRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=FinancialReportingRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: FinancialReportingRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[FinancialReportingRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=FinancialReportingRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: FinancialReportingRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[FinancialReportingRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=FinancialReportingRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: FinancialReportingRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[FinancialReportingRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=FinancialReportingRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: FinancialReportingRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[FinancialReportingRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=FinancialReportingRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: FinancialReportingRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[FinancialReportingRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=FinancialReportingRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: FinancialReportingRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[FinancialReportingRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=FinancialReportingRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: FinancialReportingRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[FinancialReportingRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=FinancialReportingRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: FinancialReportingRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[FinancialReportingRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=FinancialReportingRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: FinancialReportingRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[FinancialReportingRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=FinancialReportingRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: FinancialReportingRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[FinancialReportingRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=FinancialReportingRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: FinancialReportingRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[FinancialReportingRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=FinancialReportingRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: FinancialReportingRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[FinancialReportingRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=FinancialReportingRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: FinancialReportingRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[FinancialReportingRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=FinancialReportingRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: FinancialReportingRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[FinancialReportingRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=FinancialReportingRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: FinancialReportingRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[FinancialReportingRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=FinancialReportingRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: FinancialReportingRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[FinancialReportingRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=FinancialReportingRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: FinancialReportingRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[FinancialReportingRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=FinancialReportingRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: FinancialReportingRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[FinancialReportingRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=FinancialReportingRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: FinancialReportingRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[FinancialReportingRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=FinancialReportingRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: FinancialReportingRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[FinancialReportingRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=FinancialReportingRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: FinancialReportingRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[FinancialReportingRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=FinancialReportingRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: FinancialReportingRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[FinancialReportingRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=FinancialReportingRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: FinancialReportingRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[FinancialReportingRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=FinancialReportingRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: FinancialReportingRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[FinancialReportingRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return FinancialReportingService.list_components_25(db, master_entity_id)

