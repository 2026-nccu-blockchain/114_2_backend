import cloudinary
from cloudinary.uploader import upload
from fastapi import HTTPException, status, UploadFile
from app.core.config import settings
from app.core.exceptions import APIException
from typing import List

cloudinary.config(
    cloud_name=settings.cloudinary_cloud_name,
    api_key=settings.cloudinary_api_key,
    api_secret=settings.cloudinary_api_secret
)

async def upload_image(image: UploadFile):
    upload_result = upload(image.file)
    file_url = upload_result['secure_url']
    return file_url
