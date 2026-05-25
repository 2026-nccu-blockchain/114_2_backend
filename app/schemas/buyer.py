from pydantic import BaseModel, EmailStr
from typing import Optional


class BuyerUpdateRequest(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    email: EmailStr
