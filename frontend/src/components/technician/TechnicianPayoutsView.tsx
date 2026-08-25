import React, { useState, useEffect } from 'react';
import { DollarSign, CreditCard, ArrowUpRight, CheckCircle2 } from 'lucide-react';
import api from '../../services/api';

interface Payout {
  id: number;
  period_start: string;
  period_end: string;
  gross_earnings: number;
  platform_commission: number;
  net_payout: number;
  status: string;
  payout_method: string;
  reference_number?: string;
}

export const TechnicianPayoutsView: React.FC = () => {
  const [payouts, setPayouts] = useState<Payout[]>([]);

  useEffect(() => {
    api.get('/technicians/management/payouts').then((r) => setPayouts(r.data)).catch(() => {});
  }, []);

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-6">
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <h2 className="text-xl font-bold text-slate-100 flex items-center gap-2">
          <DollarSign className="w-5 h-5 text-emerald-400" /> Earnings & Commission Payout Ledger
        </h2>
      </div>

      <div className="space-y-4">
        {payouts.map((p) => (
          <div key={p.id} className="p-5 bg-slate-950/60 border border-slate-800 rounded-2xl flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <span className="text-xs font-semibold text-slate-500 uppercase">Period: {p.period_start} to {p.period_end}</span>
              <h3 className="text-2xl font-black text-emerald-400 mt-1">${p.net_payout.toFixed(2)}</h3>
              <p className="text-xs text-slate-400 mt-1">
                Gross: ${p.gross_earnings.toFixed(2)} • Commission: -${p.platform_commission.toFixed(2)}
              </p>
            </div>

            <div className="flex items-center gap-3">
              <span className={`px-3 py-1.5 text-xs font-bold rounded-full border ${
                p.status === 'PAID'
                  ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30'
                  : 'bg-amber-500/20 text-amber-400 border-amber-500/30'
              }`}>
                {p.status}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
export default TechnicianPayoutsView;
