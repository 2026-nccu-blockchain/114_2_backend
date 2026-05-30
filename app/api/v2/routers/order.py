from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.session import get_db
from app.schemas.common import APIResponse
from app.models.model import Order, SelledProduct, Cart, OrderStatus, Seller
from app.core.exceptions import APIException
from app.core.deps import verify_token, return_payload
from app.schemas.order import (
    OrderCreateRequest,
    OrderUpdateStatusRequest,
)
from decimal import Decimal
from snowflake import SnowflakeGenerator
from collections import defaultdict
import pytz


router = APIRouter()
gen = SnowflakeGenerator(42)


@router.post("/order", response_model=APIResponse, response_model_exclude_none=True)
def add_order(request: Request, data: OrderCreateRequest, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "buyer":
        raise APIException(403, "00004", "forbidden")
    cart = db.query(Cart).filter(Cart.buyer_id == payload["id"], Cart.is_delete == False).all()
    if not cart:
        raise APIException(404, "20001", "product not found")
    grouped = defaultdict(list)
    for item in cart:
        grouped[item.seller_id].append(item)
    # try:
    for seller_id, products in grouped.items():
        seller = db.query(Seller).filter(Seller.id == seller_id).first()
        new_order = Order(
            oid=f"O{next(gen)}",
            buyer_id=payload["id"],
            seller_id=seller_id,
            from_address=seller.company_address,
            to_address=data.to_addr,
            total_price=0,
            order_status=OrderStatus(data.order_status)
        )
        db.add(new_order)
        db.flush()
        total_price = 0
        for product in products:
            total_price = Decimal(total_price + product.price * product.count).quantize(Decimal("0.00"))
            selled_product = SelledProduct(
                product_id=product.product_id,
                name=product.name,
                price=product.price,
                count=product.count,
                order_id=new_order.id
            )
            db.add(selled_product)
            db.flush()
        new_order.total_price = total_price
    db.commit()
    # except:
    #     db.rollback()
    #     raise APIException(500, "20010", "new order failed")
        
        
    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        
    )


@router.get("/{OrderId}")
def get_order(
    OrderId: str,
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
    OrderId: str,
    data: OrderUpdateStatusRequest,
    db: Session = Depends(get_db)
) -> dict:

    return APIResponse(
        status_code="00000",
        desc="order updated",
        response_datetime=datetime.utcnow(),
    )