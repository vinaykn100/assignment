from fastapi import APIRouter

from .endpoints import images

router = APIRouter()
router.include_router(images.router, prefix="/images", tags=["images"])