import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Wrench, LogOut, Shield, Home, LayoutDashboard, Grid } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

export const Navbar: React.FC = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const getDashboardPath = () => {
    if (!user) return '/';
    switch (user.role) {
      case 'ADMIN':
        return '/admin-dashboard';
      case 'TECHNICIAN':
        return '/technician-dashboard';
      case 'CUSTOMER':
      default:
        return '/customer-dashboard';
    }
  };

  return (
    <nav className="navbar">
      <Link to="/" className="nav-brand">
        <div style={{
          background: 'rgba(239, 68, 68, 0.1)',
          border: '1px solid rgba(239, 68, 68, 0.2)',
          padding: '0.45rem',
          borderRadius: '10px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center'
        }}>
          <Wrench size={22} color="#ef4444" />
        </div>
        <span>Smart<span className="brand-badge">Home</span></span>
      </Link>

      <ul className="nav-links">
        <li>
          <Link to="/" className="nav-item" style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
            <Home size={18} /> Home
          </Link>
        </li>
        <li>
          <Link to="/services" className="nav-item" style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
            <Grid size={18} /> Services Catalog
          </Link>
        </li>

        {user ? (
          <>
            <li>
              <Link to={getDashboardPath()} className="nav-item" style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
                <LayoutDashboard size={18} /> Dashboard
              </Link>
            </li>
            <li style={{ display: 'flex', alignItems: 'center', gap: '0.85rem' }}>
              <span className={`role-badge ${user.role.toLowerCase()}`}>
                {user.role === 'ADMIN' && <Shield size={12} />}
                {user.role}
              </span>
              <span style={{ fontWeight: 600, fontSize: '0.9rem', color: '#0f172a' }}>
                {user.full_name}
              </span>
              <button 
                onClick={handleLogout} 
                className="btn btn-secondary" 
                style={{ padding: '0.45rem 0.9rem', fontSize: '0.85rem' }}
              >
                <LogOut size={14} /> Logout
              </button>
            </li>
          </>
        ) : (
          <>
            <li>
              <Link to="/login" className="nav-item">Login</Link>
            </li>
            <li>
              <Link to="/register" className="btn btn-primary" style={{ padding: '0.55rem 1.35rem', fontSize: '0.9rem' }}>
                Get Started
              </Link>
            </li>
          </>
        )}
      </ul>
    </nav>
  );
};
