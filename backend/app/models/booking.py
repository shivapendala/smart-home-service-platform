import enum
from datetime import datetime, timezone, date
from typing import Optional
from sqlalchemy import String, Enum as SQLEnum, DateTime, Integer, Float, Text, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class BookingStatus(str, enum.Enum):
    PENDING = "PENDING"
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    technician_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    service_id: Mapped[int] = mapped_column(Integer, ForeignKey("services.id", ondelete="RESTRICT"), nullable=False)

    scheduled_date: Mapped[date] = mapped_column(Date, nullable=False)
    scheduled_time_slot: Mapped[str] = mapped_column(String(50), nullable=False)  # e.g., "10:00 AM - 12:00 PM"
    
    address_line: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    zip_code: Mapped[str] = mapped_column(String(20), nullable=False)
    
    notes: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[BookingStatus] = mapped_column(
        SQLEnum(BookingStatus), default=BookingStatus.PENDING, nullable=False
    )
    total_amount: Mapped[float] = mapped_column(Float, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    # Relationships
    customer: Mapped["User"] = relationship("User", foreign_keys=[customer_id])
    technician: Mapped["User"] = relationship("User", foreign_keys=[technician_id])
    service: Mapped["Service"] = relationship("Service")

    def __repr__(self) -> str:
        return f"<Booking(id={self.id}, status='{self.status}', amount={self.total_amount})>"
