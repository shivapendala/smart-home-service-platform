import React, { useState, useEffect } from 'react';
import { TrendingUp, Users, DollarSign, PieChart, Download, RefreshCw } from 'lucide-react';
import api from '../../services/api';

export const ExecutiveAnalyticsDashboard: React.FC = () => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    api.get('/analytics/dashboard')
      .then((r) => setData(r.data))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-10 space-y-8">
      <div className="border-b border-slate-800 pb-6 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-extrabold bg-gradient-to-r from-emerald-400 via-teal-400 to-cyan-400 bg-clip-text text-transparent">
            Executive Analytics & BI Engine
          </h1>
          <p className="text-slate-400 mt-1 text-sm">
            Revenue & net margin analytics, technician efficiency rankings, category heatmaps, and report exports.
          </p>
        </div>
      </div>

      {loading ? (
        <div className="flex justify-center py-20">
          <RefreshCw className="w-8 h-8 animate-spin text-teal-500" />
        </div>
      ) : data ? (
        <div className="space-y-8">
          {/* KPI Row */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
              <span className="text-xs uppercase font-semibold text-slate-400">Gross Revenue</span>
              <h2 className="text-3xl font-black text-emerald-400 mt-2">${data.revenue_summary?.total_gross_revenue}</h2>
              <span className="text-xs text-slate-500">Net margin: {data.revenue_summary?.net_margin_percentage}%</span>
            </div>
            <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
              <span className="text-xs uppercase font-semibold text-slate-400">Tax Collected</span>
              <h2 className="text-3xl font-black text-cyan-400 mt-2">${data.revenue_summary?.total_tax_collected}</h2>
              <span className="text-xs text-slate-500">Sales tax compliance</span>
            </div>
            <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
              <span className="text-xs uppercase font-semibold text-slate-400">Completed Jobs</span>
              <h2 className="text-3xl font-black text-slate-100 mt-2">{data.revenue_summary?.total_completed_bookings}</h2>
              <span className="text-xs text-slate-500">Avg ticket: ${data.revenue_summary?.avg_ticket_size}</span>
            </div>
            <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
              <span className="text-xs uppercase font-semibold text-slate-400">Discounts Allowed</span>
              <h2 className="text-3xl font-black text-purple-400 mt-2">${data.revenue_summary?.total_discount_given}</h2>
              <span className="text-xs text-slate-500">Promo codes & loyalty</span>
            </div>
          </div>

          {/* Tables */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4">
              <h3 className="text-lg font-bold text-slate-100">Top Technician Performance</h3>
              <div className="space-y-3">
                {data.top_technicians?.map((t: any) => (
                  <div key={t.technician_id} className="p-4 bg-slate-950/60 border border-slate-800 rounded-2xl flex items-center justify-between text-xs">
                    <div>
                      <h4 className="font-bold text-slate-200 text-sm">{t.technician_name}</h4>
                      <p className="text-slate-500">{t.total_jobs_completed} jobs • CSAT: {t.avg_csat_rating} ★</p>
                    </div>
                    <span className="font-bold text-emerald-400 text-sm">${t.total_revenue_generated}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4">
              <h3 className="text-lg font-bold text-slate-100">Category Revenue Heatmap</h3>
              <div className="space-y-3">
                {data.category_breakdown?.map((c: any, idx: number) => (
                  <div key={idx} className="p-4 bg-slate-950/60 border border-slate-800 rounded-2xl space-y-2">
                    <div className="flex justify-between text-xs font-bold text-slate-200">
                      <span>{c.category_name}</span>
                      <span>${c.revenue_generated} ({c.percentage_of_total}%)</span>
                    </div>
                    <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                      <div className="bg-teal-400 h-full rounded-full" style={{ width: `${c.percentage_of_total}%` }} />
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      ) : null}
    </div>
  );
};
export default ExecutiveAnalyticsDashboard;
