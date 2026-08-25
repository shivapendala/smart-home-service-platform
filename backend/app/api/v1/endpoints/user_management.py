from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.user_management import UserManagementStatus
from app.schemas.user_management import (
    UserManagementMasterEntityCreate, UserManagementMasterEntityUpdate, UserManagementMasterEntityResponse,
    UserManagementRelationalComponent1Create, UserManagementRelationalComponent1Response ,UserManagementRelationalComponent2Create, UserManagementRelationalComponent2Response ,UserManagementRelationalComponent3Create, UserManagementRelationalComponent3Response ,UserManagementRelationalComponent4Create, UserManagementRelationalComponent4Response ,UserManagementRelationalComponent5Create, UserManagementRelationalComponent5Response ,UserManagementRelationalComponent6Create, UserManagementRelationalComponent6Response ,UserManagementRelationalComponent7Create, UserManagementRelationalComponent7Response ,UserManagementRelationalComponent8Create, UserManagementRelationalComponent8Response ,UserManagementRelationalComponent9Create, UserManagementRelationalComponent9Response ,UserManagementRelationalComponent10Create, UserManagementRelationalComponent10Response ,UserManagementRelationalComponent11Create, UserManagementRelationalComponent11Response ,UserManagementRelationalComponent12Create, UserManagementRelationalComponent12Response ,UserManagementRelationalComponent13Create, UserManagementRelationalComponent13Response ,UserManagementRelationalComponent14Create, UserManagementRelationalComponent14Response ,UserManagementRelationalComponent15Create, UserManagementRelationalComponent15Response ,UserManagementRelationalComponent16Create, UserManagementRelationalComponent16Response ,UserManagementRelationalComponent17Create, UserManagementRelationalComponent17Response ,UserManagementRelationalComponent18Create, UserManagementRelationalComponent18Response ,UserManagementRelationalComponent19Create, UserManagementRelationalComponent19Response ,UserManagementRelationalComponent20Create, UserManagementRelationalComponent20Response ,UserManagementRelationalComponent21Create, UserManagementRelationalComponent21Response ,UserManagementRelationalComponent22Create, UserManagementRelationalComponent22Response ,UserManagementRelationalComponent23Create, UserManagementRelationalComponent23Response ,UserManagementRelationalComponent24Create, UserManagementRelationalComponent24Response ,UserManagementRelationalComponent25Create, UserManagementRelationalComponent25Response
)
from app.services.user_management_service import UserManagementService

router = APIRouter()

@router.post("/master", response_model=UserManagementMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: UserManagementMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[UserManagementMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[UserManagementStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=UserManagementMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=UserManagementMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: UserManagementMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    UserManagementService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=UserManagementRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: UserManagementRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[UserManagementRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=UserManagementRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: UserManagementRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[UserManagementRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=UserManagementRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: UserManagementRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[UserManagementRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=UserManagementRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: UserManagementRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[UserManagementRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=UserManagementRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: UserManagementRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[UserManagementRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=UserManagementRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: UserManagementRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[UserManagementRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=UserManagementRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: UserManagementRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[UserManagementRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=UserManagementRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: UserManagementRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[UserManagementRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=UserManagementRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: UserManagementRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[UserManagementRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=UserManagementRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: UserManagementRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[UserManagementRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=UserManagementRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: UserManagementRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[UserManagementRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=UserManagementRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: UserManagementRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[UserManagementRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=UserManagementRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: UserManagementRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[UserManagementRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=UserManagementRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: UserManagementRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[UserManagementRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=UserManagementRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: UserManagementRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[UserManagementRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=UserManagementRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: UserManagementRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[UserManagementRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=UserManagementRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: UserManagementRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[UserManagementRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=UserManagementRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: UserManagementRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[UserManagementRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=UserManagementRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: UserManagementRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[UserManagementRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=UserManagementRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: UserManagementRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[UserManagementRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=UserManagementRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: UserManagementRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[UserManagementRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=UserManagementRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: UserManagementRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[UserManagementRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=UserManagementRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: UserManagementRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[UserManagementRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=UserManagementRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: UserManagementRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[UserManagementRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=UserManagementRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: UserManagementRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[UserManagementRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return UserManagementService.list_components_25(db, master_entity_id)
