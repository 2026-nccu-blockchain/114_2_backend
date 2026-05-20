from pydantic import BaseModel
from typing import Optional


class ProductCreateRequest(BaseModel):
    product_name: str
    price: int
    stock: int
    description: str


class ProductUpdateRequest(BaseModel):
    product_name: Optional[str] = None
    price: Optional[int] = None
    stock: Optional[int] = None
    description: Optional[str] = None


class ProductResponse(BaseModel):
    product_id: int
    product_name: str
    price: int
    stock: int
    description: str