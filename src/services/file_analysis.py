from string import punctuation
from collections import defaultdict
from .word_analysis import get_phonetic_analysis


def get_all_words_from_files(list_of_files: list) -> list:
    """
    Get all words in main folder.

    :param list_of_files: all files in the folder
    :return: list of all words in main folder
    """
    all_words = []
    for files in list_of_files:
        with open(files, encoding="utf-8") as text:
            words = [x.strip(punctuation).lower() for x in text.read().split()]
            all_words.extend(words)
    return all_words


def get_common_and_rare_words(words: list) -> dict:
    """
    Find the rarest and the most common words in list.

    :param words: list of words
    :return: the rarest and the most common words
    """
    counter_of_words = defaultdict(int)
    for word in words:
        if len(word) >= 2:
            counter_of_words[word] += 1
    top_of_words = {
        "common_word": sorted(
            counter_of_words.items(), key=lambda item: item[1], reverse=True
        )[0][0],
        "rarest_word": sorted(counter_of_words.items(), key=lambda item: item[1])[0][0],
    }
    return top_of_words


def get_averages_word_len(words: list) -> int:
    """
    Calculate average word length.

    :param words: list of words
    :return: number, average word length
    """
    len_of_words = [len(word) for word in words]
    average_word_len = int(sum(len_of_words) / len(len_of_words))
    return average_word_len


def make_words_analysis(words: list) -> dict:
    """
    Make words analysis ane save it into one dict.

    :param words: list of words
    :return: dict of analysis of words
    """
    most_common_word = get_common_and_rare_words(words)["common_word"]
    rarest_word = get_common_and_rare_words(words)["rarest_word"]

    average_len_of_words = get_averages_word_len(words)
    phonetic_analysis_of_word = get_phonetic_analysis(words)

    words_info = {
        "the most common word": most_common_word,
        "the rarest word": rarest_word,
        "average len of words": average_len_of_words,
        **phonetic_analysis_of_word,
    }
    return words_info


def collect_file_info(filename: str, path_to_file: list) -> dict:
    """
    Collect information about words in the file into one dict.

    :param filename: name of the file
    :param path_to_file: root to the file
    :return: dict of info about some file.
    """
    prepared_words = get_all_words_from_files(path_to_file)
    words_analysis_info = make_words_analysis(prepared_words)

    file_info = {"name of file": filename, **words_analysis_info}
    return file_info
