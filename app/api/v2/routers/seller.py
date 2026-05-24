from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.schemas.seller import SellerUpdateRequest
from app.db.session import get_db
from app.models.model import Seller
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from app.core.deps import verify_token

router = APIRouter()

@router.get("/me")
def get_seller_me(seller_id: str, db: Session = Depends(get_db)):
    seller = db.query(Seller).filter(Seller.id == seller_id, Seller.is_delete == False).first()
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
def update_seller_me(seller_id: str, data: SellerUpdateRequest, db: Session = Depends(get_db)):
    seller = db.query(Seller).filter(Seller.id == seller_id, Seller.is_delete == False).first()
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
        desc="seller profile updated successfully",
        response_datetime=datetime.utcnow(),
        email=seller.email,
        phone=seller.phone,
        name=seller.name,
        company_address=seller.company_address,
        company_phone=seller.company_phone,
        company_name=seller.company_name,
    )


@router.delete("/{SellerId}")
def delete_seller(SellerId: str, db: Session = Depends(get_db)):
    seller = db.query(Seller).filter(Seller.id == SellerId, Seller.is_delete == False).first()
    if not seller:
        raise APIException(404, "10001", "not found")

    seller.is_delete = True
    db.commit()

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )