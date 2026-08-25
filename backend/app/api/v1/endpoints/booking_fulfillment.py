from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.booking_fulfillment import BookingFulfillmentStatus
from app.schemas.booking_fulfillment import (
    BookingFulfillmentMasterEntityCreate, BookingFulfillmentMasterEntityUpdate, BookingFulfillmentMasterEntityResponse,
    BookingFulfillmentRelationalComponent1Create, BookingFulfillmentRelationalComponent1Response ,BookingFulfillmentRelationalComponent2Create, BookingFulfillmentRelationalComponent2Response ,BookingFulfillmentRelationalComponent3Create, BookingFulfillmentRelationalComponent3Response ,BookingFulfillmentRelationalComponent4Create, BookingFulfillmentRelationalComponent4Response ,BookingFulfillmentRelationalComponent5Create, BookingFulfillmentRelationalComponent5Response ,BookingFulfillmentRelationalComponent6Create, BookingFulfillmentRelationalComponent6Response ,BookingFulfillmentRelationalComponent7Create, BookingFulfillmentRelationalComponent7Response ,BookingFulfillmentRelationalComponent8Create, BookingFulfillmentRelationalComponent8Response ,BookingFulfillmentRelationalComponent9Create, BookingFulfillmentRelationalComponent9Response ,BookingFulfillmentRelationalComponent10Create, BookingFulfillmentRelationalComponent10Response ,BookingFulfillmentRelationalComponent11Create, BookingFulfillmentRelationalComponent11Response ,BookingFulfillmentRelationalComponent12Create, BookingFulfillmentRelationalComponent12Response ,BookingFulfillmentRelationalComponent13Create, BookingFulfillmentRelationalComponent13Response ,BookingFulfillmentRelationalComponent14Create, BookingFulfillmentRelationalComponent14Response ,BookingFulfillmentRelationalComponent15Create, BookingFulfillmentRelationalComponent15Response ,BookingFulfillmentRelationalComponent16Create, BookingFulfillmentRelationalComponent16Response ,BookingFulfillmentRelationalComponent17Create, BookingFulfillmentRelationalComponent17Response ,BookingFulfillmentRelationalComponent18Create, BookingFulfillmentRelationalComponent18Response ,BookingFulfillmentRelationalComponent19Create, BookingFulfillmentRelationalComponent19Response ,BookingFulfillmentRelationalComponent20Create, BookingFulfillmentRelationalComponent20Response ,BookingFulfillmentRelationalComponent21Create, BookingFulfillmentRelationalComponent21Response ,BookingFulfillmentRelationalComponent22Create, BookingFulfillmentRelationalComponent22Response ,BookingFulfillmentRelationalComponent23Create, BookingFulfillmentRelationalComponent23Response ,BookingFulfillmentRelationalComponent24Create, BookingFulfillmentRelationalComponent24Response ,BookingFulfillmentRelationalComponent25Create, BookingFulfillmentRelationalComponent25Response
)
from app.services.booking_fulfillment_service import BookingFulfillmentService

router = APIRouter()

@router.post("/master", response_model=BookingFulfillmentMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: BookingFulfillmentMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[BookingFulfillmentMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[BookingFulfillmentStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=BookingFulfillmentMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=BookingFulfillmentMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: BookingFulfillmentMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    BookingFulfillmentService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=BookingFulfillmentRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: BookingFulfillmentRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[BookingFulfillmentRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=BookingFulfillmentRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: BookingFulfillmentRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[BookingFulfillmentRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=BookingFulfillmentRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: BookingFulfillmentRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[BookingFulfillmentRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=BookingFulfillmentRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: BookingFulfillmentRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[BookingFulfillmentRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=BookingFulfillmentRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: BookingFulfillmentRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[BookingFulfillmentRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=BookingFulfillmentRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: BookingFulfillmentRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[BookingFulfillmentRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=BookingFulfillmentRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: BookingFulfillmentRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[BookingFulfillmentRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=BookingFulfillmentRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: BookingFulfillmentRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[BookingFulfillmentRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=BookingFulfillmentRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: BookingFulfillmentRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[BookingFulfillmentRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=BookingFulfillmentRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: BookingFulfillmentRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[BookingFulfillmentRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=BookingFulfillmentRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: BookingFulfillmentRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[BookingFulfillmentRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=BookingFulfillmentRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: BookingFulfillmentRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[BookingFulfillmentRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=BookingFulfillmentRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: BookingFulfillmentRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[BookingFulfillmentRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=BookingFulfillmentRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: BookingFulfillmentRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[BookingFulfillmentRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=BookingFulfillmentRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: BookingFulfillmentRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[BookingFulfillmentRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=BookingFulfillmentRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: BookingFulfillmentRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[BookingFulfillmentRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=BookingFulfillmentRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: BookingFulfillmentRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[BookingFulfillmentRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=BookingFulfillmentRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: BookingFulfillmentRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[BookingFulfillmentRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=BookingFulfillmentRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: BookingFulfillmentRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[BookingFulfillmentRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=BookingFulfillmentRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: BookingFulfillmentRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[BookingFulfillmentRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=BookingFulfillmentRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: BookingFulfillmentRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[BookingFulfillmentRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=BookingFulfillmentRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: BookingFulfillmentRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[BookingFulfillmentRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=BookingFulfillmentRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: BookingFulfillmentRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[BookingFulfillmentRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=BookingFulfillmentRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: BookingFulfillmentRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[BookingFulfillmentRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=BookingFulfillmentRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: BookingFulfillmentRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[BookingFulfillmentRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingFulfillmentService.list_components_25(db, master_entity_id)

