import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.api.v1.api import api_router
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.services import router as services_router
from app.api.v1.endpoints.bookings import router as bookings_router
from app.api.v1.endpoints.technicians import router as technicians_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Ensure database tables exist
    Base.metadata.create_all(bind=engine)
    # Ensure local upload storage directory exists
    os.makedirs(settings.LOCAL_STORAGE_DIR, exist_ok=True)
    yield
    # Shutdown logic if needed


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# Configure CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static storage endpoint
os.makedirs(settings.LOCAL_STORAGE_DIR, exist_ok=True)
app.mount("/static/uploads", StaticFiles(directory=settings.LOCAL_STORAGE_DIR), name="uploads")

# Mount API Routers under /api/v1 and direct aliases /api/auth, /api/services, /api/bookings, /api/technicians
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication Direct"])
app.include_router(services_router, prefix="/api/services", tags=["Service Catalog Direct"])
app.include_router(bookings_router, prefix="/api/bookings", tags=["Bookings Direct"])
app.include_router(technicians_router, prefix="/api/technicians", tags=["Technicians Direct"])


@app.get("/health", tags=["Health"])
def health_check():
    """Application status health check endpoint."""
    return {
        "status": "healthy",
        "app_name": settings.PROJECT_NAME,
        "version": "1.0.0"
    }
