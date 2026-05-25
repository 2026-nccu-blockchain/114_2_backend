from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.model import Admin, Buyer, Seller, Driver
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime, timedelta
import re
from app.core.jwt import create_access_token
from app.schemas.auth import (
    LoginRequest,
    AdminRegisterRequest,
    BuyerRegisterRequest,
    SellerRegisterRequest,
    DriverRegisterRequest,
    PasswordResetRequest,
    PasswordForgetRequest
)

router = APIRouter()

def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    return True

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
    if not is_strong_password(data.password):
        raise APIException(400, "10010", "password is not strong")
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
    payload = {"id": f"{user.id}", "role": "buyer"}
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
    if not is_strong_password(data.password):
        raise APIException(400, "10010", "password is not strong")
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
    if not is_strong_password(data.password):
        raise APIException(400, "10010", "password is not strong")
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
    if not is_strong_password(data.password):
        raise APIException(400, "10010", "password is not strong")
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

@router.post("/password/reset/me")
def reset_password(data: PasswordResetRequest, db: Session = Depends(get_db)):
    # TODO: auth 完成後，用 token 找目前登入使用者
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow()
    )


@router.post("/password/forget")
def forget_password(data: PasswordForgetRequest, db: Session = Depends(get_db)):
    user = (
        db.query(Buyer).filter(Buyer.email == data.email, Buyer.phone == data.phone).first()
        or db.query(Seller).filter(Seller.email == data.email, Seller.phone == data.phone).first()
        or db.query(Driver).filter(Driver.email == data.email, Driver.phone == data.phone).first()
    )

    if not user:
        raise APIException(404, "10001", "not found")

    user.set_password(data.password)
    db.commit()

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow()
    )
