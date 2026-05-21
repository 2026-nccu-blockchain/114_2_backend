from pydantic import BaseModel


class ProductCreateRequest(BaseModel):
    name: str
    price: float
    stock: int
    status: bool
    desc: str
    type: str


class ProductUpdateRequest(BaseModel):
    name: str
    price: float
    stock: int
    status: bool
    desc: str
    type: str