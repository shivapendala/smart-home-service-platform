import os
from typing import List, Union
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Smart Home Service Platform"
    API_V1_STR: str = "/api/v1"
    
    # JWT Secrets
    SECRET_KEY: str = "SUPER_SECRET_KEY_CHANGE_IN_PRODUCTION_9876543210_SMART_HOME"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "*",
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        "https://localhost",
        "http://localhost",
    ]

    # Database
    DATABASE_URL: str = os.getenv("TEST_DATABASE_URL", "sqlite:///./test.db") if os.getenv("TESTING") == "1" else "sqlite:///./smarthome.db"
    
    # Storage
    STORAGE_TYPE: str = "local"  # "local" or "s3"
    LOCAL_STORAGE_DIR: str = os.path.join(os.getcwd(), "uploads")
    S3_BUCKET_NAME: str = "smart-home-service-bucket"
    AWS_REGION: str = "us-east-1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


settings = Settings()
