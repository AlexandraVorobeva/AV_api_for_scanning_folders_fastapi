from fastapi import APIRouter
from .folder_router import router as folder_router
from .files_router import router as file_router
from .word_router import router as word_router

router = APIRouter()
router.include_router(folder_router)
router.include_router(file_router)
router.include_router(word_router)
