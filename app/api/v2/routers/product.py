from fastapi import APIRouter, Request
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.model import Product, SelledProduct
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime, timedelta
from app.core.deps import verify_token, return_payload
from app.schemas.product import ProductCreateRequest, ProductUpdateRequest, ProductTypeCreateRequest
from decimal import Decimal, ROUND_HALF_UP
from snowflake import SnowflakeGenerator
import pytz

router = APIRouter()
gen = SnowflakeGenerator(42)

@router.post("/add", response_model=APIResponse, response_model_exclude_none=True)
def add_product(request: Request, data: ProductCreateRequest, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "seller":
        raise APIException(403, "00004", "forbidden")
    product = db.query(Product).filter(Product.name == data.name, Product.seller_id == payload["id"], Product.is_delete == False).first()
    if product is not None:
        raise APIException(400, "20007", "product existed")
    new_product = Product(
        pid=f"P{next(gen)}",
        name=data.name,
        price=Decimal(data.price).quantize(Decimal("0.00")),
        stock=data.stock,
        status=data.status,
        seller_id=payload["id"],
        desc=data.desc,
        type=data.type,
    )
    if data.product_url is not None:
        new_product.product_url = data.product_url
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return APIResponse(
        status_code="00000",
        message="product created",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        uuid=new_product.id,
        pid=new_product.pid,
        name=new_product.name,
        price=new_product.price,
        stock=new_product.stock,
        status=new_product.status,
        seller_id=new_product.seller_id,
        desc=new_product.desc,
        type=new_product.type,
        product_url=new_product.product_url
    )

@router.post("/add/type/{ProductId}", response_model=APIResponse, response_model_exclude_none=True)
def add_product_type(request: Request, ProductId: str, data: ProductTypeCreateRequest, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "seller":
        raise APIException(403, "00004", "forbidden")
    product = db.query(Product).filter(Product.pid == ProductId, Product.is_delete == False).first()
    if product is None:
        raise APIException(400, "20001", "product not found")
    if product.seller_id != payload["id"]:
        raise APIException(403, "00004", "forbidden")
    same_product = db.query(Product).filter(Product.pid == ProductId, Product.type == data.type, Product.is_delete == False).first()
    if same_product is not None:
        raise APIException(400, "20007", "product existed")
    new_product_type = Product(
        pid=ProductId,
        name=product.name,
        price=Decimal(data.price).quantize(Decimal("0.00")),
        stock=data.stock,
        status=data.status,
        seller_id=payload["id"],
        desc=data.desc,
        type=data.type,
    )
    if data.product_url is not None:
        new_product_type.product_url = data.product_url
    db.add(new_product_type)
    db.commit()
    db.refresh(new_product_type)

    return APIResponse(
        status_code="00000",
        message="product created",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        uuid=new_product_type.id,
        pid=new_product_type.pid,
        name=new_product_type.name,
        price=new_product_type.price,
        stock=new_product_type.stock,
        status=new_product_type.status,
        seller_id=new_product_type.seller_id,
        desc=new_product_type.desc,
        type=new_product_type.type,
        product_url=new_product_type.product_url
    )


@router.put("/{ProductId}", response_model=APIResponse, response_model_exclude_none=True)
def update_product(request: Request, ProductId: str, data: ProductUpdateRequest, db: Session = Depends(get_db)) -> dict:
    # verify_token(request)
    # payload = return_payload(request)
    # if payload["role"] != "seller":
    #     raise APIException(403, "00004", "forbidden")
    product = db.query(Product).filter(Product.pid == ProductId, Product.is_delete == False).first()
    if product is None:
        raise APIException(400, "20001", "product not found")
    # if product.seller_id is not payload["id"]:
    #     raise APIException(403, "00004", "forbidden")
    product.name = data.name
    product.price = Decimal(data.price).quantize(Decimal("0.00"))
    product.stock = data.stock
    product.status = data.status
    product.desc = data.desc
    product.type = data.type
    product.product_url = data.product_url
    db.commit()
    db.refresh(product)

    return APIResponse(
        status_code="00000",
        message="product updated",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
        pid=product.pid,
        name=product.name,
        price=product.price,
        stock=product.stock,
        status=product.status,
        seller_id=product.seller_id,
        desc=product.desc,
        type=product.type,
        product_url=product.product_url
    )


@router.delete("/{ProductId}", response_model=APIResponse, response_model_exclude_none=True)
def delete_product(request: Request, ProductId: str, db: Session = Depends(get_db)) -> dict:
    # verify_token(request)
    # payload = return_payload(request)
    # if payload["role"] != "seller":
    #     raise APIException(403, "00004", "forbidden")
    product = db.query(Product).filter(Product.pid == ProductId, Product.is_delete == False).first()
    if product is None:
        raise APIException(400, "20001", "product not found")
    # if product.seller_id is not payload["id"]:
    #     raise APIException(403, "00004", "forbidden")
    product.is_delete = True
    db.commit()
    db.refresh(product)

    return APIResponse(
        status_code="00000",
        message="product deleted",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
    )


@router.get("/{ProductId}", response_model=APIResponse, response_model_exclude_none=True)
def get_product(ProductId: int, db: Session = Depends(get_db)) -> dict:
    # verify_token(request)
    product = db.query(Product).filter(Product.pid == ProductId, Product.is_delete == False).first()
    if product is None:
        raise APIException(400, "20001", "product not found")

    return APIResponse(
        status_code="00000",
        message="get single product",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
        pid=product.pid,
        name=product.name,
        price=product.price,
        stock=product.stock,
        status=product.status,
        seller_id=product.seller_id,
        desc=product.desc,
        type=product.type,
        product_url=product.product_url
    )


@router.get("/me", response_model=APIResponse, response_model_exclude_none=True)
def get_my_products(db: Session = Depends(get_db)) -> dict:

    return APIResponse(
        status_code="00000",
        message="get my products",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
    )