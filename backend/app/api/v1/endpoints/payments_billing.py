from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.payments_billing import PaymentsBillingStatus
from app.schemas.payments_billing import (
    PaymentsBillingMasterEntityCreate, PaymentsBillingMasterEntityUpdate, PaymentsBillingMasterEntityResponse,
    PaymentsBillingRelationalComponent1Create, PaymentsBillingRelationalComponent1Response ,PaymentsBillingRelationalComponent2Create, PaymentsBillingRelationalComponent2Response ,PaymentsBillingRelationalComponent3Create, PaymentsBillingRelationalComponent3Response ,PaymentsBillingRelationalComponent4Create, PaymentsBillingRelationalComponent4Response ,PaymentsBillingRelationalComponent5Create, PaymentsBillingRelationalComponent5Response ,PaymentsBillingRelationalComponent6Create, PaymentsBillingRelationalComponent6Response ,PaymentsBillingRelationalComponent7Create, PaymentsBillingRelationalComponent7Response ,PaymentsBillingRelationalComponent8Create, PaymentsBillingRelationalComponent8Response ,PaymentsBillingRelationalComponent9Create, PaymentsBillingRelationalComponent9Response ,PaymentsBillingRelationalComponent10Create, PaymentsBillingRelationalComponent10Response ,PaymentsBillingRelationalComponent11Create, PaymentsBillingRelationalComponent11Response ,PaymentsBillingRelationalComponent12Create, PaymentsBillingRelationalComponent12Response ,PaymentsBillingRelationalComponent13Create, PaymentsBillingRelationalComponent13Response ,PaymentsBillingRelationalComponent14Create, PaymentsBillingRelationalComponent14Response ,PaymentsBillingRelationalComponent15Create, PaymentsBillingRelationalComponent15Response ,PaymentsBillingRelationalComponent16Create, PaymentsBillingRelationalComponent16Response ,PaymentsBillingRelationalComponent17Create, PaymentsBillingRelationalComponent17Response ,PaymentsBillingRelationalComponent18Create, PaymentsBillingRelationalComponent18Response ,PaymentsBillingRelationalComponent19Create, PaymentsBillingRelationalComponent19Response ,PaymentsBillingRelationalComponent20Create, PaymentsBillingRelationalComponent20Response ,PaymentsBillingRelationalComponent21Create, PaymentsBillingRelationalComponent21Response ,PaymentsBillingRelationalComponent22Create, PaymentsBillingRelationalComponent22Response ,PaymentsBillingRelationalComponent23Create, PaymentsBillingRelationalComponent23Response ,PaymentsBillingRelationalComponent24Create, PaymentsBillingRelationalComponent24Response ,PaymentsBillingRelationalComponent25Create, PaymentsBillingRelationalComponent25Response
)
from app.services.payments_billing_service import PaymentsBillingService

router = APIRouter()

@router.post("/master", response_model=PaymentsBillingMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: PaymentsBillingMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[PaymentsBillingMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[PaymentsBillingStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=PaymentsBillingMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=PaymentsBillingMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: PaymentsBillingMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    PaymentsBillingService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=PaymentsBillingRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: PaymentsBillingRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[PaymentsBillingRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=PaymentsBillingRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: PaymentsBillingRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[PaymentsBillingRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=PaymentsBillingRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: PaymentsBillingRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[PaymentsBillingRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=PaymentsBillingRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: PaymentsBillingRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[PaymentsBillingRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=PaymentsBillingRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: PaymentsBillingRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[PaymentsBillingRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=PaymentsBillingRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: PaymentsBillingRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[PaymentsBillingRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=PaymentsBillingRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: PaymentsBillingRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[PaymentsBillingRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=PaymentsBillingRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: PaymentsBillingRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[PaymentsBillingRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=PaymentsBillingRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: PaymentsBillingRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[PaymentsBillingRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=PaymentsBillingRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: PaymentsBillingRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[PaymentsBillingRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=PaymentsBillingRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: PaymentsBillingRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[PaymentsBillingRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=PaymentsBillingRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: PaymentsBillingRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[PaymentsBillingRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=PaymentsBillingRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: PaymentsBillingRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[PaymentsBillingRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=PaymentsBillingRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: PaymentsBillingRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[PaymentsBillingRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=PaymentsBillingRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: PaymentsBillingRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[PaymentsBillingRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=PaymentsBillingRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: PaymentsBillingRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[PaymentsBillingRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=PaymentsBillingRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: PaymentsBillingRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[PaymentsBillingRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=PaymentsBillingRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: PaymentsBillingRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[PaymentsBillingRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=PaymentsBillingRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: PaymentsBillingRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[PaymentsBillingRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=PaymentsBillingRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: PaymentsBillingRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[PaymentsBillingRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=PaymentsBillingRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: PaymentsBillingRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[PaymentsBillingRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=PaymentsBillingRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: PaymentsBillingRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[PaymentsBillingRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=PaymentsBillingRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: PaymentsBillingRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[PaymentsBillingRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=PaymentsBillingRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: PaymentsBillingRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[PaymentsBillingRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=PaymentsBillingRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: PaymentsBillingRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[PaymentsBillingRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return PaymentsBillingService.list_components_25(db, master_entity_id)
