import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient
from models import Task, Users
from schemas import TaskStatus, UserRole
from database import Base, get_db
from main import app
from routers.auth import bcrypt_context

TEST_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def client():
    yield TestClient(app)



def override_get_current_user_teacher():
    return {"username": "teacher1", "id": 1, "user_role": UserRole.TEACHER}

def override_get_current_user_student():
    return {"username": "student1", "id": 2, "user_role": UserRole.STUDENT}

@pytest.fixture
def test_teacher():
    teacher = Users(
        id=1,
        username="teacher1",
        email="teacher1@example.com",
        first_name="Teach",
        last_name="Er",
        hashed_password=bcrypt_context.hash("password"),
        role=UserRole.TEACHER,
    )
    db = TestingSessionLocal()
    db.add(teacher)
    db.commit()
    yield teacher
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM users;"))
        conn.commit()


@pytest.fixture
def test_student():
    student = Users(
        id=2,
        username="student1",
        email="student1@example.com",
        first_name="Stu",
        last_name="Dent",
        hashed_password=bcrypt_context.hash("password"),
        role=UserRole.STUDENT,
    )
    db = TestingSessionLocal()
    db.add(student)
    db.commit()
    yield student
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM users;"))
        conn.commit()


@pytest.fixture
def test_task(test_teacher, test_student):
    task = Task(
        student_id=test_student.id,
        teacher_id=test_teacher.id,
        task="Initial Homework",
        description="Solve algebra problems",
        task_status=TaskStatus.PENDING,
    )
    db = TestingSessionLocal()
    db.add(task)
    db.commit()
    db.refresh(task)
    yield task
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM tasks;"))
        conn.commit()
