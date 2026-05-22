<<<<<<< HEAD:app/api/v1/routers/order.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.schemas.common import APIResponse
from app.schemas.order import (
    OrderCreateRequest,
    DriverTakeOrderRequest,
    OrderUpdateStatusRequest,
)

router = APIRouter()


@router.post("/add")
def add_order(
    data: OrderCreateRequest,
    db: Session = Depends(get_db)
) -> dict:

    return APIResponse(
        status_code="00000",
        desc="order created",
        response_datetime=datetime.utcnow(),
    )


@router.get("/driver/look")
def driver_look_orders(
    db: Session = Depends(get_db)
) -> dict:

    return APIResponse(
        status_code="00000",
        desc="get waiting orders",
        response_datetime=datetime.utcnow(),
    )


@router.post("/driver/look/take/{OrderId}")
def driver_take_order(
    OrderId: int,
    data: DriverTakeOrderRequest,
    db: Session = Depends(get_db)
) -> dict:

    return APIResponse(
        status_code="00000",
        desc="driver take order",
        response_datetime=datetime.utcnow(),
    )


@router.get("/{OrderId}")
def get_order(
    OrderId: int,
    db: Session = Depends(get_db)
) -> dict:

    return APIResponse(
        status_code="00000",
        desc="get order",
        response_datetime=datetime.utcnow(),
    )


@router.get("/me")
def get_my_orders(
    db: Session = Depends(get_db)
) -> dict:

    return APIResponse(
        status_code="00000",
        desc="get my orders",
        response_datetime=datetime.utcnow(),
    )


@router.put("/{OrderId}")
def update_order_status(
    OrderId: int,
    data: OrderUpdateStatusRequest,
    db: Session = Depends(get_db)
) -> dict:

    return APIResponse(
        status_code="00000",
        desc="order updated",
        response_datetime=datetime.utcnow(),
    )
=======
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
# from app.schemas.order import
from app.db.session import get_db
from app.models.model import Order, SelledProduct
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token

router = APIRouter()
>>>>>>> origin/develop:app/api/v2/routers/order.py
