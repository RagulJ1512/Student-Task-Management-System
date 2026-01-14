from starlette import status
from main import app
from routers.auth import get_current_user
from .utils import *


def test_update_task_status_student_authorised(client, test_task):
    app.dependency_overrides[get_current_user] = override_get_current_user_student
    response = client.patch(
        f"/student/{test_task.id}",
        params={"new_status": "COMPLETED"}
    )
    assert response.status_code == status.HTTP_202_ACCEPTED
    data = response.json()
    assert data["task_status"] == "COMPLETED"

    db = TestingSessionLocal()
    updated_task = db.query(Task).filter(Task.id == test_task.id).first()
    assert updated_task.task_status == TaskStatus.COMPLETED


def test_get_tasks_student_authorised(client, test_task, test_teacher):
    app.dependency_overrides[get_current_user] = override_get_current_user_student
    response = client.get("/student/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert any(task["task"] == "Initial Homework" for task in data)


def test_get_tasks_with_status_filter_student_authorised(client, test_task):
    app.dependency_overrides[get_current_user] = override_get_current_user_student
    response = client.get("/student/", params={"status_filter": "PENDING"})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert all(task["task_status"] == "PENDING" for task in data)


def test_get_tasks_with_teacher_filter_student_authorised(client, test_task):
    app.dependency_overrides[get_current_user] = override_get_current_user_student
    response = client.get("/student/", params={"teacher_id": test_task.teacher_id})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert all(task["teacher_id"] == test_task.teacher_id for task in data)

# ------------------- Teacher Unauthorised -----------------
def test_update_task_status_teacher_unauthorised(client, test_task):
    app.dependency_overrides[get_current_user] = override_get_current_user_teacher
    response = client.patch(
        f"/student/{test_task.id}",
        params={"new_status": "COMPLETED"}
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_get_tasks_teacher_unauthorised(client, test_task):
    app.dependency_overrides[get_current_user] = override_get_current_user_teacher
    response = client.get("/student/")
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_get_tasks_with_status_filter_teacher_unauthorised(client, test_task):
    app.dependency_overrides[get_current_user] = override_get_current_user_teacher
    response = client.get("/student/", params={"status_filter": "PENDING"})
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_get_tasks_with_teacher_filter_teacher_unauthorised(client, test_task):
    app.dependency_overrides[get_current_user] = override_get_current_user_teacher
    response = client.get("/student/", params={"teacher_id": test_task.teacher_id})
    assert response.status_code == status.HTTP_403_FORBIDDEN
