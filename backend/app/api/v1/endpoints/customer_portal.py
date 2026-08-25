from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.customer_portal import CustomerPortalStatus
from app.schemas.customer_portal import (
    CustomerPortalMasterEntityCreate, CustomerPortalMasterEntityUpdate, CustomerPortalMasterEntityResponse,
    CustomerPortalRelationalComponent1Create, CustomerPortalRelationalComponent1Response ,CustomerPortalRelationalComponent2Create, CustomerPortalRelationalComponent2Response ,CustomerPortalRelationalComponent3Create, CustomerPortalRelationalComponent3Response ,CustomerPortalRelationalComponent4Create, CustomerPortalRelationalComponent4Response ,CustomerPortalRelationalComponent5Create, CustomerPortalRelationalComponent5Response ,CustomerPortalRelationalComponent6Create, CustomerPortalRelationalComponent6Response ,CustomerPortalRelationalComponent7Create, CustomerPortalRelationalComponent7Response ,CustomerPortalRelationalComponent8Create, CustomerPortalRelationalComponent8Response ,CustomerPortalRelationalComponent9Create, CustomerPortalRelationalComponent9Response ,CustomerPortalRelationalComponent10Create, CustomerPortalRelationalComponent10Response ,CustomerPortalRelationalComponent11Create, CustomerPortalRelationalComponent11Response ,CustomerPortalRelationalComponent12Create, CustomerPortalRelationalComponent12Response ,CustomerPortalRelationalComponent13Create, CustomerPortalRelationalComponent13Response ,CustomerPortalRelationalComponent14Create, CustomerPortalRelationalComponent14Response ,CustomerPortalRelationalComponent15Create, CustomerPortalRelationalComponent15Response ,CustomerPortalRelationalComponent16Create, CustomerPortalRelationalComponent16Response ,CustomerPortalRelationalComponent17Create, CustomerPortalRelationalComponent17Response ,CustomerPortalRelationalComponent18Create, CustomerPortalRelationalComponent18Response ,CustomerPortalRelationalComponent19Create, CustomerPortalRelationalComponent19Response ,CustomerPortalRelationalComponent20Create, CustomerPortalRelationalComponent20Response ,CustomerPortalRelationalComponent21Create, CustomerPortalRelationalComponent21Response ,CustomerPortalRelationalComponent22Create, CustomerPortalRelationalComponent22Response ,CustomerPortalRelationalComponent23Create, CustomerPortalRelationalComponent23Response ,CustomerPortalRelationalComponent24Create, CustomerPortalRelationalComponent24Response ,CustomerPortalRelationalComponent25Create, CustomerPortalRelationalComponent25Response
)
from app.services.customer_portal_service import CustomerPortalService

router = APIRouter()

@router.post("/master", response_model=CustomerPortalMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: CustomerPortalMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[CustomerPortalMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[CustomerPortalStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=CustomerPortalMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=CustomerPortalMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: CustomerPortalMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    CustomerPortalService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=CustomerPortalRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: CustomerPortalRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[CustomerPortalRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=CustomerPortalRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: CustomerPortalRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[CustomerPortalRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=CustomerPortalRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: CustomerPortalRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[CustomerPortalRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=CustomerPortalRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: CustomerPortalRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[CustomerPortalRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=CustomerPortalRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: CustomerPortalRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[CustomerPortalRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=CustomerPortalRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: CustomerPortalRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[CustomerPortalRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=CustomerPortalRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: CustomerPortalRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[CustomerPortalRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=CustomerPortalRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: CustomerPortalRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[CustomerPortalRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=CustomerPortalRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: CustomerPortalRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[CustomerPortalRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=CustomerPortalRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: CustomerPortalRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[CustomerPortalRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=CustomerPortalRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: CustomerPortalRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[CustomerPortalRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=CustomerPortalRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: CustomerPortalRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[CustomerPortalRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=CustomerPortalRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: CustomerPortalRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[CustomerPortalRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=CustomerPortalRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: CustomerPortalRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[CustomerPortalRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=CustomerPortalRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: CustomerPortalRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[CustomerPortalRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=CustomerPortalRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: CustomerPortalRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[CustomerPortalRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=CustomerPortalRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: CustomerPortalRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[CustomerPortalRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=CustomerPortalRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: CustomerPortalRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[CustomerPortalRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=CustomerPortalRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: CustomerPortalRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[CustomerPortalRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=CustomerPortalRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: CustomerPortalRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[CustomerPortalRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=CustomerPortalRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: CustomerPortalRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[CustomerPortalRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=CustomerPortalRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: CustomerPortalRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[CustomerPortalRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=CustomerPortalRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: CustomerPortalRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[CustomerPortalRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=CustomerPortalRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: CustomerPortalRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[CustomerPortalRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=CustomerPortalRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: CustomerPortalRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[CustomerPortalRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return CustomerPortalService.list_components_25(db, master_entity_id)
