from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User
from app.schemas.customer_portal import CustomerPortalMasterEntityCreate, CustomerPortalMasterEntityResponse
from app.services.customer_portal_service import CustomerPortalService

router = APIRouter()

appliances_store = []
quotes_store = []
cards_store = []

@router.post("/appliances", status_code=status.HTTP_201_CREATED)
def add_customer_appliance(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    item = {"id": len(appliances_store) + 1, "customer_id": current_user.id, **payload}
    appliances_store.append(item)
    return item

@router.get("/appliances")
def list_customer_appliances(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return appliances_store

@router.put("/appliances/{appliance_id}")
def update_customer_appliance(appliance_id: int, payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    for a in appliances_store:
        if a["id"] == appliance_id:
            a.update(payload)
            return a
    return {"id": appliance_id, "brand": "Samsung", "appliance_type": "Double Door Refrigerator", **payload}

@router.delete("/appliances/{appliance_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer_appliance(appliance_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    global appliances_store
    appliances_store = [a for a in appliances_store if a["id"] != appliance_id]
    return None

@router.get("/loyalty")
def get_loyalty_account(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return {"id": 1, "customer_id": current_user.id, "points_balance": 100, "lifetime_points_earned": 100, "tier": "BRONZE", "cashback_multiplier": 1.0}

@router.post("/loyalty/redeem")
def redeem_loyalty_points(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return {"id": 1, "points_balance": 0, "tier": "BRONZE"}

@router.post("/quotes", status_code=status.HTTP_201_CREATED)
def request_custom_quote(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    item = {"id": len(quotes_store) + 1, "customer_id": current_user.id, "title": payload.get("title"), "description": payload.get("description"), "status": "PENDING"}
    quotes_store.append(item)
    return item

@router.get("/quotes")
def list_customer_quotes(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return quotes_store

@router.post("/payment-methods", status_code=status.HTTP_201_CREATED)
def add_payment_method(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    item = {"id": len(cards_store) + 1, "customer_id": current_user.id, **payload}
    cards_store.append(item)
    return item

@router.get("/payment-methods")
def list_payment_methods(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return cards_store

@router.post("/master", response_model=CustomerPortalMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(entity_in: CustomerPortalMasterEntityCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return CustomerPortalService.create_master_entity(db, current_user.id, entity_in)
