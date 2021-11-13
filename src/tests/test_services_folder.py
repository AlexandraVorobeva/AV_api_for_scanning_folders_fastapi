import pytest
from src.services.folder_analysis import get_names_and_roots_of_files


test_dir = "/Users/aleksandravorobeva/fastapi-docker-api/src/tests/data_for_test"


def test_get_names_and_roots_of_files():
    expected_result = {
        "one2.txt": "/Users/aleksandravorobeva/fastapi-docker-api/src/tests/data_for_test/one2.txt",
        "one.txt": "/Users/aleksandravorobeva/fastapi-docker-api/src/tests/data_for_test/one.txt",
        "two.txt": "/Users/aleksandravorobeva/fastapi-docker-api/src/tests/data_for_test/new2/two.txt",
        "one3.txt": "/Users/aleksandravorobeva/fastapi-docker-api/src/tests/data_for_test/new2/new3/one3.txt",
    }
    actual_result = get_names_and_roots_of_files(test_dir)
    assert actual_result == expected_result



