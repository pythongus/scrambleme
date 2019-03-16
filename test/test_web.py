"""
Unit tests for the main web app.
"""
import re
import pytest
from web.app import app


@pytest.fixture
def client():
    return app.test_client()


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_scramble(client):
    text = "Test the scrambler"
    response = client.post("/scramble", data=dict(text=text))
    assert response.status_code == 200
    assert re.search(f"[{text}]{{{len(text)}}}", response.data.decode("UTF-8"))


def test_more(client):
    response = client.get("/more")
    assert response.status_code == 200
