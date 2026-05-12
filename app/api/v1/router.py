from fastapi import APIRouter

from app.api.v1.routers import health
from app.api.v1.routers import auth

api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
