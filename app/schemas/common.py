from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# 合法請求的回應格式
class APIResponse(BaseModel):
    status_code: str
    desc: str
    response_datetime: datetime
    # 不加 data 欄位，或直接把要回傳的欄位寫在這層
    user_id: Optional[int] = None
    username: Optional[str] = None
    access_token: Optional[str] = None
    # 其他欄位依需求加
    product_id: Optional[str] = None
    product_name: Optional[str] = None
    
# 錯誤回應的格式 
class ErrorResponse(BaseModel):
    status_code: str
    desc: str
    response_datetime: datetime