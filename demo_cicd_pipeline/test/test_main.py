from fastapi.testclient import TestClient
from src.main import api

client = TestClient(api)


# Test home endpoint
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


# Test POST
def test_create_todo():
    response = client.post("/todos", json={
        "id": 1,
        "name": "Study",
        "description": "Prepare for exams"
    })
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Study"


# Test GET all
def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


# Test PUT
def test_update_todo():
    response = client.put("/todos/1", json={
        "id": 1,
        "name": "Study Updated",
        "description": "Prepare for math exams"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Study Updated"


# Test DELETE
def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Study Updated",
        "description": "Prepare for math exams"
    }