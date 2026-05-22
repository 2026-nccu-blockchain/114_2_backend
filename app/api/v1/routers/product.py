from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.model import Product
from app.db.session import get_db
from app.schemas.common import APIResponse
from app.schemas.product import ProductCreateRequest, ProductUpdateRequest
from app.core.exceptions import APIException
import uuid
router = APIRouter()


@router.post("/add")
def add_product(
    data: ProductCreateRequest,
    db: Session = Depends(get_db)
):

    new_product = Product(
        p_id=str(uuid.uuid4()),
        name=data.name,
        price=data.price,
        stock=data.stock,
        status=data.status,
        seller_id=data.seller_id,
        desc=data.desc,
        type=data.type
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow()
    )

@router.put("/{ProductId}")
def update_product(
    ProductId: str,
    data: ProductUpdateRequest,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(Product.id == ProductId).first()

    if not product:
        raise APIException(404, "40401", "Product not found")

    product.name = data.name
    product.price = data.price
    product.stock = data.stock
    product.status = data.status
    product.desc = data.desc
    product.type = data.type

    db.commit()
    db.refresh(product)

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        product_id=product.id,
        product_name=product.name
    )


@router.delete("/{ProductId}")
def delete_product(
    ProductId: str,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(Product.id == ProductId).first()

    if not product:
        raise APIException(404, "40401", "Product not found")

    db.delete(product)
    db.commit()

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow()
    )


@router.get("/{ProductId}")
def get_product(ProductId: str, db: Session = Depends(get_db)):

    product = db.query(Product).filter(Product.id == ProductId).first()

    if not product:
        raise APIException(404, "40401", "Product not found")

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        product_id=product.id,
        product_name=product.name,
    )


@router.get("/me")
def get_my_products(db: Session = Depends(get_db)) -> dict:

    return APIResponse(
        status_code="00000",
        desc="get my products",
        response_datetime=datetime.utcnow(),
    )