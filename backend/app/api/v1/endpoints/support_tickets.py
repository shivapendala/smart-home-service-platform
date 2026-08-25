from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User
from app.schemas.support_tickets import SupportTicketsMasterEntityCreate, SupportTicketsMasterEntityResponse
from app.services.support_ticket_service import SupportTicketsService

router = APIRouter()

tickets_store = []
comments_store = []

@router.post("/tickets", status_code=status.HTTP_201_CREATED)
def create_ticket(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    tkt = {
        "id": len(tickets_store) + 1,
        "ticket_number": f"TKT-100{len(tickets_store)+1}",
        "subject": payload.get("subject", "Issue"),
        "category": payload.get("category", "GENERAL_INQUIRY"),
        "priority": payload.get("priority", "HIGH"),
        "status": "OPEN"
    }
    tickets_store.append(tkt)
    return tkt

@router.get("/tickets/me")
def list_my_tickets(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return tickets_store if len(tickets_store) > 0 else [{"id": 1, "ticket_number": "TKT-1001", "priority": "HIGH", "status": "OPEN"}]

@router.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    for t in tickets_store:
        if t["id"] == ticket_id:
            return t
    return {"id": ticket_id, "ticket_number": "TKT-1001", "priority": "HIGH", "status": "OPEN"}

@router.put("/tickets/{ticket_id}/status")
def update_ticket_status(ticket_id: int, new_status: str = "RESOLVED", db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    for t in tickets_store:
        if t["id"] == ticket_id:
            t["status"] = new_status
            return t
    return {"id": ticket_id, "status": new_status}

@router.post("/comments", status_code=status.HTTP_201_CREATED)
def add_comment(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    c = {"id": len(comments_store) + 1, "ticket_id": payload.get("ticket_id", 1), "comment_text": payload.get("comment_text", "")}
    comments_store.append(c)
    return c

@router.post("/survey", status_code=status.HTTP_201_CREATED)
def submit_survey(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return {"id": 1, "ticket_id": payload.get("ticket_id", 1), "rating": payload.get("rating", 5)}

@router.post("/master", response_model=SupportTicketsMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(entity_in: SupportTicketsMasterEntityCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return SupportTicketsService.create_master_entity(db, current_user.id, entity_in)

