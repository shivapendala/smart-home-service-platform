from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User, UserRole
from app.models.service_catalog import ServiceCatalogStatus
from app.schemas.service_catalog import (
    ServiceCatalogMasterEntityCreate, ServiceCatalogMasterEntityUpdate, ServiceCatalogMasterEntityResponse,
    ServiceCatalogRelationalComponent1Create, ServiceCatalogRelationalComponent1Response ,ServiceCatalogRelationalComponent2Create, ServiceCatalogRelationalComponent2Response ,ServiceCatalogRelationalComponent3Create, ServiceCatalogRelationalComponent3Response ,ServiceCatalogRelationalComponent4Create, ServiceCatalogRelationalComponent4Response ,ServiceCatalogRelationalComponent5Create, ServiceCatalogRelationalComponent5Response ,ServiceCatalogRelationalComponent6Create, ServiceCatalogRelationalComponent6Response ,ServiceCatalogRelationalComponent7Create, ServiceCatalogRelationalComponent7Response ,ServiceCatalogRelationalComponent8Create, ServiceCatalogRelationalComponent8Response ,ServiceCatalogRelationalComponent9Create, ServiceCatalogRelationalComponent9Response ,ServiceCatalogRelationalComponent10Create, ServiceCatalogRelationalComponent10Response ,ServiceCatalogRelationalComponent11Create, ServiceCatalogRelationalComponent11Response ,ServiceCatalogRelationalComponent12Create, ServiceCatalogRelationalComponent12Response ,ServiceCatalogRelationalComponent13Create, ServiceCatalogRelationalComponent13Response ,ServiceCatalogRelationalComponent14Create, ServiceCatalogRelationalComponent14Response ,ServiceCatalogRelationalComponent15Create, ServiceCatalogRelationalComponent15Response ,ServiceCatalogRelationalComponent16Create, ServiceCatalogRelationalComponent16Response ,ServiceCatalogRelationalComponent17Create, ServiceCatalogRelationalComponent17Response ,ServiceCatalogRelationalComponent18Create, ServiceCatalogRelationalComponent18Response ,ServiceCatalogRelationalComponent19Create, ServiceCatalogRelationalComponent19Response ,ServiceCatalogRelationalComponent20Create, ServiceCatalogRelationalComponent20Response ,ServiceCatalogRelationalComponent21Create, ServiceCatalogRelationalComponent21Response ,ServiceCatalogRelationalComponent22Create, ServiceCatalogRelationalComponent22Response ,ServiceCatalogRelationalComponent23Create, ServiceCatalogRelationalComponent23Response ,ServiceCatalogRelationalComponent24Create, ServiceCatalogRelationalComponent24Response ,ServiceCatalogRelationalComponent25Create, ServiceCatalogRelationalComponent25Response
)
from app.services.service_catalog_service import ServiceCatalogService

router = APIRouter()

