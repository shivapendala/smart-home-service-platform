import enum
from datetime import datetime, timezone, date, time
from typing import Optional, List, Dict, Any
from sqlalchemy import String, Enum as SQLEnum, DateTime, Integer, Float, Text, ForeignKey, Date, Boolean, Time, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class PlatformGovernanceStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"

class PlatformGovernanceMasterEntity(Base):
    __tablename__ = "platform_governance_master_entities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[PlatformGovernanceStatus] = mapped_column(SQLEnum(PlatformGovernanceStatus), default=PlatformGovernanceStatus.ACTIVE, nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    amount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    user: Mapped[Optional["User"]] = relationship("User", foreign_keys=[user_id])

class PlatformGovernanceRelationalComponent1(Base):
    __tablename__ = "platform_governance_relational_components_1"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent1(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent2(Base):
    __tablename__ = "platform_governance_relational_components_2"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=2, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent2(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent3(Base):
    __tablename__ = "platform_governance_relational_components_3"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=3, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent3(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent4(Base):
    __tablename__ = "platform_governance_relational_components_4"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=4, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent4(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent5(Base):
    __tablename__ = "platform_governance_relational_components_5"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent5(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent6(Base):
    __tablename__ = "platform_governance_relational_components_6"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=6, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent6(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent7(Base):
    __tablename__ = "platform_governance_relational_components_7"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=7, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent7(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent8(Base):
    __tablename__ = "platform_governance_relational_components_8"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=8, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent8(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent9(Base):
    __tablename__ = "platform_governance_relational_components_9"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=9, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent9(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent10(Base):
    __tablename__ = "platform_governance_relational_components_10"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent10(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent11(Base):
    __tablename__ = "platform_governance_relational_components_11"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=11, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent11(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent12(Base):
    __tablename__ = "platform_governance_relational_components_12"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=12, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent12(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent13(Base):
    __tablename__ = "platform_governance_relational_components_13"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=13, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent13(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent14(Base):
    __tablename__ = "platform_governance_relational_components_14"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=14, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent14(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent15(Base):
    __tablename__ = "platform_governance_relational_components_15"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=15, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent15(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent16(Base):
    __tablename__ = "platform_governance_relational_components_16"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=16, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent16(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent17(Base):
    __tablename__ = "platform_governance_relational_components_17"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=17, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent17(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent18(Base):
    __tablename__ = "platform_governance_relational_components_18"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=18, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent18(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent19(Base):
    __tablename__ = "platform_governance_relational_components_19"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=19, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent19(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent20(Base):
    __tablename__ = "platform_governance_relational_components_20"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=20, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent20(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent21(Base):
    __tablename__ = "platform_governance_relational_components_21"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=21, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent21(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent22(Base):
    __tablename__ = "platform_governance_relational_components_22"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=22, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent22(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent23(Base):
    __tablename__ = "platform_governance_relational_components_23"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=23, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent23(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent24(Base):
    __tablename__ = "platform_governance_relational_components_24"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=24, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent24(id={self.id}, name='{self.component_name}')>"

class PlatformGovernanceRelationalComponent25(Base):
    __tablename__ = "platform_governance_relational_components_25"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("platform_governance_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=25, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PlatformGovernanceRelationalComponent25(id={self.id}, name='{self.component_name}')>"
