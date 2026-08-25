import React, { useState } from 'react';
import { Briefcase, Clock, Star, CheckCircle2, ToggleLeft, ToggleRight } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

export const TechnicianDashboard: React.FC = () => {
  const { user } = useAuth();
  const [isAvailable, setIsAvailable] = useState(true);

  return (
    <div style={{ padding: '2rem 3rem' }}>
      {/* Technician Banner */}
      <div className="glass-panel" style={{ padding: '2rem 2.5rem', marginBottom: '2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <span className="role-badge technician" style={{ marginBottom: '0.5rem' }}>Technician Portal</span>
          <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#ffffff' }}>
            Welcome, {user?.full_name}! 🛠️
          </h1>
          <p style={{ color: '#94a3b8', fontSize: '0.95rem' }}>
            Specialization: <strong style={{ color: '#06b6d4' }}>{user?.specialization || 'General Technician'}</strong> ({user?.experience_years || 0} Yrs Experience)
          </p>
        </div>

        <button 
          onClick={() => setIsAvailable(!isAvailable)}
          className={`btn ${isAvailable ? 'btn-primary' : 'btn-secondary'}`}
          style={{ padding: '0.75rem 1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}
        >
          {isAvailable ? <ToggleRight size={22} color="#10b981" /> : <ToggleLeft size={22} color="#94a3b8" />}
          <span>Status: <strong>{isAvailable ? 'Available for Jobs' : 'Offline'}</strong></span>
        </button>
      </div>

      {/* Metrics Row */}
      <div className="grid-3" style={{ marginBottom: '2rem' }}>
        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Assigned Jobs</span>
            <Briefcase size={20} color="#6366f1" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#ffffff', marginTop: '0.5rem' }}>0</div>
          <span style={{ fontSize: '0.8rem', color: '#64748b' }}>Jobs awaiting your response</span>
        </div>

        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Completed Jobs</span>
            <CheckCircle2 size={20} color="#10b981" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#ffffff', marginTop: '0.5rem' }}>0</div>
          <span style={{ fontSize: '0.8rem', color: '#64748b' }}>Total jobs completed</span>
        </div>

        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Performance Rating</span>
            <Star size={20} color="#f59e0b" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#f59e0b', marginTop: '0.5rem' }}>
            {user?.rating || '5.0'} ★
          </div>
          <span style={{ fontSize: '0.8rem', color: '#64748b' }}>Based on customer reviews</span>
        </div>
      </div>

      {/* Jobs Queue */}
      <div className="glass-panel" style={{ padding: '2rem' }}>
        <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#ffffff', marginBottom: '1rem' }}>
          Job Dispatch Queue
        </h3>
        
        <div style={{
          padding: '3rem 2rem',
          textAlign: 'center',
          background: 'rgba(15, 23, 42, 0.4)',
          borderRadius: '12px',
          border: '1px dashed rgba(255, 255, 255, 0.1)'
        }}>
          <Clock size={40} color="#64748b" style={{ marginBottom: '0.75rem' }} />
          <h4 style={{ color: '#f8fafc', fontWeight: 600, fontSize: '1.1rem', marginBottom: '0.25rem' }}>No New Dispatch Requests</h4>
          <p style={{ color: '#94a3b8', fontSize: '0.9rem' }}>
            When customers book services matching your specialization ({user?.specialization || 'Technician'}), job orders will appear here.
          </p>
        </div>
      </div>
    </div>
  );
};
