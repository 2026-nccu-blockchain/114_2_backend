from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.schemas.driver import DriverUpdateRequest
from app.db.session import get_db
from app.models.model import Driver
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token, return_payload
import pytz

router = APIRouter()


@router.get("/me", response_model=APIResponse, response_model_exclude_none=True)
def get_driver_me(
    request: Request,
    db: Session = Depends(get_db)
):
    verify_token(request)
    payload = return_payload(request)

    if payload["role"] != "driver":
        raise APIException(403, "10008", "permission denied")

    token_id = payload["id"]

    driver = db.query(Driver).filter(
        Driver.id == token_id,
        Driver.is_delete == False
    ).first()

    if not driver:
        raise APIException(404, "10001", "driver not found")

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
        user_id=driver.id,
        email=driver.email,
        phone=driver.phone,
        name=driver.name,
    )


@router.put("/me", response_model=APIResponse, response_model_exclude_none=True)
def update_driver_me(
    request: Request,
    data: DriverUpdateRequest,
    db: Session = Depends(get_db)
):
    verify_token(request)
    payload = return_payload(request)

    if payload["role"] != "driver":
        raise APIException(403, "10008", "permission denied")

    token_id = payload["id"]

    driver = db.query(Driver).filter(
        Driver.id == token_id,
        Driver.is_delete == False
    ).first()

    if not driver:
        raise APIException(404, "10001", "driver not found")

    driver.email = data.email
    driver.phone = data.phone
    driver.name = data.name

    db.commit()
    db.refresh(driver)

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
        user_id=driver.id,
        email=driver.email,
        phone=driver.phone,
        name=driver.name,
    )


@router.delete("/me", response_model=APIResponse, response_model_exclude_none=True)
def delete_driver_me(
    request: Request,
    db: Session = Depends(get_db)
):
    verify_token(request)
    payload = return_payload(request)

    if payload["role"] != "driver":
        raise APIException(403, "10008", "permission denied")

    token_id = payload["id"]

    driver = db.query(Driver).filter(
        Driver.id == token_id,
        Driver.is_delete == False
    ).first()

    if not driver:
        raise APIException(404, "10001", "driver not found")

    driver.is_delete = True
    db.commit()

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone("Asia/Taipei")),
    )