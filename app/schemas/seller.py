from pydantic import BaseModel
from typing import Optional


class SellerUpdateRequest(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    company_name: Optional[str] = None
    company_phone: Optional[str] = None
    company_address: Optional[str] = None


class SellerResponse(BaseModel):
    seller_id: int
    name: str
    phone: str
    company_name: str
    company_phone: str
    company_address: str