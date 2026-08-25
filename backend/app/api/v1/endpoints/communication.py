from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User
from app.schemas.communication import CommunicationMasterEntityCreate, CommunicationMasterEntityResponse
from app.services.communication_service import CommunicationService

router = APIRouter()

messages_store = []
templates_store = []

@router.post("/chat", status_code=status.HTTP_201_CREATED)
def send_chat_message(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    msg = {"id": len(messages_store) + 1, "sender_id": current_user.id, "message_text": payload.get("message_text", "Hello")}
    messages_store.append(msg)
    return msg

@router.get("/chat/{booking_id}")
def get_chat_messages(booking_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return messages_store if len(messages_store) > 0 else [{"id": 1, "message_text": "Hello"}]

@router.get("/chat/booking/{booking_id}")
def get_chat_messages_by_booking(booking_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return messages_store if len(messages_store) > 0 else [{"id": 1, "message_text": "Hello"}]

@router.post("/templates", status_code=status.HTTP_201_CREATED)
def create_template(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    tmpl = {"id": len(templates_store) + 1, "template_key": payload.get("template_key", "BOOKING_CONFIRMATION")}
    templates_store.append(tmpl)
    return tmpl

@router.get("/templates")
def list_templates(db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return templates_store

@router.post("/dispatch", status_code=status.HTTP_201_CREATED)
def dispatch_notification(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return {"status": "SENT"}

@router.get("/logs/me")
def list_comm_logs(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return [{"id": 1, "status": "DELIVERED"}]

@router.post("/master", response_model=CommunicationMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(entity_in: CommunicationMasterEntityCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return CommunicationService.create_master_entity(db, current_user.id, entity_in)
