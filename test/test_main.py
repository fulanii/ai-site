


import pytest
from flask_ai.ai_backend import ask_open_ai
from flask_ai import app
from flask.testing import FlaskClient


def test_openai():
    assert ask_open_ai("what does the nba stand for?") != ""


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client



def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_form(client):
    response = client.post("/chat", data={"user_chat": "Flask"})
    assert response.status_code == 200