from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    jwt_algorithm: str
    database_url: str 
    jwt_expiration_minutes: int 
    cloudinary_cloud_name: str
    cloudinary_api_key: str
    cloudinary_api_secret: str

    class Config:
        env_file = ".env"

settings = Settings()