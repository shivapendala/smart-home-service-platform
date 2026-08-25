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
          background: 'linear-gradient(135deg, #6366f1, #06b6d4)',
          padding: '0.4rem',
          borderRadius: '10px',
          display: 'flex',
          alignItems: 'center'
        }}>
          <Wrench size={22} color="#ffffff" />
        </div>
        <span>Smart<span className="brand-badge">Home</span></span>
      </Link>

      <ul className="nav-links">
        <li>
          <Link to="/" className="nav-item" style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
            <Home size={18} /> Home
          </Link>
        </li>
        <li>
          <Link to="/services" className="nav-item" style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
            <Grid size={18} /> Services Catalog
          </Link>
        </li>

        {user ? (
          <>
            <li>
              <Link to={getDashboardPath()} className="nav-item" style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
                <LayoutDashboard size={18} /> Dashboard
              </Link>
            </li>
            <li style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
              <span className={`role-badge ${user.role.toLowerCase()}`}>
                {user.role === 'ADMIN' && <Shield size={12} />}
                {user.role}
              </span>
              <span style={{ fontWeight: 600, fontSize: '0.9rem', color: '#f8fafc' }}>
                {user.full_name}
              </span>
              <button 
                onClick={handleLogout} 
                className="btn btn-secondary" 
                style={{ padding: '0.4rem 0.85rem', fontSize: '0.85rem' }}
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
              <Link to="/register" className="btn btn-primary" style={{ padding: '0.5rem 1.25rem' }}>
                Get Started
              </Link>
            </li>
          </>
        )}
      </ul>
    </nav>
  );
};
