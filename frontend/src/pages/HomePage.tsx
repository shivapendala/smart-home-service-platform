import React from 'react';
import { Link } from 'react-router-dom';
import { ShieldCheck, Zap, Clock, Star, ArrowRight, UserCheck } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export const HomePage: React.FC = () => {
  const { user } = useAuth();

  const serviceCategories = [
    { title: 'AC Repair & Service', icon: '❄️', count: '120+ Technicians', desc: 'Deep cleaning, gas refill, compressor repair & installation.' },
    { title: 'Refrigerator Repair', icon: '🧊', count: '85+ Technicians', desc: 'Cooling issues, leak repair, thermostat replacement & maintenance.' },
    { title: 'Washing Machine Repair', icon: '🧺', count: '95+ Technicians', desc: 'Front load & top load motor repair, drum balancing & drainage.' },
    { title: 'Plumbing Services', icon: '🚰', count: '150+ Technicians', desc: 'Pipe leakages, tap installation, drain unblocking & fitting.' },
    { title: 'Electrical Repairs', icon: '⚡', count: '110+ Technicians', desc: 'Short circuit fix, wiring, DB box setup & appliance install.' },
    { title: 'General Appliance Fix', icon: '🏠', count: '75+ Technicians', desc: 'Microwave repair, water heater service, chimney cleaning.' },
  ];

  return (
    <div style={{ padding: '2rem 3rem' }}>
      {/* Hero Section */}
      <div className="glass-panel" style={{
        padding: '4rem 3rem',
        marginBottom: '3rem',
        background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%)',
        position: 'relative',
        overflow: 'hidden'
      }}>
        <div style={{ maxWidth: '750px', position: 'relative', zIndex: 2 }}>
          <div style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '0.5rem',
            padding: '0.35rem 1rem',
            background: 'rgba(99, 102, 241, 0.15)',
            border: '1px solid rgba(99, 102, 241, 0.3)',
            borderRadius: '9999px',
            color: '#818cf8',
            fontWeight: 600,
            fontSize: '0.85rem',
            marginBottom: '1.25rem'
          }}>
            <ShieldCheck size={16} /> Certified & Verified Professional Technicians
          </div>

          <h1 style={{ fontSize: '3rem', fontWeight: 800, lineHeight: 1.15, marginBottom: '1.25rem', color: '#ffffff' }}>
            Book Trusted Home Services <br />
            <span style={{
              background: 'linear-gradient(135deg, #6366f1 0%, #06b6d4 100%)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent'
            }}>
              At Your Doorstep, In Minutes.
            </span>
          </h1>

          <p style={{ fontSize: '1.1rem', color: '#94a3b8', marginBottom: '2rem', lineHeight: 1.6 }}>
            Connect with background-checked local technicians for AC repair, plumbing, electrical work, and home appliance maintenance. Fast, transparent pricing & guaranteed satisfaction.
          </p>

          <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
            {user ? (
              <Link to={user.role === 'ADMIN' ? '/admin-dashboard' : user.role === 'TECHNICIAN' ? '/technician-dashboard' : '/customer-dashboard'} className="btn btn-primary" style={{ padding: '0.85rem 2rem', fontSize: '1rem' }}>
                Go to Dashboard <ArrowRight size={18} />
              </Link>
            ) : (
              <>
                <Link to="/register" className="btn btn-primary" style={{ padding: '0.85rem 2rem', fontSize: '1rem' }}>
                  Book Service Now <ArrowRight size={18} />
                </Link>
                <Link to="/register?role=TECHNICIAN" className="btn btn-secondary" style={{ padding: '0.85rem 1.75rem', fontSize: '1rem' }}>
                  Join as Technician <UserCheck size={18} />
                </Link>
              </>
            )}
          </div>
        </div>
      </div>

      {/* Service Categories */}
      <div style={{ marginBottom: '3rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: '1.5rem' }}>
          <div>
            <h2 style={{ fontSize: '1.75rem', fontWeight: 800, color: '#f8fafc' }}>Popular Home Services</h2>
            <p style={{ color: '#94a3b8', fontSize: '0.95rem' }}>Choose from top rated service categories in your area</p>
          </div>
        </div>

        <div className="grid-3">
          {serviceCategories.map((cat, idx) => (
            <div key={idx} className="glass-panel" style={{ padding: '1.75rem', cursor: 'pointer' }}>
              <div style={{ fontSize: '2.5rem', marginBottom: '0.75rem' }}>{cat.icon}</div>
              <h3 style={{ fontSize: '1.2rem', fontWeight: 700, marginBottom: '0.35rem', color: '#f8fafc' }}>{cat.title}</h3>
              <p style={{ color: '#94a3b8', fontSize: '0.88rem', marginBottom: '1rem', minHeight: '40px' }}>{cat.desc}</p>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: '0.75rem', borderTop: '1px solid rgba(255, 255, 255, 0.08)' }}>
                <span style={{ fontSize: '0.8rem', color: '#06b6d4', fontWeight: 600 }}>{cat.count}</span>
                <span style={{ color: '#818cf8', fontWeight: 600, fontSize: '0.85rem', display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
                  Book Service <ArrowRight size={14} />
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Platform Features */}
      <div className="grid-3" style={{ marginTop: '3rem' }}>
        <div className="glass-panel" style={{ padding: '1.75rem' }}>
          <Zap size={32} color="#6366f1" style={{ marginBottom: '1rem' }} />
          <h4 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: '0.5rem' }}>Instant Technician Assignment</h4>
          <p style={{ color: '#94a3b8', fontSize: '0.9rem' }}>Smart matching system assigns the nearest qualified technician to your request in under 5 minutes.</p>
        </div>
        <div className="glass-panel" style={{ padding: '1.75rem' }}>
          <Clock size={32} color="#06b6d4" style={{ marginBottom: '1rem' }} />
          <h4 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: '0.5rem' }}>Real-time Service Tracking</h4>
          <p style={{ color: '#94a3b8', fontSize: '0.9rem' }}>Track technician status, arrival time, and service stage with clear live updates.</p>
        </div>
        <div className="glass-panel" style={{ padding: '1.75rem' }}>
          <Star size={32} color="#f59e0b" style={{ marginBottom: '1rem' }} />
          <h4 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: '0.5rem' }}>Verified Reviews & Ratings</h4>
          <p style={{ color: '#94a3b8', fontSize: '0.9rem' }}>All technicians are background-checked and customer rated for consistent premium quality.</p>
        </div>
      </div>
    </div>
  );
};
