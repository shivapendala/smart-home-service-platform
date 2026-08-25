from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.support_tickets import SupportTicketsStatus
from app.schemas.support_tickets import (
    SupportTicketsMasterEntityCreate, SupportTicketsMasterEntityUpdate, SupportTicketsMasterEntityResponse,
    SupportTicketsRelationalComponent1Create, SupportTicketsRelationalComponent1Response ,SupportTicketsRelationalComponent2Create, SupportTicketsRelationalComponent2Response ,SupportTicketsRelationalComponent3Create, SupportTicketsRelationalComponent3Response ,SupportTicketsRelationalComponent4Create, SupportTicketsRelationalComponent4Response ,SupportTicketsRelationalComponent5Create, SupportTicketsRelationalComponent5Response ,SupportTicketsRelationalComponent6Create, SupportTicketsRelationalComponent6Response ,SupportTicketsRelationalComponent7Create, SupportTicketsRelationalComponent7Response ,SupportTicketsRelationalComponent8Create, SupportTicketsRelationalComponent8Response ,SupportTicketsRelationalComponent9Create, SupportTicketsRelationalComponent9Response ,SupportTicketsRelationalComponent10Create, SupportTicketsRelationalComponent10Response ,SupportTicketsRelationalComponent11Create, SupportTicketsRelationalComponent11Response ,SupportTicketsRelationalComponent12Create, SupportTicketsRelationalComponent12Response ,SupportTicketsRelationalComponent13Create, SupportTicketsRelationalComponent13Response ,SupportTicketsRelationalComponent14Create, SupportTicketsRelationalComponent14Response ,SupportTicketsRelationalComponent15Create, SupportTicketsRelationalComponent15Response ,SupportTicketsRelationalComponent16Create, SupportTicketsRelationalComponent16Response ,SupportTicketsRelationalComponent17Create, SupportTicketsRelationalComponent17Response ,SupportTicketsRelationalComponent18Create, SupportTicketsRelationalComponent18Response ,SupportTicketsRelationalComponent19Create, SupportTicketsRelationalComponent19Response ,SupportTicketsRelationalComponent20Create, SupportTicketsRelationalComponent20Response ,SupportTicketsRelationalComponent21Create, SupportTicketsRelationalComponent21Response ,SupportTicketsRelationalComponent22Create, SupportTicketsRelationalComponent22Response ,SupportTicketsRelationalComponent23Create, SupportTicketsRelationalComponent23Response ,SupportTicketsRelationalComponent24Create, SupportTicketsRelationalComponent24Response ,SupportTicketsRelationalComponent25Create, SupportTicketsRelationalComponent25Response
)
from app.services.support_tickets_service import SupportTicketsService

router = APIRouter()

@router.post("/master", response_model=SupportTicketsMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: SupportTicketsMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[SupportTicketsMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[SupportTicketsStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=SupportTicketsMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=SupportTicketsMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: SupportTicketsMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    SupportTicketsService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=SupportTicketsRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: SupportTicketsRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[SupportTicketsRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=SupportTicketsRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: SupportTicketsRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[SupportTicketsRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=SupportTicketsRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: SupportTicketsRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[SupportTicketsRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=SupportTicketsRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: SupportTicketsRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[SupportTicketsRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=SupportTicketsRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: SupportTicketsRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[SupportTicketsRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=SupportTicketsRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: SupportTicketsRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[SupportTicketsRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=SupportTicketsRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: SupportTicketsRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[SupportTicketsRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=SupportTicketsRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: SupportTicketsRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[SupportTicketsRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=SupportTicketsRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: SupportTicketsRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[SupportTicketsRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=SupportTicketsRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: SupportTicketsRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[SupportTicketsRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=SupportTicketsRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: SupportTicketsRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[SupportTicketsRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=SupportTicketsRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: SupportTicketsRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[SupportTicketsRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=SupportTicketsRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: SupportTicketsRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[SupportTicketsRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=SupportTicketsRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: SupportTicketsRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[SupportTicketsRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=SupportTicketsRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: SupportTicketsRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[SupportTicketsRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=SupportTicketsRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: SupportTicketsRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[SupportTicketsRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=SupportTicketsRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: SupportTicketsRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[SupportTicketsRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=SupportTicketsRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: SupportTicketsRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[SupportTicketsRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=SupportTicketsRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: SupportTicketsRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[SupportTicketsRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=SupportTicketsRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: SupportTicketsRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[SupportTicketsRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=SupportTicketsRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: SupportTicketsRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[SupportTicketsRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=SupportTicketsRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: SupportTicketsRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[SupportTicketsRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=SupportTicketsRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: SupportTicketsRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[SupportTicketsRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=SupportTicketsRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: SupportTicketsRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[SupportTicketsRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=SupportTicketsRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: SupportTicketsRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[SupportTicketsRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return SupportTicketsService.list_components_25(db, master_entity_id)
