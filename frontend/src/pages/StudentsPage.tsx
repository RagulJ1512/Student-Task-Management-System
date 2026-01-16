import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getStudents, getTeacherTasks, updateTask, deleteTask, createTask } from '../services/api';

export function StudentsPage() {
  const [students, setStudents] = useState<any[]>([]);
  const [tasks, setTasks] = useState<any[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');
  const [selectedStudent, setSelectedStudent] = useState<any>(null);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [editForm, setEditForm] = useState<any>({});
  const [updating, setUpdating] = useState<number | null>(null);
  const [statusFilter, setStatusFilter] = useState<string>('');
  const [showCreateForm, setShowCreateForm] = useState<boolean>(false);
  const [newTask, setNewTask] = useState<any>({
    task: '',
    description: '',
  });
  const [creating, setCreating] = useState<boolean>(false);
  const navigate = useNavigate();
  const token = localStorage.getItem('token');
  const role = localStorage.getItem('role');

  if (!token || role !== 'TEACHER') {
    navigate('/login');
    return null;
  }

  useEffect(() => {
    loadStudents();
  }, []);

  const loadStudents = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await getStudents();
      setStudents(response.data);
      setSelectedStudent(null);
      setTasks([]);
    } catch (err) {
      setError('Failed to load students');
    } finally {
      setLoading(false);
    }
  };

  const handleSelectStudent = async (student: any) => {
    setSelectedStudent(student);
    setEditingId(null);
    setShowCreateForm(false);
    setStatusFilter('');
    setLoading(true);
    try {
      const response = await getTeacherTasks(undefined, student.id);
      setTasks(response.data);
    } catch (err) {
      setError('Failed to load student tasks');
    } finally {
      setLoading(false);
    }
  };

  const handleEditStart = (task: any) => {
    setEditingId(task.id);
    setEditForm({
      task: task.task,
      description: task.description || '',
      task_status: task.task_status,
    });
  };

  const handleSaveEdit = async () => {
    setUpdating(editingId);
    try {
      await updateTask(editingId as number, editForm);
      const updated = tasks.map((t) =>
        t.id === editingId ? { ...t, ...editForm } : t
      );
      setTasks(updated);
      setEditingId(null);
      setEditForm({});
    } catch (err: any) {
      setError('Failed to update task');
    } finally {
      setUpdating(null);
    }
  };

  const handleDelete = async (taskId: number) => {
    if (!window.confirm('Delete this task?')) return;
    setUpdating(taskId);
    try {
      await deleteTask(taskId);
      setTasks(tasks.filter((t) => t.id !== taskId));
    } catch (err: any) {
      setError('Failed to delete task');
    } finally {
      setUpdating(null);
    }
  };

  const handleCreateTask = async () => {
    if (!newTask.task.trim()) {
      setError('Task name is required');
      return;
    }
    setCreating(true);
    setError('');
    try {
      await createTask({
        student_id: selectedStudent.id,
        task: newTask.task,
        description: newTask.description || null,
      });
      setNewTask({ task: '', description: '' });
      setShowCreateForm(false);
      await handleSelectStudent(selectedStudent);
    } catch (err: any) {
      setError('Failed to create task');
    } finally {
      setCreating(false);
    }
  };

  const filteredTasks = statusFilter
    ? tasks.filter((t) => t.task_status === statusFilter)
    : tasks;

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'COMPLETED':
        return '#4caf50';
      case 'PENDING':
        return '#ff9800';
      case 'NOTCOMPLETED':
        return '#f44336';
      default:
        return '#999';
    }
  };

  return (
    <div className="container">
      <div className="page-header">
        <h1>Students</h1>
      </div>

      {error && <div className="error-msg">{error}</div>}
      {/* student list */}
      <div className="students-layout">
        <div className="students-list">
          <h3>All Students</h3>
          {students.length === 0 ? (
            <div className="no-data">No students found</div>
          ) : (
            <div className="student-items">
              {students.map((student) => (
                <div
                  key={student.id}
                  className={`student-item ${selectedStudent?.id === student.id ? 'active' : ''}`}
                  onClick={() => handleSelectStudent(student)}
                >
                  <div className="student-name">
                    {student.first_name} {student.last_name}
                  </div>
                  <div className="student-username">{student.username}</div>
                  <div className="student-email">{student.email}</div>
                </div>
              ))}
            </div>
          )}
        </div>
          {/* task name */}
        <div className="tasks-panel">
          {selectedStudent ? (
            <>
              <div className="panel-header">
                <h2>
                  Tasks for {selectedStudent.first_name} {selectedStudent.last_name}
                </h2>
                <button 
                  className="btn-add" 
                  onClick={() => setShowCreateForm(!showCreateForm)}
                >
                  {showCreateForm ? 'Cancel' : '+ Add Task'}
                </button>
              </div>

              {showCreateForm && (
                <div className="create-form">
                  <div className="form-group">
                    <label>Task Name</label>
                    <input
                      type="text"
                      value={newTask.task}
                      onChange={(e) => setNewTask({ ...newTask, task: e.target.value })}
                      placeholder="Enter task name"
                      disabled={creating}
                    />
                  </div>
                  <div className="form-group">
                    <label>Description</label>
                    <textarea
                      value={newTask.description}
                      onChange={(e) => setNewTask({ ...newTask, description: e.target.value })}
                      placeholder="Enter task description (optional)"
                      rows={3}
                      disabled={creating}
                    />
                  </div>
                  <div className="form-actions">
                    <button 
                      className="btn-save" 
                      onClick={handleCreateTask}
                      disabled={creating}
                    >
                      {creating ? 'Creating...' : 'Create Task'}
                    </button>
                    <button 
                      className="btn-cancel" 
                      onClick={() => setShowCreateForm(false)}
                      disabled={creating}
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              )}

              {tasks.length > 0 && (
                <div className="filter-section">
                  <label>Filter by Status:</label>
                  <select 
                    value={statusFilter} 
                    onChange={(e) => setStatusFilter(e.target.value)}
                    className="status-filter"
                  >
                    <option value="">All Tasks</option>
                    <option value="PENDING">Pending</option>
                    <option value="COMPLETED">Completed</option>
                    <option value="NOTCOMPLETED">Not Completed</option>
                  </select>
                </div>
              )}

              {loading ? (
                <div className="no-data">Loading...</div>
              ) : filteredTasks.length === 0 ? (
                <div className="no-data">
                  {tasks.length === 0 ? 'No tasks assigned' : 'No tasks with this status'}
                </div>
              ) : (

                // listing tasks
                <div className="tasks-table">
                  <table>
                    <thead>
                      <tr>
                        <th>Task</th>
                        <th>Description</th>
                        <th>Status</th>
                        <th>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {filteredTasks.map((task) => (
                        <tr key={task.id}>
                          {editingId === task.id ? (
                            <>
                              <td>
                                <input
                                  type="text"
                                  value={editForm.task}
                                  onChange={(e) => setEditForm({ ...editForm, task: e.target.value })}
                                  className="edit-input"
                                />
                              </td>
                              <td>
                                <textarea
                                  value={editForm.description}
                                  onChange={(e) => setEditForm({ ...editForm, description: e.target.value })}
                                  className="edit-input"
                                  rows={2}
                                />
                              </td>
                              <td>
                                <select
                                  value={editForm.task_status}
                                  onChange={(e) => setEditForm({ ...editForm, task_status: e.target.value })}
                                  className="status-select"
                                >
                                  <option value="PENDING">Pending</option>
                                  <option value="COMPLETED">Completed</option>
                                  <option value="NOTCOMPLETED">Not Completed</option>
                                </select>
                              </td>
                              <td>
                                <div className="action-btns">
                                  <button className="btn-small btn-save" onClick={handleSaveEdit} disabled={updating === task.id}>
                                    Save
                                  </button>
                                  <button className="btn-small btn-cancel" onClick={() => setEditingId(null)}>
                                    Cancel
                                  </button>
                                </div>
                              </td>
                            </>
                          ) : (
                            <>
                              <td>{task.task}</td>
                              <td>{task.description || '-'}</td>
                              <td>
                                <span
                                  className="status-badge"
                                  style={{ backgroundColor: getStatusColor(task.task_status) }}
                                >
                                  {task.task_status}
                                </span>
                              </td>
                              <td>
                                <div className="action-btns">
                                  <button className="btn-small btn-edit" onClick={() => handleEditStart(task)}>
                                    Edit
                                  </button>
                                  <button className="btn-small btn-delete" onClick={() => handleDelete(task.id)} disabled={updating === task.id}>
                                    Delete
                                  </button>
                                </div>
                              </td>
                            </>
                          )}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </>
          ) : (
            <div className="no-data">Select a student to view tasks</div>
          )}
        </div>
      </div>
    </div>
  );
}
