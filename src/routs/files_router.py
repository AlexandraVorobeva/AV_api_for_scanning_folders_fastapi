from fastapi import APIRouter, HTTPException, status
from src.services.file_analysis import collect_file_info
from src.services.folder_analysis import get_names_and_roots_of_files


router = APIRouter(
    prefix="/file",
)


@router.get("/{filename}/")
def get_file_info(filename: str):
    """
    GET information about any file in the main folder.

    :param filename: name of file
    :return: file information
    """
    path = []
    names_and_roots = get_names_and_roots_of_files()
    if filename in names_and_roots.keys():
        path.append(names_and_roots[filename])
        return collect_file_info(filename, path)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The main folder does not contain such file.",
        )
