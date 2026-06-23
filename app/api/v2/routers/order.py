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
                    type=cart_product.type,
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
                    "oid": new_order.oid,
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
                            "type": product.type,
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
        
    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        order=order_response
    )


@router.get("/order/{OrderId}", response_model=APIResponse, response_model_exclude_none=True)
def get_order(request: Request, OrderId: str, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    order = db.query(Order).filter(Order.id == OrderId).first()
    if order is None:
        raise APIException(404, "20004", "order not found")
    if payload["role"] == "buyer" and order.buyer_id == payload["id"] or payload["role"] == "seller" and order.seller_id == payload["id"]:
        products = order.selled_products
        
        return APIResponse(
            status_code="00000",
            message="success",
            response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
            order_id=order.id,
            oid=order.oid,
            buyer_id=order.buyer_id,
            seller_id=order.seller_id,
            driver_id=order.driver_id,
            from_addr=order.from_address,
            to_addr=order.to_address,
            order_status=order.order_status.value,
            total_price=float(order.total_price),
            product=[
                {
                    "product_id": product.product_id,
                    "name": product.name,
                    "type": product.type,
                    "price": float(product.price),
                    "count": product.count
                }
                for product in products
            ]
        )
    elif payload["role"] == "driver" and order.driver_id == payload["id"]:
        return APIResponse(
            status_code="00000",
            message="success",
            response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
            order_id=order.id,
            oid=order.oid,
            buyer_id=order.buyer_id,
            seller_id=order.seller_id,
            driver_id=order.driver_id,
            from_addr=order.from_address,
            to_addr=order.to_address,
            order_status=order.order_status.value,
            total_price=float(order.total_price)
        )
    else:
        raise APIException(403, "00004", "forbidden")


def serialize_order(order):
    return {
        "order_id": order.id,
        "oid": order.oid,
        "buyer_id": order.buyer_id,
        "seller_id": order.seller_id,
        "driver_id": order.driver_id,
        "from_addr": order.from_address,
        "to_addr": order.to_address,
        "order_status": order.order_status.value,
        "total_price": float(order.total_price)
    }

@router.get("/me", response_model=APIResponse, response_model_exclude_none=True)
def get_my_orders(request: Request, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] == "buyer":
        ordered_orders = db.query(Order).filter(Order.buyer_id == payload["id"], Order.order_status == OrderStatus.ORDERED).all()
        ordered_list = []
        if ordered_orders:
            for order in ordered_orders:
                ordered_list.append(serialize_order(order))
        success_orders = db.query(Order).filter(Order.buyer_id == payload["id"], Order.order_status == OrderStatus.SUCCESS).all()
        success_list = []
        if success_orders:
            for order in success_orders:
                success_list.append(serialize_order(order))
        packed_orders = db.query(Order).filter(Order.buyer_id == payload["id"], Order.order_status == OrderStatus.PACKED).all()
        packed_list = []
        if packed_orders:
            for order in packed_orders:
                packed_list.append(serialize_order(order))
        deliver_orders = db.query(Order).filter(Order.buyer_id == payload["id"], Order.order_status == OrderStatus.DELIVER).all()
        deliver_list = []
        if deliver_orders:
            for order in deliver_orders:
                deliver_list.append(serialize_order(order))
        arrived_orders = db.query(Order).filter(Order.buyer_id == payload["id"], Order.order_status == OrderStatus.ARRIVED).all()
        arrived_list = []
        if arrived_orders:
            for order in arrived_orders:
                arrived_list.append(serialize_order(order))
        refund_orders = db.query(Order).filter(Order.buyer_id == payload["id"], Order.order_status == OrderStatus.REFUND).all()
        refund_list = []
        if refund_orders:
            for order in refund_orders:
                refund_list.append(serialize_order(order))
        fail_orders = db.query(Order).filter(Order.buyer_id == payload["id"], Order.order_status == OrderStatus.FAIL).all()
        fail_list = []
        if fail_orders:
            for order in fail_orders:
                fail_list.append(serialize_order(order))

        return APIResponse(
            status_code="00000",
            message="success",
            response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
            ordered_order=ordered_list,
            success_order=success_list,
            packed_order=packed_list,
            deliver_order=deliver_list,
            arrived_order=arrived_list,
            refund_order=refund_list,
            fail_order=fail_list
        )
    elif payload["role"] == "seller":
        ordered_orders = db.query(Order).filter(Order.seller_id == payload["id"], Order.order_status == OrderStatus.ORDERED).all()
        ordered_list = []
        if ordered_orders:
            for order in ordered_orders:
                ordered_list.append(serialize_order(order))
        success_orders = db.query(Order).filter(Order.seller_id == payload["id"], Order.order_status == OrderStatus.SUCCESS).all()
        success_list = []
        if success_orders:
            for order in success_orders:
                success_list.append(serialize_order(order))
        packed_orders = db.query(Order).filter(Order.seller_id == payload["id"], Order.order_status == OrderStatus.PACKED).all()
        packed_list = []
        if packed_orders:
            for order in packed_orders:
                packed_list.append(serialize_order(order))
        deliver_orders = db.query(Order).filter(Order.seller_id == payload["id"], Order.order_status == OrderStatus.DELIVER).all()
        deliver_list = []
        if deliver_orders:
            for order in deliver_orders:
                deliver_list.append(serialize_order(order))
        arrived_orders = db.query(Order).filter(Order.seller_id == payload["id"], Order.order_status == OrderStatus.ARRIVED).all()
        arrived_list = []
        if arrived_orders:
            for order in arrived_orders:
                arrived_list.append(serialize_order(order))
        refund_orders = db.query(Order).filter(Order.seller_id == payload["id"], Order.order_status == OrderStatus.REFUND).all()
        refund_list = []
        if refund_orders:
            for order in refund_orders:
                refund_list.append(serialize_order(order))
        fail_orders = db.query(Order).filter(Order.seller_id == payload["id"], Order.order_status == OrderStatus.FAIL).all()
        fail_list = []
        if fail_orders:
            for order in fail_orders:
                fail_list.append(serialize_order(order))

        return APIResponse(
            status_code="00000",
            message="success",
            response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
            ordered_order=ordered_list,
            success_order=success_list,
            packed_order=packed_list,
            deliver_order=deliver_list,
            arrived_order=arrived_list,
            refund_order=refund_list,
            fail_order=fail_list
        )
    elif payload["role"] == "driver":
        deliver_orders = db.query(Order).filter(Order.seller_id == payload["id"], Order.order_status == OrderStatus.DELIVER).all()
        deliver_list = []
        if deliver_orders:
            for order in deliver_orders:
                deliver_list.append(serialize_order(order))
        arrived_orders = db.query(Order).filter(Order.seller_id == payload["id"], Order.order_status == OrderStatus.ARRIVED).all()
        arrived_list = []
        if arrived_orders:
            for order in arrived_orders:
                arrived_list.append(serialize_order(order))
        refund_orders = db.query(Order).filter(Order.seller_id == payload["id"], Order.order_status == OrderStatus.REFUND).all()
        refund_list = []
        if refund_orders:
            for order in refund_orders:
                refund_list.append(serialize_order(order))

        return APIResponse(
            status_code="00000",
            message="success",
            response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
            deliver_order=deliver_list,
            arrived_order=arrived_list,
            refund_order=refund_list
        )
    else:
        raise APIException(403, "00004", "forbidden")


@router.put("/order/{OrderId}", response_model=APIResponse, response_model_exclude_none=True)
def update_order_status(request: Request, OrderId: str, data: OrderUpdateStatusRequest, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    order = db.query(Order).filter(Order.id == OrderId).first()
    if order is None:
        raise APIException(404, "20004", "order not found")
    if payload["role"] == "buyer" and order.buyer_id == payload["id"]:
        if data.status == "refund" and order.order_status != OrderStatus.FAIL:
            order.order_status = OrderStatus.REFUND
            selled_products = order.selled_products
            for sp in selled_products:
                product = sp.product
                product.stock += sp.count
                sp.is_refund = True
        else:
            raise APIException(403, "00004", "forbidden")
        db.commit()
        db.refresh(order)

        return APIResponse(
            status_code="00000",
            message="success",
            response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
            order_id=order.id,
            oid=order.oid,
            buyer_id=order.buyer_id,
            seller_id=order.seller_id,
            driver_id=order.driver_id,
            from_addr=order.from_address,
            to_addr=order.to_address,
            order_status=order.order_status.value,
            total_price=float(order.total_price),
            product=[
                {
                    "product_id": product.product_id,
                    "name": product.name,
                    "type": product.type,
                    "price": float(product.price),
                    "count": product.count
                }
                for product in selled_products
            ]
        )
    elif payload["role"] == "seller" and order.seller_id == payload["id"]:
        if data.status == "success" and order.order_status == OrderStatus.ORDERED:
            order.order_status = OrderStatus.SUCCESS
        elif data.status == "fail" and order.order_status == OrderStatus.ORDERED:
            order.order_status = OrderStatus.FAIL
            selled_products = order.selled_products
            for sp in selled_products:
                product = sp.product
                product.stock += sp.count
                sp.is_refund = True
        elif data.status == "packed" and order.order_status == OrderStatus.SUCCESS:
            order.order_status = OrderStatus.PACKED
        else:
            raise APIException(403, "00004", "forbidden")
        selled_products = order.selled_products
        db.commit()
        db.refresh(order)

        return APIResponse(
            status_code="00000",
            message="success",
            response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
            order_id=order.id,
            oid=order.oid,
            buyer_id=order.buyer_id,
            seller_id=order.seller_id,
            driver_id=order.driver_id,
            from_addr=order.from_address,
            to_addr=order.to_address,
            order_status=order.order_status.value,
            total_price=float(order.total_price),
            product=[
                {
                    "product_id": product.product_id,
                    "name": product.name,
                    "type": product.type,
                    "price": float(product.price),
                    "count": product.count
                }
                for product in selled_products
            ]
        )
    elif payload["role"] == "driver" and order.driver_id == payload["id"]:
        if data.status == "deliver" and order.order_status == OrderStatus.PACKED:
            order.order_status = OrderStatus.DELIVER
        elif data.status == "arrived" and order.order_status == OrderStatus.DELIVER:
            order.order_status = OrderStatus.ARRIVED
        else:
            raise APIException(403, "00004", "forbidden")
        db.commit()
        db.refresh(order)
            
        return APIResponse(
            status_code="00000",
            message="success",
            response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
            order_id=order.id,
            oid=order.oid,
            buyer_id=order.buyer_id,
            seller_id=order.seller_id,
            driver_id=order.driver_id,
            from_addr=order.from_address,
            to_addr=order.to_address,
            order_status=order.order_status.value,
            total_price=float(order.total_price)
        )
    else:
        raise APIException(403, "00004", "forbidden")