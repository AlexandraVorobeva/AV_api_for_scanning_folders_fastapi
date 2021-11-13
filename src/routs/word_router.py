from fastapi import APIRouter, HTTPException, status
from src.services.word_analysis import collect_one_word_info
from src.services.file_analysis import get_all_words_from_files
from src.services.folder_analysis import get_names_and_roots_of_files


router = APIRouter(
    prefix="/word",
)


@router.get("/{word}/")
def get_word_info(word: str):
    """
    GET information about any word in the main folder.

    :param word: any word
    :return: phonetic analysis of the word
    """
    all_file_roots = list(get_names_and_roots_of_files().values())
    all_words = get_all_words_from_files(all_file_roots)
    if word in all_words:
        return collect_one_word_info(word)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The main folder does not contain such word.",
        )
