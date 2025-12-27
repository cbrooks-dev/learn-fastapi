import requests

BASE = "http://127.0.0.1:8000"


def test_get_tasks():
    response = requests.get(BASE + "/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_task():
    response = requests.get(BASE + "/tasks/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert "id" in response.json()
