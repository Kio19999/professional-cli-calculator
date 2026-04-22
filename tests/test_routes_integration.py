from fastapi.testclient import TestClient
from app.calculator.app import app

client = TestClient(app)


def test_register_user():
    response = client.post(
        "/users/register",
        json={
            "username": "testuser_route",
            "email": "testuser_route@example.com",
            "password": "Strong123"
        }
    )
    assert response.status_code in [200, 201]


def test_login_user():
    client.post(
        "/users/register",
        json={
            "username": "loginuser",
            "email": "loginuser@example.com",
            "password": "Strong123"
        }
    )

    response = client.post(
        "/users/login",
        json={
            "username": "loginuser",
            "password": "Strong123"
        }
    )
    assert response.status_code == 200


def test_create_calculation():
    response = client.post(
        "/calculations",
        json={
            "a": 8,
            "b": 2,
            "type": "divide"
        }
    )
    assert response.status_code in [200, 201]
    assert response.json()["result"] == 4


def test_get_calculations():
    response = client.get("/calculations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_and_delete_calculation():
    create_response = client.post(
        "/calculations",
        json={
            "a": 5,
            "b": 5,
            "type": "add"
        }
    )
    assert create_response.status_code in [200, 201]
    calculation_id = create_response.json()["id"]

    update_response = client.put(
        f"/calculations/{calculation_id}",
        json={
            "a": 9,
            "b": 3,
            "type": "multiply"
        }
    )
    assert update_response.status_code == 200
    assert update_response.json()["result"] == 27

    delete_response = client.delete(f"/calculations/{calculation_id}")
    assert delete_response.status_code == 200