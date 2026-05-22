from fastapi import APIRouter

from app.api.v2.routers import health
from app.api.v2.routers import admin
from app.api.v2.routers import auth
from app.api.v2.routers import buyer
from app.api.v2.routers import driver
from app.api.v2.routers import order
from app.api.v2.routers import other
from app.api.v2.routers import product
from app.api.v2.routers import seller


api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(admin.router, prefix="/api/v2/admin", tags=["admin"])
api_router.include_router(auth.router, prefix="/api/v2/auth", tags=["auth"])
api_router.include_router(buyer.router, prefix="/api/v2/buyer", tags=["buyer"])
api_router.include_router(driver.router, prefix="/api/v2/driver", tags=["driver"])
api_router.include_router(order.router, prefix="/api/v2/order", tags=["order"])
api_router.include_router(other.router, prefix="/api/v2", tags=["other"])
api_router.include_router(product.router, prefix="/api/v2/product", tags=["product"])
api_router.include_router(seller.router, prefix="/api/v2/seller", tags=["seller"])

