import React, { useState, useEffect } from 'react';
import { X, Clock, MapPin, AlertCircle, Wrench } from 'lucide-react';
import { ServiceItem } from '../../types';
import { catalogService, bookingService } from '../../services/api';

interface BookingModalProps {
  initialService?: ServiceItem | null;
  isOpen: boolean;
  onClose: () => void;
  onSuccess: () => void;
}

export const BookingModal: React.FC<BookingModalProps> = ({
  initialService,
  isOpen,
  onClose,
  onSuccess,
}) => {
  const [services, setServices] = useState<ServiceItem[]>([]);
  const [selectedServiceId, setSelectedServiceId] = useState<number>(initialService?.id || 1);
  const [scheduledDate, setScheduledDate] = useState<string>(
    new Date(Date.now() + 86400000).toISOString().split('T')[0]
  );
  const [timeSlot, setTimeSlot] = useState('10:00 AM - 12:00 PM');
  const [addressLine, setAddressLine] = useState('');
  const [city, setCity] = useState('');
  const [zipCode, setZipCode] = useState('');
  const [notes, setNotes] = useState('');

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (initialService) {
      setSelectedServiceId(initialService.id);
    }
    const loadServices = async () => {
      try {
        const list = await catalogService.getServices();
        setServices(list);
        if (!initialService && list.length > 0) {
          setSelectedServiceId(list[0].id);
        }
      } catch (err) {
        console.error('Failed to load service items:', err);
      }
    };
    if (isOpen) loadServices();
  }, [isOpen, initialService]);

  if (!isOpen) return null;

  const currentService = services.find((s) => s.id === selectedServiceId) || initialService;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      await bookingService.createBooking({
        service_id: selectedServiceId,
        scheduled_date: scheduledDate,
        scheduled_time_slot: timeSlot,
        address_line: addressLine,
        city: city,
        zip_code: zipCode,
        notes: notes,
      });

      onSuccess();
      onClose();
    } catch (err: any) {
      const msg = err.response?.data?.detail || 'Failed to submit booking. Please try again.';
      setError(msg);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      position: 'fixed',
      top: 0, left: 0, right: 0, bottom: 0,
      background: 'rgba(15, 23, 42, 0.85)',
      backdropFilter: 'blur(12px)',
      display: 'flex', justifyContent: 'center', alignItems: 'center',
      zIndex: 1000,
      padding: '1.5rem'
    }}>
      <div className="glass-panel" style={{ width: '100%', maxWidth: '540px', padding: '2.25rem', position: 'relative', maxHeight: '90vh', overflowY: 'auto' }}>
        <button
          onClick={onClose}
          style={{ position: 'absolute', right: '1.25rem', top: '1.25rem', background: 'transparent', border: 'none', color: '#94a3b8', cursor: 'pointer' }}
        >
          <X size={22} />
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1.25rem' }}>
          <div style={{
            background: 'linear-gradient(135deg, #6366f1, #06b6d4)',
            padding: '0.5rem',
            borderRadius: '10px',
            display: 'flex',
            alignItems: 'center'
          }}>
            <Wrench size={20} color="#ffffff" />
          </div>
          <div>
            <h3 style={{ fontSize: '1.4rem', fontWeight: 800, color: '#ffffff' }}>
              Schedule Service Booking
            </h3>
            <p style={{ color: '#94a3b8', fontSize: '0.88rem' }}>Upfront transparent pricing & instant technician dispatch</p>
          </div>
        </div>

        {error && (
          <div className="alert-box alert-error">
            <AlertCircle size={18} />
            <span>{error}</span>
          </div>
        )}

        <form onSubmit={handleSubmit}>
          {/* Service Selection */}
          <div className="form-group">
            <label className="form-label">Select Home Service</label>
            <select
              className="form-select"
              value={selectedServiceId}
              onChange={(e) => setSelectedServiceId(Number(e.target.value))}
            >
              {services.map((s) => (
                <option key={s.id} value={s.id}>
                  {s.name} — ${s.base_price.toFixed(2)} ({s.duration_minutes} Mins)
                </option>
              ))}
            </select>
          </div>

          {/* Pricing Highlight Box */}
          {currentService && (
            <div style={{
              background: 'rgba(99, 102, 241, 0.12)',
              border: '1px solid rgba(99, 102, 241, 0.3)',
              borderRadius: '10px',
              padding: '1rem',
              marginBottom: '1.25rem',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center'
            }}>
              <div>
                <span style={{ fontSize: '0.8rem', color: '#818cf8', fontWeight: 600, display: 'block' }}>Estimated Total Cost</span>
                <span style={{ fontSize: '1.5rem', fontWeight: 800, color: '#ffffff' }}>${currentService.base_price.toFixed(2)}</span>
              </div>
              <span style={{ fontSize: '0.85rem', color: '#06b6d4', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
                <Clock size={14} /> ~{currentService.duration_minutes} Mins Duration
              </span>
            </div>
          )}

          {/* Date & Time Slot */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
            <div className="form-group">
              <label className="form-label">Service Date</label>
              <div style={{ position: 'relative' }}>
                <input
                  type="date"
                  className="form-input"
                  min={new Date().toISOString().split('T')[0]}
                  value={scheduledDate}
                  onChange={(e) => setScheduledDate(e.target.value)}
                  required
                />
              </div>
            </div>

            <div className="form-group">
              <label className="form-label">Preferred Time Slot</label>
              <select
                className="form-select"
                value={timeSlot}
                onChange={(e) => setTimeSlot(e.target.value)}
              >
                <option value="09:00 AM - 11:00 AM">09:00 AM - 11:00 AM</option>
                <option value="11:00 AM - 01:00 PM">11:00 AM - 01:00 PM</option>
                <option value="02:00 PM - 04:00 PM">02:00 PM - 04:00 PM</option>
                <option value="04:00 PM - 06:00 PM">04:00 PM - 06:00 PM</option>
                <option value="06:00 PM - 08:00 PM">06:00 PM - 08:00 PM</option>
              </select>
            </div>
          </div>

          {/* Address Fields */}
          <div className="form-group">
            <label className="form-label">Street Address</label>
            <div style={{ position: 'relative' }}>
              <input
                type="text"
                className="form-input"
                placeholder="Apartment #, House No., Street Name"
                value={addressLine}
                onChange={(e) => setAddressLine(e.target.value)}
                required
                style={{ paddingLeft: '2.5rem' }}
              />
              <MapPin size={18} color="#64748b" style={{ position: 'absolute', left: '0.85rem', top: '50%', transform: 'translateY(-50%)' }} />
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
            <div className="form-group">
              <label className="form-label">City</label>
              <input
                type="text"
                className="form-input"
                placeholder="Metropolis"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                required
              />
            </div>

            <div className="form-group">
              <label className="form-label">Zip Code</label>
              <input
                type="text"
                className="form-input"
                placeholder="10001"
                value={zipCode}
                onChange={(e) => setZipCode(e.target.value)}
                required
              />
            </div>
          </div>

          {/* Notes */}
          <div className="form-group" style={{ marginBottom: '1.5rem' }}>
            <label className="form-label">Special Instructions (Optional)</label>
            <textarea
              className="form-textarea"
              rows={2}
              placeholder="e.g. AC unit is on the balcony, call before arriving..."
              value={notes}
              onChange={(e) => setNotes(e.target.value)}
            />
          </div>

          <button
            type="submit"
            className="btn btn-primary"
            disabled={loading}
            style={{ width: '100%', padding: '0.85rem', fontSize: '1rem' }}
          >
            {loading ? 'Confirming Booking...' : 'Confirm & Request Dispatch'}
          </button>
        </form>
      </div>
    </div>
  );
};
