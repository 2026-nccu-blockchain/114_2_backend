from fastapi import APIRouter

from app.api.v2.routers import health
from app.api.v2.routers import admin
from app.api.v2.routers import auth
from app.api.v2.routers import buyer
from app.api.v2.routers import driver
from app.api.v2.routers import order
from app.api.v2.routers import product
from app.api.v2.routers import seller
from app.api.v2.routers import upload
from app.api.v2.routers import cart

api_router = APIRouter(prefix="/api/v2")
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(buyer.router, prefix="/buyer", tags=["buyer"])
api_router.include_router(seller.router, prefix="/seller", tags=["seller"])
api_router.include_router(driver.router, prefix="/driver", tags=["driver"])
api_router.include_router(order.router, prefix="/orders", tags=["order"])
api_router.include_router(product.router, prefix="/products", tags=["product"])
api_router.include_router(upload.router, prefix="upload", tags=["upload"])
api_router.include_router(cart.router, prefix="/carts", tags=["cart"])
