from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.audit_security import AuditLog


class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        # Audit sensitive mutations (POST, PUT, DELETE)
        if request.method in ["POST", "PUT", "DELETE"] and not request.url.path.startswith("/docs"):
            try:
                db: Session = SessionLocal()
                client_ip = request.client.host if request.client else "127.0.0.1"
                user_agent = request.headers.get("user-agent", "Unknown")

                audit_entry = AuditLog(
                    action=f"HTTP_{request.method}",
                    entity_name=request.url.path[:100],
                    ip_address=client_ip[:45],
                    user_agent=user_agent[:255]
                )
                db.add(audit_entry)
                db.commit()
                db.close()
            except Exception:
                pass

        return response
