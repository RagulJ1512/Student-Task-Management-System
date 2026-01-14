import pytest
from sqlalchemy import text
from starlette import status
from main import app
from models import Users, UserRole
from routers.auth import bcrypt_context, get_current_user
from .utils import *


def test_create_user_authorized(client, test_teacher):
    app.dependency_overrides[get_current_user] = override_get_current_user_teacher

    request_data = {
        "username": "newstudent",
        "email": "newstudent@example.com",
        "first_name": "New",
        "last_name": "Student",
        "password": "password123",
        "role": "STUDENT"
    }
    response = client.post("/user/", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED

    db = TestingSessionLocal()
    created_user = db.query(Users).filter(Users.username == "newstudent").first()
    assert created_user is not None
    assert created_user.role == UserRole.STUDENT



def test_create_user_unauthorized(client, test_student):
    app.dependency_overrides[get_current_user] = override_get_current_user_student

    request_data = {
        "username": "badcreate",
        "email": "badcreate@example.com",
        "first_name": "Bad",
        "last_name": "Create",
        "password": "password123",
        "role": "STUDENT"
    }
    response = client.post("/user/", json=request_data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_get_user_authorized(client, test_teacher):
    app.dependency_overrides[get_current_user] = override_get_current_user_teacher

    response = client.get("/user/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["username"] == "teacher1"
    assert data["email"] == "teacher1@example.com"


def test_get_user_unauthorized(client):
    #user none
    app.dependency_overrides[get_current_user] = lambda: None

    response = client.get("/user/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
