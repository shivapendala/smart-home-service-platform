import React, { useState, useEffect } from 'react';
import { ShieldCheck, Calendar, RefreshCw, CheckCircle2 } from 'lucide-react';
import api from '../../services/api';

interface Subscription {
  id: number;
  start_date: string;
  expiry_date: string;
  visits_remaining: number;
  is_active: boolean;
  amc_plan?: {
    plan_name: string;
    tier: string;
  };
}

export const SubscriptionManager: React.FC = () => {
  const [subs, setSubs] = useState<Subscription[]>([]);

  useEffect(() => {
    api.get('/amc-warranty/subscriptions/me').then((r) => setSubs(r.data)).catch(() => {});
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-10 space-y-8">
      <div className="border-b border-slate-800 pb-6">
        <h1 className="text-3xl font-extrabold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
          My Active AMC Protection Contracts
        </h1>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {subs.map((s) => (
          <div key={s.id} className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-purple-400 uppercase">{s.amc_plan?.tier || 'ACTIVE PLAN'}</span>
              <span className="px-3 py-1 bg-emerald-500/20 text-emerald-400 text-xs font-bold rounded-full border border-emerald-500/30">
                ACTIVE
              </span>
            </div>

            <h2 className="text-xl font-bold text-slate-100">{s.amc_plan?.plan_name || 'Home Protection Plan'}</h2>

            <div className="grid grid-cols-2 gap-4 bg-slate-950/60 p-4 rounded-2xl border border-slate-800 text-xs">
              <div>
                <span className="text-slate-500">Contract Expiry</span>
                <p className="font-semibold text-slate-200 mt-0.5">{s.expiry_date}</p>
              </div>
              <div>
                <span className="text-slate-500">Remaining Visits</span>
                <p className="font-extrabold text-purple-400 text-base mt-0.5">{s.visits_remaining} Visits</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
export default SubscriptionManager;
