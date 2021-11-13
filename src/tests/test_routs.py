from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_folder_info():
    response = client.get("/folder/")
    assert response.status_code == 200


def test_get_word_info():
    response = client.get("/word/one/")
    assert response.status_code == 200
    assert response.json() == {
        "word": "one",
        "len of word": 3,
        "count of vowels": 2,
        "count of consonants": 1,
        "syllables": 2,
    }


def test_get_word_info_negative():
    response = client.get("/word/no/")
    assert response.status_code == 404
    assert response.json() == {"detail": "The main folder does not contain such word."}


def test_get_file_info():
    response = client.get("file/one.txt/")
    assert response.status_code == 200
    assert response.json() == {
        "name of file": "one.txt",
        "the most common word": "one",
        "the rarest word": "один",
        "average len of words": 3,
        "count of vowels": 8,
        "count of consonants": 5,
        "syllables": 8,
    }


def test_get_file_info_negative():
    response = client.get("/file/no/")
    assert response.status_code == 404
    assert response.json() == {"detail": "The main folder does not contain such file."}
