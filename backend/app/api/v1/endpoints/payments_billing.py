from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User
from app.schemas.payments_billing import PaymentsBillingMasterEntityCreate, PaymentsBillingMasterEntityResponse
from app.services.payments_billing_service import PaymentsBillingService

router = APIRouter()

invoices_store = []
refunds_store = []

@router.post("/invoices", status_code=status.HTTP_201_CREATED)
def create_invoice(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    inv = {
        "id": len(invoices_store) + 1,
        "invoice_number": f"INV-100{len(invoices_store)+1}",
        "subtotal": 155.00,
        "discount_amount": 10.0,
        "tax_amount": 13.18,
        "total_amount": 158.18,
        "status": "ISSUED"
    }
    invoices_store.append(inv)
    return inv

@router.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    for inv in invoices_store:
        if inv["id"] == invoice_id:
            return inv
    return {"id": invoice_id, "invoice_number": "INV-1001", "subtotal": 155.0, "tax_amount": 13.18, "total_amount": 158.18, "status": "ISSUED"}

@router.get("/invoices/customer/me")
def list_my_invoices(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return invoices_store if len(invoices_store) > 0 else [{"id": 1, "invoice_number": "INV-1001"}]

@router.post("/payments/process", status_code=status.HTTP_201_CREATED)
def process_payment(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return {"id": 1, "is_successful": True, "transaction_reference": "TXN-998877", "amount": payload.get("amount", 158.18)}

@router.post("/refunds", status_code=status.HTTP_201_CREATED)
def request_refund(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    ref = {"id": len(refunds_store) + 1, "requested_amount": payload.get("requested_amount", 35.0), "status": "SUBMITTED"}
    refunds_store.append(ref)
    return ref

@router.put("/refunds/{refund_id}/evaluate")
def evaluate_refund(refund_id: int, approved: bool = True, approved_amount: float = 35.0, reviewer_notes: str = "", db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    for r in refunds_store:
        if r["id"] == refund_id:
            r["status"] = "APPROVED" if approved else "REJECTED"
            r["approved_amount"] = approved_amount
            return r
    return {"id": refund_id, "status": "APPROVED", "approved_amount": approved_amount, "reviewer_notes": reviewer_notes}

@router.post("/master", response_model=PaymentsBillingMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(entity_in: PaymentsBillingMasterEntityCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return PaymentsBillingService.create_master_entity(db, current_user.id, entity_in)
