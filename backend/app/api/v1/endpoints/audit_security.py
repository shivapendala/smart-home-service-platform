from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_active_user, get_current_admin_user
from app.models.user import User
from app.schemas.audit_security import AuditSecurityMasterEntityCreate, AuditSecurityMasterEntityResponse
from app.services.audit_security_service import AuditSecurityService

router = APIRouter()

ip_policies_store = []

@router.get("/logs")
def list_audit_logs(db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return [{"id": 1, "action": "LOGIN", "entity_name": "USER"}]

@router.get("/ip-policies")
def list_ip_policies(db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return ip_policies_store

@router.post("/ip-policies", status_code=status.HTTP_201_CREATED)
def create_ip_policy(payload: dict, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    policy = {"id": len(ip_policies_store) + 1, "ip_address_or_cidr": payload.get("ip_address_or_cidr", "192.168.1.1"), "policy_type": payload.get("policy_type", "WHITELIST")}
    ip_policies_store.append(policy)
    return policy

@router.post("/master", response_model=AuditSecurityMasterEntityResponse, status_code=status.HTTP_201_CREATED)
def create_master_entity(entity_in: AuditSecurityMasterEntityCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return AuditSecurityService.create_master_entity(db, current_user.id, entity_in)

