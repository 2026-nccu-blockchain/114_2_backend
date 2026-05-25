from fastapi import APIRouter, UploadFile, Request
from app.db.session import get_db
from app.models.model import Admin, Buyer, Seller, Driver
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token
from app.core.cloudinary import upload_image

router = APIRouter()

ALLOWED_IMAGE_TYPES = [
    "image/jpeg",
    "image/png",
    "image/webp",
]


@router.post("/upload", response_model=APIResponse, response_model_exclude_none=True)
async def handle_upload(request: Request, image: UploadFile):
    verify_token(request)
    if image.content_type not in ALLOWED_IMAGE_TYPES:
        raise APIException(400, "40001", "upload not an image")
    try:
        url = await upload_image(image)
        return APIResponse(
            status_code="00000",
            message="upload successfully",
            response_datetime=datetime.utcnow(),
            url=url
        )
    except Exception:
        raise APIException(500, "00002", "backend have some problems")
