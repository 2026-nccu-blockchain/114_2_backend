from pydantic import BaseModel, EmailStr
from typing import Optional


class DriverUpdateRequest(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: EmailStr
