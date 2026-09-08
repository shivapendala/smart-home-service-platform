import React from 'react';
import { Activity, ShieldCheck, AlertCircle } from 'lucide-react';

export const ApplianceHealthWidget: React.FC = () => {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-bold text-slate-100 flex items-center gap-2">
          <Activity className="w-5 h-5 text-emerald-400" /> Predictive Appliance Health Score
        </h3>
        <span className="px-3 py-1 bg-emerald-500/20 text-emerald-400 text-xs font-bold rounded-full border border-emerald-500/30">
          HEALTHY (88%)
        </span>
      </div>

      <p className="text-xs text-slate-400">
        AI predictive maintenance model analyzed 4 registered appliances. No critical failure risk detected.
      </p>

      <div className="space-y-2">
        <div className="p-3 bg-slate-950/60 border border-slate-800 rounded-xl flex items-center justify-between text-xs">
          <span className="text-slate-200">Living Room Split AC (Samsung)</span>
          <span className="text-emerald-400 font-bold">12% Risk</span>
        </div>
        <div className="p-3 bg-slate-950/60 border border-slate-800 rounded-xl flex items-center justify-between text-xs">
          <span className="text-slate-200">Kitchen Double Door Fridge</span>
          <span className="text-amber-400 font-bold">45% Risk (Filter Clean Due)</span>
        </div>
      </div>
    </div>
  );
};
export default ApplianceHealthWidget;
