from fastapi import APIRouter, Depends
from typing import Optional
from sqlalchemy.orm import Session
from datetime import datetime
from app.schemas.seller import SellerUpdateRequest
from app.db.session import get_db
from app.models.model import Seller
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from app.core.deps import return_payload

router = APIRouter()

@router.get("/me")
def get_seller_me(
    seller_id: Optional[str] = None,
    db: Session = Depends(get_db),
    payload: dict = Depends(return_payload)
):
    token_id = payload.get("id")
    if payload.get("role") != "seller" or not token_id:
        raise APIException(403, "10008", "permission denied")
    if seller_id is not None and seller_id != token_id:
        raise APIException(403, "10008", "permission denied")
    seller = db.query(Seller).filter(Seller.id == token_id, Seller.is_delete == False).first()
    if not seller:
        raise APIException(404, "10001", "seller not found")

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        user_id=seller.id,
        email=seller.email,
        phone=seller.phone,
        name=seller.name,
        company_address=seller.company_address,
        company_phone=seller.company_phone,
        company_name=seller.company_name,
    )


@router.put("/me")
def update_seller_me(
    data: SellerUpdateRequest,
    seller_id: Optional[str] = None,
    db: Session = Depends(get_db),
    payload: dict = Depends(return_payload)
):
    token_id = payload.get("id")
    if payload.get("role") != "seller" or not token_id:
        raise APIException(403, "10008", "permission denied")
    if seller_id is not None and seller_id != token_id:
        raise APIException(403, "10008", "permission denied")
    seller = db.query(Seller).filter(Seller.id == token_id, Seller.is_delete == False).first()
    if not seller:
        raise APIException(404, "10001", "seller not found")

    seller.email = data.email
    seller.phone = data.phone
    seller.name = data.name
    seller.company_address = data.company_address
    seller.company_phone = data.company_phone
    seller.company_name = data.company_name

    db.commit()
    db.refresh(seller)

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        email=seller.email,
        phone=seller.phone,
        name=seller.name,
        company_address=seller.company_address,
        company_phone=seller.company_phone,
        company_name=seller.company_name,
    )


@router.delete("/{SellerId}")
def delete_seller(
    SellerId: str,
    db: Session = Depends(get_db),
    payload: dict = Depends(return_payload)
):
    token_id = payload.get("id")
    if payload.get("role") != "seller" or not token_id:
        raise APIException(403, "10008", "permission denied")
    if SellerId != token_id:
        raise APIException(403, "10008", "permission denied")
    seller = db.query(Seller).filter(Seller.id == token_id, Seller.is_delete == False).first()
    if not seller:
        raise APIException(404, "10001", "not found")

    seller.is_delete = True
    db.commit()

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )
