from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
# from app.schemas.admin import
from app.schemas.admin import AdminUpdateRequest
from app.db.session import get_db
from app.models.model import Admin, Buyer, Seller, Driver
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token

router = APIRouter()

@router.get("/me")
def get_admin_me(admin_id: str, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == admin_id, Admin.is_delete == False).first()
    if not admin:
        raise APIException(404, "10001", "admin not found")

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        user_id=admin.id,
        email=admin.email,
        name=admin.name,
    )


@router.put("/me")
def update_admin_me(admin_id: str, data: AdminUpdateRequest, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == admin_id, Admin.is_delete == False).first()
    if not admin:
        raise APIException(404, "10001", "admin not found")

    admin.email = data.email
    admin.name = data.name

    db.commit()
    db.refresh(admin)

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        email=admin.email,
        name=admin.name,
    )


@router.get("/buyer")
def get_all_buyers(db: Session = Depends(get_db)):
    buyers = db.query(Buyer).filter(Buyer.is_delete == False).all()
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        buyer=[
            {
                "uuid": buyer.id,
                "email": buyer.email,
                "phone": buyer.phone,
                "name": buyer.name,
                "address": buyer.address,
            }
            for buyer in buyers
        ],
    )


@router.get("/seller")
def get_all_sellers(db: Session = Depends(get_db)):
    sellers = db.query(Seller).filter(Seller.is_delete == False).all()
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        seller=[
            {
                "uuid": seller.id,
                "email": seller.email,
                "phone": seller.phone,
                "name": seller.name,
                "company_address": seller.company_address,
                "company_phone": seller.company_phone,
                "company_name": seller.company_name,
            }
            for seller in sellers
        ],
    )


@router.get("/driver")
def get_all_drivers(db: Session = Depends(get_db)):
    drivers = db.query(Driver).filter(Driver.is_delete == False).all()
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        driver=[
            {
                "uuid": driver.id,
                "email": driver.email,
                "phone": driver.phone,
                "name": driver.name,
            }
            for driver in drivers
        ],
    )
