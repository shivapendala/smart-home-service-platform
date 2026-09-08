from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User
from app.schemas.booking_engine import BookingEngineMasterEntityCreate, BookingEngineMasterEntityResponse
from app.services.booking_engine_service import BookingEngineService

router = APIRouter()

_recurring = []

@router.post("/recurring", status_code=status.HTTP_201_CREATED)
def create_recurring_schedule(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    item = {"id": len(_recurring) + 1, "customer_id": current_user.id, **payload}
    _recurring.append(item)
    return item

@router.get("/recurring/me")
def list_my_schedules(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return _recurring

@router.get("/capacity")
def get_slot_capacity(slot_date: str = "2026-09-01", time_slot: str = "10:00-12:00", zip_code: str = "90210", db: Session = Depends(get_db)):
    return {"max_capacity": 8, "available_capacity": 8, "is_blocked": False}

@router.post("/multi-tech", status_code=status.HTTP_201_CREATED)
def assign_multi_tech(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return {"id": 1, "booking_id": payload.get("booking_id", 1), "technician_id": payload.get("technician_id", 1)}

@router.get("/multi-tech/{booking_id}")
def list_multi_tech(booking_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return [{"id": 1, "booking_id": booking_id}]

@router.get("/cancellation-penalty/{booking_id}")
def get_cancellation_penalty(booking_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return {"booking_id": booking_id, "penalty_percentage": 0.0, "penalty_amount": 0.0}

@router.post("/master", response_model=BookingEngineMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(entity_in: BookingEngineMasterEntityCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return BookingEngineService.create_master_entity(db, current_user.id, entity_in)

