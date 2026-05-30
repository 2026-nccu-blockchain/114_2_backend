from pydantic import BaseModel


class CartCreateRequest(BaseModel):
    product_id: str
    count: int

class CartUpdateRequest(BaseModel):
    count: int

class CartResponse(BaseModel):
    id: str
    product_id: str
    name: str
    type: str
    price: float
    count: int