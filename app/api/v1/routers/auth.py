from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.schemas.common import APIResponse
from app.schemas.auth import (
    LoginRequest,
    AdminRegisterRequest,
    BuyerRegisterRequest,
    SellerRegisterRequest,
    DriverRegisterRequest,
)

router = APIRouter()


@router.post("/admin/login")
def admin_login(data: LoginRequest, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )


@router.post("/admin/register")
def admin_register(data: AdminRegisterRequest, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )


@router.post("/buyer/login")
def buyer_login(data: LoginRequest, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )


@router.post("/buyer/register")
def buyer_register(data: BuyerRegisterRequest, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )


@router.post("/seller/login")
def seller_login(data: LoginRequest, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )


@router.post("/seller/register")
def seller_register(data: SellerRegisterRequest, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )


@router.post("/driver/login")
def driver_login(data: LoginRequest, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )


@router.post("/driver/register")
def driver_register(data: DriverRegisterRequest, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )