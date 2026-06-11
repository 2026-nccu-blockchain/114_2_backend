from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.schemas.admin import AdminUpdateRequest
from app.db.session import get_db
from app.models.model import Admin, Buyer, Seller, Driver
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token, return_payload
import pytz

router = APIRouter()


def verify_admin(request: Request) -> dict:
    verify_token(request)
    payload = return_payload(request)

    if payload["role"] != "admin":
        raise APIException(403, "10008", "permission denied")

    return payload


@router.get("/me", response_model=APIResponse, response_model_exclude_none=True)
def get_admin_me(
    request: Request,
    db: Session = Depends(get_db)
):
    payload = verify_admin(request)
    token_id = payload["id"]

    admin = db.query(Admin).filter(
        Admin.id == token_id,
        Admin.is_delete == False
    ).first()

    if not admin:
        raise APIException(404, "10001", "admin not found")

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
        user_id=admin.id,
        email=admin.email,
        name=admin.name,
    )


@router.put("/me", response_model=APIResponse, response_model_exclude_none=True)
def update_admin_me(
    request: Request,
    data: AdminUpdateRequest,
    db: Session = Depends(get_db)
):
    payload = verify_admin(request)
    token_id = payload["id"]

    admin = db.query(Admin).filter(
        Admin.id == token_id,
        Admin.is_delete == False
    ).first()

    if not admin:
        raise APIException(404, "10001", "admin not found")

    admin.email = data.email
    admin.name = data.name

    db.commit()
    db.refresh(admin)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
        user_id=admin.id,
        email=admin.email,
        name=admin.name,
    )


@router.get("/buyer", response_model=APIResponse, response_model_exclude_none=True)
def get_all_buyers(
    request: Request,
    db: Session = Depends(get_db)
):
    verify_admin(request)

    buyers = db.query(Buyer).filter(Buyer.is_delete == False).all()

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
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


@router.get("/seller", response_model=APIResponse, response_model_exclude_none=True)
def get_all_sellers(
    request: Request,
    db: Session = Depends(get_db)
):
    verify_admin(request)

    sellers = db.query(Seller).filter(Seller.is_delete == False).all()

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
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


@router.get("/driver", response_model=APIResponse, response_model_exclude_none=True)
def get_all_drivers(
    request: Request,
    db: Session = Depends(get_db)
):
    verify_admin(request)

    drivers = db.query(Driver).filter(Driver.is_delete == False).all()

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
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