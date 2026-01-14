from database import Base
from sqlalchemy import Column, Integer, String, Enum as SqlEnum

from schemas import TaskStatus, UserRole

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    role = Column(SqlEnum(UserRole),default=UserRole.STUDENT)

class Task(Base):
    __tablename__ = 'tasks'
    id=Column(Integer, primary_key=True, index=True)
    student_id=Column(Integer)
    teacher_id=Column(Integer)
    task=Column(String)
    description=Column(String)
    task_status=Column(SqlEnum(TaskStatus), default=TaskStatus.PENDING)