from database import Base
from sqlalchemy import Column, Integer, String, Enum as SqlEnum
from sqlalchemy import ForeignKey 
from sqlalchemy.orm import relationship
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
    student_id=Column(Integer,ForeignKey("users.id"))
    teacher_id=Column(Integer,ForeignKey("users.id"))
    task=Column(String)
    description=Column(String)
    task_status=Column(SqlEnum(TaskStatus), default=TaskStatus.PENDING)

    student = relationship("Users", foreign_keys=[student_id]) 
    teacher = relationship("Users", foreign_keys=[teacher_id])