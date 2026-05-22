from pydantic import BaseModel, EmailStr


class PasswordResetRequest(BaseModel):
    password: str


class PasswordForgetRequest(BaseModel):
    email: EmailStr
    phone: str
    password: str


class UploadRequest(BaseModel):
    email: EmailStr