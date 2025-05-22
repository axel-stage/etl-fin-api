import pytest

from extract.api_client import fetch_api_data


def test_fetch_api_data():
    # arrange
    url: str = "https://jsonplaceholder.typicode.com/todos/1"
    expect: dict = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }
    # act
    test = fetch_api_data(url)
    # assert
    assert expect == test
