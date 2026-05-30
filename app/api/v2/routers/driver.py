from fastapi import APIRouter, Depends, Request
from typing import Optional
from sqlalchemy.orm import Session
from app.schemas.driver import DriverUpdateRequest
from app.db.session import get_db
from app.models.model import Driver, Order, OrderStatus
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token, return_payload
from decimal import Decimal
import pytz

router = APIRouter()

@router.get("/me")
def get_driver_me(
    driver_id: Optional[str] = None,
    db: Session = Depends(get_db),
    payload: dict = Depends(return_payload)
):
    token_id = payload.get("id")
    if payload.get("role") != "driver" or not token_id:
        raise APIException(403, "10008", "permission denied")
    if driver_id is not None and driver_id != token_id:
        raise APIException(403, "10008", "permission denied")
    driver = db.query(Driver).filter(Driver.id == token_id, Driver.is_delete == False).first()
    if not driver:
        raise APIException(404, "10001", "driver not found")

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        user_id=driver.id,
        email=driver.email,
        phone=driver.phone,
        name=driver.name,
    )


@router.put("/me")
def update_driver_me(
    data: DriverUpdateRequest,
    driver_id: Optional[str] = None,
    db: Session = Depends(get_db),
    payload: dict = Depends(return_payload)
):
    token_id = payload.get("id")
    if payload.get("role") != "driver" or not token_id:
        raise APIException(403, "10008", "permission denied")
    if driver_id is not None and driver_id != token_id:
        raise APIException(403, "10008", "permission denied")
    driver = db.query(Driver).filter(Driver.id == token_id, Driver.is_delete == False).first()
    if not driver:
        raise APIException(404, "10001", "driver not found")

    driver.email = data.email
    driver.phone = data.phone
    driver.name = data.name

    db.commit()
    db.refresh(driver)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        email=driver.email,
        phone=driver.phone,
        name=driver.name,
    )


@router.delete("/{DriverId}")
def delete_driver(
    DriverId: str,
    db: Session = Depends(get_db),
    payload: dict = Depends(return_payload)
):
    token_id = payload.get("id")
    if payload.get("role") != "driver" or not token_id:
        raise APIException(403, "10008", "permission denied")
    if DriverId != token_id:
        raise APIException(403, "10008", "permission denied")
    driver = db.query(Driver).filter(Driver.id == token_id, Driver.is_delete == False).first()
    if not driver:
        raise APIException(404, "10001", "not found")

    driver.is_delete = True
    db.commit()

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
    )


@router.get("/look", response_model=APIResponse, response_model_exclude_none=True)
def driver_look_orders(request: Request, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "driver":
        raise APIException(403, "00004", "forbidden")
    orders = db.query(Order).filter(Order.driver_id.is_(None), Order.order_status == OrderStatus.PACKED).all()
    if not orders:
        raise APIException(404, "20004", "order not found")

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        order=[
            {
                "order_id": order.id,
                "buyer_id": order.buyer_id,
                "seller_id": order.seller_id,
                "from_addr": order.from_address,
                "to_addr": order.to_address,
                "order_status": order.order_status.value,
                "total_price": float(order.total_price)
            }
            for order in orders
        ]
    )


@router.post("/take/{OrderId}", response_model=APIResponse, response_model_exclude_none=True)
def driver_take_order(request: Request, OrderId: str, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "driver":
        raise APIException(403, "00004", "forbidden")
    order = db.query(Order).filter(Order.id == OrderId, Order.driver_id.is_(None), Order.order_status == OrderStatus.PACKED).first()
    if order is None:
        raise APIException(404, "20004", "order not found")
    order.driver_id = payload["id"]
    db.commit()
    db.refresh(order)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        order_id=order.id,
        buyer_id=order.buyer_id,
        seller_id=order.seller_id,
        driver_id=order.driver_id,
        from_addr=order.from_address,
        to_addr=order.to_address,
        order_status=order.order_status.value,
        total_price=float(order.total_price)
    )