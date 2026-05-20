from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.schemas.common import APIResponse

router = APIRouter()

@router.get("/")
def get_admin(db: Session = Depends(get_db)) -> dict:
    return APIResponse(
        status_code="ADMIN_GET_SUCCESS",
        desc="Admin router works",
        response_datetime=datetime.utcnow()
    )