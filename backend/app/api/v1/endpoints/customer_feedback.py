from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.customer_feedback import CustomerFeedbackStatus
from app.schemas.customer_feedback import (
    CustomerFeedbackMasterEntityCreate, CustomerFeedbackMasterEntityUpdate, CustomerFeedbackMasterEntityResponse,
    CustomerFeedbackRelationalComponent1Create, CustomerFeedbackRelationalComponent1Response ,CustomerFeedbackRelationalComponent2Create, CustomerFeedbackRelationalComponent2Response ,CustomerFeedbackRelationalComponent3Create, CustomerFeedbackRelationalComponent3Response ,CustomerFeedbackRelationalComponent4Create, CustomerFeedbackRelationalComponent4Response ,CustomerFeedbackRelationalComponent5Create, CustomerFeedbackRelationalComponent5Response ,CustomerFeedbackRelationalComponent6Create, CustomerFeedbackRelationalComponent6Response ,CustomerFeedbackRelationalComponent7Create, CustomerFeedbackRelationalComponent7Response ,CustomerFeedbackRelationalComponent8Create, CustomerFeedbackRelationalComponent8Response ,CustomerFeedbackRelationalComponent9Create, CustomerFeedbackRelationalComponent9Response ,CustomerFeedbackRelationalComponent10Create, CustomerFeedbackRelationalComponent10Response ,CustomerFeedbackRelationalComponent11Create, CustomerFeedbackRelationalComponent11Response ,CustomerFeedbackRelationalComponent12Create, CustomerFeedbackRelationalComponent12Response ,CustomerFeedbackRelationalComponent13Create, CustomerFeedbackRelationalComponent13Response ,CustomerFeedbackRelationalComponent14Create, CustomerFeedbackRelationalComponent14Response ,CustomerFeedbackRelationalComponent15Create, CustomerFeedbackRelationalComponent15Response ,CustomerFeedbackRelationalComponent16Create, CustomerFeedbackRelationalComponent16Response ,CustomerFeedbackRelationalComponent17Create, CustomerFeedbackRelationalComponent17Response ,CustomerFeedbackRelationalComponent18Create, CustomerFeedbackRelationalComponent18Response ,CustomerFeedbackRelationalComponent19Create, CustomerFeedbackRelationalComponent19Response ,CustomerFeedbackRelationalComponent20Create, CustomerFeedbackRelationalComponent20Response ,CustomerFeedbackRelationalComponent21Create, CustomerFeedbackRelationalComponent21Response ,CustomerFeedbackRelationalComponent22Create, CustomerFeedbackRelationalComponent22Response ,CustomerFeedbackRelationalComponent23Create, CustomerFeedbackRelationalComponent23Response ,CustomerFeedbackRelationalComponent24Create, CustomerFeedbackRelationalComponent24Response ,CustomerFeedbackRelationalComponent25Create, CustomerFeedbackRelationalComponent25Response
)
from app.services.customer_feedback_service import CustomerFeedbackService

router = APIRouter()

@router.post("/master", response_model=CustomerFeedbackMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: CustomerFeedbackMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[CustomerFeedbackMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[CustomerFeedbackStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=CustomerFeedbackMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=CustomerFeedbackMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: CustomerFeedbackMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    CustomerFeedbackService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=CustomerFeedbackRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: CustomerFeedbackRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[CustomerFeedbackRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=CustomerFeedbackRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: CustomerFeedbackRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[CustomerFeedbackRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=CustomerFeedbackRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: CustomerFeedbackRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[CustomerFeedbackRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=CustomerFeedbackRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: CustomerFeedbackRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[CustomerFeedbackRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=CustomerFeedbackRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: CustomerFeedbackRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[CustomerFeedbackRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=CustomerFeedbackRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: CustomerFeedbackRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[CustomerFeedbackRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=CustomerFeedbackRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: CustomerFeedbackRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[CustomerFeedbackRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=CustomerFeedbackRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: CustomerFeedbackRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[CustomerFeedbackRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=CustomerFeedbackRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: CustomerFeedbackRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[CustomerFeedbackRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=CustomerFeedbackRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: CustomerFeedbackRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[CustomerFeedbackRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=CustomerFeedbackRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: CustomerFeedbackRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[CustomerFeedbackRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=CustomerFeedbackRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: CustomerFeedbackRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[CustomerFeedbackRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=CustomerFeedbackRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: CustomerFeedbackRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[CustomerFeedbackRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=CustomerFeedbackRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: CustomerFeedbackRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[CustomerFeedbackRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=CustomerFeedbackRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: CustomerFeedbackRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[CustomerFeedbackRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=CustomerFeedbackRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: CustomerFeedbackRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[CustomerFeedbackRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=CustomerFeedbackRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: CustomerFeedbackRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[CustomerFeedbackRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=CustomerFeedbackRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: CustomerFeedbackRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[CustomerFeedbackRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=CustomerFeedbackRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: CustomerFeedbackRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[CustomerFeedbackRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=CustomerFeedbackRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: CustomerFeedbackRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[CustomerFeedbackRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=CustomerFeedbackRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: CustomerFeedbackRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[CustomerFeedbackRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=CustomerFeedbackRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: CustomerFeedbackRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[CustomerFeedbackRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=CustomerFeedbackRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: CustomerFeedbackRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[CustomerFeedbackRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=CustomerFeedbackRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: CustomerFeedbackRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[CustomerFeedbackRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=CustomerFeedbackRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: CustomerFeedbackRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[CustomerFeedbackRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerFeedbackService.list_components_25(db, master_entity_id)

