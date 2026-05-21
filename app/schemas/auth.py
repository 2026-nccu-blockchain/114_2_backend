from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: str
    password: str

class AdminRegisterRequest(BaseModel):
    email: str
    password: str
    name: str

class BuyerRegisterRequest(BaseModel):
    email: str
    password: str
    phone: str
    name: str
    address: str

class SellerRegisterRequest(BaseModel):
    email: str
    password: str
    phone: str
    name: str
    company_address: str
    company_phone: str
    company_name: str

class DriverRegisterRequest(BaseModel):
    email: str
    password: str
    phone: str
    name: str