from pydantic import BaseModel


class CartCreateRequest(BaseModel):
    product_id: str
    count: int

class CartUpdateRequest(BaseModel):
    count: int

