import enum
from datetime import datetime, timezone, date
from typing import Optional, List
from sqlalchemy import String, Enum as SQLEnum, DateTime, Integer, Float, Text, ForeignKey, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class BookingStatus(str, enum.Enum):
    PENDING = "PENDING"
    ASSIGNED = "ASSIGNED"
    ACCEPTED = "ACCEPTED"
    ON_THE_WAY = "ON_THE_WAY"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


# Valid state machine transitions
ALLOWED_TRANSITIONS = {
    BookingStatus.PENDING: {BookingStatus.ASSIGNED, BookingStatus.CANCELLED},
    BookingStatus.ASSIGNED: {BookingStatus.ACCEPTED, BookingStatus.CANCELLED, BookingStatus.PENDING},
    BookingStatus.ACCEPTED: {BookingStatus.ON_THE_WAY, BookingStatus.CANCELLED},
    BookingStatus.ON_THE_WAY: {BookingStatus.IN_PROGRESS, BookingStatus.CANCELLED},
    BookingStatus.IN_PROGRESS: {BookingStatus.COMPLETED, BookingStatus.CANCELLED},
    BookingStatus.COMPLETED: set(),
    BookingStatus.CANCELLED: set(),
}


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    street_address: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str] = mapped_column(String(100), nullable=False, default="CA")
    zip_code: Mapped[str] = mapped_column(String(20), nullable=False)
    is_default: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )

    def __repr__(self) -> str:
        return f"<Address(id={self.id}, street='{self.street_address}', city='{self.city}')>"


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    service_id: Mapped[int] = mapped_column(Integer, ForeignKey("services.id", ondelete="RESTRICT"), nullable=False)
    address_id: Mapped[int] = mapped_column(Integer, ForeignKey("addresses.id", ondelete="RESTRICT"), nullable=False)
    technician_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    problem_description: Mapped[str] = mapped_column(Text, nullable=False)
    scheduled_date: Mapped[date] = mapped_column(Date, nullable=False)
    scheduled_time: Mapped[str] = mapped_column(String(50), nullable=False)

    status: Mapped[BookingStatus] = mapped_column(
        SQLEnum(BookingStatus), default=BookingStatus.PENDING, nullable=False
    )
    estimated_price: Mapped[float] = mapped_column(Float, nullable=False)
    final_price: Mapped[float] = mapped_column(Float, nullable=False)

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
    address: Mapped["Address"] = relationship("Address")
    status_history: Mapped[List["BookingStatusHistory"]] = relationship("BookingStatusHistory", back_populates="booking", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Booking(id={self.id}, status='{self.status}', estimated={self.estimated_price})>"


class BookingStatusHistory(Base):
    __tablename__ = "booking_status_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    booking_id: Mapped[int] = mapped_column(Integer, ForeignKey("bookings.id", ondelete="CASCADE"), nullable=False)
    old_status: Mapped[str] = mapped_column(String(50), nullable=False)
    new_status: Mapped[str] = mapped_column(String(50), nullable=False)
    changed_by_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    notes: Mapped[str] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )

    booking: Mapped["Booking"] = relationship("Booking", back_populates="status_history")

    def __repr__(self) -> str:
        return f"<BookingStatusHistory(booking_id={self.booking_id}, {self.old_status} -> {self.new_status})>"
