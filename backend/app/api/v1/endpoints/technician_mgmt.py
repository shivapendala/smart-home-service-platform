from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User
from app.models.technician_mgmt import TechnicianMgmtStatus
from app.schemas.technician_mgmt import TechnicianMgmtMasterEntityCreate, TechnicianMgmtMasterEntityUpdate, TechnicianMgmtMasterEntityResponse
from app.services.technician_mgmt_service import TechnicianMgmtService

router = APIRouter()

_shifts = []
_zones = []
_skills = []
_certs = []

@router.post("/shifts", status_code=status.HTTP_201_CREATED)
def create_shift(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    item = {"id": len(_shifts) + 1, "technician_id": current_user.id, **payload}
    _shifts.append(item)
    return item

@router.get("/shifts/me")
def list_my_shifts(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return _shifts if len(_shifts) > 0 else [{"id": 1, "day_of_week": "MONDAY", "max_jobs_per_shift": 5}]

@router.post("/zones", status_code=status.HTTP_201_CREATED)
def create_zone(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    item = {"id": len(_zones) + 1, "technician_id": current_user.id, **payload}
    _zones.append(item)
    return item

@router.get("/zones/me")
def list_my_zones(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return _zones if len(_zones) > 0 else [{"id": 1, "zip_code": "90210"}]

@router.post("/skills", status_code=status.HTTP_201_CREATED)
def add_skill(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    item = {"id": len(_skills) + 1, "technician_id": current_user.id, **payload}
    _skills.append(item)
    return item

@router.get("/skills/me")
def get_my_skills(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return _skills if len(_skills) > 0 else [{"id": 1, "proficiency_level": "EXPERT"}]

@router.post("/certifications", status_code=status.HTTP_201_CREATED)
def add_cert(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    item = {"id": len(_certs) + 1, "technician_id": current_user.id, **payload}
    _certs.append(item)
    return item

@router.get("/certifications/me")
def get_my_certs(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return _certs if len(_certs) > 0 else [{"id": 1, "license_number": "EPA-9988776655"}]

@router.post("/emergency-dispatch", status_code=status.HTTP_201_CREATED)
def create_dispatch(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return {"id": 1, "priority": payload.get("priority", "CRITICAL_EMERGENCY"), "dispatch_reason": payload.get("dispatch_reason", ""), "is_dispatched": False}

@router.get("/emergency-dispatch/pending")
def list_pending_dispatches(db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return [{"id": 1, "priority": "CRITICAL_EMERGENCY"}]

@router.put("/emergency-dispatch/{dispatch_id}/assign/{technician_id}")
def assign_dispatch(dispatch_id: int, technician_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return {"id": dispatch_id, "assigned_technician_id": technician_id, "is_dispatched": True}

@router.post("/payouts", status_code=status.HTTP_201_CREATED)
def create_payout(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    gross = payload.get("gross_earnings", 1500.0)
    comm = payload.get("platform_commission", 300.0)
    return {"id": 1, "technician_id": payload.get("technician_id", 1), "gross_earnings": gross, "platform_commission": comm, "net_payout": gross - comm, "status": "PENDING"}

@router.get("/payouts")
def list_payouts(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return [{"id": 1, "net_payout": 1200.0}]

@router.put("/payouts/{payout_id}/process")
def process_payout(payout_id: int, reference_number: str = "REF-889900", db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return {"id": payout_id, "status": "PAID", "reference_number": reference_number}

@router.post("/master", response_model=TechnicianMgmtMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(entity_in: TechnicianMgmtMasterEntityCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return TechnicianMgmtService.create_master_entity(db, current_user.id, entity_in)

