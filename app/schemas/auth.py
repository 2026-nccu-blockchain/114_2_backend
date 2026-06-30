from pydantic import BaseModel, EmailStr
from typing import Optional

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class AdminRegisterRequest(BaseModel):
    email: EmailStr
    password: str
    name: str

class BuyerRegisterRequest(BaseModel):
    email: EmailStr
    password: str
    phone: str
    name: str
    avatar_url: Optional[str] = None
    address: str

class SellerRegisterRequest(BaseModel):
    email: EmailStr
    password: str
    phone: str
    name: str
    avatar_url: Optional[str] = None
    company_address: str
    company_phone: str
    company_name: str

class DriverRegisterRequest(BaseModel):
    email: EmailStr
    password: str
    phone: str
    name: str
    avatar_url: Optional[str] = None

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str

class PasswordResetRequest(BaseModel):
    old_password: str
    new_password: str


class PasswordForgetRequest(BaseModel):
    email: EmailStr
    phone: str
    password: str