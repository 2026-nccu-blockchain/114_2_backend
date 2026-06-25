from fastapi import FastAPI
from fastapi import Request
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pytz

from app.api.v2.router import api_router
from app.db.session import init_db
from app.core.exceptions import APIException
from app.schemas.common import ErrorResponse
from app.core.middleware import CustomHeaderMiddleware, RateLimitMiddleware
from app.core.config import settings


MAX_REQUESTS=settings.max_requests
WINDOW_SECONDS=settings.window_seconds

app = FastAPI(title="FastAPI SQLite Service")

app.add_middleware(CustomHeaderMiddleware)
app.add_middleware(
    RateLimitMiddleware,
    max_requests=MAX_REQUESTS,
    window_seconds=WINDOW_SECONDS
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup() -> None:
    init_db()

@app.exception_handler(APIException)
async def api_exception_handler(request: Request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
          content=jsonable_encoder(ErrorResponse(
            status_code=exc.status_code_str,
            message=exc.message,
            response_datetime=datetime.now(pytz.timezone('Asia/Taipei'))
          ))
    )

app.include_router(api_router)
