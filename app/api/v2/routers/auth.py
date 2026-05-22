from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.model import Admin, Buyer, Seller, Driver
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime, timedelta
from app.core.jwt import create_access_token
from app.schemas.auth import (
    LoginRequest,
    AdminRegisterRequest,
    BuyerRegisterRequest,
    SellerRegisterRequest,
    DriverRegisterRequest,
)

router = APIRouter()

@router.post("/admin/login", response_model=APIResponse, response_model_exclude_none=True)
def admin_login(data: LoginRequest, db: Session = Depends(get_db)) -> dict:
    if not Admin.verify_email(data.email):
        raise APIException(400, "10007", "incorrect email format")
    user = db.query(Admin).filter(Admin.email == data.email).first()
    if user is None:
        raise APIException(400, "10001", "user not found")
    if not user.verify_password(data.password):
        raise APIException(400, "10002", "invalid password")
    payload = {"id": f"{user.id}", "role": "admin"}
    token = create_access_token(payload)
    is_first_login = False
    if user.is_first_login == True:
        user.is_first_login = False
        db.commit()
        db.refresh(user)
        is_first_login = True
    
    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
        token=token,
        is_first_login=is_first_login
    )


@router.post("/admin/register", response_model=APIResponse, response_model_exclude_none=True)
def admin_register(data: AdminRegisterRequest, db: Session = Depends(get_db)) -> dict:
    if not Admin.verify_email(data.email):
        raise APIException(400, "10007", "incorrect email format")
    if db.query(Admin).filter(Admin.email == data.email).first() is not None:
        raise APIException(400, "10006", "register duplicate")
    new_admin = Admin(
        email=data.email,
        hash_password=" ", #不能是null，下面才會設密碼
        name=data.name
    )
    new_admin.set_password(data.password)
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
    )


@router.post("/buyer/login", response_model=APIResponse, response_model_exclude_none=True)
def buyer_login(data: LoginRequest, db: Session = Depends(get_db)) -> dict:
    if not Buyer.verify_email(data.email):
        raise APIException(400, "10007", "incorrect email format")
    user = db.query(Buyer).filter(Buyer.email == data.email, Buyer.is_delete == False).first()
    if user is None:
        raise APIException(400, "10001", "user not found")
    if not user.verify_password(data.password):
        raise APIException(400, "10002", "invalid password")
    payload = {"user": f"{user.id}", "role": "buyer"}
    token = create_access_token(payload)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
        token=token,
    )


@router.post("/buyer/register", response_model=APIResponse, response_model_exclude_none=True)
def buyer_register(data: BuyerRegisterRequest, db: Session = Depends(get_db)) -> dict:
    if not Buyer.verify_email(data.email):
        raise APIException(400, "10007", "incorrect email format")
    if not Buyer.verify_phone(data.phone):
        raise APIException(400, "10009", "incorrect phone format")
    if db.query(Buyer).filter(Buyer.email == data.email, Buyer.is_delete == False).first() is not None:
        raise APIException(400, "10006", "register duplicate, email has been uesd")
    if db.query(Buyer).filter(Buyer.phone == data.phone, Buyer.is_delete == False).first() is not None:
        raise APIException(400, "10006", "register duplicate, phone has been uesd")
    new_buyer = Buyer(
        email=data.email,
        hash_password=" ", #不能是null，下面才會設密碼
        name=data.name,
        phone=data.phone,
        address=data.address
    )
    new_buyer.set_password(data.password)
    db.add(new_buyer)
    db.commit()
    db.refresh(new_buyer)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
    )


@router.post("/seller/login", response_model=APIResponse, response_model_exclude_none=True)
def seller_login(data: LoginRequest, db: Session = Depends(get_db)) -> dict:
    if not Seller.verify_email(data.email):
        raise APIException(400, "10007", "incorrect email format")
    user = db.query(Seller).filter(Seller.email == data.email, Seller.is_delete == False).first()
    if user is None:
        raise APIException(400, "10001", "user not found")
    if not user.verify_password(data.password):
        raise APIException(400, "10002", "invalid password")
    payload = {"id": f"{user.id}", "role": "seller"}
    token = create_access_token(payload)
    is_first_login = False
    if user.is_first_login == True:
        user.is_first_login = False
        db.commit()
        db.refresh(user)
        is_first_login = True

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
        token=token,
        is_first_login=is_first_login
    )


@router.post("/seller/register", response_model=APIResponse, response_model_exclude_none=True)
def seller_register(data: SellerRegisterRequest, db: Session = Depends(get_db)) -> dict:
    if not Seller.verify_email(data.email):
        raise APIException(400, "10007", "incorrect email format")
    if not Seller.verify_phone(data.phone):
        raise APIException(400, "10009", "incorrect phone format")
    if db.query(Seller).filter(Seller.email == data.email, Seller.is_delete == False).first() is not None:
        raise APIException(400, "10006", "register duplicate, email has been uesd")
    if db.query(Seller).filter(Seller.phone == data.phone, Seller.is_delete == False).first() is not None:
        raise APIException(400, "10006", "register duplicate, phone has been uesd")
    new_seller = Seller(
        email=data.email,
        hash_password=" ", #不能是null，下面才會設密碼
        name=data.name,
        phone=data.phone,
        company_name=data.company_name,
        company_phone=data.company_phone,
        company_address=data.company_address
    )
    new_seller.set_password(data.password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
    )


@router.post("/driver/login", response_model=APIResponse, response_model_exclude_none=True)
def driver_login(data: LoginRequest, db: Session = Depends(get_db)) -> dict:
    if not Driver.verify_email(data.email):
        raise APIException(400, "10007", "incorrect email format")
    user = db.query(Driver).filter(Driver.email == data.email, Driver.is_delete == False).first()
    if user is None:
        raise APIException(400, "10001", "user not found")
    if not user.verify_password(data.password):
        raise APIException(400, "10002", "invalid password")
    payload = {"id": f"{user.id}", "role": "driver"}
    token = create_access_token(payload)
    is_first_login = False
    if user.is_first_login == True:
        user.is_first_login = False
        db.commit()
        db.refresh(user)
        is_first_login = True
        
    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
        token=token,
        is_first_login=is_first_login
    )


@router.post("/driver/register", response_model=APIResponse, response_model_exclude_none=True)
def driver_register(data: DriverRegisterRequest, db: Session = Depends(get_db)) -> dict:
    if not Driver.verify_email(data.email):
        raise APIException(400, "10007", "incorrect email format")
    if not Driver.verify_phone(data.phone):
        raise APIException(400, "10009", "incorrect phone format")
    if db.query(Driver).filter(Driver.email == data.email, Driver.is_delete == False).first() is not None:
        raise APIException(400, "10006", "register duplicate, email has been uesd")
    if db.query(Driver).filter(Driver.phone == data.phone, Driver.is_delete == False).first() is not None:
        raise APIException(400, "10006", "register duplicate, phone has been uesd")
    new_driver = Driver(
        email=data.email,
        hash_password=" ", #不能是null，下面才會設密碼
        name=data.name,
        phone=data.phone
    )
    new_driver.set_password(data.password)
    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.utcnow() +  timedelta(hours=8),
    )