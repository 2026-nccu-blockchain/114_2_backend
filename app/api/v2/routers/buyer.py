from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.schemas.buyer import BuyerUpdateRequest
from app.db.session import get_db
from app.models.model import Buyer
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token, return_payload
import pytz

router = APIRouter()


@router.get("/me", response_model=APIResponse, response_model_exclude_none=True)
def get_buyer_me(
    request: Request,
    db: Session = Depends(get_db)
):
    verify_token(request)
    payload = return_payload(request)

    if payload["role"] != "buyer":
        raise APIException(403, "10008", "permission denied")

    token_id = payload["id"]

    buyer = db.query(Buyer).filter(
        Buyer.id == token_id,
        Buyer.is_delete == False
    ).first()

    if not buyer:
        raise APIException(404, "10001", "buyer not found")

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
        user_id=buyer.id,
        email=buyer.email,
        phone=buyer.phone,
        name=buyer.name,
        address=buyer.address,
    )


@router.put("/me", response_model=APIResponse, response_model_exclude_none=True)
def update_buyer_me(
    request: Request,
    data: BuyerUpdateRequest,
    db: Session = Depends(get_db)
):
    verify_token(request)
    payload = return_payload(request)

    if payload["role"] != "buyer":
        raise APIException(403, "10008", "permission denied")

    token_id = payload["id"]

    buyer = db.query(Buyer).filter(
        Buyer.id == token_id,
        Buyer.is_delete == False
    ).first()

    if not buyer:
        raise APIException(404, "10001", "buyer not found")

    buyer.email = data.email
    buyer.phone = data.phone
    buyer.name = data.name
    buyer.address = data.address

    db.commit()
    db.refresh(buyer)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
        user_id=buyer.id,
        email=buyer.email,
        phone=buyer.phone,
        name=buyer.name,
        address=buyer.address,
    )


@router.delete("/me", response_model=APIResponse, response_model_exclude_none=True)
def delete_buyer_me(
    request: Request,
    db: Session = Depends(get_db)
):
    verify_token(request)
    payload = return_payload(request)

    if payload["role"] != "buyer":
        raise APIException(403, "10008", "permission denied")

    token_id = payload["id"]

    buyer = db.query(Buyer).filter(
        Buyer.id == token_id,
        Buyer.is_delete == False
    ).first()

    if not buyer:
        raise APIException(404, "10001", "buyer not found")

    buyer.is_delete = True
    db.commit()

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
    )