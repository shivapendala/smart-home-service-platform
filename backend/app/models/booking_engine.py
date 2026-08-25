import enum
from datetime import datetime, timezone, date, time
from typing import Optional, List
from sqlalchemy import String, Enum as SQLEnum, DateTime, Integer, Float, Text, ForeignKey, Date, Boolean, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class RecurrenceFrequency(str, enum.Enum):
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    BIANNUALLY = "BIANNUALLY"

class ScheduleStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    CANCELLED = "CANCELLED"
    EXPIRED = "EXPIRED"

class RecurringBookingSchedule(Base):
    __tablename__ = "recurring_booking_schedules"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    service_id: Mapped[int] = mapped_column(Integer, ForeignKey("services.id", ondelete="CASCADE"), nullable=False, index=True)
    address_id: Mapped[int] = mapped_column(Integer, ForeignKey("addresses.id", ondelete="CASCADE"), nullable=False)
    frequency: Mapped[RecurrenceFrequency] = mapped_column(SQLEnum(RecurrenceFrequency), default=RecurrenceFrequency.MONTHLY, nullable=False)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    preferred_time_slot: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[ScheduleStatus] = mapped_column(SQLEnum(ScheduleStatus), default=ScheduleStatus.ACTIVE, nullable=False)
    next_execution_date: Mapped[date] = mapped_column(Date, nullable=False)
    total_occurrences_created: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    customer: Mapped["User"] = relationship("User", foreign_keys=[customer_id])
    service: Mapped["Service"] = relationship("Service")

class TimeSlotCapacity(Base):
    __tablename__ = "time_slot_capacities"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    slot_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    time_slot: Mapped[str] = mapped_column(String(50), nullable=False)
    zip_code: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    max_capacity: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
    booked_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    surge_price_multiplier: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

class MultiTechAssignment(Base):
    __tablename__ = "multi_tech_assignments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    booking_id: Mapped[int] = mapped_column(Integer, ForeignKey("bookings.id", ondelete="CASCADE"), nullable=False, index=True)
    technician_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    role_title: Mapped[str] = mapped_column(String(100), default="ASSISTANT_TECHNICIAN", nullable=False)
    assigned_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    booking: Mapped["Booking"] = relationship("Booking")
    technician: Mapped["User"] = relationship("User", foreign_keys=[technician_id])

class BookingPenaltyPolicy(Base):
    __tablename__ = "booking_penalty_policies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    policy_name: Mapped[str] = mapped_column(String(100), nullable=False)
    hours_before_cancellation: Mapped[int] = mapped_column(Integer, nullable=False)
    penalty_percentage: Mapped[float] = mapped_column(Float, nullable=False)
    fixed_fee: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)


import enum
from datetime import datetime, timezone, date, time
from typing import Optional, List, Dict, Any
from sqlalchemy import String, Enum as SQLEnum, DateTime, Integer, Float, Text, ForeignKey, Date, Boolean, Time, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class BookingEngineStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    ARCHIVED = "ARCHIVED"

class BookingEnginePriority(str, enum.Enum):
    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class BookingEngineCategoryType(str, enum.Enum):
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"
    CUSTOM = "CUSTOM"
    ENTERPRISE = "ENTERPRISE"

class BookingEngineMasterEntity(Base):
    __tablename__ = "booking_engine_master_entities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[BookingEngineStatus] = mapped_column(SQLEnum(BookingEngineStatus), default=BookingEngineStatus.ACTIVE, nullable=False)
    priority: Mapped[BookingEnginePriority] = mapped_column(SQLEnum(BookingEnginePriority), default=BookingEnginePriority.NORMAL, nullable=False)
    category_type: Mapped[BookingEngineCategoryType] = mapped_column(SQLEnum(BookingEngineCategoryType), default=BookingEngineCategoryType.PRIMARY, nullable=False)

    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    amount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    score: Mapped[float] = mapped_column(Float, default=100.0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_flagged: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    user: Mapped[Optional["User"]] = relationship("User", foreign_keys=[user_id])

class BookingEngineRelationalComponent1(Base):
    __tablename__ = "booking_engine_relational_components_1"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent1(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent2(Base):
    __tablename__ = "booking_engine_relational_components_2"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent2(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent3(Base):
    __tablename__ = "booking_engine_relational_components_3"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent3(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent4(Base):
    __tablename__ = "booking_engine_relational_components_4"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent4(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent5(Base):
    __tablename__ = "booking_engine_relational_components_5"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent5(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent6(Base):
    __tablename__ = "booking_engine_relational_components_6"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent6(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent7(Base):
    __tablename__ = "booking_engine_relational_components_7"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent7(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent8(Base):
    __tablename__ = "booking_engine_relational_components_8"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent8(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent9(Base):
    __tablename__ = "booking_engine_relational_components_9"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent9(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent10(Base):
    __tablename__ = "booking_engine_relational_components_10"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent10(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent11(Base):
    __tablename__ = "booking_engine_relational_components_11"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent11(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent12(Base):
    __tablename__ = "booking_engine_relational_components_12"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent12(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent13(Base):
    __tablename__ = "booking_engine_relational_components_13"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent13(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent14(Base):
    __tablename__ = "booking_engine_relational_components_14"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent14(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent15(Base):
    __tablename__ = "booking_engine_relational_components_15"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent15(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent16(Base):
    __tablename__ = "booking_engine_relational_components_16"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent16(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent17(Base):
    __tablename__ = "booking_engine_relational_components_17"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent17(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent18(Base):
    __tablename__ = "booking_engine_relational_components_18"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent18(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent19(Base):
    __tablename__ = "booking_engine_relational_components_19"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent19(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent20(Base):
    __tablename__ = "booking_engine_relational_components_20"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent20(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent21(Base):
    __tablename__ = "booking_engine_relational_components_21"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent21(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent22(Base):
    __tablename__ = "booking_engine_relational_components_22"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent22(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent23(Base):
    __tablename__ = "booking_engine_relational_components_23"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent23(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent24(Base):
    __tablename__ = "booking_engine_relational_components_24"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent24(id={self.id}, name='{self.component_name}')>"

class BookingEngineRelationalComponent25(Base):
    __tablename__ = "booking_engine_relational_components_25"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("booking_engine_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<BookingEngineRelationalComponent25(id={self.id}, name='{self.component_name}')>"
