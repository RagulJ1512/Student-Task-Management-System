from sqlalchemy import text
from starlette import status
from .utils import *




# POST /auth/token - valid credentials
def test_login_valid_credentials(client, test_teacher):
    response = client.post(
        "/auth/token",
        data={"username": "teacher1", "password": "password"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == status.HTTP_202_ACCEPTED
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


# POST /auth/token - invalid credentials
def test_login_invalid_credentials(client, test_teacher):
    response = client.post(
        "/auth/token",
        data={"username": "teacher1", "password": "wrongpassword"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    data = response.json()
    assert data["detail"] == "Could not validate user."


# POST /auth/token - non-existent user
def test_login_nonexistent_user(client):
    response = client.post(
        "/auth/token",
        data={"username": "ghost", "password": "password123"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    data = response.json()
    assert data["detail"] == "Could not validate user."
