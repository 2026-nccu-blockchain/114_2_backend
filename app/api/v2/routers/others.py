from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import bcrypt

from app.db.session import get_db
from app.schemas.common import APIResponse
from app.schemas.others import PasswordResetRequest, PasswordForgetRequest, UploadRequest
from app.models.model import Admin, Buyer, Seller, Driver
from app.core.exceptions import APIException

router = APIRouter()


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


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

    user.hash_password = hash_password(data.password)
    db.commit()

    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow()
    )


@router.post("/upload")
def upload_image(data: UploadRequest, db: Session = Depends(get_db)):
    # TODO: 之後接 Cloudinary / 檔案上傳
    return APIResponse(
        status_code="00000",
        desc="success",
        response_datetime=datetime.utcnow(),
        url="https://example.com/image.jpg"
    )