"""
Unit tests for the main web app.
"""
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
    assert response.json == "".join(reversed(text))


def test_more(client):
    response = client.get("/more")
    assert response.status_code == 200
