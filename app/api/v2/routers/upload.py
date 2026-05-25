from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.schemas.common import APIResponse
from app.schemas.upload import UploadRequest

router = APIRouter()


@router.post("/")
def upload_image(
    data: UploadRequest,
    db: Session = Depends(get_db)
):

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        url=f"https://example.com/{data.file_name}"
    )