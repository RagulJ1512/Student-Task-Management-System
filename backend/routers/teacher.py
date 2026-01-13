from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import Task, TaskStatus, UserRole, Users
from routers.auth import get_current_user
from schemas import StudentResponse, TaskCreate, TaskUpdate
from database import get_db
router = APIRouter(
    prefix='/teacher',
    tags=['teacher']
)




db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

# add task
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(user:user_dependency,db:db_dependency,task_request:TaskCreate):
    if user.get("user_role") != UserRole.TEACHER: 
        raise HTTPException(status_code=403, detail="Only teachers can perform this operation")

    student = db.query(Users).filter(Users.id == task_request.student_id, Users.role == UserRole.STUDENT).first() 
    if not student: 
        raise HTTPException(status_code=404, detail="Student not found") 
    new_task = Task( 
        student_id=task_request.student_id, 
        teacher_id=user["id"], 
        task=task_request.task, 
        description=task_request.description, 
        task_status=TaskStatus.PENDING ) 
    db.add(new_task) 
    db.commit() 
    db.refresh(new_task) 
    return new_task

# update task
@router.put("/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_task(task_id:int,db:db_dependency,user:user_dependency,task_update:TaskUpdate):

    if user.get("user_role") != UserRole.TEACHER: 
        raise HTTPException(status_code=403, detail="Only teachers can perform this operation")
    task = db.query(Task).filter(Task.id == task_id, Task.teacher_id == user["id"]).first() 
    if task_update.student_id is not None: 
        student = db.query(Users).filter( Users.id == task_update.student_id, Users.role == UserRole.STUDENT ).first() 
        if not student: 
            raise HTTPException(status_code=404, detail="Student not found") 
        task.student_id = task_update.student_id 

    if task_update.task is not None: 
        task.task = task_update.task 
    if task_update.description is not None: 
        task.description = task_update.description 
    if task_update.task_status is not None: 
        task.task_status = task_update.task_status 
    db.commit() 
    db.refresh(task) 
    return task

# delete task
@router.delete("/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id:int,db:db_dependency,user:user_dependency):
    if user.get("user_role") != UserRole.TEACHER: 
        raise HTTPException(status_code=403, detail="Only teachers can perform this operation")
    task = db.query(Task).filter(Task.id == task_id, Task.teacher_id == user["id"]).first() 
    if not task: 
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()


# get task advanced filtering
@router.get("/", status_code=status.HTTP_200_OK)
async def get_tasks(user:user_dependency,db:db_dependency,status_filter:Optional[TaskStatus]=None,student_id:Optional[int]=None):
    if user.get("user_role") != UserRole.TEACHER: 
        raise HTTPException(status_code=403, detail="Only teachers can perform this operation")
    query = db.query(Task).filter(Task.teacher_id==user["id"])
    if status_filter:
        query.filter(Task.task_status==status_filter)
    if student_id:
        query = db.query(Users).filter(Users.id == student_id, Users.role == UserRole.STUDENT).first() 
    return query.all()


#get student
@router.get('/students',response_model=List[StudentResponse],status_code=status.HTTP_200_OK)
async def get_students(db:db_dependency,user:user_dependency):
    if user.get("user_role") != UserRole.TEACHER: 
        raise HTTPException(status_code=403, detail="Only teachers can perform this operation")
    return db.query(Users).filter(Users.role==UserRole.STUDENT).all()