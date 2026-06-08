from pydantic import BaseModel
from typing import List


class OrderCreateRequest(BaseModel):
    to_addr: str


class OrderUpdateStatusRequest(BaseModel):
    status: str