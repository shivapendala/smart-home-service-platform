import React from 'react';
import { NavLink } from 'react-router-dom';
import { Home, Grid, LayoutDashboard, User, LogIn } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

export const MobileBottomNav: React.FC = () => {
  const { user } = useAuth();

  const getDashboardPath = () => {
    if (!user) return '/login';
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
    <nav className="mobile-bottom-nav">
      <NavLink to="/" className={({ isActive }) => `mobile-nav-item ${isActive ? 'active' : ''}`}>
        <Home size={22} />
        <span>Home</span>
      </NavLink>

      <NavLink to="/services" className={({ isActive }) => `mobile-nav-item ${isActive ? 'active' : ''}`}>
        <Grid size={22} />
        <span>Services</span>
      </NavLink>

      {user ? (
        <NavLink to={getDashboardPath()} className={({ isActive }) => `mobile-nav-item ${isActive ? 'active' : ''}`}>
          <LayoutDashboard size={22} />
          <span>Dashboard</span>
        </NavLink>
      ) : (
        <NavLink to="/login" className={({ isActive }) => `mobile-nav-item ${isActive ? 'active' : ''}`}>
          <LogIn size={22} />
          <span>Login</span>
        </NavLink>
      )}

      {user ? (
        <NavLink to={getDashboardPath()} className={({ isActive }) => `mobile-nav-item ${isActive ? 'active' : ''}`}>
          <User size={22} />
          <span>Account</span>
        </NavLink>
      ) : (
        <NavLink to="/register" className={({ isActive }) => `mobile-nav-item ${isActive ? 'active' : ''}`}>
          <User size={22} />
          <span>Sign Up</span>
        </NavLink>
      )}
    </nav>
  );
};
