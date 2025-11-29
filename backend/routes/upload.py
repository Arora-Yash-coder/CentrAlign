from fastapi import APIRouter, UploadFile, File, HTTPException
from services.cloudinary_service import upload_image_to_cloud

router = APIRouter()

@router.post("/image")
async def upload_image(file: UploadFile = File(...)):
    """
    Accepts multipart/form-data image and uploads to Cloudinary.
    Returns a secure URL.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files allowed")

    url = upload_image_to_cloud(file)
    return {"url": url}
