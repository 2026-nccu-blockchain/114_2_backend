from pydantic import BaseModel, EmailStr

class AdminUpdateRequest(BaseModel):
    email: EmailStr
    name: str
    avatar_url: str
    email: EmailStr