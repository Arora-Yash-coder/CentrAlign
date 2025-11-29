import cloudinary.uploader
from config.cloudinary_config import init_cloudinary

# initialize config once
init_cloudinary()


def upload_image_to_cloud(file):
    """
    Upload image file-like object to Cloudinary.
    Returns secure URL.
    """
    result = cloudinary.uploader.upload(
        file.file,
        resource_type="image"
    )
    return result.get("secure_url")
