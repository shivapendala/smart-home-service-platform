from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import String, DateTime, Integer, Text, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    action: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    entity_name: Mapped[str] = mapped_column(String(100), nullable=False)
    entity_id: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=False)
    user_agent: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    changes_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    user: Mapped[Optional["User"]] = relationship("User", foreign_keys=[user_id])

class UserSession(Base):
    __tablename__ = "user_sessions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    session_token: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=False)
    is_revoked: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    user: Mapped["User"] = relationship("User", foreign_keys=[user_id])

class SecurityIpPolicy(Base):
    __tablename__ = "security_ip_policies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    ip_address_or_cidr: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    policy_type: Mapped[str] = mapped_column(String(20), default="WHITELIST", nullable=False)
    reason: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)


import enum
from datetime import datetime, timezone, date, time
from typing import Optional, List, Dict, Any
from sqlalchemy import String, Enum as SQLEnum, DateTime, Integer, Float, Text, ForeignKey, Date, Boolean, Time, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class AuditSecurityStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    ARCHIVED = "ARCHIVED"

class AuditSecurityPriority(str, enum.Enum):
    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class AuditSecurityCategoryType(str, enum.Enum):
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"
    CUSTOM = "CUSTOM"
    ENTERPRISE = "ENTERPRISE"

class AuditSecurityMasterEntity(Base):
    __tablename__ = "audit_security_master_entities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[AuditSecurityStatus] = mapped_column(SQLEnum(AuditSecurityStatus), default=AuditSecurityStatus.ACTIVE, nullable=False)
    priority: Mapped[AuditSecurityPriority] = mapped_column(SQLEnum(AuditSecurityPriority), default=AuditSecurityPriority.NORMAL, nullable=False)
    category_type: Mapped[AuditSecurityCategoryType] = mapped_column(SQLEnum(AuditSecurityCategoryType), default=AuditSecurityCategoryType.PRIMARY, nullable=False)

    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    amount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    score: Mapped[float] = mapped_column(Float, default=100.0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_flagged: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    user: Mapped[Optional["User"]] = relationship("User", foreign_keys=[user_id])

class AuditSecurityRelationalComponent1(Base):
    __tablename__ = "audit_security_relational_components_1"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent1(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent2(Base):
    __tablename__ = "audit_security_relational_components_2"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent2(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent3(Base):
    __tablename__ = "audit_security_relational_components_3"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent3(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent4(Base):
    __tablename__ = "audit_security_relational_components_4"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent4(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent5(Base):
    __tablename__ = "audit_security_relational_components_5"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent5(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent6(Base):
    __tablename__ = "audit_security_relational_components_6"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent6(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent7(Base):
    __tablename__ = "audit_security_relational_components_7"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent7(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent8(Base):
    __tablename__ = "audit_security_relational_components_8"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent8(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent9(Base):
    __tablename__ = "audit_security_relational_components_9"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent9(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent10(Base):
    __tablename__ = "audit_security_relational_components_10"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent10(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent11(Base):
    __tablename__ = "audit_security_relational_components_11"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent11(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent12(Base):
    __tablename__ = "audit_security_relational_components_12"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent12(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent13(Base):
    __tablename__ = "audit_security_relational_components_13"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent13(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent14(Base):
    __tablename__ = "audit_security_relational_components_14"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent14(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent15(Base):
    __tablename__ = "audit_security_relational_components_15"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent15(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent16(Base):
    __tablename__ = "audit_security_relational_components_16"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent16(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent17(Base):
    __tablename__ = "audit_security_relational_components_17"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent17(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent18(Base):
    __tablename__ = "audit_security_relational_components_18"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent18(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent19(Base):
    __tablename__ = "audit_security_relational_components_19"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent19(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent20(Base):
    __tablename__ = "audit_security_relational_components_20"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent20(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent21(Base):
    __tablename__ = "audit_security_relational_components_21"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent21(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent22(Base):
    __tablename__ = "audit_security_relational_components_22"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent22(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent23(Base):
    __tablename__ = "audit_security_relational_components_23"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent23(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent24(Base):
    __tablename__ = "audit_security_relational_components_24"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent24(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent25(Base):
    __tablename__ = "audit_security_relational_components_25"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<AuditSecurityRelationalComponent25(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent26(Base):
    __tablename__ = "audit_security_relational_components_26"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<AuditSecurityRelationalComponent26(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent27(Base):
    __tablename__ = "audit_security_relational_components_27"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<AuditSecurityRelationalComponent27(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent28(Base):
    __tablename__ = "audit_security_relational_components_28"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<AuditSecurityRelationalComponent28(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent29(Base):
    __tablename__ = "audit_security_relational_components_29"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<AuditSecurityRelationalComponent29(id={self.id}, name='{self.component_name}')>"

class AuditSecurityRelationalComponent30(Base):
    __tablename__ = "audit_security_relational_components_30"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("audit_security_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<AuditSecurityRelationalComponent30(id={self.id}, name='{self.component_name}')>"
