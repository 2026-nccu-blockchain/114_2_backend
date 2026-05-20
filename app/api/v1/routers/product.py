from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.schemas.common import APIResponse

router = APIRouter()


@router.post("/add")
def add_product(db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="product created",
        response_datetime=datetime.utcnow(),
    )


@router.put("/{ProductId}")
def update_product(ProductId: int, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="product updated",
        response_datetime=datetime.utcnow(),
    )


@router.delete("/{ProductId}")
def delete_product(ProductId: int, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="product deleted",
        response_datetime=datetime.utcnow(),
    )


@router.get("/{ProductId}")
def get_product(ProductId: int, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="get single product",
        response_datetime=datetime.utcnow(),
    )


@router.get("/me")
def get_my_products(db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="get my products",
        response_datetime=datetime.utcnow(),
    )