
# 🎨 Frontend — Student Task Management System

The **frontend** is built with **React (Vite + TypeScript)**. It provides the user interface for both **students** and **teachers**, consuming the FastAPI backend via REST APIs. All API calls are centralized in `src/services/api.ts`.

---

## 📂 Project Structure

```
frontend/
├── public/                    # Static assets
├── src/
│   ├── components/
│   │   └── Navbar.tsx         # Role-based navigation bar
│   ├── pages/
│   │   ├── LoginPage.tsx      # Login form, JWT decoding, role-based routing
│   │   ├── RegisterPage.tsx   # Teacher-only user registration
│   │   ├── StudentDashboard.tsx # Student-only dashboard
│   │   └── StudentsPage.tsx   # Teacher-only student management
│   ├── services/
│   │   └── api.ts             # Centralized API calls (Axios)
│   ├── styles/
│   │   └── main.css           # Global styles
│   ├── App.tsx                # Route definitions
│   └── main.tsx               # Entry point
├── index.html
├── package.json
├── vite.config.ts
├── tsconfig.json
└── README.md
```

---

## 🚀 Features

### 👨‍🏫 Teacher UI
- Register new users (students or teachers)
- View all students
- Assign tasks
- Edit and delete tasks
- Filter tasks by status or student

### 🎓 Student UI
- Login with credentials
- View assigned tasks
- Filter tasks by status
- Update task status (`PENDING`, `COMPLETED`, `NOTCOMPLETED`)

---

## ⚙️ Tech Stack

- **React (TypeScript)** — UI framework with type safety  
- **Vite** — Fast bundler & dev server  
- **Axios** — HTTP client for API calls  
- **CSS** — Styling (global + modular)  

---

## 🔑 Authentication & Routing Flow

1. **Initial Load**
   - App starts at **Login Page** (`/login`).
   - User enters credentials.
   - Backend returns JWT with role (`STUDENT` or `TEACHER`).

2. **Role-Based Routing**
   - **Student** → `/dashboard`
   - **Teacher** → `/students`

3. **Access Control**
   - **Students** can only access `/dashboard`.
   - **Teachers** can access `/students` and `/register`.
   - Unauthorized access redirects to `/login`.

---

## 📡 API Integration (`api.ts`)

Centralized API layer using Axios. JWT token is attached to requests automatically.

### Auth
- `login(username, password)` → `POST /auth/token`

### User
- `registerUser(userData)` → `POST /user/`
- `getUser()` → `GET /user/`

### Student
- `getStudentTasks(statusFilter?, teacherId?)` → `GET /student/`
- `updateTaskStatus(taskId, newStatus)` → `PATCH /student/{task_id}`

### Teacher
- `createTask(taskData)` → `POST /teacher/`
- `getTeacherTasks(statusFilter?, studentId?)` → `GET /teacher/`
- `updateTask(taskId, updates)` → `PUT /teacher/{task_id}`
- `deleteTask(taskId)` → `DELETE /teacher/{task_id}`
- `getStudents()` → `GET /teacher/students`

---

## 📊 Component Workflows

### Navbar
- Displays links based on role:
  - Student → `My Tasks`
  - Teacher → `Students`, `Add User`
- Shows username and role badge.
- Logout clears localStorage and redirects to `/login`.

### LoginPage
- Submits credentials via `login()`.
- Decodes JWT payload to extract role, id, username.
- Stores values in localStorage.
- Redirects:
  - Student → `/dashboard`
  - Teacher → `/students`

### RegisterPage (Teacher-only)
- Accessible only if `role === 'TEACHER'`.
- Teachers can register new users.
- Calls `registerUser()` API.
- Redirects back to `/students`.

### StudentDashboard
- Loads tasks via `getStudentTasks()`.
- Displays statistics (total, completed, pending, not completed).
- Allows filtering by status.
- Allows updating task status via `updateTaskStatus()`.

### StudentsPage (Teacher-only)
- Loads all students via `getStudents()`.
- Teacher selects a student → tasks load via `getTeacherTasks()`.
- Features:
  - Create new task (`createTask()`)
  - Edit task (`updateTask()`)
  - Delete task (`deleteTask()`)
  - Filter tasks by status
- UI updates optimistically after each action.

---

## 🧪 Testing

Frontend testing uses **Jest + React Testing Library**.

Run tests:
```bash
npm test
```

Test coverage includes:
- Authentication flow (login/logout)
- Protected routes (role-based access)
- API calls (mock backend responses)
- UI rendering (task lists, forms, error states)

---

## ⚙️ Getting Started

1. Install dependencies:
   ```bash
   npm install
   ```
2. Configure `.env`:
   ```
   VITE_API_BASE_URL=http://localhost:8080
   ```
3. Run dev server:
   ```bash
   npm run dev
   ```
   - Default URL: `http://localhost:5173`
4. Build for production:
   ```bash
   npm run build
   ```
5. Preview production build:
   ```bash
   npm run preview
   ```

---

## 📑 Example Workflow

### Teacher Workflow
1. Teacher logs in → redirected to `/students`.
2. Teacher views all students.
3. Teacher selects a student → tasks load.
4. Teacher can:
   - Add a new task.
   - Edit or delete tasks.
   - Filter tasks by status.
5. Teacher can register new users via `/register`.

### Student Workflow
1. Student logs in → redirected to `/dashboard`.
2. Student views assigned tasks.
3. Student filters tasks by status.
4. Student updates task status.
5. Statistics update automatically.

---

## 📌 Notes

- Teachers are the only ones allowed to register new users.  
- Students are restricted to their dashboard only.  
- Ensure backend is running before starting frontend.  
- Update `VITE_API_BASE_URL` in `.env` if backend runs on a different port.  
- Use HTTPS in production for secure JWT transmission.  
