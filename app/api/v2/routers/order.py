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
        raise APIException(404, "20011", "no product in cart")
    grouped = defaultdict(list)
    for item in cart:
        grouped[item.seller_id].append(item)
    order_response = []
    try:
        for seller_id, cart_products in grouped.items():
            seller = db.query(Seller).filter(Seller.id == seller_id).first()
            new_order = Order(
                oid=f"O{next(gen)}",
                buyer_id=payload["id"],
                seller_id=seller_id,
                from_address=seller.company_address,
                to_address=data.to_addr,
                total_price=0,
                order_status=OrderStatus.ORDERED
            )
            db.add(new_order)
            db.flush()
            total_price = 0
            products = []
            for cart_product in cart_products:
                total_price = Decimal(total_price + cart_product.price * cart_product.count).quantize(Decimal("0.00"))
                selled_product = SelledProduct(
                    product_id=cart_product.product_id,
                    name=cart_product.name,
                    price=cart_product.price,
                    count=cart_product.count,
                    order_id=new_order.id
                )
                cart_product.is_delete = True
                db.add(selled_product)
                db.flush()
                products.append(selled_product)
            new_order.total_price = total_price
            order_response.append(
                {
                    "order_id": new_order.id,
                    "buyer_id": new_order.buyer_id,
                    "seller_id": new_order.seller_id,
                    "from_addr": new_order.from_address,
                    "to_addr": new_order.to_address,
                    "order_status": new_order.order_status.value,
                    "total_price": float(new_order.total_price),
                    "product": [
                        {
                            "product_id": product.id,
                            "name": product.name,
                            # "type": product.type,
                            "price": float(product.price),
                            "count": product.count
                        }
                        for product in products
                    ]
                }
            )
        db.commit()
    except:
        db.rollback()
        raise APIException(500, "20010", "new order failed")
    db.refresh(new_order)
        
    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        order=order_response
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