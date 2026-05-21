from fastapi import APIRouter, Request
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.model import Product, SelledProduct
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime, timedelta
from app.core.deps import verify_token, return_payload
from app.schemas.product import ProductCreateRequest, ProductUpdateRequest
from decimal import Decimal, ROUND_HALF_UP
import time

router = APIRouter()

@router.post("/add", response_model=APIResponse, response_model_exclude_none=True)
def add_product(request: Request, data: ProductCreateRequest, db: Session = Depends(get_db)) -> dict:
    # verify_token(request)
    # payload = return_payload(request)
    # if payload["role"] != "seller":
    #     raise APIException(403, "00004", "forbidden")
    new_product = Product(
        pid=f"P{int(time.time())}",
        name=data.name,
        price=Decimal(data.price).quantize(Decimal("0.00")),
        stock=data.stock,
        status=data.status,
        # seller_id=payload["id"],
        desc=data.desc,
        type=data.type
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return APIResponse(
        status_code="00000",
        message="product created",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
    )


@router.put("/{ProductId}", response_model=APIResponse, response_model_exclude_none=True)
def update_product(request: Request, ProductId: str, data: ProductUpdateRequest, db: Session = Depends(get_db)) -> dict:
    # verify_token(request)
    # if return_payload(request)["role"] != "seller":
    #     raise APIException(403, "00004", "forbidden")
    product = db.query(Product).filter(Product.pid == ProductId).first()
    if product is None:
        raise APIException(400, "20001", "product not found")
    product.name = data.name
    product.price = Decimal(data.price).quantize(Decimal("0.00"))
    product.stock = data.stock
    product.status = data.status
    product.desc = data.desc
    product.type = data.type
    db.commit()
    db.refresh(product)

    return APIResponse(
        status_code="00000",
        message="product updated",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
    )


@router.delete("/{ProductId}", response_model=APIResponse, response_model_exclude_none=True)
def delete_product(ProductId: int, db: Session = Depends(get_db)) -> dict:

    return APIResponse(
        status_code="00000",
        message="product deleted",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
    )


@router.get("/{ProductId}", response_model=APIResponse, response_model_exclude_none=True)
def get_product(ProductId: int, db: Session = Depends(get_db)) -> dict:

    return APIResponse(
        status_code="00000",
        message="get single product",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
    )


@router.get("/me", response_model=APIResponse, response_model_exclude_none=True)
def get_my_products(db: Session = Depends(get_db)) -> dict:

    return APIResponse(
        status_code="00000",
        message="get my products",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
    )