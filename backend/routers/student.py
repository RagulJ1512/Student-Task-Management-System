from typing import Annotated, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from database import get_db
from database import SessionLocal
from models import Task, TaskStatus, UserRole, Users
from routers.auth import get_current_user

router = APIRouter(
    prefix='/student',
    tags=['student']
)


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

# update status
@router.patch("/{task_id}",status_code=status.HTTP_202_ACCEPTED)
async def update_task_status(task_id:int,user:user_dependency,db:db_dependency,new_status:TaskStatus):
    if user.get("user_role") != UserRole.STUDENT: 
        raise HTTPException(status_code=403, detail="Only students can perform this operation")
    task = db.query(Task).filter(Task.id == task_id, Task.student_id == user["id"]).first() 
    if not task: 
        raise HTTPException(status_code=404, detail="Task not found or not assigned to you")
    task.task_status = new_status 
    db.commit() 
    db.refresh(task) 
    return task

# get filter
@router.get("/", status_code=status.HTTP_200_OK)
async def get_task(
    user: user_dependency,
    db: db_dependency,
    status_filter: Optional[TaskStatus] = None,
    teacher_id: Optional[int] = None
):
    if user.get("user_role") != UserRole.STUDENT:
        raise HTTPException(status_code=403, detail="Only students can perform this operation")

    query = (
        db.query(Task, Users.first_name, Users.last_name)
        .join(Users, Task.teacher_id == Users.id)
        .filter(Task.student_id == user["id"])
    )

    if status_filter:
        query = query.filter(Task.task_status == status_filter)
    if teacher_id:
        query = query.filter(Task.teacher_id == teacher_id)

    results = query.all()

    return [
        {
            "id": task.id,
            "task": task.task,
            "description": task.description,
            "task_status": task.task_status,
            "teacher_id": task.teacher_id,
            "teacher_name": f"{fname} {lname}"
        }
        for task, fname, lname in results
    ]

