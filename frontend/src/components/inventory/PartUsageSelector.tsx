import React, { useState } from 'react';
import { PackageCheck, Plus } from 'lucide-react';
import api from '../../services/api';

export const PartUsageSelector: React.FC<{ bookingId: number }> = ({ bookingId }) => {
  const [partId, setPartId] = useState<number>(1);
  const [qty, setQty] = useState<number>(1);
  const [usageList, setUsageList] = useState<any[]>([]);

  const handleRecord = async () => {
    try {
      const res = await api.post('/inventory/use-part', {
        booking_id: bookingId,
        spare_part_id: partId,
        quantity_used: qty
      });
      setUsageList([...usageList, res.data]);
    } catch (err) {
      console.error('Usage record error', err);
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4">
      <h3 className="text-lg font-bold text-slate-100 flex items-center gap-2">
        <PackageCheck className="w-5 h-5 text-amber-400" /> Log Installed Spare Parts
      </h3>

      <div className="flex gap-3">
        <input
          type="number"
          value={partId}
          onChange={(e) => setPartId(Number(e.target.value))}
          placeholder="Part ID"
          className="bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-slate-100 w-28"
        />
        <input
          type="number"
          value={qty}
          onChange={(e) => setQty(Number(e.target.value))}
          placeholder="Qty"
          className="bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-slate-100 w-20"
        />
        <button onClick={handleRecord} className="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold px-4 py-2 rounded-xl text-xs">
          Deduct Van Stock & Bill
        </button>
      </div>

      <div className="space-y-2">
        {usageList.map((u, i) => (
          <div key={i} className="p-3 bg-slate-950/60 border border-slate-800 rounded-xl flex justify-between text-xs text-slate-200">
            <span>Spare Part #{u.spare_part_id} x{u.quantity_used}</span>
            <span className="font-bold text-emerald-400">${u.total_charged.toFixed(2)}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
export default PartUsageSelector;
