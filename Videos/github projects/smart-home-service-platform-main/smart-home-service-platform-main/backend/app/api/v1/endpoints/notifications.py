from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.notification import NotificationResponse, NotificationListResponse
from app.services.notification_service import NotificationService
from app.models.user import User
from app.api.deps import get_current_user

router = APIRouter()


@router.get("", response_model=NotificationListResponse)
@router.get("/", response_model=NotificationListResponse)
def get_user_notifications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Retrieve in-app notifications and unread count for current user."""
    return NotificationService.get_user_notifications(db=db, user_id=current_user.id)


@router.patch("/read-all")
def mark_all_as_read(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Mark all unread notifications for current user as read."""
    count = NotificationService.mark_all_as_read(db=db, user_id=current_user.id)
    return {"message": "All notifications marked as read", "marked_count": count}


@router.patch("/{notification_id}/read", response_model=NotificationResponse)
def mark_single_as_read(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Mark a single notification as read (User isolation check)."""
    return NotificationService.mark_as_read(db=db, notification_id=notification_id, current_user=current_user)
