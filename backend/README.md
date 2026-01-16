
# ⚡ Backend — Student Task Management System

The **backend** is built with **FastAPI** and provides REST APIs for managing students, teachers, and tasks. It implements **JWT authentication**, **role‑based access control**, and **CRUD operations** with a relational database.

---

## 📂 Project Structure

```
backend/
├── .venv/                 # Virtual environment
├── .env                   # Environment variables (DB URL, secrets)
├── studentapp.db          # SQLite database (development)
├── testdb.db              # SQLite database (testing)
│
├── routers/               # API route handlers
│   ├── auth.py            # Authentication endpoints
│   ├── student.py         # Student endpoints
│   ├── teacher.py         # Teacher endpoints
│   └── user.py            # User endpoints
│
├── tests/                 # Pytest test cases
│   ├── test_auth.py
│   ├── test_student.py
│   ├── test_teacher.py
│   └── test_user.py
│
├── utils.py               # Utility functions (JWT helpers, etc.)
├── database.py            # Database connection setup
├── main.py                # FastAPI entry point
├── models.py              # SQLAlchemy models
├── schemas.py             # Pydantic schemas
├── requirements.txt       # Python dependencies
└── README.md              # Backend documentation
```

---

## ⚙️ Environment Setup

### `.env` File
```env
DATABASE_URL=sqlite:///./studentapp.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🔑 Authentication

### `POST /auth/token` — Login for Access Token
Obtain a JWT access token using username and password.

**Request Body (form‑urlencoded):**
```json
{
  "grant_type": "password",
  "username": "string",
  "password": "string",
  "scope": "",
  "client_id": null,
  "client_secret": null
}
```

**Response:**
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

---

## 👤 User Endpoints

### `GET /user/` — Get User
Retrieve current user info.  
**Security:** JWT required  

**Response:**
```json
{
  "username": "string",
  "email": "string",
  "first_name": "string",
  "last_name": "string",
  "role": "string"
}
```

---

### `POST /user/` — Create User
Create a new user (teacher or student).  
**Security:** JWT required  

**Request Body:**
```json
{
  "username": "string",
  "email": "string",
  "first_name": "string",
  "last_name": "string",
  "password": "string",
  "role": "string"
}
```

**Response:**
```json
{
  "id": 1,
  "username": "string",
  "email": "string",
  "first_name": "string",
  "last_name": "string"
}
```

---

## 🎓 Student Endpoints

### `PATCH /student/{task_id}` — Update Task Status
Update the status of a student’s task.  
**Security:** JWT required  

**Parameters:**
- `task_id` *(path, integer, required)*  
- `new_status` *(query, enum: `PENDING`, `COMPLETED`, `NOTCOMPLETED`)*  

**Response:**
```json
{
  "task_id": 1,
  "new_status": "COMPLETED"
}
```

---

### `GET /student/` — Get Task
Retrieve tasks filtered by status or teacher.  
**Security:** JWT required  

**Parameters:**
- `status_filter` *(query, enum: `PENDING`, `COMPLETED`, `NOTCOMPLETED`)*  
- `teacher_id` *(query, integer)*  

**Response:**
```json
[
  {
    "task_id": 1,
    "task": "string",
    "description": "string",
    "status": "PENDING",
    "teacher_id": 2
  }
]
```

---

## 👨‍🏫 Teacher Endpoints

### `POST /teacher/` — Create Task
Assign a new task to a student.  
**Security:** JWT required  

**Request Body:**
```json
{
  "student_id": 1,
  "task": "string",
  "description": "string"
}
```

**Response:**
```json
{
  "task_id": 1,
  "student_id": 1,
  "task": "string",
  "description": "string",
  "status": "PENDING"
}
```

---

### `GET /teacher/` — Get Tasks
Retrieve tasks filtered by status or student.  
**Security:** JWT required  

**Parameters:**
- `status_filter` *(query, enum: `PENDING`, `COMPLETED`, `NOTCOMPLETED`)*  
- `student_id` *(query, integer)*  

**Response:**
```json
[
  {
    "task_id": 1,
    "student_id": 1,
    "task": "string",
    "description": "string",
    "status": "PENDING"
  }
]
```

---

### `PUT /teacher/{task_id}` — Update Task
Update an existing task.  
**Security:** JWT required  

**Parameters:**
- `task_id` *(path, integer, required)*  

**Request Body:**
```json
{
  "student_id": 1,
  "task": "string",
  "description": "string",
  "task_status": "COMPLETED"
}
```

**Response:**  
`204 No Content`

---

### `DELETE /teacher/{task_id}` — Delete Task
Delete a task by ID.  
**Security:** JWT required  

**Parameters:**
- `task_id` *(path, integer, required)*  

**Response:**  
`204 No Content`

---

### `GET /teacher/students` — Get Students
Retrieve all students.  
**Security:** JWT required  

**Response:**
```json
[
  {
    "id": 1,
    "username": "string",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string"
  }
]
```

---

## 📑 Common Schemas

- **Token**
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

- **CreateUserRequest**
```json
{
  "username": "string",
  "email": "string",
  "first_name": "string",
  "last_name": "string",
  "password": "string",
  "role": "string"
}
```

- **TaskStatus Enum**
```
PENDING | COMPLETED | NOTCOMPLETED
```

- **ValidationError**
```json
{
  "loc": ["string", 0],
  "msg": "string",
  "type": "string"
}
```

---

## 🧪 Testing

The backend uses **pytest** for automated testing.

Run tests:
```bash
pytest
```

Tests include:
- **Authentication** (`test_auth.py`)  
- **Student endpoints** (`test_student.py`)  
- **Teacher endpoints** (`test_teacher.py`)  
- **User endpoints** (`test_user.py`)  

---

## 🚀 Getting Started

1. Create virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure `.env` file (see above).

4. Run the server:
   ```bash
   uvicorn main:app --reload --port 8080
   ```

5. Access API docs:
   - Swagger UI → `http://localhost:8080/docs`  
   - ReDoc → `http://localhost:8080/redoc`  

