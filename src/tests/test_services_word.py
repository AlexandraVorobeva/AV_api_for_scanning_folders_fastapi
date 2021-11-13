import pytest
from src.services.word_analysis import get_phonetic_analysis, collect_one_word_info

words_for_test = ["питон", "питон", "fastapi", "python", "питон"]


def test_get_phonetic_analysis():
    expected_result = {
        "count of vowels": 11,
        "count of consonants": 17,
        "syllables": 11,
    }
    assert get_phonetic_analysis(words_for_test) == expected_result


def test_collect_one_word_info():
    expected_result = {
        "word": "питон",
        "len of word": 5,
        "count of vowels": 2,
        "count of consonants": 3,
        "syllables": 2,
    }
    assert collect_one_word_info("питон") == expected_result