@router.post("/master", response_model=ServiceCatalogMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(
    entity_in: ServiceCatalogMasterEntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.create_master_entity(db, current_user.id, entity_in)

@router.get("/master", response_model=List[ServiceCatalogMasterEntityResponse])
def list_master_entities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status_filter: Optional[ServiceCatalogStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_master_entities(db, skip, limit, status_filter)

@router.get("/master/{entity_id}", response_model=ServiceCatalogMasterEntityResponse)
def get_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.get_master_entity_by_id(db, entity_id)

@router.put("/master/{entity_id}", response_model=ServiceCatalogMasterEntityResponse)
def update_master_entity(
    entity_id: int,
    update_in: ServiceCatalogMasterEntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.update_master_entity(db, entity_id, update_in)

@router.delete("/master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_master_entity(
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    ServiceCatalogService.delete_master_entity(db, entity_id)
    return None

@router.post("/component-1", response_model=ServiceCatalogRelationalComponent1Response, status_code=status.HTTP_201_CREATED)
def add_component_1(
    comp_in: ServiceCatalogRelationalComponent1Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_1(db, comp_in)

@router.get("/component-1", response_model=List[ServiceCatalogRelationalComponent1Response])
def list_components_1(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_1(db, master_entity_id)

@router.post("/component-2", response_model=ServiceCatalogRelationalComponent2Response, status_code=status.HTTP_201_CREATED)
def add_component_2(
    comp_in: ServiceCatalogRelationalComponent2Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_2(db, comp_in)

@router.get("/component-2", response_model=List[ServiceCatalogRelationalComponent2Response])
def list_components_2(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_2(db, master_entity_id)

@router.post("/component-3", response_model=ServiceCatalogRelationalComponent3Response, status_code=status.HTTP_201_CREATED)
def add_component_3(
    comp_in: ServiceCatalogRelationalComponent3Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_3(db, comp_in)

@router.get("/component-3", response_model=List[ServiceCatalogRelationalComponent3Response])
def list_components_3(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_3(db, master_entity_id)

@router.post("/component-4", response_model=ServiceCatalogRelationalComponent4Response, status_code=status.HTTP_201_CREATED)
def add_component_4(
    comp_in: ServiceCatalogRelationalComponent4Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_4(db, comp_in)

@router.get("/component-4", response_model=List[ServiceCatalogRelationalComponent4Response])
def list_components_4(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_4(db, master_entity_id)

@router.post("/component-5", response_model=ServiceCatalogRelationalComponent5Response, status_code=status.HTTP_201_CREATED)
def add_component_5(
    comp_in: ServiceCatalogRelationalComponent5Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_5(db, comp_in)

@router.get("/component-5", response_model=List[ServiceCatalogRelationalComponent5Response])
def list_components_5(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_5(db, master_entity_id)

@router.post("/component-6", response_model=ServiceCatalogRelationalComponent6Response, status_code=status.HTTP_201_CREATED)
def add_component_6(
    comp_in: ServiceCatalogRelationalComponent6Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_6(db, comp_in)

@router.get("/component-6", response_model=List[ServiceCatalogRelationalComponent6Response])
def list_components_6(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_6(db, master_entity_id)

@router.post("/component-7", response_model=ServiceCatalogRelationalComponent7Response, status_code=status.HTTP_201_CREATED)
def add_component_7(
    comp_in: ServiceCatalogRelationalComponent7Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_7(db, comp_in)

@router.get("/component-7", response_model=List[ServiceCatalogRelationalComponent7Response])
def list_components_7(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_7(db, master_entity_id)

@router.post("/component-8", response_model=ServiceCatalogRelationalComponent8Response, status_code=status.HTTP_201_CREATED)
def add_component_8(
    comp_in: ServiceCatalogRelationalComponent8Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_8(db, comp_in)

@router.get("/component-8", response_model=List[ServiceCatalogRelationalComponent8Response])
def list_components_8(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_8(db, master_entity_id)

@router.post("/component-9", response_model=ServiceCatalogRelationalComponent9Response, status_code=status.HTTP_201_CREATED)
def add_component_9(
    comp_in: ServiceCatalogRelationalComponent9Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_9(db, comp_in)

@router.get("/component-9", response_model=List[ServiceCatalogRelationalComponent9Response])
def list_components_9(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_9(db, master_entity_id)

@router.post("/component-10", response_model=ServiceCatalogRelationalComponent10Response, status_code=status.HTTP_201_CREATED)
def add_component_10(
    comp_in: ServiceCatalogRelationalComponent10Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_10(db, comp_in)

@router.get("/component-10", response_model=List[ServiceCatalogRelationalComponent10Response])
def list_components_10(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_10(db, master_entity_id)

@router.post("/component-11", response_model=ServiceCatalogRelationalComponent11Response, status_code=status.HTTP_201_CREATED)
def add_component_11(
    comp_in: ServiceCatalogRelationalComponent11Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_11(db, comp_in)

@router.get("/component-11", response_model=List[ServiceCatalogRelationalComponent11Response])
def list_components_11(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_11(db, master_entity_id)

@router.post("/component-12", response_model=ServiceCatalogRelationalComponent12Response, status_code=status.HTTP_201_CREATED)
def add_component_12(
    comp_in: ServiceCatalogRelationalComponent12Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_12(db, comp_in)

@router.get("/component-12", response_model=List[ServiceCatalogRelationalComponent12Response])
def list_components_12(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_12(db, master_entity_id)

@router.post("/component-13", response_model=ServiceCatalogRelationalComponent13Response, status_code=status.HTTP_201_CREATED)
def add_component_13(
    comp_in: ServiceCatalogRelationalComponent13Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_13(db, comp_in)

@router.get("/component-13", response_model=List[ServiceCatalogRelationalComponent13Response])
def list_components_13(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_13(db, master_entity_id)

@router.post("/component-14", response_model=ServiceCatalogRelationalComponent14Response, status_code=status.HTTP_201_CREATED)
def add_component_14(
    comp_in: ServiceCatalogRelationalComponent14Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_14(db, comp_in)

@router.get("/component-14", response_model=List[ServiceCatalogRelationalComponent14Response])
def list_components_14(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_14(db, master_entity_id)

@router.post("/component-15", response_model=ServiceCatalogRelationalComponent15Response, status_code=status.HTTP_201_CREATED)
def add_component_15(
    comp_in: ServiceCatalogRelationalComponent15Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_15(db, comp_in)

@router.get("/component-15", response_model=List[ServiceCatalogRelationalComponent15Response])
def list_components_15(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_15(db, master_entity_id)

@router.post("/component-16", response_model=ServiceCatalogRelationalComponent16Response, status_code=status.HTTP_201_CREATED)
def add_component_16(
    comp_in: ServiceCatalogRelationalComponent16Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_16(db, comp_in)

@router.get("/component-16", response_model=List[ServiceCatalogRelationalComponent16Response])
def list_components_16(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_16(db, master_entity_id)

@router.post("/component-17", response_model=ServiceCatalogRelationalComponent17Response, status_code=status.HTTP_201_CREATED)
def add_component_17(
    comp_in: ServiceCatalogRelationalComponent17Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_17(db, comp_in)

@router.get("/component-17", response_model=List[ServiceCatalogRelationalComponent17Response])
def list_components_17(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_17(db, master_entity_id)

@router.post("/component-18", response_model=ServiceCatalogRelationalComponent18Response, status_code=status.HTTP_201_CREATED)
def add_component_18(
    comp_in: ServiceCatalogRelationalComponent18Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_18(db, comp_in)

@router.get("/component-18", response_model=List[ServiceCatalogRelationalComponent18Response])
def list_components_18(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_18(db, master_entity_id)

@router.post("/component-19", response_model=ServiceCatalogRelationalComponent19Response, status_code=status.HTTP_201_CREATED)
def add_component_19(
    comp_in: ServiceCatalogRelationalComponent19Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_19(db, comp_in)

@router.get("/component-19", response_model=List[ServiceCatalogRelationalComponent19Response])
def list_components_19(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_19(db, master_entity_id)

@router.post("/component-20", response_model=ServiceCatalogRelationalComponent20Response, status_code=status.HTTP_201_CREATED)
def add_component_20(
    comp_in: ServiceCatalogRelationalComponent20Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_20(db, comp_in)

@router.get("/component-20", response_model=List[ServiceCatalogRelationalComponent20Response])
def list_components_20(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_20(db, master_entity_id)

@router.post("/component-21", response_model=ServiceCatalogRelationalComponent21Response, status_code=status.HTTP_201_CREATED)
def add_component_21(
    comp_in: ServiceCatalogRelationalComponent21Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_21(db, comp_in)

@router.get("/component-21", response_model=List[ServiceCatalogRelationalComponent21Response])
def list_components_21(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_21(db, master_entity_id)

@router.post("/component-22", response_model=ServiceCatalogRelationalComponent22Response, status_code=status.HTTP_201_CREATED)
def add_component_22(
    comp_in: ServiceCatalogRelationalComponent22Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_22(db, comp_in)

@router.get("/component-22", response_model=List[ServiceCatalogRelationalComponent22Response])
def list_components_22(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_22(db, master_entity_id)

@router.post("/component-23", response_model=ServiceCatalogRelationalComponent23Response, status_code=status.HTTP_201_CREATED)
def add_component_23(
    comp_in: ServiceCatalogRelationalComponent23Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_23(db, comp_in)

@router.get("/component-23", response_model=List[ServiceCatalogRelationalComponent23Response])
def list_components_23(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_23(db, master_entity_id)

@router.post("/component-24", response_model=ServiceCatalogRelationalComponent24Response, status_code=status.HTTP_201_CREATED)
def add_component_24(
    comp_in: ServiceCatalogRelationalComponent24Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_24(db, comp_in)

@router.get("/component-24", response_model=List[ServiceCatalogRelationalComponent24Response])
def list_components_24(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_24(db, master_entity_id)

@router.post("/component-25", response_model=ServiceCatalogRelationalComponent25Response, status_code=status.HTTP_201_CREATED)
def add_component_25(
    comp_in: ServiceCatalogRelationalComponent25Create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.add_component_25(db, comp_in)

@router.get("/component-25", response_model=List[ServiceCatalogRelationalComponent25Response])
def list_components_25(
    master_entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return ServiceCatalogService.list_components_25(db, master_entity_id)
