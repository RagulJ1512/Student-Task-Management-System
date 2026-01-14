
# FastAPI Project — API Documentation

**Version:** 0.1.0  
**OpenAPI:** 3.1  
**Base URL:** `/openapi.json`

---

## 🔑 Authentication

### POST `/auth/token` — Login for Access Token
Obtain an access token using username and password.

**Request Body (form‑urlencoded):**
- `grant_type` (string, must match `password`)
- `username` *(required)* — string  
- `password` *(required)* — string  
- `scope` — string (default: `""`)  
- `client_id` — string or null  
- `client_secret` — string or null  

**Response:**
```json
{
  "access_token": "string",
  "token_type": "string"
}
```

---

## 👤 User

### GET `/user/` — Get User
Returns user information.

**Response:**
```json
"string"
```

---

### POST `/user/` — Create User
Create a new user.

**Request Body (JSON):**
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
"string"
```

---

## 🎓 Student

### PATCH `/student/{task_id}` — Update Task Status
Update the status of a student’s task.

**Parameters:**
- `task_id` *(path, integer, required)*  
- `new_status` *(query, string, required)* — one of: `PENDING`, `COMPLETED`, `NOTCOMPLETED`

**Response:**
```json
"string"
```

---

### GET `/student/` — Get Task
Retrieve tasks filtered by status or teacher.

**Parameters:**
- `status_filter` *(query, string)* — `PENDING`, `COMPLETED`, `NOTCOMPLETED`  
- `teacher_id` *(query, integer)*  

**Response:**
```json
"string"
```

---

## 👨‍🏫 Teacher

### POST `/teacher/` — Create Task
Assign a new task to a student.

**Request Body (JSON):**
```json
{
  "student_id": 0,
  "task": "string",
  "description": "string"
}
```

**Response:**
```json
"string"
```

---

### GET `/teacher/` — Get Tasks
Retrieve tasks filtered by status or student.

**Parameters:**
- `status_filter` *(query, string)* — `PENDING`, `COMPLETED`, `NOTCOMPLETED`  
- `student_id` *(query, integer)*  

**Response:**
```json
"string"
```

---

### PUT `/teacher/{task_id}` — Update Task
Update an existing task.

**Parameters:**
- `task_id` *(path, integer, required)*  

**Request Body (JSON):**
```json
{
  "student_id": 0,
  "task": "string",
  "description": "string",
  "task_status": "PENDING"
}
```

**Response:**  
`204 No Content`

---

### DELETE `/teacher/{task_id}` — Delete Task
Delete a task by ID.

**Parameters:**
- `task_id` *(path, integer, required)*  

**Response:**  
`204 No Content`

---

### GET `/teacher/students` — Get Students
Retrieve all students.

**Response:**
```json
[
  {
    "id": 0,
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
  "token_type": "string"
}
```

- **ValidationError**
```json
{
  "loc": ["string", 0],
  "msg": "string",
  "type": "string"
}
```

- **TaskStatus Enum**
```
PENDING | COMPLETED | NOTCOMPLETED
```

---

## 🚀 Getting Started

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
3. Access interactive docs:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

---


