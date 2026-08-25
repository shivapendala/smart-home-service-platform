import React from 'react';
import { Clock, Wrench, Shield, CheckCircle, PlusCircle, Search } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

export const CustomerDashboard: React.FC = () => {
  const { user } = useAuth();

  return (
    <div style={{ padding: '2rem 3rem' }}>
      {/* Header Banner */}
      <div className="glass-panel" style={{ padding: '2rem 2.5rem', marginBottom: '2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <span className="role-badge customer" style={{ marginBottom: '0.5rem' }}>Customer Portal</span>
          <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#ffffff' }}>
            Welcome back, {user?.full_name}! 👋
          </h1>
          <p style={{ color: '#94a3b8', fontSize: '0.95rem' }}>
            Book new technician visits, track active service requests, and review service history.
          </p>
        </div>

        <button className="btn btn-primary" style={{ padding: '0.75rem 1.5rem' }}>
          <PlusCircle size={18} /> Book New Service
        </button>
      </div>

      {/* Metrics Row */}
      <div className="grid-3" style={{ marginBottom: '2rem' }}>
        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Active Bookings</span>
            <Clock size={20} color="#06b6d4" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#ffffff', marginTop: '0.5rem' }}>0</div>
          <span style={{ fontSize: '0.8rem', color: '#64748b' }}>No active bookings currently</span>
        </div>

        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Completed Services</span>
            <CheckCircle size={20} color="#10b981" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#ffffff', marginTop: '0.5rem' }}>0</div>
          <span style={{ fontSize: '0.8rem', color: '#64748b' }}>Lifetime service count</span>
        </div>

        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Account Status</span>
            <Shield size={20} color="#6366f1" />
          </div>
          <div style={{ fontSize: '1.25rem', fontWeight: 700, color: '#10b981', marginTop: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
            Verified Customer
          </div>
          <span style={{ fontSize: '0.8rem', color: '#64748b' }}>{user?.email}</span>
        </div>
      </div>

      {/* Bookings & Technicians Overview */}
      <div className="glass-panel" style={{ padding: '2rem' }}>
        <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#ffffff', marginBottom: '1rem' }}>
          Your Service Bookings
        </h3>
        
        <div style={{
          padding: '3rem 2rem',
          textAlign: 'center',
          background: 'rgba(15, 23, 42, 0.4)',
          borderRadius: '12px',
          border: '1px dashed rgba(255, 255, 255, 0.1)'
        }}>
          <Wrench size={40} color="#64748b" style={{ marginBottom: '0.75rem' }} />
          <h4 style={{ color: '#f8fafc', fontWeight: 600, fontSize: '1.1rem', marginBottom: '0.25rem' }}>No Service Bookings Yet</h4>
          <p style={{ color: '#94a3b8', fontSize: '0.9rem', marginBottom: '1.25rem' }}>
            Ready to fix household issues? Select from our catalog of certified repair technicians.
          </p>
          <button className="btn btn-outline" style={{ padding: '0.6rem 1.25rem' }}>
            <Search size={16} /> Explore Service Catalog
          </button>
        </div>
      </div>
    </div>
  );
};
