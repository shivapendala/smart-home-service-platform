import React, { useState } from 'react';
import { ShieldAlert, Send } from 'lucide-react';
import api from '../../services/api';

export const WarrantyClaimModal: React.FC<{ isOpen: boolean; onClose: () => void; bookingId: number }> = ({ isOpen, onClose, bookingId }) => {
  const [desc, setDesc] = useState('');

  if (!isOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/amc-warranty/claims', {
        booking_id: bookingId,
        issue_description: desc
      });
      onClose();
    } catch (err) {
      console.error('Warranty claim error', err);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
      <div className="bg-slate-900 border border-slate-800 w-full max-w-lg rounded-3xl p-6 shadow-2xl space-y-6">
        <div className="flex items-center gap-3">
          <div className="p-3 bg-rose-500/10 border border-rose-500/30 rounded-2xl">
            <ShieldAlert className="w-6 h-6 text-rose-400" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-slate-100">Submit 30-Day Free Service Warranty Claim</h2>
            <p className="text-xs text-slate-400">All completed repairs include 30-day post-service guarantee.</p>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4 text-sm">
          <div>
            <label className="block text-slate-400 mb-1">Issue Recurrence Description</label>
            <textarea
              required
              rows={4}
              value={desc}
              onChange={(e) => setDesc(e.target.value)}
              placeholder="Describe what issue re-appeared after technician visit..."
              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2 text-slate-100"
            />
          </div>

          <div className="flex justify-end gap-3 pt-4 border-t border-slate-800">
            <button type="button" onClick={onClose} className="px-4 py-2 text-slate-400">Cancel</button>
            <button type="submit" className="px-6 py-2.5 bg-rose-600 hover:bg-rose-500 text-white font-bold rounded-xl">
              File Free Warranty Claim
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
export default WarrantyClaimModal;
