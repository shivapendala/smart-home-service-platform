import React, { useState, useEffect } from 'react';
import { Users, Wrench, FileText, CheckCircle, AlertTriangle, Activity } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { authService } from '../../services/api';
import { User } from '../../types';

export const AdminDashboard: React.FC = () => {
  const { user } = useAuth();
  const [technicians, setTechnicians] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTechs = async () => {
      try {
        const list = await authService.getTechnicians();
        setTechnicians(list);
      } catch (err) {
        console.error('Failed to load technicians:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchTechs();
  }, []);

  return (
    <div style={{ padding: '2rem 3rem' }}>
      {/* Admin Header */}
      <div className="glass-panel" style={{ padding: '2rem 2.5rem', marginBottom: '2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <span className="role-badge admin" style={{ marginBottom: '0.5rem' }}>Platform Control Center</span>
          <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#ffffff' }}>
            System Administration Dashboard
          </h1>
          <p style={{ color: '#94a3b8', fontSize: '0.95rem' }}>
            Administrator: <strong style={{ color: '#f43f5e' }}>{user?.full_name}</strong> ({user?.email})
          </p>
        </div>

        <div style={{ display: 'flex', gap: '0.75rem' }}>
          <button className="btn btn-secondary" style={{ padding: '0.65rem 1.25rem' }}>
            <FileText size={16} /> Export System Report
          </button>
        </div>
      </div>

      {/* Metrics Row */}
      <div className="grid-3" style={{ marginBottom: '2rem' }}>
        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Registered Technicians</span>
            <Wrench size={20} color="#10b981" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#ffffff', marginTop: '0.5rem' }}>
            {technicians.length}
          </div>
          <span style={{ fontSize: '0.8rem', color: '#10b981' }}>Active technician accounts</span>
        </div>

        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>System Status</span>
            <Activity size={20} color="#06b6d4" />
          </div>
          <div style={{ fontSize: '1.25rem', fontWeight: 700, color: '#10b981', marginTop: '0.75rem', display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
            <CheckCircle size={18} /> All Services Operational
          </div>
          <span style={{ fontSize: '0.8rem', color: '#64748b' }}>FastAPI Backend & DB Healthy</span>
        </div>

        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Pending Complaints</span>
            <AlertTriangle size={20} color="#f59e0b" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#ffffff', marginTop: '0.5rem' }}>0</div>
          <span style={{ fontSize: '0.8rem', color: '#64748b' }}>No open customer complaints</span>
        </div>
      </div>

      {/* Registered Technicians Management Table */}
      <div className="glass-panel" style={{ padding: '2rem' }}>
        <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#ffffff', marginBottom: '1.25rem' }}>
          Registered Platform Technicians
        </h3>

        {loading ? (
          <div style={{ textAlign: 'center', color: '#94a3b8', padding: '2rem' }}>Loading technicians...</div>
        ) : technicians.length === 0 ? (
          <div style={{
            padding: '2.5rem',
            textAlign: 'center',
            background: 'rgba(15, 23, 42, 0.4)',
            borderRadius: '12px',
            border: '1px dashed rgba(255, 255, 255, 0.1)'
          }}>
            <Users size={36} color="#64748b" style={{ marginBottom: '0.5rem' }} />
            <p style={{ color: '#94a3b8' }}>No technician accounts registered yet. Technicians can register via the Join as Technician flow.</p>
          </div>
        ) : (
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', color: '#f8fafc', fontSize: '0.9rem' }}>
              <thead>
                <tr style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.1)', color: '#94a3b8' }}>
                  <th style={{ padding: '0.75rem 1rem' }}>ID</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Name</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Email</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Specialization</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Experience</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Rating</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Status</th>
                </tr>
              </thead>
              <tbody>
                {technicians.map((t) => (
                  <tr key={t.id} style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.05)' }}>
                    <td style={{ padding: '0.75rem 1rem', color: '#64748b' }}>#{t.id}</td>
                    <td style={{ padding: '0.75rem 1rem', fontWeight: 600 }}>{t.full_name}</td>
                    <td style={{ padding: '0.75rem 1rem', color: '#94a3b8' }}>{t.email}</td>
                    <td style={{ padding: '0.75rem 1rem', color: '#06b6d4' }}>{t.specialization || 'General'}</td>
                    <td style={{ padding: '0.75rem 1rem' }}>{t.experience_years} Yrs</td>
                    <td style={{ padding: '0.75rem 1rem', color: '#f59e0b' }}>{t.rating} ★</td>
                    <td style={{ padding: '0.75rem 1rem' }}>
                      <span className="role-badge technician">Active</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};
