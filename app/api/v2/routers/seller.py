from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.session import get_db
from app.models.model import Seller
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from app.core.deps import verify_token

router = APIRouter()


@router.get("/me")
def get_seller_me(db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )


@router.put("/me")
def update_seller_me(db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )


@router.delete("/{SellerId}")
def delete_seller(SellerId: int, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )