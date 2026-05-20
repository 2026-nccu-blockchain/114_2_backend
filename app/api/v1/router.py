from fastapi import APIRouter

from app.api.v1.routers import health
from app.api.v1.routers import auth
from app.api.v1.routers import buyer
from app.api.v1.routers import seller
from app.api.v1.routers import product
from app.api.v1.routers import order
from app.api.v1.routers import driver
from app.api.v1.routers import admin

api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(buyer.router, prefix="/buyer", tags=["buyer"])
api_router.include_router(seller.router, prefix="/seller", tags=["seller"])
api_router.include_router(product.router, prefix="/product", tags=["product"])
api_router.include_router(order.router, prefix="/order", tags=["order"])
api_router.include_router(driver.router, prefix="/driver", tags=["driver"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
