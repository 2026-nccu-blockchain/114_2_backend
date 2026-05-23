from pydantic import BaseModel
from typing import Optional

class ProductCreateRequest(BaseModel):
    name: str
    price: float
    stock: int
    status: bool
    desc: str
    type: str
    product_url: Optional[str] = None

class ProductTypeCreateRequest(BaseModel):
    price: float
    stock: int
    status: bool
    desc: str
    type: str
    product_url: Optional[str] = None

class ProductUpdateRequest(BaseModel):
    name: str

class ProductTypeUpdateRequest(BaseModel):
    price: float
    stock: int
    status: bool
    desc: str
    type: str
    product_url: str
