from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
# from app.schemas.auth import
from app.db.session import get_db
from app.models.model import Admin, Buyer, Seller, Driver
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.jwt import create_access_token
from app.core.deps import verify_token

router = APIRouter()