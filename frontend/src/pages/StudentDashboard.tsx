import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getStudentTasks, updateTaskStatus } from '../services/api';

export function StudentDashboard() {
  const [tasks, setTasks] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [statusFilter, setStatusFilter] = useState('');
  const [selectedStatus, setSelectedStatus] = useState<{ [key: number]: string }>({});
  const [updating, setUpdating] = useState<number | null>(null);
  const navigate = useNavigate();
  const token = localStorage.getItem('token');
  const role = localStorage.getItem('role');

  if (!token || role !== 'STUDENT') {
    navigate('/login');
    return null;
  }

  useEffect(() => {
    loadTasks();
  }, []);

  const loadTasks = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await getStudentTasks();
      setTasks(response.data);
    } catch (err: any) {
      setError('Failed to load tasks');
    } finally {
      setLoading(false);
    }
  };

  const handleStatusChange = async (taskId: number, newStatus: string) => {
    setUpdating(taskId);
    try {
      await updateTaskStatus(taskId, newStatus);
      const updated = tasks.map((t) =>
        t.id === taskId ? { ...t, task_status: newStatus } : t
      );
      setTasks(updated);
      setSelectedStatus({ ...selectedStatus, [taskId]: '' });
    } catch (err: any) {
      setError('Failed to update task');
    } finally {
      setUpdating(null);
    }
  };

  const getFiltered = () => {
    if (!statusFilter) return tasks;
    return tasks.filter((t) => t.task_status === statusFilter);
  };

  const stats = {
    total: tasks.length,
    completed: tasks.filter((t) => t.task_status === 'COMPLETED').length,
    pending: tasks.filter((t) => t.task_status === 'PENDING').length,
    notCompleted: tasks.filter((t) => t.task_status === 'NOTCOMPLETED').length,
  };

  const filteredTasks = getFiltered();

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
        <h1>My Tasks</h1>
        <button className="btn-refresh" onClick={loadTasks} disabled={loading}>
          {loading ? 'Loading...' : 'Refresh'}
        </button>
      </div>

      {error && <div className="error-msg">{error}</div>}

      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-number">{stats.total}</div>
          <div className="stat-label">Total Tasks</div>
        </div>
        <div className="stat-card completed">
          <div className="stat-number">{stats.completed}</div>
          <div className="stat-label">Completed</div>
        </div>
        <div className="stat-card pending">
          <div className="stat-number">{stats.pending}</div>
          <div className="stat-label">Pending</div>
        </div>
        <div className="stat-card notcompleted">
          <div className="stat-number">{stats.notCompleted}</div>
          <div className="stat-label">Not Completed</div>
        </div>
      </div>

      <div className="filter-section">
        <label>Filter by Status:</label>
        <select value={statusFilter} onChange={(e) => setStatusFilter(e.target.value)}>
          <option value="">All Tasks</option>
          <option value="PENDING">Pending</option>
          <option value="COMPLETED">Completed</option>
          <option value="NOTCOMPLETED">Not Completed</option>
        </select>
      </div>

      {filteredTasks.length === 0 ? (
        <div className="no-data">No tasks found</div>
      ) : (
        <div className="tasks-table">
          <table>
            <thead>
              <tr>
                <th>Task</th>
                <th>Description</th>
                <th>From Teacher</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {filteredTasks.map((task) => (
                <tr key={task.id}>
                  <td>{task.task}</td>
                  <td>{task.description || '-'}</td>
                  <td>{task.teacher_name}</td>
                  <td>
                    <span
                      className="status-badge"
                      style={{ backgroundColor: getStatusColor(task.task_status) }}
                    >
                      {task.task_status}
                    </span>
                  </td>
                  <td>
                    <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                      <select
                        value={selectedStatus[task.id] || task.task_status}
                        onChange={(e) => setSelectedStatus({ ...selectedStatus, [task.id]: e.target.value })}
                        className="status-select"
                      >
                        <option value="PENDING">Pending</option>
                        <option value="COMPLETED">Completed</option>
                        <option value="NOTCOMPLETED">Not Completed</option>
                      </select>
                      <button
                        className="btn-small btn-save"
                        onClick={() => handleStatusChange(task.id, selectedStatus[task.id] || task.task_status)}
                        disabled={updating === task.id}
                      >
                        Update
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
