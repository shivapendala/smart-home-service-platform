import uuid
from datetime import datetime, timezone, timedelta
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.support_tickets import (
    SupportTicket, TicketComment, SatisfactionSurvey,
    TicketPriority, TicketStatus
)
from app.schemas.support_tickets import (
    SupportTicketCreate, TicketCommentCreate, SatisfactionSurveyCreate
)


class SupportTicketService:

    @staticmethod
    def create_ticket(db: Session, customer_id: int, ticket_in: SupportTicketCreate) -> SupportTicket:
        t_num = f"TCK-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"

        sla_hours = 24
        if ticket_in.priority == TicketPriority.CRITICAL_URGENT:
            sla_hours = 2
        elif ticket_in.priority == TicketPriority.HIGH:
            sla_hours = 6

        sla_due = datetime.now(timezone.utc) + timedelta(hours=sla_hours)

        ticket = SupportTicket(
            ticket_number=t_num,
            customer_id=customer_id,
            booking_id=ticket_in.booking_id,
            subject=ticket_in.subject,
            category=ticket_in.category,
            priority=ticket_in.priority,
            status=TicketStatus.OPEN,
            sla_due_at=sla_due
        )
        db.add(ticket)
        db.flush()

        initial_comment = TicketComment(
            ticket_id=ticket.id,
            author_id=customer_id,
            comment_text=ticket_in.initial_comment,
            is_internal_note=False
        )
        db.add(initial_comment)

        db.commit()
        db.refresh(ticket)
        return ticket

    @staticmethod
    def add_comment(db: Session, author_id: int, comment_in: TicketCommentCreate) -> TicketComment:
        ticket = db.query(SupportTicket).filter(SupportTicket.id == comment_in.ticket_id).first()
        if not ticket:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")

        comment = TicketComment(
            ticket_id=comment_in.ticket_id,
            author_id=author_id,
            comment_text=comment_in.comment_text,
            is_internal_note=comment_in.is_internal_note
        )
        db.add(comment)

        ticket.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(comment)
        return comment

    @staticmethod
    def update_ticket_status(db: Session, ticket_id: int, new_status: TicketStatus) -> SupportTicket:
        ticket = db.query(SupportTicket).filter(SupportTicket.id == ticket_id).first()
        if not ticket:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")

        ticket.status = new_status
        ticket.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(ticket)
        return ticket

    @staticmethod
    def get_customer_tickets(db: Session, customer_id: int) -> List[SupportTicket]:
        return db.query(SupportTicket).filter(SupportTicket.customer_id == customer_id).order_by(SupportTicket.created_at.desc()).all()

    @staticmethod
    def submit_survey(db: Session, survey_in: SatisfactionSurveyCreate) -> SatisfactionSurvey:
        ticket = db.query(SupportTicket).filter(SupportTicket.id == survey_in.ticket_id).first()
        if not ticket:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")

        survey = SatisfactionSurvey(
            ticket_id=survey_in.ticket_id,
            rating=survey_in.rating,
            feedback_notes=survey_in.feedback_notes
        )
        db.add(survey)
        db.commit()
        db.refresh(survey)
        return survey
