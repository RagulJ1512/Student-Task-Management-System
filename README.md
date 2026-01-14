# 📚 Student Task Management System

## 📝 Problem Statement
The Student Task Management System is designed to streamline communication between teachers and students.  
Teachers can add students and assign tasks, while students can log in and update their task progress as **Completed**, **Pending**, or **Not Completed**.  
Teachers can then view and filter students based on task status to track progress efficiently.

---

## ⚙️ Functionality & Workflow

### 👨‍🏫 Teacher Features
- **Add Students**: Register new students with basic details (username, email, name).
- **Assign Tasks**: Create tasks for specific students, including description and status.
- **Manage Tasks**:
  - Update existing tasks (edit description, change status).
  - Delete tasks when no longer needed.
- **View Tasks**:
  - Retrieve all tasks.
  - Filter tasks by status (`PENDING`, `COMPLETED`, `NOTCOMPLETED`) or by student.
- **View Students**: Get a list of all registered students.

### 🎓 Student Features
- **Login & Authentication**:
  - Students log in using their credentials to receive an access token.
- **View Tasks**:
  - Retrieve assigned tasks.
  - Filter tasks by status or teacher.
- **Update Task Status**:
  - Mark tasks as `COMPLETED`, `PENDING`, or `NOTCOMPLETED`.

### 🔑 Authentication
- Secure login via `/auth/token` endpoint.
- Access token required for protected routes.

---

## 🔄 System Workflow

1. **Teacher registers students** → `/user/`  
2. **Teacher assigns tasks** → `/teacher/`  
3. **Student logs in** → `/auth/token`  
4. **Student views tasks** → `/student/`  
5. **Student updates task status** → `/student/{task_id}`  
6. **Teacher monitors progress** → `/teacher/` (with filters)  
7. **Teacher manages tasks** → update or delete via `/teacher/{task_id}`  

---

## 📑 Example Use Case
- A teacher creates a student profile and assigns a math homework task.  
- The student logs in, sees the task, and marks it as **Completed** once finished.  
- The teacher filters tasks by status to quickly see which students have completed their work.  

---

## 🚀 Tech Stack
- **Backend**: FastAPI  
- **API Spec**: OpenAPI 3.1  
- **Authentication**: OAuth2 with password grant  
- **Database**: (to be specified, e.g., PostgreSQL, SQLite)  

---
