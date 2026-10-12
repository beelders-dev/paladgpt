from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["Health"])
def get_health() -> dict[str, str]:
    """Return the backend's basic availability status."""
    return {"status": "ok"}
