from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.schemas.buyer import BuyerUpdateRequest
from app.db.session import get_db
from app.models.model import Buyer
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token

router = APIRouter()
@router.get("/me")
def get_buyer_me(buyer_id: str, db: Session = Depends(get_db)):
    buyer = db.query(Buyer).filter(Buyer.id == buyer_id, Buyer.is_delete == False).first()
    if not buyer:
        raise APIException(404, "10001", "buyer not found")

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        user_id=buyer.id,
        email=buyer.email,
        phone=buyer.phone,
        name=buyer.name,
        address=buyer.address,
    )


@router.put("/me")
def update_buyer_me(buyer_id: str, data: BuyerUpdateRequest, db: Session = Depends(get_db)):
    buyer = db.query(Buyer).filter(Buyer.id == buyer_id, Buyer.is_delete == False).first()
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
        desc="success",
        response_datetime=datetime.utcnow(),
        email=buyer.email,
        phone=buyer.phone,
        name=buyer.name,
        address=buyer.address,
    )


@router.delete("/{BuyerId}")
def delete_buyer(BuyerId: str, db: Session = Depends(get_db)):
    buyer = db.query(Buyer).filter(Buyer.id == BuyerId, Buyer.is_delete == False).first()
    if not buyer:
        raise APIException(404, "10001", "not found")

    buyer.is_delete = True
    db.commit()

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )
