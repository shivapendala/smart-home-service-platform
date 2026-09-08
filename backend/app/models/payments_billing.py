import enum
from datetime import datetime, timezone, date
from typing import Optional, List
from sqlalchemy import String, Enum as SQLEnum, DateTime, Integer, Float, Text, ForeignKey, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class InvoiceStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    ISSUED = "ISSUED"
    PAID = "PAID"
    OVERDUE = "OVERDUE"
    VOID = "VOID"
    PARTIALLY_REFUNDED = "PARTIALLY_REFUNDED"
    FULLY_REFUNDED = "FULLY_REFUNDED"

class RefundStatus(str, enum.Enum):
    SUBMITTED = "SUBMITTED"
    UNDER_REVIEW = "UNDER_REVIEW"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PROCESSED = "PROCESSED"

class GatewayProvider(str, enum.Enum):
    STRIPE = "STRIPE"
    PAYPAL = "PAYPAL"
    RAZORPAY = "RAZORPAY"
    MOCK_GATEWAY = "MOCK_GATEWAY"

class Invoice(Base):
    __tablename__ = "invoices"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    invoice_number: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True)
    booking_id: Mapped[int] = mapped_column(Integer, ForeignKey("bookings.id", ondelete="CASCADE"), nullable=False, index=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    subtotal: Mapped[float] = mapped_column(Float, nullable=False)
    tax_amount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    discount_amount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    total_amount: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[InvoiceStatus] = mapped_column(SQLEnum(InvoiceStatus), default=InvoiceStatus.ISSUED, nullable=False)
    due_date: Mapped[date] = mapped_column(Date, nullable=False)
    paid_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    booking: Mapped["Booking"] = relationship("Booking")
    customer: Mapped["User"] = relationship("User", foreign_keys=[customer_id])
    items: Mapped[List["InvoiceItem"]] = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan")

class InvoiceItem(Base):
    __tablename__ = "invoice_items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    invoice_id: Mapped[int] = mapped_column(Integer, ForeignKey("invoices.id", ondelete="CASCADE"), nullable=False, index=True)
    item_description: Mapped[str] = mapped_column(String(255), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)
    item_type: Mapped[str] = mapped_column(String(50), default="LABOR", nullable=False)
    invoice: Mapped["Invoice"] = relationship("Invoice", back_populates="items")

class TaxRateConfig(Base):
    __tablename__ = "tax_rate_configs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    state_code: Mapped[str] = mapped_column(String(10), nullable=False, index=True)
    tax_name: Mapped[str] = mapped_column(String(100), nullable=False)
    tax_rate_percent: Mapped[float] = mapped_column(Float, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

class PaymentGatewayLog(Base):
    __tablename__ = "payment_gateway_logs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    invoice_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("invoices.id", ondelete="SET NULL"), nullable=True)
    booking_id: Mapped[int] = mapped_column(Integer, ForeignKey("bookings.id", ondelete="CASCADE"), nullable=False, index=True)
    provider: Mapped[GatewayProvider] = mapped_column(SQLEnum(GatewayProvider), default=GatewayProvider.MOCK_GATEWAY, nullable=False)
    transaction_reference: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    currency: Mapped[str] = mapped_column(String(10), default="USD", nullable=False)
    raw_response_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_successful: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

class RefundRequest(Base):
    __tablename__ = "refund_requests"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    invoice_id: Mapped[int] = mapped_column(Integer, ForeignKey("invoices.id", ondelete="CASCADE"), nullable=False, index=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    requested_amount: Mapped[float] = mapped_column(Float, nullable=False)
    approved_amount: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    reason: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[RefundStatus] = mapped_column(SQLEnum(RefundStatus), default=RefundStatus.SUBMITTED, nullable=False)
    reviewer_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    processed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    invoice: Mapped["Invoice"] = relationship("Invoice")
    customer: Mapped["User"] = relationship("User", foreign_keys=[customer_id])


import enum
from datetime import datetime, timezone, date, time
from typing import Optional, List, Dict, Any
from sqlalchemy import String, Enum as SQLEnum, DateTime, Integer, Float, Text, ForeignKey, Date, Boolean, Time, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class PaymentsBillingStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    ARCHIVED = "ARCHIVED"

class PaymentsBillingPriority(str, enum.Enum):
    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class PaymentsBillingCategoryType(str, enum.Enum):
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"
    CUSTOM = "CUSTOM"
    ENTERPRISE = "ENTERPRISE"

class PaymentsBillingMasterEntity(Base):
    __tablename__ = "payments_billing_master_entities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[PaymentsBillingStatus] = mapped_column(SQLEnum(PaymentsBillingStatus), default=PaymentsBillingStatus.ACTIVE, nullable=False)
    priority: Mapped[PaymentsBillingPriority] = mapped_column(SQLEnum(PaymentsBillingPriority), default=PaymentsBillingPriority.NORMAL, nullable=False)
    category_type: Mapped[PaymentsBillingCategoryType] = mapped_column(SQLEnum(PaymentsBillingCategoryType), default=PaymentsBillingCategoryType.PRIMARY, nullable=False)

    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    amount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    score: Mapped[float] = mapped_column(Float, default=100.0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_flagged: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    user: Mapped[Optional["User"]] = relationship("User", foreign_keys=[user_id])

class PaymentsBillingRelationalComponent1(Base):
    __tablename__ = "payments_billing_relational_components_1"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent1(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent2(Base):
    __tablename__ = "payments_billing_relational_components_2"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent2(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent3(Base):
    __tablename__ = "payments_billing_relational_components_3"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent3(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent4(Base):
    __tablename__ = "payments_billing_relational_components_4"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent4(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent5(Base):
    __tablename__ = "payments_billing_relational_components_5"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent5(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent6(Base):
    __tablename__ = "payments_billing_relational_components_6"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent6(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent7(Base):
    __tablename__ = "payments_billing_relational_components_7"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent7(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent8(Base):
    __tablename__ = "payments_billing_relational_components_8"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent8(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent9(Base):
    __tablename__ = "payments_billing_relational_components_9"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent9(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent10(Base):
    __tablename__ = "payments_billing_relational_components_10"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent10(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent11(Base):
    __tablename__ = "payments_billing_relational_components_11"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent11(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent12(Base):
    __tablename__ = "payments_billing_relational_components_12"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent12(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent13(Base):
    __tablename__ = "payments_billing_relational_components_13"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent13(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent14(Base):
    __tablename__ = "payments_billing_relational_components_14"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent14(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent15(Base):
    __tablename__ = "payments_billing_relational_components_15"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent15(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent16(Base):
    __tablename__ = "payments_billing_relational_components_16"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent16(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent17(Base):
    __tablename__ = "payments_billing_relational_components_17"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent17(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent18(Base):
    __tablename__ = "payments_billing_relational_components_18"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent18(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent19(Base):
    __tablename__ = "payments_billing_relational_components_19"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent19(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent20(Base):
    __tablename__ = "payments_billing_relational_components_20"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent20(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent21(Base):
    __tablename__ = "payments_billing_relational_components_21"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent21(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent22(Base):
    __tablename__ = "payments_billing_relational_components_22"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent22(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent23(Base):
    __tablename__ = "payments_billing_relational_components_23"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent23(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent24(Base):
    __tablename__ = "payments_billing_relational_components_24"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent24(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent25(Base):
    __tablename__ = "payments_billing_relational_components_25"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
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
        return f"<PaymentsBillingRelationalComponent25(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent26(Base):
    __tablename__ = "payments_billing_relational_components_26"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PaymentsBillingRelationalComponent26(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent27(Base):
    __tablename__ = "payments_billing_relational_components_27"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PaymentsBillingRelationalComponent27(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent28(Base):
    __tablename__ = "payments_billing_relational_components_28"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PaymentsBillingRelationalComponent28(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent29(Base):
    __tablename__ = "payments_billing_relational_components_29"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PaymentsBillingRelationalComponent29(id={self.id}, name='{self.component_name}')>"

class PaymentsBillingRelationalComponent30(Base):
    __tablename__ = "payments_billing_relational_components_30"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    master_entity_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payments_billing_master_entities.id", ondelete="CASCADE"), nullable=True, index=True)
    component_name: Mapped[str] = mapped_column(String(150), nullable=False)
    component_type: Mapped[str] = mapped_column(String(100), default="STANDARD", nullable=False)
    metric_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cost_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status_flag: Mapped[str] = mapped_column(String(50), default="ENABLED", nullable=False)
    notes_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self) -> str:
        return f"<PaymentsBillingRelationalComponent30(id={self.id}, name='{self.component_name}')>"
