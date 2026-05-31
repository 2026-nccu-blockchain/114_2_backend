from fastapi import APIRouter, Request, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.model import Product, Cart
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token, return_payload
from app.schemas.cart import CartCreateRequest, CartUpdateRequest
from decimal import Decimal
from snowflake import SnowflakeGenerator
import pytz

router = APIRouter()
gen = SnowflakeGenerator(42)

@router.post("/cart", response_model=APIResponse, response_model_exclude_none=True)
def add_cart(request: Request, data: CartCreateRequest, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "buyer":
        raise APIException(403, "00004", "forbidden")
    if data.count <= 0:
        raise APIException(400, "20009", "number invalid")
    product = db.query(Product).filter(Product.id == data.product_id, Product.status == True, Product.is_delete == False).first()
    if product is None:
        raise APIException(404, "20001", "product not found")
    same_product = db.query(Cart).filter(Cart.product_id == data.product_id, Cart.is_delete == False).first()
    if same_product is not None:
        raise APIException(400, "20007", "product existed")
    if product.status == False:
        raise APIException(400, "20003", "product can't buy")
    if data.count > product.stock:
        raise APIException(400, "20002", "product out of stock")
    product.stock -= data.count
    new_cart = Cart(
        product_id=data.product_id,
        name=product.name,
        type=product.type,
        price=Decimal(product.price).quantize(Decimal("0.00")),
        count=data.count,
        buyer_id=payload["id"],
        seller_id=product.seller_id
    )
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        cart_id=new_cart.id,
        product_id=new_cart.product_id,
        name=product.name,
        type=product.type,
        price=new_cart.price,
        count=new_cart.count,
        seller_id=product.seller_id
    )


@router.put("/cart/{CartId}", response_model=APIResponse, response_model_exclude_none=True)
def update_cart(request: Request, CartId: str, data: CartUpdateRequest, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "buyer":
        raise APIException(403, "00004", "forbidden")
    if data.count <= 0:
        raise APIException(400, "20009", "number invalid")
    cart_product = db.query(Cart).filter(Cart.id == CartId, Cart.buyer_id == payload["id"], Cart.is_delete == False).first()
    if cart_product is None:
        raise APIException(404, "20001", "product not found")
    product = cart_product.products
    if product.stock + cart_product.count - data.count < 0:
        raise APIException(400, "20002", "product out of stock")
    product.stock = product.stock + cart_product.count - data.count
    cart_product.count = data.count
    cart_product.price = Decimal(product.price).quantize(Decimal("0.00"))
    db.commit()
    db.refresh(cart_product)
    db.refresh(product)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        cart_id=cart_product.id,
        product_id=cart_product.product_id,
        name=product.name,
        type=product.type,
        price=cart_product.price,
        count=cart_product.count,
        seller_id=product.seller_id
    )


@router.delete("/cart/{CartId}", response_model=APIResponse, response_model_exclude_none=True)
def update_cart(request: Request, CartId: str, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "buyer":
        raise APIException(403, "00004", "forbidden")
    cart_product = db.query(Cart).filter(Cart.id == CartId, Cart.buyer_id == payload["id"], Cart.is_delete == False).first()
    if cart_product is None:
        raise APIException(404, "20001", "product not found")
    product = cart_product.products
    product.stock += cart_product.count
    cart_product.is_delete = True
    db.commit()

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
    )


@router.get("/me", response_model=APIResponse, response_model_exclude_none=True)
def update_cart(request: Request, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "buyer":
        raise APIException(403, "00004", "forbidden")
    cart_products = db.query(Cart).filter(Cart.buyer_id == payload["id"], Cart.is_delete == False).all()
    if not cart_products:
        raise APIException(404, "20001", "product not found")
    
    return APIResponse(
            status_code="00000",
            message="success",
            response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
            cart=[
                {
                    "cart_id": product.id,
                    "product_id": product.product_id,
                    "name": product.name,
                    "type": product.type,
                    "price": float(product.price),
                    "count": product.count,
                    "seller_id": product.seller_id
                }
                for product in cart_products
            ]
        )