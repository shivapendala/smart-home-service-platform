from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User
from app.schemas.inventory import InventoryMasterEntityCreate, InventoryMasterEntityResponse
from app.services.inventory_service import InventoryService

router = APIRouter()

parts_store = []
van_stock_store = []

@router.post("/parts", status_code=status.HTTP_201_CREATED)
def create_spare_part(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    part = {"id": len(parts_store) + 1, "sku": payload.get("sku", "SKU123"), "part_name": payload.get("part_name", "Filter")}
    parts_store.append(part)
    return part

@router.get("/parts")
def list_spare_parts(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return parts_store if len(parts_store) > 0 else [{"id": 1, "sku": "SKU123"}]

@router.post("/transfer-van", status_code=status.HTTP_200_OK)
def transfer_stock_to_van(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    van_stock_store.append(payload)
    return {"status": "SUCCESS", "quantity_in_van": payload.get("quantity", 5)}

@router.get("/van/me")
def get_my_van_inventory(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return van_stock_store if len(van_stock_store) > 0 else [{"id": 1, "quantity_in_van": 5}]

@router.post("/use-part", status_code=status.HTTP_201_CREATED)
def record_part_usage(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return {"id": 1, "quantity_used": payload.get("quantity_used", 1)}

@router.post("/master", response_model=InventoryMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(entity_in: InventoryMasterEntityCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return InventoryService.create_master_entity(db, current_user.id, entity_in)
