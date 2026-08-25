from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.service import (
    CategoryCreate, CategoryResponse,
    ServiceCreate, ServiceUpdate, ServiceResponse
)
from app.services.catalog_service import CatalogService
from app.models.user import UserRole
from app.api.deps import require_roles

router = APIRouter()


# --- Categories API ---

@router.get("/categories", response_model=List[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    """Fetch all service categories."""
    return CatalogService.get_categories(db)


@router.post(
    "/categories",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles([UserRole.ADMIN]))]
)
def create_category(
    category_in: CategoryCreate,
    db: Session = Depends(get_db)
):
    """Create a new service category (Admin only)."""
    return CatalogService.create_category(db=db, category_in=category_in)


# --- Services API ---

@router.get("/items", response_model=List[ServiceResponse])
def list_services(
    category_id: Optional[int] = Query(None, description="Filter services by category ID"),
    search: Optional[str] = Query(None, description="Search services by keyword"),
    db: Session = Depends(get_db)
):
    """Fetch active services with optional category filtering and search."""
    return CatalogService.get_services(
        db=db, category_id=category_id, search=search, only_active=True
    )


@router.get("/items/{service_id}", response_model=ServiceResponse)
def get_service_item(service_id: int, db: Session = Depends(get_db)):
    """Retrieve details for a single service item."""
    return CatalogService.get_service_by_id(db=db, service_id=service_id)


@router.post(
    "/items",
    response_model=ServiceResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles([UserRole.ADMIN]))]
)
def create_service(
    service_in: ServiceCreate,
    db: Session = Depends(get_db)
):
    """Create a new service item (Admin only)."""
    return CatalogService.create_service(db=db, service_in=service_in)


@router.put(
    "/items/{service_id}",
    response_model=ServiceResponse,
    dependencies=[Depends(require_roles([UserRole.ADMIN]))]
)
def update_service(
    service_id: int,
    service_in: ServiceUpdate,
    db: Session = Depends(get_db)
):
    """Update existing service item details or base price (Admin only)."""
    return CatalogService.update_service(db=db, service_id=service_id, service_in=service_in)


@router.delete(
    "/items/{service_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(require_roles([UserRole.ADMIN]))]
)
def delete_service(
    service_id: int,
    db: Session = Depends(get_db)
):
    """Delete a service item from catalog (Admin only)."""
    CatalogService.delete_service(db=db, service_id=service_id)
    return None
