import requests
import pytest


book_list = [{"title": "Some", "author": "122"}, {"title": "!@#%^", "author": "@$&("}]


@pytest.mark.parametrize("book_data", book_list, ids=[str(i) for i in book_list])
def test_create_book(base_url, book_data):
    # book_data = {"title": "Some", "author": "122"}
    resp = requests.post(f"{base_url}/books/", data=book_data)
    assert resp.status_code == 201
    body = resp.json()
    assert "id" in body
    for key in book_data:
        assert body[key] == book_data[key]
