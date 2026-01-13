from fastapi import FastAPI

from routers import student, teacher, user
import models
from database import engine


from routers import auth
app=FastAPI()


models.Base.metadata.create_all(bind=engine)



app.include_router(auth.router)
app.include_router(user.router)
app.include_router(student.router)
app.include_router(teacher.router)