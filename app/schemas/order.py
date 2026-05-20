from pydantic import BaseModel


class OrderCreateRequest(BaseModel):
    product_id: int
    quantity: int


class OrderResponse(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    total_price: int