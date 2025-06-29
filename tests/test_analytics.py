from fastapi.testclient import TestClient
from main import app  # Ensure main.py exposes `app = FastAPI()`
import pytest

client = TestClient(app)


# Register an admin user and login to get a token
def get_admin_token():
    # Register admin user
    client.post("/register", json={
        "username": "admin",
        "password": "adminpass",
        "role": "admin"
    })

    # Login and get token
    response = client.post("/login", data={
        "username": "admin",
        "password": "adminpass"
    })

    assert response.status_code == 200
    return response.json()["access_token"]


def test_analytics_access():
    token = get_admin_token()

    # Create a short URL
    response = client.post("/shorten", json={
        "original_url": "http://example.com"
    }, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    short_code = response.json()["short_code"]

    # Now test analytics
    response = client.get("/analytics", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()

    # Check if the shortened URL is listed
    assert any(entry["code"] == short_code for entry in data)
