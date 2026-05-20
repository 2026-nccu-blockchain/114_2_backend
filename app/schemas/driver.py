from pydantic import BaseModel
from typing import Optional


class DriverUpdateRequest(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None


class DriverResponse(BaseModel):
    driver_id: int
    name: str
    phone: str