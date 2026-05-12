from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate, UserLogin
from app.db.session import get_db
from app.models.model import User
from app.core.exceptions import APIException
from app.schemas.common import APIResponse
from datetime import datetime
from app.core.jwt import create_access_token
from app.core.deps import verify_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)) -> dict:
    existing_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if existing_user:
        raise APIException(400, "99999", "Username or email already exists")
    
    new_user = User(username=user.username, email=user.email)
    new_user.set_password(user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return APIResponse(
        status_code="USER_CREATED",
        desc="User registered successfully",
        response_datetime=datetime.utcnow(),
        user_id=new_user.id,
        username=new_user.username
    )
    
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)) -> dict:
    existing_user = db.query(User).filter(User.username == user.username).first()
    if not existing_user or not existing_user.verify_password(user.password):
        raise APIException(401, "99998", "Invalid username or password")
    
    token = create_access_token({"user_id": existing_user.id})
    
    return APIResponse(
        status_code="LOGIN_SUCCESS",
        desc="User logged in successfully",
        response_datetime=datetime.utcnow(),
        user_id=existing_user.id,
        username=existing_user.username,
        access_token=token
    )
    
@router.get("/me")
def get_current_user(db: Session = Depends(get_db), _: None = Depends(verify_token)) -> dict:
    return APIResponse(
        status_code="USER_INFO",
        desc="User information retrieved successfully",
        response_datetime=datetime.utcnow()
    )