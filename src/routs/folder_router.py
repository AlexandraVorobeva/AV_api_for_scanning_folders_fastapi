from fastapi import APIRouter, Depends
from ..services.folder_analysis import collect_folder_info


router = APIRouter(
    prefix="/folder",
)


@router.get("/")
def get_folder_info():
    """
    GET information about main folder.
    """
    return collect_folder_info()
