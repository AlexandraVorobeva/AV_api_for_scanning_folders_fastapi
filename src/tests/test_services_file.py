import pytest
from src.services.file_analysis import (
    get_all_words_from_files,
    get_common_and_rare_words,
    get_averages_word_len,
    make_words_analysis,
    collect_file_info,
)

test_file = [
    "/Users/aleksandravorobeva/fastapi-docker-api/src/tests/data_for_test/one.txt"
]
words_for_test = ["питон", "питон", "fastapi", "python", "питон"]


def test_get_all_words_from_files():
    expected_result = ["one", "one", "one", "один"]
    assert get_all_words_from_files(test_file) == expected_result


def test_get_common_and_rare_words():
    expected_result = {"common_word": "питон", "rarest_word": "fastapi"}
    assert get_common_and_rare_words(words_for_test) == expected_result


def test_get_averages_word_len():
    expected_result = 5
    assert get_averages_word_len(words_for_test) == expected_result


def test_make_words_analysis():
    expected_result = {
        "the most common word": "питон",
        "the rarest word": "fastapi",
        "average len of words": 5,
        "count of vowels": 11,
        "count of consonants": 17,
        "syllables": 11,
    }
    assert make_words_analysis(words_for_test) == expected_result


def test_collect_file_info():
    expected_result = {
        "name of file": "one.txt",
        "the most common word": "one",
        "the rarest word": "один",
        "average len of words": 3,
        "count of vowels": 8,
        "count of consonants": 5,
        "syllables": 8,
    }
    assert collect_file_info("one.txt", test_file) == expected_result
