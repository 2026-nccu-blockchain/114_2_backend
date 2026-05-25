from fastapi import APIRouter
from fastapi import Depends
from typing import Optional
from sqlalchemy.orm import Session
from app.schemas.buyer import BuyerUpdateRequest
from app.db.session import get_db
from app.models.model import Buyer
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import return_payload
import pytz

router = APIRouter()
@router.get("/me")
def get_buyer_me(
    buyer_id: Optional[str] = None,
    db: Session = Depends(get_db),
    payload: dict = Depends(return_payload)
):
    token_id = payload.get("id")
    if payload.get("role") != "buyer" or not token_id:
        raise APIException(403, "10008", "permission denied")
    if buyer_id is not None and buyer_id != token_id:
        raise APIException(403, "10008", "permission denied")
    buyer = db.query(Buyer).filter(Buyer.id == token_id, Buyer.is_delete == False).first()
    if not buyer:
        raise APIException(404, "10001", "buyer not found")

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        user_id=buyer.id,
        email=buyer.email,
        phone=buyer.phone,
        name=buyer.name,
        address=buyer.address,
    )


@router.put("/me")
def update_buyer_me(
    data: BuyerUpdateRequest,
    buyer_id: Optional[str] = None,
    db: Session = Depends(get_db),
    payload: dict = Depends(return_payload)
):
    token_id = payload.get("id")
    if payload.get("role") != "buyer" or not token_id:
        raise APIException(403, "10008", "permission denied")
    if buyer_id is not None and buyer_id != token_id:
        raise APIException(403, "10008", "permission denied")
    buyer = db.query(Buyer).filter(Buyer.id == token_id, Buyer.is_delete == False).first()
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
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        email=buyer.email,
        phone=buyer.phone,
        name=buyer.name,
        address=buyer.address,
    )


@router.delete("/{BuyerId}")
def delete_buyer(
    BuyerId: str,
    db: Session = Depends(get_db),
    payload: dict = Depends(return_payload)
):
    token_id = payload.get("id")
    if payload.get("role") != "buyer" or not token_id:
        raise APIException(403, "10008", "permission denied")
    if BuyerId != token_id:
        raise APIException(403, "10008", "permission denied")
    buyer = db.query(Buyer).filter(Buyer.id == token_id, Buyer.is_delete == False).first()
    if not buyer:
        raise APIException(404, "10001", "not found")

    buyer.is_delete = True
    db.commit()

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
    )
