from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.review_ratings import ReviewRatingsStatus
from app.schemas.review_ratings import (
    ReviewRatingsMasterEntityCreate, ReviewRatingsMasterEntityUpdate, ReviewRatingsMasterEntityResponse,
    ReviewRatingsRelationalComponent1Create, ReviewRatingsRelationalComponent1Response ,ReviewRatingsRelationalComponent2Create, ReviewRatingsRelationalComponent2Response ,ReviewRatingsRelationalComponent3Create, ReviewRatingsRelationalComponent3Response ,ReviewRatingsRelationalComponent4Create, ReviewRatingsRelationalComponent4Response ,ReviewRatingsRelationalComponent5Create, ReviewRatingsRelationalComponent5Response ,ReviewRatingsRelationalComponent6Create, ReviewRatingsRelationalComponent6Response ,ReviewRatingsRelationalComponent7Create, ReviewRatingsRelationalComponent7Response ,ReviewRatingsRelationalComponent8Create, ReviewRatingsRelationalComponent8Response ,ReviewRatingsRelationalComponent9Create, ReviewRatingsRelationalComponent9Response ,ReviewRatingsRelationalComponent10Create, ReviewRatingsRelationalComponent10Response ,ReviewRatingsRelationalComponent11Create, ReviewRatingsRelationalComponent11Response ,ReviewRatingsRelationalComponent12Create, ReviewRatingsRelationalComponent12Response ,ReviewRatingsRelationalComponent13Create, ReviewRatingsRelationalComponent13Response ,ReviewRatingsRelationalComponent14Create, ReviewRatingsRelationalComponent14Response ,ReviewRatingsRelationalComponent15Create, ReviewRatingsRelationalComponent15Response ,ReviewRatingsRelationalComponent16Create, ReviewRatingsRelationalComponent16Response ,ReviewRatingsRelationalComponent17Create, ReviewRatingsRelationalComponent17Response ,ReviewRatingsRelationalComponent18Create, ReviewRatingsRelationalComponent18Response ,ReviewRatingsRelationalComponent19Create, ReviewRatingsRelationalComponent19Response ,ReviewRatingsRelationalComponent20Create, ReviewRatingsRelationalComponent20Response ,ReviewRatingsRelationalComponent21Create, ReviewRatingsRelationalComponent21Response ,ReviewRatingsRelationalComponent22Create, ReviewRatingsRelationalComponent22Response ,ReviewRatingsRelationalComponent23Create, ReviewRatingsRelationalComponent23Response ,ReviewRatingsRelationalComponent24Create, ReviewRatingsRelationalComponent24Response ,ReviewRatingsRelationalComponent25Create, ReviewRatingsRelationalComponent25Response
)
from app.services.review_ratings_service import ReviewRatingsService

router = APIRouter()

@router.post("/master", response_model=ReviewRatingsMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: ReviewRatingsMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[ReviewRatingsMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[ReviewRatingsStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=ReviewRatingsMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=ReviewRatingsMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: ReviewRatingsMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    ReviewRatingsService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=ReviewRatingsRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: ReviewRatingsRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[ReviewRatingsRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=ReviewRatingsRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: ReviewRatingsRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[ReviewRatingsRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=ReviewRatingsRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: ReviewRatingsRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[ReviewRatingsRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=ReviewRatingsRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: ReviewRatingsRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[ReviewRatingsRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=ReviewRatingsRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: ReviewRatingsRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[ReviewRatingsRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=ReviewRatingsRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: ReviewRatingsRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[ReviewRatingsRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=ReviewRatingsRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: ReviewRatingsRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[ReviewRatingsRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=ReviewRatingsRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: ReviewRatingsRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[ReviewRatingsRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=ReviewRatingsRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: ReviewRatingsRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[ReviewRatingsRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=ReviewRatingsRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: ReviewRatingsRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[ReviewRatingsRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=ReviewRatingsRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: ReviewRatingsRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[ReviewRatingsRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=ReviewRatingsRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: ReviewRatingsRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[ReviewRatingsRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=ReviewRatingsRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: ReviewRatingsRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[ReviewRatingsRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=ReviewRatingsRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: ReviewRatingsRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[ReviewRatingsRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=ReviewRatingsRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: ReviewRatingsRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[ReviewRatingsRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=ReviewRatingsRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: ReviewRatingsRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[ReviewRatingsRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=ReviewRatingsRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: ReviewRatingsRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[ReviewRatingsRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=ReviewRatingsRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: ReviewRatingsRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[ReviewRatingsRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=ReviewRatingsRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: ReviewRatingsRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[ReviewRatingsRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=ReviewRatingsRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: ReviewRatingsRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[ReviewRatingsRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=ReviewRatingsRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: ReviewRatingsRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[ReviewRatingsRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=ReviewRatingsRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: ReviewRatingsRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[ReviewRatingsRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=ReviewRatingsRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: ReviewRatingsRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[ReviewRatingsRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=ReviewRatingsRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: ReviewRatingsRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[ReviewRatingsRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=ReviewRatingsRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: ReviewRatingsRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[ReviewRatingsRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ReviewRatingsService.list_components_25(db, master_entity_id)

