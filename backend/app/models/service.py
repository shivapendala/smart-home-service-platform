from datetime import datetime, timezone
from typing import List
from sqlalchemy import String, Boolean, DateTime, Integer, Float, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    icon: Mapped[str] = mapped_column(String(50), nullable=False, default="🛠️")
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )

    # Relationship to services
    services: Mapped[List["Service"]] = relationship("Service", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Category(id={self.id}, name='{self.name}')>"


class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(150), index=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(150), unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    base_price: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False, default=60)
    image_url: Mapped[str] = mapped_column(String(500), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    # Relationship to Category
    category: Mapped["Category"] = relationship("Category", back_populates="services")

    def __repr__(self) -> str:
        return f"<Service(id={self.id}, name='{self.name}', base_price={self.base_price})>"
