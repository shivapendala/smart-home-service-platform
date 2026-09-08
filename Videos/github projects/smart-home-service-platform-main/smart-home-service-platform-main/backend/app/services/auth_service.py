from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User, UserRole
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password, create_access_token
from app.schemas.token import Token


class AuthService:

    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[User]:
        """Fetch user by email address."""
        return db.query(User).filter(User.email == email.lower()).first()

    @staticmethod
    def get_by_id(db: Session, user_id: int) -> Optional[User]:
        """Fetch user by primary key ID."""
        return db.query(User).filter(User.id == user_id).first()

    @classmethod
    def register_user(cls, db: Session, user_in: UserCreate) -> User:
        """Register a new user (Customer, Technician, or Admin)."""
        existing_user = cls.get_by_email(db, user_in.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists."
            )

        hashed_password = get_password_hash(user_in.password)
        db_user = User(
            email=user_in.email.lower(),
            hashed_password=hashed_password,
            full_name=user_in.full_name,
            phone=user_in.phone,
            role=user_in.role,
            specialization=user_in.specialization,
            experience_years=user_in.experience_years or 0,
            bio=user_in.bio,
            is_active=True,
            is_verified=False
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @classmethod
    def authenticate_user(cls, db: Session, email: str, password: str) -> User:
        """Authenticate user by email and password."""
        user = cls.get_by_email(db, email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Inactive user account."
            )
        return user

    @classmethod
    def login_and_generate_token(cls, db: Session, email: str, password: str) -> Token:
        """Authenticate user and generate access token."""
        user = cls.authenticate_user(db, email, password)
        access_token = create_access_token(subject=user.id, role=user.role.value)
        return Token(
            access_token=access_token,
            token_type="bearer",
            user_id=user.id,
            email=user.email,
            role=user.role
        )

    @classmethod
    def update_user_profile(cls, db: Session, user: User, user_update: UserUpdate) -> User:
        """Update profile fields for existing user."""
        update_data = user_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
