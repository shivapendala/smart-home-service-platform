import os
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.core.logging import setup_logging
from app.db.base import Base
from app.db.session import engine
from app.api.v1.api import api_router
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.services import router as services_router
from app.api.v1.endpoints.bookings import router as bookings_router
from app.api.v1.endpoints.technicians import router as technicians_router
from app.api.v1.endpoints.admin import router as admin_router
from app.api.v1.endpoints.notifications import router as notifications_router

# Setup structured logging
setup_logging()
logger = logging.getLogger("smart_home_platform")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Ensure database tables exist
    logger.info("Initializing database tables...")
    Base.metadata.create_all(bind=engine)
    # Ensure local upload storage directory exists
    os.makedirs(settings.LOCAL_STORAGE_DIR, exist_ok=True)
    logger.info("Application startup complete.")
    yield
    logger.info("Application shutting down.")


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Global Production Error Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Exception on {request.method} {request.url.path}: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An internal server error occurred. Please try again later."}
    )

# Configure CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static storage endpoint
os.makedirs(settings.LOCAL_STORAGE_DIR, exist_ok=True)
app.mount("/static/uploads", StaticFiles(directory=settings.LOCAL_STORAGE_DIR), name="uploads")

# Mount API Routers under /api/v1 and direct aliases /api/auth, /api/services, /api/bookings, /api/technicians, /api/admin, /api/notifications
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication Direct"])
app.include_router(services_router, prefix="/api/services", tags=["Service Catalog Direct"])
app.include_router(bookings_router, prefix="/api/bookings", tags=["Bookings Direct"])
app.include_router(technicians_router, prefix="/api/technicians", tags=["Technicians Direct"])
app.include_router(admin_router, prefix="/api/admin", tags=["Admin Direct"])
app.include_router(admin_router, prefix="/api", tags=["Payments Reviews Complaints Direct"])
app.include_router(notifications_router, prefix="/api/notifications", tags=["Notifications Direct"])


@app.get("/health", tags=["Health"])
def health_check():
    """Application status health check endpoint."""
    return {
        "status": "healthy",
        "app_name": settings.PROJECT_NAME,
        "version": "1.0.0"
    }
