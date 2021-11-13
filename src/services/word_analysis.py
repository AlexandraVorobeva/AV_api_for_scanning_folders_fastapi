VOWELS = [
    "a",
    "e",
    "i",
    "o",
    "u",
    "y",
    "а",
    "е",
    "ё",
    "и",
    "о",
    "у",
    "ы",
    "э",
    "ю",
    "я",
]
CONSONANTS = [
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "z",
    "б",
    "г",
    "д",
    "ж",
    "з",
    "й",
    "к",
    "л",
    "м",
    "н",
    "п",
    "р",
    "с",
    "т",
    "ф",
    "х",
    "ц",
    "ч",
    "ш",
    "щ",
    "ь",
    "ъ",
]


def get_phonetic_analysis(words: list[str]) -> dict:
    """
    Make phonetic analysis for words in the list.

    :param words: list of words
    :return: phonetic information about words
    """
    count_of_vowels = 0
    count_of_consonants = 0
    for word in words:
        lowercase_word = word.lower()
        for letter in lowercase_word:
            if letter in VOWELS:
                count_of_vowels += 1
            if letter in CONSONANTS:
                count_of_consonants += 1

    syllables = count_of_vowels  # сколько в слове гласных, столько и слогов :)
    phonetic_info = {
        "count of vowels": count_of_vowels,
        "count of consonants": count_of_consonants,
        "syllables": syllables,
    }
    return phonetic_info


def collect_one_word_info(word: str) -> dict:
    """
    Collect information about word into one dict.

    :param word: any word
    :return: information about word
    """
    phonetic_analysis_of_word = get_phonetic_analysis(list(word))
    word_info = {"word": word, "len of word": len(word), **phonetic_analysis_of_word}
    return word_info
