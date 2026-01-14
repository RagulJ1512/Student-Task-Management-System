import pytest
from sqlalchemy import text
from starlette import status
from main import app
from models import Task, TaskStatus
from routers.auth import get_current_user
from .utils import *


def test_create_task_teacher_authorised(client, test_teacher, test_student):
    app.dependency_overrides[get_current_user] = override_get_current_user_teacher
    request_data = {
        "student_id": test_student.id,
        "task": "Math Homework",
        "description": "Solve algebra problems"
    }
    response = client.post("/teacher/", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["task"] == "Math Homework"
    assert data["task_status"] == "PENDING"

    db = TestingSessionLocal()
    task = db.query(Task).filter(Task.id == data["id"]).first()
    assert task is not None
    assert task.task == "Math Homework"


def test_get_tasks_teacher_authorised(client, test_task, test_student):
    app.dependency_overrides[get_current_user] = override_get_current_user_teacher
    response = client.get("/teacher/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert any(task["task"] == "Initial Homework" for task in data)


def test_update_task_teacher_authorised(client, test_task):
    app.dependency_overrides[get_current_user] = override_get_current_user_teacher
    request_data = {
        "task": "Updated Homework",
        "description": "Solve geometry problems",
        "task_status": "COMPLETED"
    }
    response = client.put(f"/teacher/{test_task.id}", json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    updated_task = db.query(Task).filter(Task.id == test_task.id).first()
    assert updated_task.task == "Updated Homework"
    assert updated_task.task_status == TaskStatus.COMPLETED


def test_delete_task_teacher_authorised(client, test_task):
    app.dependency_overrides[get_current_user] = override_get_current_user_teacher
    response = client.delete(f"/teacher/{test_task.id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    deleted_task = db.query(Task).filter(Task.id == test_task.id).first()
    assert deleted_task is None


def test_get_students_teacher_authorised(client, test_teacher, test_student):
    app.dependency_overrides[get_current_user] = override_get_current_user_teacher
    response = client.get("/teacher/students")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert any(student["username"] == "student1" for student in data)


# ------------------------ STUDENT UNAUTHORISED ------------------------------

def test_create_task_student_unauthorised(client, test_teacher, test_student):
    app.dependency_overrides[get_current_user] = override_get_current_user_student
    request_data = {
        "student_id": test_student.id,
        "task": "Math Homework",
        "description": "Solve algebra problems"
    }
    response = client.post("/teacher/", json=request_data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_get_tasks_student_unauthorised(client, test_task):
    app.dependency_overrides[get_current_user] = override_get_current_user_student
    response = client.get("/teacher/")
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_update_task_student_unauthorised(client, test_task):
    app.dependency_overrides[get_current_user] = override_get_current_user_student
    request_data = {
        "task": "Updated Homework",
        "description": "Solve geometry problems",
        "task_status": "COMPLETED"
    }
    response = client.put(f"/teacher/{test_task.id}", json=request_data)
    assert response.status_code == status.HTTP_403_FORBIDDEN

def test_delete_task_student_unauthorised(client, test_task):
    app.dependency_overrides[get_current_user] = override_get_current_user_student
    response = client.delete(f"/teacher/{test_task.id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_get_students_student_unauthorised(client, test_teacher, test_student):
    app.dependency_overrides[get_current_user] = override_get_current_user_student
    response = client.get("/teacher/students")
    assert response.status_code == status.HTTP_403_FORBIDDEN
