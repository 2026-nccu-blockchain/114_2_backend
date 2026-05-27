from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.schemas.product import ProductResponse
from app.schemas.cart import CartResponse


# 合法請求的回應格式
class APIResponse(BaseModel):
    status_code: str
    message: Optional[str] = None
    response_datetime: datetime
    # 不加 data 欄位，或直接把要回傳的欄位寫在這層
    # 其他欄位依需求加
    token: Optional[str] = None
    uuid: Optional[str] = None
    product_id: Optional[str] = None
    pid: Optional[str] = None
    oid: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    avatar_url: Optional[str] = None
    company_address: Optional[str] = None
    company_phone: Optional[str] = None
    company_name: Optional[str] = None
    buyer: Optional[list] = None
    seller: Optional[list] = None
    driver: Optional[list] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    status: Optional[bool] = None
    desc: Optional[str] = None
    type: Optional[str] = None
    product_url: Optional[str] = None
    product: Optional[list[ProductResponse]] = None
    order_status: Optional[str] = None
    cart_id: Optional[str] = None
    buyer_id: Optional[str] = None
    seller_id: Optional[str] = None
    driver_id: Optional[str] = None
    order_id: Optional[str] = None
    to_addr: Optional[str] = None
    from_addr: Optional[str] = None
    total_price: Optional[float] = None
    count: Optional[int] = None
    order: Optional[list] = None
    is_first_login: Optional[bool] = None
    product_id: Optional[str] = None
    product_name: Optional[str] = None
    url: Optional[str] = None
    cart: Optional[list[CartResponse]] = None

# 錯誤回應的格式 
class ErrorResponse(BaseModel):
    status_code: str
    message: str
    response_datetime: datetime