import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

const api = axios.create({
  baseURL: API_BASE_URL,
});


api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = 'Bearer ' + token;
  }
  return config;
});

export const login = (username: string, password: string) =>
  api.post('/auth/token', new URLSearchParams({ username, password }), {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  });

export const registerUser = (userData: any) => api.post('/user/', userData);

export const getStudentTasks = (statusFilter?: string, teacherId?: number) => {
  const params = new URLSearchParams();
  if (statusFilter) params.append('status_filter', statusFilter);
  if (teacherId) params.append('teacher_id', teacherId.toString());
  return api.get('/student/?' + params.toString());
};

export const updateTaskStatus = (taskId: number, newStatus: string) =>
  api.patch(`/student/${taskId}?new_status=${newStatus}`);

export const createTask = (taskData: any) => api.post('/teacher/', taskData);

export const getTeacherTasks = (statusFilter?: string, studentId?: number) => {
  const params = new URLSearchParams();
  if (statusFilter) params.append('status_filter', statusFilter);
  if (studentId) params.append('student_id', studentId.toString());
  return api.get('/teacher/?' + params.toString());
};

export const updateTask = (taskId: number, updates: any) => api.put('/teacher/' + taskId, updates);

export const deleteTask = (taskId: number) => api.delete('/teacher/' + taskId);

export const getStudents = () => api.get('/teacher/students');

export default api;
