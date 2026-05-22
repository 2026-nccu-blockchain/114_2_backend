from pydantic import BaseModel
from typing import List


class OrderCreateRequest(BaseModel):
    buyer_id: str
    seller_id: str
    to_addr: str
    order_status: str
    product_id: List[str]
    count: List[int]


class DriverTakeOrderRequest(BaseModel):
    driver_id: str


class OrderUpdateStatusRequest(BaseModel):
    status: str