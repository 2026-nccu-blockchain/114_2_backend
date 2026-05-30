from pydantic import BaseModel
from typing import List


class OrderCreateRequest(BaseModel):
    to_addr: str
    order_status: str


class DriverTakeOrderRequest(BaseModel):
    driver_id: str


class OrderUpdateStatusRequest(BaseModel):
    status: str