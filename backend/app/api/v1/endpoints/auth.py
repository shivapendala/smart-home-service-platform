from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserCreate, UserLogin, UserResponse, UserUpdate
from app.schemas.token import Token
from app.services.auth_service import AuthService
from app.models.user import User, UserRole
from app.api.deps import get_current_user, require_roles

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    """Register a new user (Customer, Technician, or Admin)."""
    return AuthService.register_user(db=db, user_in=user_in)


@router.post("/login", response_model=Token)
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    """Authenticate user with JSON credentials and return JWT access token."""
    return AuthService.login_and_generate_token(
        db=db, email=user_in.email, password=user_in.password
    )


@router.post("/login/token", response_model=Token)
def login_form(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """Authenticate user with Form Data (Swagger UI compatible) and return JWT access token."""
    return AuthService.login_and_generate_token(
        db=db, email=form_data.username, password=form_data.password
    )


@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    """Retrieve profile details for currently authenticated user."""
    return current_user


@router.put("/me", response_model=UserResponse)
def update_current_user(
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update profile details for currently authenticated user."""
    return AuthService.update_user_profile(
        db=db, user=current_user, user_update=user_update
    )


@router.get("/technicians", response_model=List[UserResponse])
def list_technicians(db: Session = Depends(get_db)):
    """List all registered technicians in the platform."""
    return db.query(User).filter(
        User.role == UserRole.TECHNICIAN,
        User.is_active == True
    ).all()
