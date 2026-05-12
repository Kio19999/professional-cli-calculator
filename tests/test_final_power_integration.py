from fastapi.testclient import TestClient
from app.calculator.app import app

client = TestClient(app)


def test_create_power_calculation():
    response = client.post(
        "/calculations",
        json={
            "a": 2,
            "b": 3,
            "type": "power"
        }
    )

    assert response.status_code in [200, 201]
    data = response.json()
    assert data["type"] == "power"
    assert data["result"] == 8