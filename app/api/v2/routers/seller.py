from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.schemas.seller import SellerUpdateRequest
from app.db.session import get_db
from app.models.model import Seller
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from app.core.deps import verify_token, return_payload
import pytz

router = APIRouter()


@router.get("/me", response_model=APIResponse, response_model_exclude_none=True)
def get_seller_me(
    request: Request,
    db: Session = Depends(get_db)
):
    verify_token(request)
    payload = return_payload(request)

    if payload["role"] != "seller":
        raise APIException(403, "10008", "permission denied")

    token_id = payload["id"]

    seller = db.query(Seller).filter(
        Seller.id == token_id,
        Seller.is_delete == False
    ).first()

    if not seller:
        raise APIException(404, "10001", "seller not found")

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
        user_id=seller.id,
        email=seller.email,
        phone=seller.phone,
        name=seller.name,
        avatar_url=seller.avatar_url,
        company_address=seller.company_address,
        company_phone=seller.company_phone,
        company_name=seller.company_name,
    )


@router.put("/me", response_model=APIResponse, response_model_exclude_none=True)
def update_seller_me(
    request: Request,
    data: SellerUpdateRequest,
    db: Session = Depends(get_db)
):
    verify_token(request)
    payload = return_payload(request)

    if payload["role"] != "seller":
        raise APIException(403, "10008", "permission denied")

    token_id = payload["id"]

    seller = db.query(Seller).filter(
        Seller.id == token_id,
        Seller.is_delete == False
    ).first()

    if not seller:
        raise APIException(404, "10001", "seller not found")

    seller.email = data.email
    seller.phone = data.phone
    seller.name = data.name
    seller.avatar_url = data.avatar_url,
    seller.company_address = data.company_address
    seller.company_phone = data.company_phone
    seller.company_name = data.company_name

    db.commit()
    db.refresh(seller)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
        user_id=seller.id,
        email=seller.email,
        phone=seller.phone,
        name=seller.name,
        avatar_url=seller.avatar_url,
        company_address=seller.company_address,
        company_phone=seller.company_phone,
        company_name=seller.company_name,
    )


@router.delete("/me", response_model=APIResponse, response_model_exclude_none=True)
def delete_seller_me(
    request: Request,
    db: Session = Depends(get_db)
):
    verify_token(request)
    payload = return_payload(request)

    if payload["role"] != "seller":
        raise APIException(403, "10008", "permission denied")

    token_id = payload["id"]

    seller = db.query(Seller).filter(
        Seller.id == token_id,
        Seller.is_delete == False
    ).first()

    if not seller:
        raise APIException(404, "10001", "seller not found")

    seller.is_delete = True
    db.commit()

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
    )