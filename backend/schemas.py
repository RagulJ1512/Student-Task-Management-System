import enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserRole(enum.Enum):
    TEACHER="TEACHER"
    STUDENT="STUDENT"

class TaskStatus(enum.Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    NOTCOMPLETED = "NOTCOMPLETED"

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)

class TaskResponse(BaseModel):
    id: int 
    student_id: int 
    teacher_id: int 
    task: str 
    description: Optional[str] 
    task_status: TaskStatus

class TaskCreate(BaseModel): 
    student_id: int 
    task: str 
    description: Optional[str] = None

class TaskUpdate(BaseModel): 
    student_id: Optional[int]=None
    task: Optional[str] = None 
    description: Optional[str] = None 
    task_status: Optional[TaskStatus] = None

class StudentResponse(BaseModel): 
    id: int 
    username: str 
    email: EmailStr 
    first_name: str 
    last_name: str