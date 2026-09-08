import React, { useState, useEffect } from 'react';
import { Clock, Wrench, Shield, CheckCircle, PlusCircle, Calendar, MapPin, UserCheck, AlertCircle } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { bookingService } from '../../services/api';
import { Booking, BookingStatus } from '../../types';
import { BookingModal } from '../../components/booking/BookingModal';

export const CustomerDashboard: React.FC = () => {
  const { user } = useAuth();
  const [bookings, setBookings] = useState<Booking[]>([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchBookings = async () => {
    setLoading(true);
    try {
      const list = await bookingService.getMyBookings();
      setBookings(list);
    } catch (err) {
      console.error('Failed to load user bookings:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchBookings();
  }, []);

  const activeBookings = bookings.filter((b) => ['PENDING', 'ASSIGNED', 'IN_PROGRESS'].includes(b.status));
  const completedBookings = bookings.filter((b) => b.status === 'COMPLETED');

  const getStatusBadge = (status: BookingStatus) => {
    switch (status) {
      case 'PENDING':
        return <span className="role-badge" style={{ background: 'rgba(245, 158, 11, 0.15)', color: '#f59e0b', border: '1px solid rgba(245, 158, 11, 0.3)' }}>Finding Technician</span>;
      case 'ASSIGNED':
        return <span className="role-badge" style={{ background: 'rgba(6, 182, 212, 0.15)', color: '#06b6d4', border: '1px solid rgba(6, 182, 212, 0.3)' }}>Technician Assigned</span>;
      case 'IN_PROGRESS':
        return <span className="role-badge" style={{ background: 'rgba(99, 102, 241, 0.15)', color: '#818cf8', border: '1px solid rgba(99, 102, 241, 0.3)' }}>Service In Progress</span>;
      case 'COMPLETED':
        return <span className="role-badge" style={{ background: 'rgba(16, 185, 129, 0.15)', color: '#10b981', border: '1px solid rgba(16, 185, 129, 0.3)' }}>Completed</span>;
      case 'CANCELLED':
        return <span className="role-badge" style={{ background: 'rgba(244, 63, 94, 0.15)', color: '#f43f5e', border: '1px solid rgba(244, 63, 94, 0.3)' }}>Cancelled</span>;
    }
  };

  const getStepProgressIndex = (status: BookingStatus) => {
    switch (status) {
      case 'PENDING': return 1;
      case 'ASSIGNED': return 2;
      case 'IN_PROGRESS': return 3;
      case 'COMPLETED': return 4;
      default: return 0;
    }
  };

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
            Book new technician visits, track active service requests, and view service history.
          </p>
        </div>

        <button onClick={() => setIsModalOpen(true)} className="btn btn-primary" style={{ padding: '0.75rem 1.5rem' }}>
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
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#ffffff', marginTop: '0.5rem' }}>
            {activeBookings.length}
          </div>
          <span style={{ fontSize: '0.8rem', color: '#64748b' }}>Live service requests in progress</span>
        </div>

        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Completed Services</span>
            <CheckCircle size={20} color="#10b981" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#ffffff', marginTop: '0.5rem' }}>
            {completedBookings.length}
          </div>
          <span style={{ fontSize: '0.8rem', color: '#10b981' }}>Total services delivered</span>
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

      {/* Service Bookings List */}
      <div className="glass-panel" style={{ padding: '2rem' }}>
        <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#ffffff', marginBottom: '1.5rem' }}>
          Your Service Bookings & Live Tracking
        </h3>

        {loading ? (
          <div style={{ textAlign: 'center', color: '#94a3b8', padding: '3rem 0' }}>
            Loading your bookings...
          </div>
        ) : bookings.length === 0 ? (
          <div style={{
            padding: '3.5rem 2rem',
            textAlign: 'center',
            background: 'rgba(15, 23, 42, 0.4)',
            borderRadius: '12px',
            border: '1px dashed rgba(255, 255, 255, 0.1)'
          }}>
            <Wrench size={40} color="#64748b" style={{ marginBottom: '0.75rem' }} />
            <h4 style={{ color: '#f8fafc', fontWeight: 600, fontSize: '1.1rem', marginBottom: '0.25rem' }}>No Service Bookings Yet</h4>
            <p style={{ color: '#94a3b8', fontSize: '0.9rem', marginBottom: '1.25rem' }}>
              Have household repair needs? Book certified AC, plumbing, or electrical technicians.
            </p>
            <button onClick={() => setIsModalOpen(true)} className="btn btn-primary" style={{ padding: '0.65rem 1.5rem' }}>
              <PlusCircle size={16} /> Schedule First Service
            </button>
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            {bookings.map((booking) => {
              const step = getStepProgressIndex(booking.status);
              return (
                <div key={booking.id} className="glass-panel" style={{ padding: '1.75rem', background: 'rgba(15, 23, 42, 0.6)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1rem', marginBottom: '1.25rem' }}>
                    <div>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '0.35rem' }}>
                        <span style={{ fontSize: '1.2rem', fontWeight: 700, color: '#ffffff' }}>
                          {booking.service?.name || `Booking #${booking.id}`}
                        </span>
                        {getStatusBadge(booking.status)}
                      </div>
                      <div style={{ color: '#94a3b8', fontSize: '0.88rem', display: 'flex', gap: '1.25rem', flexWrap: 'wrap' }}>
                        <span style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
                          <Calendar size={14} color="#6366f1" /> {booking.scheduled_date} ({booking.scheduled_time_slot})
                        </span>
                        <span style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
                          <MapPin size={14} color="#06b6d4" /> {booking.address_line}, {booking.city}
                        </span>
                      </div>
                    </div>

                    <div style={{ textAlign: 'right' }}>
                      <span style={{ fontSize: '1.35rem', fontWeight: 800, color: '#10b981' }}>
                        ${booking.total_amount.toFixed(2)}
                      </span>
                      <span style={{ display: 'block', fontSize: '0.75rem', color: '#64748b' }}>Upfront Price</span>
                    </div>
                  </div>

                  {/* Live Progress Stepper */}
                  {booking.status !== 'CANCELLED' && (
                    <div style={{
                      background: 'rgba(30, 41, 59, 0.6)',
                      borderRadius: '12px',
                      padding: '1.25rem',
                      marginBottom: '1rem',
                      border: '1px solid rgba(255,255,255,0.05)'
                    }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', position: 'relative' }}>
                        {[
                          { label: 'Booking Placed', s: 1 },
                          { label: 'Technician Assigned', s: 2 },
                          { label: 'Service In Progress', s: 3 },
                          { label: 'Completed', s: 4 },
                        ].map((item) => (
                          <div key={item.s} style={{ textAlign: 'center', flex: 1, position: 'relative', zIndex: 2 }}>
                            <div style={{
                              width: '28px',
                              height: '28px',
                              borderRadius: '50%',
                              background: step >= item.s ? '#10b981' : 'rgba(255,255,255,0.1)',
                              color: step >= item.s ? '#ffffff' : '#64748b',
                              display: 'inline-flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                              fontSize: '0.8rem',
                              fontWeight: 700,
                              marginBottom: '0.35rem'
                            }}>
                              {step > item.s ? <CheckCircle size={16} /> : item.s}
                            </div>
                            <span style={{ display: 'block', fontSize: '0.78rem', color: step >= item.s ? '#f8fafc' : '#64748b', fontWeight: step >= item.s ? 600 : 400 }}>
                              {item.label}
                            </span>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {/* Technician Info */}
                  {booking.technician ? (
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', fontSize: '0.88rem', color: '#94a3b8', background: 'rgba(6, 182, 212, 0.08)', padding: '0.75rem 1rem', borderRadius: '8px' }}>
                      <UserCheck size={18} color="#06b6d4" />
                      <span>Assigned Technician: <strong style={{ color: '#ffffff' }}>{booking.technician.full_name}</strong> ({booking.technician.phone || 'Contact via Platform'})</span>
                    </div>
                  ) : (
                    <div style={{ fontSize: '0.85rem', color: '#f59e0b', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                      <AlertCircle size={16} />
                      <span>Smart dispatch is locating the nearest available technician for your time slot.</span>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </div>

      {/* Booking Modal */}
      <BookingModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSuccess={fetchBookings}
      />
    </div>
  );
};
