from fastapi import APIRouter
from app.api.v1.endpoints import auth, services, bookings

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(services.router, prefix="/services", tags=["Service Catalog"])
api_router.include_router(bookings.router, prefix="/bookings", tags=["Bookings"])
