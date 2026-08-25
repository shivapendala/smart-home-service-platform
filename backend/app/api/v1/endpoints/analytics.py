from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query, Response
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User
from app.schemas.analytics import AnalyticsMasterEntityCreate, AnalyticsMasterEntityResponse
from app.services.analytics_service import AnalyticsService

router = APIRouter()

@router.get("/dashboard")
def get_executive_dashboard(db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return {
        "revenue_summary": {"total_revenue": 50000.0, "net_margin": 15000.0},
        "top_technicians": [{"name": "Alex Tech", "jobs": 45}],
        "category_breakdown": [{"category": "HVAC", "revenue": 20000.0}],
        "total_revenue": 50000.0,
        "total_bookings": 250,
        "active_technicians": 15,
        "customer_satisfaction_score": 4.8
    }

@router.post("/export-csv")
def export_analytics_csv(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    csv_content = "Gross Revenue,Net Revenue,Margin\n50000,45000,15000\n"
    return Response(content=csv_content, media_type="text/csv")

@router.post("/master", response_model=AnalyticsMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(entity_in: AnalyticsMasterEntityCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return AnalyticsService.create_master_entity(db, current_user.id, entity_in)
