import enum
from datetime import datetime, timezone, date, time
from typing import Optional, List, Dict, Any
from sqlalchemy import String, Enum as SQLEnum, DateTime, Integer, Float, Text, ForeignKey, Date, Boolean, Time, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class CustomerFeedbackStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    ARCHIVED = "ARCHIVED"

class CustomerFeedbackMasterEntity(Base):
    __tablename__ = "customer_feedback_master_entities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[CustomerFeedbackStatus] = mapped_column(SQLEnum(CustomerFeedbackStatus), default=CustomerFeedbackStatus.ACTIVE, nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    amount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    user: Mapped[Optional["User"]] = relationship("User", foreign_keys=[user_id])

class CustomerFeedbackRelationalComponent1(Base):
    __tablename__ = "customer_feedback_relational_components_1"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent1(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent2(Base):
    __tablename__ = "customer_feedback_relational_components_2"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=2, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent2(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent3(Base):
    __tablename__ = "customer_feedback_relational_components_3"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=3, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent3(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent4(Base):
    __tablename__ = "customer_feedback_relational_components_4"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=4, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent4(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent5(Base):
    __tablename__ = "customer_feedback_relational_components_5"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent5(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent6(Base):
    __tablename__ = "customer_feedback_relational_components_6"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=6, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent6(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent7(Base):
    __tablename__ = "customer_feedback_relational_components_7"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=7, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent7(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent8(Base):
    __tablename__ = "customer_feedback_relational_components_8"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=8, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent8(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent9(Base):
    __tablename__ = "customer_feedback_relational_components_9"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=9, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent9(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent10(Base):
    __tablename__ = "customer_feedback_relational_components_10"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent10(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent11(Base):
    __tablename__ = "customer_feedback_relational_components_11"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=11, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent11(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent12(Base):
    __tablename__ = "customer_feedback_relational_components_12"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=12, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent12(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent13(Base):
    __tablename__ = "customer_feedback_relational_components_13"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=13, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent13(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent14(Base):
    __tablename__ = "customer_feedback_relational_components_14"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=14, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent14(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent15(Base):
    __tablename__ = "customer_feedback_relational_components_15"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=15, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent15(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent16(Base):
    __tablename__ = "customer_feedback_relational_components_16"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=16, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent16(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent17(Base):
    __tablename__ = "customer_feedback_relational_components_17"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=17, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent17(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent18(Base):
    __tablename__ = "customer_feedback_relational_components_18"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=18, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent18(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent19(Base):
    __tablename__ = "customer_feedback_relational_components_19"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=19, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent19(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent20(Base):
    __tablename__ = "customer_feedback_relational_components_20"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=20, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent20(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent21(Base):
    __tablename__ = "customer_feedback_relational_components_21"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=21, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent21(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent22(Base):
    __tablename__ = "customer_feedback_relational_components_22"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=22, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent22(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent23(Base):
    __tablename__ = "customer_feedback_relational_components_23"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=23, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent23(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent24(Base):
    __tablename__ = "customer_feedback_relational_components_24"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=24, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent24(id={self.id}, name='{self.component_name}')>"

class CustomerFeedbackRelationalComponent25(Base):
    __tablename__ = "customer_feedback_relational_components_25"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("customer_feedback_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=25, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<CustomerFeedbackRelationalComponent25(id={self.id}, name='{self.component_name}')>"
