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