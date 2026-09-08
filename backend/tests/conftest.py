import os
os.environ["TESTING"] = "1"
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.db.base import Base
from app.db.session import get_db
from app.core.security import create_access_token
from app.models.user import User, UserRole

# In-memory SQLite for fast isolated unit testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Create fresh database tables for each test session."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """FastAPI TestClient with overridden get_db dependency."""
    def _override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def test_customer_token(db_session):
    user = User(
        email="customer@example.com",
        hashed_password="hashed_password_123",
        full_name="Alice Customer",
        role=UserRole.CUSTOMER,
        is_active=True
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    token = create_access_token(subject=user.id, role=user.role.value)
    return {"token": token, "user": user}


@pytest.fixture
def test_technician_token(db_session):
    user = User(
        email="tech@example.com",
        hashed_password="hashed_password_123",
        full_name="Bob Technician",
        role=UserRole.TECHNICIAN,
        specialization="AC Repair & Plumbing",
        experience_years=5,
        is_active=True
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    token = create_access_token(subject=user.id, role=user.role.value)
    return {"token": token, "user": user}


@pytest.fixture
def test_admin_token(db_session):
    user = User(
        email="admin@example.com",
        hashed_password="hashed_password_123",
        full_name="Charlie Admin",
        role=UserRole.ADMIN,
        is_active=True
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    token = create_access_token(subject=user.id, role=user.role.value)
    return {"token": token, "user": user}
