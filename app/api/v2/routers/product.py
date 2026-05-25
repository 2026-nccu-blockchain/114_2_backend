from fastapi import APIRouter, Request, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.model import Product
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token, return_payload
from app.schemas.product import ProductCreateRequest, ProductUpdateRequest, ProductTypeCreateRequest, ProductTypeUpdateRequest
from decimal import Decimal
from snowflake import SnowflakeGenerator
import pytz


router = APIRouter()
gen = SnowflakeGenerator(42)

@router.post("/product", response_model=APIResponse, response_model_exclude_none=True)
def add_product(request: Request, data: ProductCreateRequest, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "seller":
        raise APIException(403, "00004", "forbidden")
    same_product = db.query(Product).filter(Product.name == data.name, Product.seller_id == payload["id"], Product.is_delete == False).first()
    if same_product is not None:
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
        message="success",
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


@router.post("/type/{ProductId}", response_model=APIResponse, response_model_exclude_none=True)
def add_product_type(request: Request, ProductId: str, data: ProductTypeCreateRequest, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "seller":
        raise APIException(403, "00004", "forbidden")
    product = db.query(Product).filter(Product.pid == ProductId, Product.is_delete == False).first()
    if product is None:
        raise APIException(404, "20001", "product not found")
    if product.seller_id != payload["id"]:
        raise APIException(403, "00004", "forbidden")
    same_product = db.query(Product).filter(Product.pid == ProductId, Product.type == data.type, Product.seller_id == payload["id"], Product.is_delete == False).first()
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
        message="success",
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


@router.put("/product/{ProductId}", response_model=APIResponse, response_model_exclude_none=True)
def update_product(request: Request, ProductId: str, data: ProductUpdateRequest, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "seller":
        raise APIException(403, "00004", "forbidden")
    product = db.query(Product).filter(Product.pid == ProductId, Product.is_delete == False).first()
    if product is None:
        raise APIException(404, "20001", "product not found")
    if product.seller_id != payload["id"]:
        raise APIException(403, "00004", "forbidden")
    same_product = db.query(Product).filter(Product.name == data.name, Product.seller_id == payload["id"], Product.is_delete == False).first()
    if same_product is not None:
        raise APIException(400, "20007", "product existed")
    products = db.query(Product).filter(Product.pid == ProductId, Product.is_delete == False).all()
    for p in products:
        p.name = data.name
    db.commit()

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        pid=product.pid,
        name=data.name
    )


@router.put("/type/{uuid}", response_model=APIResponse, response_model_exclude_none=True)
def update_product_type(request: Request, uuid: str, data: ProductTypeUpdateRequest, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "seller":
        raise APIException(403, "00004", "forbidden")
    product = db.query(Product).filter(Product.id == uuid, Product.is_delete == False).first()
    if product is None:
        raise APIException(404, "20001", "product not found")
    if product.seller_id != payload["id"]:
        raise APIException(403, "00004", "forbidden")
    same_product = db.query(Product).filter(Product.pid == product.pid, Product.type == data.type, Product.seller_id == payload["id"], Product.is_delete == False).first()
    if same_product is not None:
        raise APIException(400, "20007", "product existed")
    product.price = data.price
    product.stock = data.stock
    product.status = data.status
    product.desc = data.desc
    product.type = data.type
    product.product_url = data.product_url
    db.commit()
    db.refresh(product)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        uuid=product.id,
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


@router.delete("/product/{ProductId}", response_model=APIResponse, response_model_exclude_none=True)
def delete_product(request: Request, ProductId: str, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "seller":
        raise APIException(403, "00004", "forbidden")
    products = db.query(Product).filter(Product.pid == ProductId, Product.is_delete == False).all()
    if not products:
        raise APIException(404, "20001", "product not found")
    if products[0].seller_id != payload["id"]:
        raise APIException(403, "00004", "forbidden")
    for p in products:
        p.is_delete = True
    db.commit()

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
    )


@router.delete("/type/{uuid}", response_model=APIResponse, response_model_exclude_none=True)
def delete_product_type(request: Request, uuid: str, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] != "seller":
        raise APIException(403, "00004", "forbidden")
    product = db.query(Product).filter(Product.id == uuid, Product.is_delete == False).first()
    if product is None:
        raise APIException(404, "20001", "product not found")
    if product.seller_id != payload["id"]:
        raise APIException(403, "00004", "forbidden")
    product.is_delete = True
    db.commit()
    db.refresh(product)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
    )


@router.get("/product/{ProductId}", response_model=APIResponse, response_model_exclude_none=True)
def get_product(request: Request, ProductId: str, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    stmt = select(Product.id, Product.pid, Product.name, Product.price, Product.stock, Product.status, Product.seller_id, Product.desc, Product.type, Product.product_url
                  ).where(Product.pid == ProductId, Product.is_delete == False)
    products = db.execute(stmt).mappings().all()
    if not products:
        raise APIException(404, "20001", "product not found")

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        product=products
    )


@router.get("", response_model=APIResponse, response_model_exclude_none=True)
def get_my_products(request: Request, db: Session = Depends(get_db)) -> dict:
    verify_token(request)
    payload = return_payload(request)
    if payload["role"] == "buyer":
        stmt = select(Product.id, Product.pid, Product.name, Product.price, Product.stock, Product.status, Product.seller_id, Product.desc, Product.type, Product.product_url
                  ).where(Product.is_delete == False).group_by(Product.pid)
        products = db.execute(stmt).mappings().all()
        if not products:
            raise APIException(404, "20001", "product not found")
        return APIResponse(
            status_code="00000",
            message="success",
            response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
            product=products
        )
    elif payload["role"] == "seller":
        stmt = select(Product.id, Product.pid, Product.name, Product.price, Product.stock, Product.status, Product.seller_id, Product.desc, Product.type, Product.product_url
                  ).where(Product.seller_id == payload["id"], Product.is_delete == False).group_by(Product.pid)
        products = db.execute(stmt).mappings().all()
        if not products:
            raise APIException(404, "20001", "product not found")
        return APIResponse(
            status_code="00000",
            message="success",
            response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
            product=products
        )
    else:
        raise APIException(403, "00004", "forbidden")
