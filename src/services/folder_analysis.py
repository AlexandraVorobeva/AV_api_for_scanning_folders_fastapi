import os
from dotenv import load_dotenv

from src.services.file_analysis import make_words_analysis, get_all_words_from_files


load_dotenv()
MAIN_FOLDER = os.getenv("MAIN_FOLDER")


def get_names_and_roots_of_files(dir=MAIN_FOLDER) -> dict:
    """
    Get dict of name and roots for all files in directory.

    :param dir: path to the folder
    :return: of name and roots
    """
    names_of_files = []
    roots_of_files = []
    for root, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if filename.endswith(".txt") or filename.endswith(".py"):
                names_of_files.append(filename)
                roots_of_files.append(os.path.join(root, filename))
    return dict(zip(names_of_files, roots_of_files))


def collect_folder_info() -> dict:
    """
    Collect information about a folder into one dict.
    :return: all folder info
    """
    filesnames = list(get_names_and_roots_of_files().keys())
    files_roots = list(get_names_and_roots_of_files().values())
    prepared_words = get_all_words_from_files(files_roots)
    words_analysis_info = make_words_analysis(prepared_words)

    folder_info = {
        "count of files": len(filesnames),
        "names of files": filesnames,
        **words_analysis_info,
    }
    return folder_info
