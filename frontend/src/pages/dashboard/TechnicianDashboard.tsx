import React, { useState, useEffect } from 'react';
import { Briefcase, Clock, Star, CheckCircle2, ToggleLeft, ToggleRight, MapPin, Calendar, Play, Check } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { bookingService } from '../../services/api';
import { Booking, BookingStatus } from '../../types';

export const TechnicianDashboard: React.FC = () => {
  const { user } = useAuth();
  const [isAvailable, setIsAvailable] = useState(true);
  const [bookings, setBookings] = useState<Booking[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchJobs = async () => {
    setLoading(true);
    try {
      const list = await bookingService.getMyBookings();
      setBookings(list);
    } catch (err) {
      console.error('Failed to load technician jobs:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchJobs();
  }, []);

  const handleStatusUpdate = async (bookingId: number, status: BookingStatus) => {
    try {
      await bookingService.updateStatus(bookingId, status);
      await fetchJobs();
    } catch (err) {
      alert('Failed to update job status.');
    }
  };

  const assignedJobs = bookings.filter((b) => ['PENDING', 'ASSIGNED', 'IN_PROGRESS'].includes(b.status));
  const completedJobs = bookings.filter((b) => b.status === 'COMPLETED');

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
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Active Dispatch Queue</span>
            <Briefcase size={20} color="#6366f1" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#ffffff', marginTop: '0.5rem' }}>
            {assignedJobs.length}
          </div>
          <span style={{ fontSize: '0.8rem', color: '#64748b' }}>Jobs assigned to you</span>
        </div>

        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Completed Jobs</span>
            <CheckCircle2 size={20} color="#10b981" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#ffffff', marginTop: '0.5rem' }}>
            {completedJobs.length}
          </div>
          <span style={{ fontSize: '0.8rem', color: '#10b981' }}>Total jobs finished</span>
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

      {/* Dispatch Queue */}
      <div className="glass-panel" style={{ padding: '2rem' }}>
        <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#ffffff', marginBottom: '1.5rem' }}>
          Job Dispatch Requests & Work Orders
        </h3>

        {loading ? (
          <div style={{ textAlign: 'center', color: '#94a3b8', padding: '3rem 0' }}>Loading dispatch queue...</div>
        ) : bookings.length === 0 ? (
          <div style={{ padding: '3.5rem 2rem', textAlign: 'center', background: 'rgba(15, 23, 42, 0.4)', borderRadius: '12px', border: '1px dashed rgba(255, 255, 255, 0.1)' }}>
            <Clock size={40} color="#64748b" style={{ marginBottom: '0.75rem' }} />
            <h4 style={{ color: '#f8fafc', fontWeight: 600, fontSize: '1.1rem', marginBottom: '0.25rem' }}>No Dispatch Requests Right Now</h4>
            <p style={{ color: '#94a3b8', fontSize: '0.9rem' }}>
              When customers book services matching your specialization ({user?.specialization || 'Technician'}), service requests will appear here.
            </p>
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            {bookings.map((job) => (
              <div key={job.id} className="glass-panel" style={{ padding: '1.75rem', background: 'rgba(15, 23, 42, 0.6)' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1rem', marginBottom: '1rem' }}>
                  <div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '0.35rem' }}>
                      <span style={{ fontSize: '1.2rem', fontWeight: 700, color: '#ffffff' }}>
                        {job.service?.name || `Job #${job.id}`}
                      </span>
                      <span className="role-badge technician">{job.status}</span>
                    </div>
                    <div style={{ color: '#94a3b8', fontSize: '0.88rem', display: 'flex', gap: '1.25rem', flexWrap: 'wrap' }}>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
                        <Calendar size={14} color="#6366f1" /> {job.scheduled_date} ({job.scheduled_time_slot})
                      </span>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
                        <MapPin size={14} color="#06b6d4" /> {job.address_line}, {job.city}
                      </span>
                    </div>
                  </div>

                  <div style={{ textAlign: 'right' }}>
                    <span style={{ fontSize: '1.35rem', fontWeight: 800, color: '#10b981' }}>
                      ${job.total_amount.toFixed(2)}
                    </span>
                    <span style={{ display: 'block', fontSize: '0.75rem', color: '#64748b' }}>Payout</span>
                  </div>
                </div>

                {job.customer && (
                  <div style={{ background: 'rgba(30, 41, 59, 0.6)', padding: '0.85rem 1.25rem', borderRadius: '8px', marginBottom: '1.25rem', fontSize: '0.88rem', color: '#f8fafc' }}>
                    <strong>Customer:</strong> {job.customer.full_name} | <strong>Phone:</strong> {job.customer.phone || 'N/A'}
                    {job.notes && <div style={{ color: '#94a3b8', marginTop: '0.25rem' }}><strong>Instructions:</strong> {job.notes}</div>}
                  </div>
                )}

                {/* Job Action Buttons */}
                <div style={{ display: 'flex', gap: '1rem' }}>
                  {job.status === 'ASSIGNED' || job.status === 'PENDING' ? (
                    <button
                      onClick={() => handleStatusUpdate(job.id, 'IN_PROGRESS')}
                      className="btn btn-primary"
                      style={{ padding: '0.6rem 1.25rem' }}
                    >
                      <Play size={16} /> Start Service Job
                    </button>
                  ) : null}

                  {job.status === 'IN_PROGRESS' ? (
                    <button
                      onClick={() => handleStatusUpdate(job.id, 'COMPLETED')}
                      className="btn btn-primary"
                      style={{ background: 'linear-gradient(135deg, #10b981, #059669)', padding: '0.6rem 1.25rem' }}
                    >
                      <Check size={16} /> Mark Job Completed
                    </button>
                  ) : null}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
