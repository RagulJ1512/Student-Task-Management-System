
# 🎨 Frontend — Student Task Management System

The **frontend** is built with **React (Vite + TypeScript)** and provides the user interface for both **students** and **teachers** to interact with the system. It consumes the FastAPI backend via REST APIs.

---

## 📂 Project Structure

```
frontend/
├── node_modules/
├── public/
├── src/
│   ├── components/
│   │   └── Navbar.tsx
│   ├── pages/
│   │   ├── LoginPage.tsx
│   │   ├── RegisterPage.tsx
│   │   ├── StudentDashboard.tsx
│   │   └── StudentsPage.tsx
│   ├── services/
│   │   └── api.ts
│   ├── styles/
│   │   └── main.css
│   ├── App.tsx
│   └── main.tsx
├── index.html
├── package.json
├── vite.config.ts
├── tsconfig.json
└── README.md
```

---

## 🚀 Features

### 👨‍🏫 Teacher UI
- Register new students
- Assign tasks
- View all students
- Filter tasks by status or student

### 🎓 Student UI
- Login with credentials
- View assigned tasks
- Update task status (`PENDING`, `COMPLETED`, `NOTCOMPLETED`)

---

## ⚙️ Tech Stack

- **React** (UI library)
- **Vite** (bundler & dev server)
- **TypeScript** (type safety)
- **Axios** (API calls)
- **CSS** (styling)

---

## 🔑 API Integration

All API calls are centralized in `src/services/api.ts`.  
The frontend communicates with the FastAPI backend endpoints:

- `/auth/token` → Login  
- `/user/` → Register students  
- `/student/` → Student task operations  
- `/teacher/` → Teacher task operations  

---

## 🧪 Testing

- Frontend testing can be done with **React Testing Library** or **Jest** (optional setup).  
- Example: test login form validation and API call responses.

---

## ⚙️ Getting Started

### 1. Install dependencies
```bash
npm install
```

### 2. Run development server
```bash
npm run dev
```
- Default URL: `http://localhost:5173`

### 3. Build for production
```bash
npm run build
```

### 4. Preview production build
```bash
npm run preview
```

---

## 📑 Example Workflow

1. Teacher registers a student via the **Register Page**.  
2. Teacher assigns a task via the **Students Page**.  
3. Student logs in via the **Login Page**.  
4. Student views tasks in the **Student Dashboard** and updates status.  
5. Teacher monitors progress via the **Students Page**.  

---

## 🎨 Styling

- Global styles in `src/styles/main.css`.  
- Component-specific styles can be added inline or via CSS modules.  

---

## 📌 Notes

- Ensure backend is running before starting frontend.  
- Update API base URL in `src/services/api.ts` if backend runs on a different port.  

---
