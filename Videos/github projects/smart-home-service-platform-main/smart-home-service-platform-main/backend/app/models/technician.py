import enum
from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import String, Boolean, DateTime, Integer, Float, Text, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class PhotoType(str, enum.Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"


class TechnicianProfile(Base):
    __tablename__ = "technician_profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    specialization: Mapped[str] = mapped_column(String(255), nullable=False, default="General Technician")
    experience_years: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    bio: Mapped[str] = mapped_column(Text, nullable=True)
    hourly_rate: Mapped[float] = mapped_column(Float, default=45.0, nullable=False)
    rating: Mapped[float] = mapped_column(Float, default=5.0, nullable=False)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    user: Mapped["User"] = relationship("User")

    def __repr__(self) -> str:
        return f"<TechnicianProfile(user_id={self.user_id}, specialization='{self.specialization}')>"


class ServicePhoto(Base):
    __tablename__ = "service_photos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    booking_id: Mapped[int] = mapped_column(Integer, ForeignKey("bookings.id", ondelete="CASCADE"), nullable=False)
    photo_url: Mapped[str] = mapped_column(String(500), nullable=False)
    photo_type: Mapped[PhotoType] = mapped_column(SQLEnum(PhotoType), default=PhotoType.BEFORE, nullable=False)
    uploaded_by_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )

    booking: Mapped["Booking"] = relationship("Booking")
    uploaded_by: Mapped["User"] = relationship("User")

    def __repr__(self) -> str:
        return f"<ServicePhoto(id={self.id}, booking_id={self.booking_id}, type='{self.photo_type}')>"


class ServiceNote(Base):
    __tablename__ = "service_notes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    booking_id: Mapped[int] = mapped_column(Integer, ForeignKey("bookings.id", ondelete="CASCADE"), nullable=False)
    note_text: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )

    booking: Mapped["Booking"] = relationship("Booking")
    author: Mapped["User"] = relationship("User")

    def __repr__(self) -> str:
        return f"<ServiceNote(id={self.id}, booking_id={self.booking_id}, author={self.author_id})>"
