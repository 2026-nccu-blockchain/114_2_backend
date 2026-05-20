from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.schemas.common import APIResponse

router = APIRouter()


@router.post("/add")
def add_order(db: Session = Depends(get_db)) -> dict:
    return APIResponse(status_code="00000", desc="success", response_datetime=datetime.utcnow())


@router.get("/driver/look")
def driver_look_orders(db: Session = Depends(get_db)) -> dict:
    return APIResponse(status_code="00000", desc="success", response_datetime=datetime.utcnow())


@router.post("/driver/look/take/{OrderId}")
def driver_take_order(OrderId: int, db: Session = Depends(get_db)) -> dict:
    return APIResponse(status_code="00000", desc="success", response_datetime=datetime.utcnow())


@router.get("/{OrderId}")
def get_order(OrderId: int, db: Session = Depends(get_db)) -> dict:
    return APIResponse(status_code="00000", desc="success", response_datetime=datetime.utcnow())


@router.get("/me")
def get_my_orders(db: Session = Depends(get_db)) -> dict:
    return APIResponse(status_code="00000", desc="success", response_datetime=datetime.utcnow())


@router.put("/{OrderId}")
def update_order_status(OrderId: int, db: Session = Depends(get_db)) -> dict:
    return APIResponse(status_code="00000", desc="success", response_datetime=datetime.utcnow())