from fastapi import APIRouter
from fastapi import Depends
from typing import Optional
from sqlalchemy.orm import Session
# from app.schemas.driver import
from app.schemas.driver import DriverUpdateRequest
from app.db.session import get_db
from app.models.model import Driver
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import return_payload
import pytz

router = APIRouter()

@router.get("/me")
def get_driver_me(
    driver_id: Optional[str] = None,
    db: Session = Depends(get_db),
    payload: dict = Depends(return_payload)
):
    token_id = payload.get("id")
    if payload.get("role") != "driver" or not token_id:
        raise APIException(403, "10008", "permission denied")
    if driver_id is not None and driver_id != token_id:
        raise APIException(403, "10008", "permission denied")
    driver = db.query(Driver).filter(Driver.id == token_id, Driver.is_delete == False).first()
    if not driver:
        raise APIException(404, "10001", "driver not found")

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        user_id=driver.id,
        email=driver.email,
        phone=driver.phone,
        name=driver.name,
    )


@router.put("/me")
def update_driver_me(
    data: DriverUpdateRequest,
    driver_id: Optional[str] = None,
    db: Session = Depends(get_db),
    payload: dict = Depends(return_payload)
):
    token_id = payload.get("id")
    if payload.get("role") != "driver" or not token_id:
        raise APIException(403, "10008", "permission denied")
    if driver_id is not None and driver_id != token_id:
        raise APIException(403, "10008", "permission denied")
    driver = db.query(Driver).filter(Driver.id == token_id, Driver.is_delete == False).first()
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
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
        email=driver.email,
        phone=driver.phone,
        name=driver.name,
    )


@router.delete("/{DriverId}")
def delete_driver(
    DriverId: str,
    db: Session = Depends(get_db),
    payload: dict = Depends(return_payload)
):
    token_id = payload.get("id")
    if payload.get("role") != "driver" or not token_id:
        raise APIException(403, "10008", "permission denied")
    if DriverId != token_id:
        raise APIException(403, "10008", "permission denied")
    driver = db.query(Driver).filter(Driver.id == token_id, Driver.is_delete == False).first()
    if not driver:
        raise APIException(404, "10001", "not found")

    driver.is_delete = True
    db.commit()

    return APIResponse(
        status_code="00000",
        message="success",
        response_datetime=datetime.now(pytz.timezone('Asia/Taipei')),
    )
