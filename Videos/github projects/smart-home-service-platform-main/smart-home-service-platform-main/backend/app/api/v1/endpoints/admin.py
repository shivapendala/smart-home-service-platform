from typing import List, Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.admin import (
    AdminDashboardStats, PaymentCreate, PaymentResponse, ReviewCreate, ReviewResponse,
    ComplaintCreate, ComplaintUpdate, ComplaintResponse
)
from app.schemas.user import UserResponse
from app.schemas.booking import BookingResponse
from app.models.user import User, UserRole
from app.services.admin_service import AdminService
from app.api.deps import get_current_user, require_roles

router = APIRouter()


# --- Admin Dashboard Stats ---

@router.get("/dashboard/stats", response_model=AdminDashboardStats)
def get_dashboard_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.ADMIN]))
):
    """Retrieve real-time admin KPIs and financial metrics (Admin only)."""
    return AdminService.get_dashboard_stats(db=db)


# --- Directory Management ---

@router.get("/customers", response_model=List[UserResponse])
def list_customers(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.ADMIN]))
):
    """Fetch customer directory list (Admin only)."""
    return db.query(User).filter(User.role == UserRole.CUSTOMER).all()


@router.get("/technicians", response_model=List[UserResponse])
def list_technicians(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.ADMIN]))
):
    """Fetch technician directory list (Admin only)."""
    return db.query(User).filter(User.role == UserRole.TECHNICIAN).all()


# --- Payments API ---

@router.get("/payments", response_model=List[PaymentResponse])
def list_payments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List payment transactions."""
    return AdminService.list_payments(db=db)


@router.post("/payments", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def process_payment(
    payment_in: PaymentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.CUSTOMER]))
):
    """Customer workflow: Pay for home service booking."""
    return AdminService.process_payment(db=db, payment_in=payment_in, customer=current_user)


@router.post("/payments/{payment_id}/refund", response_model=PaymentResponse)
def refund_payment(
    payment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.ADMIN]))
):
    """Admin workflow: Refund transaction."""
    return AdminService.refund_payment(db=db, payment_id=payment_id, admin=current_user)


# --- Reviews API ---

@router.get("/reviews", response_model=List[ReviewResponse])
def list_reviews(db: Session = Depends(get_db)):
    """Fetch all reviews."""
    return AdminService.list_reviews(db=db)


@router.post("/reviews", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
def create_review(
    review_in: ReviewCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.CUSTOMER]))
):
    """Customer workflow: Submit 1-5 star review for COMPLETED booking."""
    return AdminService.create_review(db=db, review_in=review_in, customer=current_user)


# --- Complaints API ---

@router.get("/complaints", response_model=List[ComplaintResponse])
def list_complaints(db: Session = Depends(get_db)):
    """Fetch all complaints ticketing records."""
    return AdminService.list_complaints(db=db)


@router.post("/complaints", response_model=ComplaintResponse, status_code=status.HTTP_201_CREATED)
def create_complaint(
    complaint_in: ComplaintCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.CUSTOMER]))
):
    """Customer workflow: Submit complaint regarding booking."""
    return AdminService.create_complaint(db=db, complaint_in=complaint_in, customer=current_user)


@router.patch("/complaints/{complaint_id}", response_model=ComplaintResponse)
def update_complaint(
    complaint_id: int,
    complaint_in: ComplaintUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.ADMIN]))
):
    """Admin workflow: View, assign, update, or resolve customer complaint."""
    return AdminService.update_complaint(db=db, complaint_id=complaint_id, complaint_in=complaint_in, admin=current_user)
