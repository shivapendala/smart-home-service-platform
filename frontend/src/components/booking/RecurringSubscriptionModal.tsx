import React, { useState } from 'react';
import { Calendar, Repeat, CheckCircle } from 'lucide-react';
import api from '../../services/api';

interface RecurringModalProps {
  isOpen: boolean;
  onClose: () => void;
  serviceId?: number;
}

export const RecurringSubscriptionModal: React.FC<RecurringModalProps> = ({ isOpen, onClose, serviceId = 1 }) => {
  const [frequency, setFrequency] = useState('MONTHLY');
  const [startDate, setStartDate] = useState('');
  const [preferredSlot, setPreferredSlot] = useState('09:00 - 11:00');
  const [submitted, setSubmitted] = useState(false);

  if (!isOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/booking-engine/recurring', {
        service_id: serviceId,
        address_id: 1,
        frequency,
        start_date: startDate,
        preferred_time_slot: preferredSlot
      });
      setSubmitted(true);
      setTimeout(() => {
        setSubmitted(false);
        onClose();
      }, 1500);
    } catch (err) {
      console.error('Subscription creation failed', err);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
      <div className="bg-slate-900 border border-slate-800 w-full max-w-lg rounded-3xl p-6 shadow-2xl space-y-6">
        <div className="flex items-center gap-3">
          <div className="p-3 bg-purple-500/10 border border-purple-500/30 rounded-2xl">
            <Repeat className="w-6 h-6 text-purple-400" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-slate-100">Recurring Service Subscription</h2>
            <p className="text-xs text-slate-400">Automate preventative inspections & scheduled maintenance.</p>
          </div>
        </div>

        {submitted ? (
          <div className="text-center py-8 space-y-3">
            <CheckCircle className="w-12 h-12 text-emerald-400 mx-auto animate-bounce" />
            <h3 className="text-lg font-bold text-slate-200">Subscription Active!</h3>
            <p className="text-xs text-slate-400">Your periodic booking schedule has been created.</p>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-4 text-sm">
            <div>
              <label className="block text-slate-400 mb-1">Recurrence Frequency</label>
              <select
                value={frequency}
                onChange={(e) => setFrequency(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-100"
              >
                <option value="WEEKLY">Weekly Maintenance</option>
                <option value="BIWEEKLY">Bi-Weekly</option>
                <option value="MONTHLY">Monthly Inspection (Recommended)</option>
                <option value="QUARTERLY">Quarterly (3 Months)</option>
              </select>
            </div>

            <div>
              <label className="block text-slate-400 mb-1">First Execution Date</label>
              <input
                type="date"
                required
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-100"
              />
            </div>

            <div>
              <label className="block text-slate-400 mb-1">Preferred Arrival Window</label>
              <select
                value={preferredSlot}
                onChange={(e) => setPreferredSlot(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-100"
              >
                <option value="09:00 - 11:00">Morning (09:00 - 11:00 AM)</option>
                <option value="11:00 - 13:00">Midday (11:00 - 01:00 PM)</option>
                <option value="14:00 - 16:00">Afternoon (02:00 - 04:00 PM)</option>
                <option value="16:00 - 18:00">Evening (04:00 - 06:00 PM)</option>
              </select>
            </div>

            <div className="flex justify-end gap-3 pt-4 border-t border-slate-800">
              <button type="button" onClick={onClose} className="px-4 py-2 text-slate-400 hover:text-slate-200">
                Cancel
              </button>
              <button
                type="submit"
                className="px-6 py-2.5 bg-gradient-to-r from-purple-600 to-indigo-600 text-white font-semibold rounded-xl shadow-lg shadow-purple-600/30"
              >
                Confirm Recurring Schedule
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
};
export default RecurringSubscriptionModal;
