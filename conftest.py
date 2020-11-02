import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "http://pulse-rest-testing.herokuapp.com/"


@pytest.fixture
def book(base_url):
    data = {"title": "Some", "author": "122"}
    r = requests.post(f"{base_url}/books/", data=data)
    book_data = r.json()
    yield book_data
    r = requests.delete(f"{base_url}/books/{book_data['id']}")
