import React, { useState } from 'react';
import { Cpu, CheckCircle2, AlertCircle, ArrowRight } from 'lucide-react';
import api from '../../services/api';

export const SmartDiagnosticWizard: React.FC = () => {
  const [applianceType, setApplianceType] = useState('AC');
  const [symptomInput, setSymptomInput] = useState('No Cooling, Water Leakage');
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleDiagnose = async () => {
    setLoading(true);
    try {
      const res = await api.post('/ai/diagnose', {
        appliance_type: applianceType,
        symptoms: symptomInput.split(',').map((s) => s.trim()),
        appliance_age_years: 3
      });
      setResult(res.data);
    } catch (err) {
      console.error('Diagnostic error', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-6">
      <div className="flex items-center gap-3 border-b border-slate-800 pb-4">
        <div className="p-3 bg-cyan-500/10 border border-cyan-500/30 rounded-2xl">
          <Cpu className="w-6 h-6 text-cyan-400" />
        </div>
        <div>
          <h2 className="text-xl font-bold text-slate-100">AI Symptom Diagnostic Wizard</h2>
          <p className="text-xs text-slate-400">Decision tree trouble-shooting engine for instant problem classification.</p>
        </div>
      </div>

      <div className="space-y-4 text-sm">
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-slate-400 mb-1">Appliance Type</label>
            <select
              value={applianceType}
              onChange={(e) => setApplianceType(e.target.value)}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100"
            >
              <option value="AC">Air Conditioner (AC)</option>
              <option value="Refrigerator">Refrigerator</option>
              <option value="Washing Machine">Washing Machine</option>
              <option value="Electrical Panel">Electrical Panel</option>
            </select>
          </div>
          <div>
            <label className="block text-slate-400 mb-1">Observed Symptoms (Comma separated)</label>
            <input
              type="text"
              value={symptomInput}
              onChange={(e) => setSymptomInput(e.target.value)}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100"
            />
          </div>
        </div>

        <button
          onClick={handleDiagnose}
          className="w-full bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white font-bold py-2.5 rounded-xl shadow-lg shadow-cyan-600/25 transition-all"
        >
          Run AI Troubleshooter
        </button>

        {result && (
          <div className="p-5 bg-slate-950/80 border border-cyan-500/30 rounded-2xl space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-cyan-400 uppercase">Diagnosed Root Cause</span>
              <span className="px-2.5 py-0.5 text-xs rounded-full bg-emerald-500/20 text-emerald-400 font-bold">
                {result.confidence_score_percent}% Confidence
              </span>
            </div>

            <h3 className="text-lg font-bold text-slate-100">{result.diagnosed_root_cause}</h3>
            <p className="text-xs text-slate-400">{result.recommended_action}</p>

            <div className="flex items-center justify-between text-xs pt-2 border-t border-slate-800 text-slate-300">
              <span>Category: <strong className="text-slate-100">{result.suggested_service_category}</strong></span>
              <span>Estimated Cost: <strong className="text-emerald-400">{result.estimated_cost_range}</strong></span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
export default SmartDiagnosticWizard;
