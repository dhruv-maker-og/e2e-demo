import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as c:
        yield c


def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_users_list(client):
    resp = client.get("/users")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 3


def test_user_search(client):
    resp = client.get("/user?name=Ada Lovelace")
    assert resp.status_code == 200
    assert resp.get_json()[0]["email"] == "ada@example.com"
