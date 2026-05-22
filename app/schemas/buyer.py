from pydantic import BaseModel
from typing import Optional


class BuyerUpdateRequest(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

