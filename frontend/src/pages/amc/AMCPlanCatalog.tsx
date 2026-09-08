import React, { useState, useEffect } from 'react';
import { ShieldCheck, Check, Star, Zap, RefreshCw } from 'lucide-react';
import api from '../../services/api';

interface AMCPlan {
  id: number;
  plan_name: string;
  tier: string;
  description: string;
  annual_price: number;
  duration_months: number;
  covered_visits_per_year: number;
  discount_on_spare_parts: number;
}

export const AMCPlanCatalog: React.FC = () => {
  const [plans, setPlans] = useState<AMCPlan[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    api.get('/amc-warranty/plans')
      .then((r) => setPlans(r.data))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  const handleSubscribe = async (planId: number) => {
    try {
      await api.post('/amc-warranty/subscribe', {
        amc_plan_id: planId,
        start_date: new Date().toISOString().slice(0, 10),
        is_auto_renew: true
      });
      alert('AMC Subscription Activated Successfully!');
    } catch (err) {
      console.error('Subscription error', err);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-10 space-y-8">
      <div className="border-b border-slate-800 pb-6 text-center max-w-2xl mx-auto">
        <h1 className="text-4xl font-black bg-gradient-to-r from-purple-400 via-pink-400 to-rose-300 bg-clip-text text-transparent">
          Annual Maintenance Contracts (AMC)
        </h1>
        <p className="text-slate-400 mt-2 text-sm">
          Protect your home appliances with year-round preventative inspections, 24/7 priority call-outs, and discounted spare parts.
        </p>
      </div>

      {loading ? (
        <div className="flex justify-center py-20">
          <RefreshCw className="w-8 h-8 animate-spin text-purple-500" />
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {plans.map((p) => (
            <div key={p.id} className="bg-slate-900 border border-slate-800 hover:border-purple-500/40 rounded-3xl p-8 shadow-2xl flex flex-col justify-between space-y-6 relative overflow-hidden">
              <div>
                <span className="text-xs font-bold tracking-widest text-purple-400 uppercase">{p.tier}</span>
                <h3 className="text-2xl font-extrabold text-slate-100 mt-1">{p.plan_name}</h3>
                <div className="my-4">
                  <span className="text-4xl font-black text-slate-100">${p.annual_price}</span>
                  <span className="text-xs text-slate-400"> / {p.duration_months} Months</span>
                </div>
                <p className="text-slate-400 text-xs leading-relaxed">{p.description}</p>

                <div className="space-y-3 pt-6 text-xs text-slate-300 border-t border-slate-800/80 my-6">
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span><strong>{p.covered_visits_per_year} Free Inspection Visits</strong> per year</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span><strong>{p.discount_on_spare_parts}% Discount</strong> on all genuine spare parts</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span>Priority Emergency Dispatch under 2 Hours</span>
                  </div>
                </div>
              </div>

              <button
                onClick={() => handleSubscribe(p.id)}
                className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 text-white font-bold py-3 rounded-2xl transition-all shadow-lg shadow-purple-600/25"
              >
                Subscribe Now
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
export default AMCPlanCatalog;
