from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
# from app.schemas.driver import
from app.schemas.driver import DriverUpdateRequest
from app.db.session import get_db
from app.models.model import Driver
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token

router = APIRouter()

@router.get("/me")
def get_driver_me(driver_id: str, db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id == driver_id, Driver.is_delete == False).first()
    if not driver:
        raise APIException(404, "10001", "driver not found")

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        user_id=driver.id,
        email=driver.email,
        phone=driver.phone,
        name=driver.name,
    )


@router.put("/me")
def update_driver_me(driver_id: str, data: DriverUpdateRequest, db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id == driver_id, Driver.is_delete == False).first()
    if not driver:
        raise APIException(404, "10001", "driver not found")

    driver.email = data.email
    driver.phone = data.phone
    driver.name = data.name

    db.commit()
    db.refresh(driver)

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        email=driver.email,
        phone=driver.phone,
        name=driver.name,
    )


@router.delete("/{DriverId}")
def delete_driver(DriverId: str, db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id == DriverId, Driver.is_delete == False).first()
    if not driver:
        raise APIException(404, "10001", "not found")

    driver.is_delete = True
    db.commit()

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )
