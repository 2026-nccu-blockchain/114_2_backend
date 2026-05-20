from pydantic import BaseModel


class AdminResponse(BaseModel):
    admin_id: int
    name: str
    email: str