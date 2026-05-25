from pydantic import BaseModel, EmailStr

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
    address: str

class SellerRegisterRequest(BaseModel):
    email: EmailStr
    password: str
    phone: str
    name: str
    company_address: str
    company_phone: str
    company_name: str

class DriverRegisterRequest(BaseModel):
    email: EmailStr
    password: str
    phone: str
    name: str

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str

class PasswordResetRequest(BaseModel):
    password: str


class PasswordForgetRequest(BaseModel):
    email: EmailStr
    phone: str
    password: str