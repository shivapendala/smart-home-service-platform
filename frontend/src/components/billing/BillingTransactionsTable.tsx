import React from 'react';
import { CreditCard, CheckCircle2, RefreshCcw } from 'lucide-react';

export const BillingTransactionsTable: React.FC = () => {
  const transactions = [
    { id: 'TXN-998811', date: '2026-08-20', provider: 'Stripe Gateway', amount: 120.00, status: 'SUCCESS' },
    { id: 'TXN-998812', date: '2026-08-15', provider: 'PayPal Express', amount: 85.50, status: 'SUCCESS' },
    { id: 'TXN-998813', date: '2026-08-10', provider: 'Mock Gateway', amount: 45.00, status: 'SUCCESS' }
  ];

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4">
      <h3 className="text-lg font-bold text-slate-100 flex items-center gap-2">
        <CreditCard className="w-5 h-5 text-cyan-400" /> Gateway Audit Trail
      </h3>

      <div className="space-y-3">
        {transactions.map((t) => (
          <div key={t.id} className="p-4 bg-slate-950/60 border border-slate-800 rounded-2xl flex items-center justify-between text-xs">
            <div>
              <span className="font-mono text-cyan-400 font-bold">{t.id}</span>
              <p className="text-slate-400 mt-0.5">{t.provider} • {t.date}</p>
            </div>
            <div className="text-right">
              <span className="font-bold text-slate-100 text-sm">${t.amount.toFixed(2)}</span>
              <p className="text-emerald-400 flex items-center justify-end gap-1 font-semibold mt-0.5">
                <CheckCircle2 className="w-3.5 h-3.5" /> {t.status}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
export default BillingTransactionsTable;
