import React, { useState } from 'react';
import { Truck, ArrowRight, CheckCircle2 } from 'lucide-react';
import api from '../../services/api';

export const VanStockTransferModal: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [techId, setTechId] = useState<number>(2);
  const [partId, setPartId] = useState<number>(1);
  const [qty, setQty] = useState<number>(5);

  if (!isOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/inventory/transfer-van', {
        technician_id: techId,
        spare_part_id: partId,
        quantity: qty
      });
      onClose();
    } catch (err) {
      console.error('Transfer failed', err);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
      <div className="bg-slate-900 border border-slate-800 w-full max-w-lg rounded-3xl p-6 shadow-2xl space-y-6">
        <div className="flex items-center gap-3">
          <div className="p-3 bg-amber-500/10 border border-amber-500/30 rounded-2xl">
            <Truck className="w-6 h-6 text-amber-400" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-slate-100">Transfer Warehouse Stock to Van</h2>
            <p className="text-xs text-slate-400">Re-stock mobile technician inventory.</p>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4 text-sm">
          <div>
            <label className="block text-slate-400 mb-1">Technician User ID</label>
            <input
              type="number"
              value={techId}
              onChange={(e) => setTechId(Number(e.target.value))}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2 text-slate-100"
            />
          </div>

          <div>
            <label className="block text-slate-400 mb-1">Spare Part ID</label>
            <input
              type="number"
              value={partId}
              onChange={(e) => setPartId(Number(e.target.value))}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2 text-slate-100"
            />
          </div>

          <div>
            <label className="block text-slate-400 mb-1">Transfer Quantity</label>
            <input
              type="number"
              min={1}
              value={qty}
              onChange={(e) => setQty(Number(e.target.value))}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2 text-slate-100"
            />
          </div>

          <div className="flex justify-end gap-3 pt-4 border-t border-slate-800">
            <button type="button" onClick={onClose} className="px-4 py-2 text-slate-400">Cancel</button>
            <button type="submit" className="px-6 py-2.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl">
              Execute Transfer
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
export default VanStockTransferModal;
