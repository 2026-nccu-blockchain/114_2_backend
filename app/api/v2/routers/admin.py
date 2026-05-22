<<<<<<< HEAD:app/api/v1/routers/admin.py
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
=======
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
# from app.schemas.admin import
from app.db.session import get_db
from app.models.model import Admin
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.deps import verify_token

router = APIRouter()
>>>>>>> origin/develop:app/api/v2/routers/admin.py
