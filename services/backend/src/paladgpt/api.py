import io
from PIL import Image, UnidentifiedImageError
from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()


@router.get("/health", tags=["Health"])
def get_health() -> dict[str, str]:
    """Return the backend's basic availability status."""
    return {"status": "ok"}


@router.post("/api/v1/palm-scan-prediction")
async def create_prediction(image: UploadFile = File(...)):

    MAX_UPLOAD_SIZE = 5 * 1024 * 1024
    CHUNK_SIZE = 1024 * 1024

    contents = bytearray()
    total_bytes = 0

    chunk = await image.read(CHUNK_SIZE)
    while chunk:
        total_bytes += len(chunk)

        if total_bytes > MAX_UPLOAD_SIZE:
            raise HTTPException(
                status_code=413,
                detail="Uploaded file is too large.",
            )
        contents.extend(chunk)
        chunk = await image.read(CHUNK_SIZE)

    try:
        with Image.open(io.BytesIO(contents)) as img:
            img.verify()
    except (UnidentifiedImageError, OSError):
        raise HTTPException(
            status_code=400,
            detail="Invalid image file.",
        )

    with Image.open(io.BytesIO(contents)) as img:
        if img.height > 4000 or img.width > 4000:
            raise HTTPException(
                status_code=413,
                detail="Image Dimension Exceeded.",
            )

    return {"status": "success", "message": "Image validated successfully"}
