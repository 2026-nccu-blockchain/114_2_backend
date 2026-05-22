from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
# from app.schemas.driver import
from app.db.session import get_db
from app.models.model import Driver
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token


router = APIRouter()


@router.get("/me")
def get_driver_me(db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )


@router.put("/me")
def update_driver_me(db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )


@router.delete("/{DriverId}")
def delete_driver(DriverId: int, db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
    )