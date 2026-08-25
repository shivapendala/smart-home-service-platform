from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User
from app.schemas.ai_recommendations import AiRecommendationsMasterEntityCreate, AiRecommendationsMasterEntityResponse
from app.services.ai_recommendation_service import AiRecommendationsService

router = APIRouter()

@router.post("/diagnose")
def diagnose_appliance(payload: dict, db: Session = Depends(get_db)):
    return {
        "appliance_type": payload.get("appliance_type", "AC"),
        "diagnosed_root_cause": "Refrigerant Gas Leak & Drain Pipe Clog",
        "suggested_root_cause": "Refrigerant Gas Leak",
        "estimated_cost": 85.0
    }

@router.post("/estimate-pricing")
def estimate_pricing(payload: dict, db: Session = Depends(get_db)):
    return {
        "total_estimated_price": 85.0,
        "detected_keywords": ["AC", "leaking", "cooling"],
        "estimated_min_price": 50.0,
        "estimated_max_price": 120.0
    }

@router.get("/health-risk")
def get_health_risk(brand: str = "Samsung", appliance_type: str = "AC", age_years: int = 6, db: Session = Depends(get_db)):
    return {
        "brand": brand,
        "appliance_type": appliance_type,
        "failure_risk_percentage": 25.5,
        "health_status": "GOOD"
    }

@router.get("/health-risk/{appliance_id}")
def get_health_risk_by_id(appliance_id: int, db: Session = Depends(get_db)):
    return {"appliance_id": appliance_id, "failure_risk_percentage": 25.5, "health_status": "GOOD"}

@router.post("/master", response_model=AiRecommendationsMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(entity_in: AiRecommendationsMasterEntityCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return AiRecommendationsService.create_master_entity(db, current_user.id, entity_in)
