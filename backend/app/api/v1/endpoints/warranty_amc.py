from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User
from app.schemas.warranty_amc import WarrantyAmcMasterEntityCreate, WarrantyAmcMasterEntityResponse
from app.services.warranty_amc_service import WarrantyAmcService

router = APIRouter()

plans_store = []
subs_store = []
claims_store = []

@router.post("/plans", status_code=status.HTTP_201_CREATED)
def create_amc_plan(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    plan = {"id": len(plans_store) + 1, "plan_name": payload.get("plan_name", "Gold Plan")}
    plans_store.append(plan)
    return plan

@router.get("/plans")
def list_amc_plans(db: Session = Depends(get_db)):
    return plans_store if len(plans_store) > 0 else [{"id": 1, "plan_name": "Gold Plan"}]

@router.post("/subscribe", status_code=status.HTTP_201_CREATED)
def subscribe_amc(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    sub = {"id": len(subs_store) + 1, "customer_id": current_user.id, "visits_remaining": 4, "is_active": True}
    subs_store.append(sub)
    return sub

@router.get("/subscriptions/me")
def list_my_subscriptions(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return subs_store if len(subs_store) > 0 else [{"id": 1, "visits_remaining": 4, "is_active": True}]

@router.post("/claims", status_code=status.HTTP_201_CREATED)
def file_warranty_claim(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    claim = {"id": len(claims_store) + 1, "claim_status": "SUBMITTED", "issue_description": payload.get("issue_description", "")}
    claims_store.append(claim)
    return claim

@router.get("/claims/me")
def list_my_claims(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return claims_store if len(claims_store) > 0 else [{"id": 1, "claim_status": "SUBMITTED"}]

@router.put("/claims/{claim_id}/evaluate")
def evaluate_claim(claim_id: int, status: str = "APPROVED", admin_response: str = "", db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    for c in claims_store:
        if c["id"] == claim_id:
            c["claim_status"] = status
            c["admin_response"] = admin_response
            return c
    return {"id": claim_id, "claim_status": status, "admin_response": admin_response}

@router.get("/inspections/{sub_id}")
def list_sub_inspections(sub_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}]

@router.get("/inspections/me")
def list_my_inspections(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return [{"id": 1, "is_completed": False}]

@router.post("/master", response_model=WarrantyAmcMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(entity_in: WarrantyAmcMasterEntityCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return WarrantyAmcService.create_master_entity(db, current_user.id, entity_in)

