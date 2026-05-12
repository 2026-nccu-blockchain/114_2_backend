from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    jwt_algorithm: str
    database_url: str 
    jwt_expiration_minutes: int 

    class Config:
        env_file = ".env"

settings = Settings()