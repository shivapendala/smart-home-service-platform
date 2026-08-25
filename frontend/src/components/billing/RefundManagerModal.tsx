import React, { useState } from 'react';
import { RotateCcw, AlertTriangle, Send } from 'lucide-react';
import api from '../../services/api';

interface RefundModalProps {
  isOpen: boolean;
  onClose: () => void;
  invoiceId: number;
}

export const RefundManagerModal: React.FC<RefundModalProps> = ({ isOpen, onClose, invoiceId }) => {
  const [amount, setAmount] = useState<number>(50.0);
  const [reason, setReason] = useState<string>('');

  if (!isOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/billing/refunds', {
        invoice_id: invoiceId,
        requested_amount: amount,
        reason
      });
      onClose();
    } catch (err) {
      console.error('Refund request failed', err);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
      <div className="bg-slate-900 border border-slate-800 w-full max-w-lg rounded-3xl p-6 shadow-2xl space-y-6">
        <div className="flex items-center gap-3">
          <div className="p-3 bg-amber-500/10 border border-amber-500/30 rounded-2xl">
            <RotateCcw className="w-6 h-6 text-amber-400" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-slate-100">Submit Refund Escalation</h2>
            <p className="text-xs text-slate-400">Request full or partial refund for disputed invoice items.</p>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4 text-sm">
          <div>
            <label className="block text-slate-400 mb-1">Requested Amount ($)</label>
            <input
              type="number"
              step="0.01"
              required
              value={amount}
              onChange={(e) => setAmount(Number(e.target.value))}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2 text-slate-100"
            />
          </div>

          <div>
            <label className="block text-slate-400 mb-1">Reason for Refund</label>
            <textarea
              required
              rows={3}
              value={reason}
              onChange={(e) => setReason(e.target.value)}
              placeholder="Explain the service quality issue or double billing discrepancy..."
              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2 text-slate-100"
            />
          </div>

          <div className="flex justify-end gap-3 pt-4 border-t border-slate-800">
            <button type="button" onClick={onClose} className="px-4 py-2 text-slate-400 hover:text-slate-200">
              Cancel
            </button>
            <button
              type="submit"
              className="px-6 py-2.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl shadow-lg shadow-amber-500/20"
            >
              Submit Claim
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
export default RefundManagerModal;
