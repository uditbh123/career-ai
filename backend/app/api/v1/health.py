from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.

    Returns the current status of the application.
    """

    return {
        "status": "healthy",
        "application": "Career AI",
        "version": "0.1.0",
    }