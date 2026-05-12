from fastapi import HTTPException

class APIException(HTTPException):
    def __init__(self, http_status: int, status_code: str, desc: str):
        super().__init__(status_code=http_status, detail=desc)
        self.status_code_str = status_code
        self.desc = desc