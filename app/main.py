from fastapi import FastAPI
from fastapi import Request
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.api.v1.router import api_router
from app.db.session import init_db
from app.core.exceptions import APIException
from app.schemas.common import ErrorResponse


app = FastAPI(title="FastAPI SQLite Service")


@app.on_event("startup")
def on_startup() -> None:
    init_db()

@app.exception_handler(APIException)
async def api_exception_handler(request: Request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
          content=jsonable_encoder(ErrorResponse(
            status_code=exc.status_code_str,
            desc=exc.desc,
            response_datetime=datetime.utcnow()
          ))
    )

app.include_router(api_router)
