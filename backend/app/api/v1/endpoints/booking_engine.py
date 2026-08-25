from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.booking_engine import BookingEngineStatus
from app.schemas.booking_engine import (
    BookingEngineMasterEntityCreate, BookingEngineMasterEntityUpdate, BookingEngineMasterEntityResponse,
    BookingEngineRelationalComponent1Create, BookingEngineRelationalComponent1Response ,BookingEngineRelationalComponent2Create, BookingEngineRelationalComponent2Response ,BookingEngineRelationalComponent3Create, BookingEngineRelationalComponent3Response ,BookingEngineRelationalComponent4Create, BookingEngineRelationalComponent4Response ,BookingEngineRelationalComponent5Create, BookingEngineRelationalComponent5Response ,BookingEngineRelationalComponent6Create, BookingEngineRelationalComponent6Response ,BookingEngineRelationalComponent7Create, BookingEngineRelationalComponent7Response ,BookingEngineRelationalComponent8Create, BookingEngineRelationalComponent8Response ,BookingEngineRelationalComponent9Create, BookingEngineRelationalComponent9Response ,BookingEngineRelationalComponent10Create, BookingEngineRelationalComponent10Response ,BookingEngineRelationalComponent11Create, BookingEngineRelationalComponent11Response ,BookingEngineRelationalComponent12Create, BookingEngineRelationalComponent12Response ,BookingEngineRelationalComponent13Create, BookingEngineRelationalComponent13Response ,BookingEngineRelationalComponent14Create, BookingEngineRelationalComponent14Response ,BookingEngineRelationalComponent15Create, BookingEngineRelationalComponent15Response ,BookingEngineRelationalComponent16Create, BookingEngineRelationalComponent16Response ,BookingEngineRelationalComponent17Create, BookingEngineRelationalComponent17Response ,BookingEngineRelationalComponent18Create, BookingEngineRelationalComponent18Response ,BookingEngineRelationalComponent19Create, BookingEngineRelationalComponent19Response ,BookingEngineRelationalComponent20Create, BookingEngineRelationalComponent20Response ,BookingEngineRelationalComponent21Create, BookingEngineRelationalComponent21Response ,BookingEngineRelationalComponent22Create, BookingEngineRelationalComponent22Response ,BookingEngineRelationalComponent23Create, BookingEngineRelationalComponent23Response ,BookingEngineRelationalComponent24Create, BookingEngineRelationalComponent24Response ,BookingEngineRelationalComponent25Create, BookingEngineRelationalComponent25Response
)
from app.services.booking_engine_service import BookingEngineService

router = APIRouter()

@router.post("/master", response_model=BookingEngineMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: BookingEngineMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[BookingEngineMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[BookingEngineStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=BookingEngineMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=BookingEngineMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: BookingEngineMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    BookingEngineService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=BookingEngineRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: BookingEngineRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[BookingEngineRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=BookingEngineRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: BookingEngineRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[BookingEngineRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=BookingEngineRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: BookingEngineRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[BookingEngineRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=BookingEngineRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: BookingEngineRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[BookingEngineRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=BookingEngineRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: BookingEngineRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[BookingEngineRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=BookingEngineRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: BookingEngineRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[BookingEngineRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=BookingEngineRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: BookingEngineRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[BookingEngineRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=BookingEngineRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: BookingEngineRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[BookingEngineRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=BookingEngineRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: BookingEngineRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[BookingEngineRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=BookingEngineRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: BookingEngineRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[BookingEngineRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=BookingEngineRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: BookingEngineRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[BookingEngineRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=BookingEngineRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: BookingEngineRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[BookingEngineRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=BookingEngineRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: BookingEngineRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[BookingEngineRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=BookingEngineRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: BookingEngineRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[BookingEngineRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=BookingEngineRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: BookingEngineRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[BookingEngineRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=BookingEngineRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: BookingEngineRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[BookingEngineRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=BookingEngineRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: BookingEngineRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[BookingEngineRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=BookingEngineRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: BookingEngineRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[BookingEngineRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=BookingEngineRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: BookingEngineRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[BookingEngineRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=BookingEngineRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: BookingEngineRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[BookingEngineRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=BookingEngineRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: BookingEngineRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[BookingEngineRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=BookingEngineRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: BookingEngineRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[BookingEngineRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=BookingEngineRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: BookingEngineRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[BookingEngineRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=BookingEngineRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: BookingEngineRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[BookingEngineRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=BookingEngineRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: BookingEngineRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[BookingEngineRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return BookingEngineService.list_components_25(db, master_entity_id)
