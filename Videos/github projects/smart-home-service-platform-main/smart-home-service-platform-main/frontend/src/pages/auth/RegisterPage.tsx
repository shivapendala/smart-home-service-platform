import React, { useState } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { UserPlus, Mail, Lock, User, Phone, AlertCircle, Briefcase, Award } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { UserRole } from '../../types';

export const RegisterPage: React.FC = () => {
  const [searchParams] = useSearchParams();
  const initialRole = (searchParams.get('role') as UserRole) || 'CUSTOMER';

  const [role, setRole] = useState<UserRole>(initialRole);
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');
  const [specialization, setSpecialization] = useState('AC Repair & Maintenance');
  const [experienceYears, setExperienceYears] = useState<number>(3);
  const bio = '';
  
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const { register } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      await register({
        email,
        password,
        full_name: fullName,
        phone,
        role,
        specialization: role === 'TECHNICIAN' ? specialization : undefined,
        experience_years: role === 'TECHNICIAN' ? Number(experienceYears) : undefined,
        bio: role === 'TECHNICIAN' ? bio : undefined,
      });

      if (role === 'ADMIN') navigate('/admin-dashboard');
      else if (role === 'TECHNICIAN') navigate('/technician-dashboard');
      else navigate('/customer-dashboard');
    } catch (err: any) {
      const msg = err.response?.data?.detail || 'Registration failed. Please check your information.';
      setError(msg);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '85vh', padding: '1.5rem' }}>
      <div className="glass-panel" style={{ width: '100%', maxWidth: '520px', padding: '2.5rem' }}>
        <div style={{ textAlign: 'center', marginBottom: '1.5rem' }}>
          <h2 style={{ fontSize: '1.6rem', fontWeight: 800, color: '#ffffff' }}>Create Your Account</h2>
          <p style={{ color: '#94a3b8', fontSize: '0.9rem' }}>Join the Smart Home Service Platform</p>
        </div>

        {/* Role Selector Tabs */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(3, 1fr)',
          gap: '0.5rem',
          background: 'rgba(15, 23, 42, 0.6)',
          padding: '0.35rem',
          borderRadius: '12px',
          marginBottom: '1.75rem',
          border: '1px solid rgba(255, 255, 255, 0.08)'
        }}>
          {(['CUSTOMER', 'TECHNICIAN', 'ADMIN'] as UserRole[]).map((r) => (
            <button
              key={r}
              type="button"
              onClick={() => setRole(r)}
              style={{
                padding: '0.6rem 0.5rem',
                border: 'none',
                borderRadius: '8px',
                fontSize: '0.82rem',
                fontWeight: 700,
                cursor: 'pointer',
                transition: 'all 0.2s ease',
                background: role === r ? 'linear-gradient(135deg, #6366f1, #4f46e5)' : 'transparent',
                color: role === r ? '#ffffff' : '#94a3b8',
                boxShadow: role === r ? '0 2px 10px rgba(99, 102, 241, 0.3)' : 'none'
              }}
            >
              {r}
            </button>
          ))}
        </div>

        {error && (
          <div className="alert-box alert-error">
            <AlertCircle size={18} />
            <span>{error}</span>
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label className="form-label">Full Name</label>
            <div style={{ position: 'relative' }}>
              <input
                type="text"
                className="form-input"
                placeholder="Alex Morgan"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                required
                style={{ paddingLeft: '2.5rem' }}
              />
              <User size={18} color="#64748b" style={{ position: 'absolute', left: '0.85rem', top: '50%', transform: 'translateY(-50%)' }} />
            </div>
          </div>

          <div className="form-group">
            <label className="form-label">Email Address</label>
            <div style={{ position: 'relative' }}>
              <input
                type="email"
                className="form-input"
                placeholder="alex@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                style={{ paddingLeft: '2.5rem' }}
              />
              <Mail size={18} color="#64748b" style={{ position: 'absolute', left: '0.85rem', top: '50%', transform: 'translateY(-50%)' }} />
            </div>
          </div>

          <div className="form-group">
            <label className="form-label">Phone Number</label>
            <div style={{ position: 'relative' }}>
              <input
                type="tel"
                className="form-input"
                placeholder="+1 (555) 000-0000"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
                style={{ paddingLeft: '2.5rem' }}
              />
              <Phone size={18} color="#64748b" style={{ position: 'absolute', left: '0.85rem', top: '50%', transform: 'translateY(-50%)' }} />
            </div>
          </div>

          {/* Technician Specific Fields */}
          {role === 'TECHNICIAN' && (
            <>
              <div className="form-group">
                <label className="form-label">Primary Specialization</label>
                <div style={{ position: 'relative' }}>
                  <select
                    className="form-select"
                    value={specialization}
                    onChange={(e) => setSpecialization(e.target.value)}
                    style={{ paddingLeft: '2.5rem' }}
                  >
                    <option value="AC Repair & Maintenance">AC Repair & Maintenance</option>
                    <option value="Refrigerator Repair">Refrigerator Repair</option>
                    <option value="Washing Machine Service">Washing Machine Service</option>
                    <option value="Plumbing & Fittings">Plumbing & Fittings</option>
                    <option value="Electrical Work & Wiring">Electrical Work & Wiring</option>
                    <option value="General Appliance Repair">General Appliance Repair</option>
                  </select>
                  <Briefcase size={18} color="#64748b" style={{ position: 'absolute', left: '0.85rem', top: '50%', transform: 'translateY(-50%)' }} />
                </div>
              </div>

              <div className="form-group">
                <label className="form-label">Experience (Years)</label>
                <div style={{ position: 'relative' }}>
                  <input
                    type="number"
                    min="0"
                    max="40"
                    className="form-input"
                    value={experienceYears}
                    onChange={(e) => setExperienceYears(parseInt(e.target.value) || 0)}
                    style={{ paddingLeft: '2.5rem' }}
                  />
                  <Award size={18} color="#64748b" style={{ position: 'absolute', left: '0.85rem', top: '50%', transform: 'translateY(-50%)' }} />
                </div>
              </div>
            </>
          )}

          <div className="form-group" style={{ marginBottom: '1.75rem' }}>
            <label className="form-label">Password</label>
            <div style={{ position: 'relative' }}>
              <input
                type="password"
                className="form-input"
                placeholder="Minimum 8 characters"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                minLength={6}
                style={{ paddingLeft: '2.5rem' }}
              />
              <Lock size={18} color="#64748b" style={{ position: 'absolute', left: '0.85rem', top: '50%', transform: 'translateY(-50%)' }} />
            </div>
          </div>

          <button
            type="submit"
            className="btn btn-primary"
            disabled={loading}
            style={{ width: '100%', padding: '0.85rem' }}
          >
            <UserPlus size={18} /> {loading ? 'Creating Account...' : `Register as ${role}`}
          </button>
        </form>

        <div style={{ marginTop: '1.5rem', textAlign: 'center', fontSize: '0.9rem', color: '#94a3b8' }}>
          Already registered?{' '}
          <Link to="/login" style={{ fontWeight: 600, color: '#818cf8' }}>
            Sign In
          </Link>
        </div>
      </div>
    </div>
  );
};
