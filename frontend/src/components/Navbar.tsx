import { useNavigate, useLocation } from 'react-router-dom';

export function Navbar() {
  const navigate = useNavigate();
  const location = useLocation();
  const role = localStorage.getItem('role');
  const username = localStorage.getItem('username');
  const token = localStorage.getItem('token');

  if (!token) {
    return null;
  }

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('role');
    localStorage.removeItem('userId');
    localStorage.removeItem('username');
    navigate('/login');
  };

  const isActive = (path: string) => location.pathname === path ? 'active' : '';

  return (
    <nav className="navbar">
      <div className="navbar-left">
        <h1 className="brand">📚 Task Manager</h1>
      </div>
      <div className="navbar-center">
        {role === 'STUDENT' && (
          <a href="/dashboard" className={`nav-link ${isActive('/dashboard')}`}>
            My Tasks
          </a>
        )}
        {role === 'TEACHER' && (
          <>
            <a href="/students" className={`nav-link ${isActive('/students')}`}>
              Students
            </a>
            <a href="/register" className={`nav-link ${isActive('/register')}`}>
              Add User
            </a>
          </>
        )}
      </div>
      <div className="navbar-right">
        <span className="user-info">
          {username} <span className="role-badge">{role}</span>
        </span>
        <button className="logout-btn" onClick={handleLogout}>
          Logout
        </button>
      </div>
    </nav>
  );
}
