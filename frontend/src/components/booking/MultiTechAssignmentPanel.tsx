import React, { useState } from 'react';
import { Users, UserPlus, Shield } from 'lucide-react';
import api from '../../services/api';

interface MultiTechPanelProps {
  bookingId: number;
}

export const MultiTechAssignmentPanel: React.FC<MultiTechPanelProps> = ({ bookingId }) => {
  const [techId, setTechId] = useState<number>(2);
  const [roleTitle, setRoleTitle] = useState('ASSISTANT_TECHNICIAN');
  const [assignments, setAssignments] = useState<any[]>([]);

  const handleAssign = async () => {
    try {
      const res = await api.post('/booking-engine/multi-tech', {
        booking_id: bookingId,
        technician_id: techId,
        role_title: roleTitle
      });
      setAssignments([...assignments, res.data]);
    } catch (err) {
      console.error('Assignment failed', err);
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4">
      <h3 className="text-lg font-bold text-slate-100 flex items-center gap-2">
        <Users className="w-5 h-5 text-indigo-400" /> Multi-Technician Complex Job Crew
      </h3>
      <p className="text-xs text-slate-400">Assign secondary specialists or lead technicians for multi-hour industrial jobs.</p>

      <div className="flex gap-3">
        <input
          type="number"
          value={techId}
          onChange={(e) => setTechId(Number(e.target.value))}
          placeholder="Tech User ID"
          className="bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-100 w-32"
        />
        <select
          value={roleTitle}
          onChange={(e) => setRoleTitle(e.target.value)}
          className="bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-100 flex-1"
        >
          <option value="LEAD_TECHNICIAN">Lead Technician</option>
          <option value="ASSISTANT_TECHNICIAN">Assistant Technician</option>
          <option value="ELECTRICAL_SPECIALIST">Electrical Specialist</option>
          <option value="GAS_WELDING_EXPERT">Gas Welding Expert</option>
        </select>
        <button
          onClick={handleAssign}
          className="inline-flex items-center gap-1 bg-indigo-600 hover:bg-indigo-500 text-white font-medium px-4 py-2 rounded-xl text-sm transition-all"
        >
          <UserPlus className="w-4 h-4" /> Add Crew Member
        </button>
      </div>

      <div className="space-y-2 pt-2">
        {assignments.map((a, idx) => (
          <div key={idx} className="p-3 bg-slate-950/60 border border-slate-800 rounded-xl flex items-center justify-between text-xs">
            <span className="text-slate-300">Technician ID #{a.technician_id}</span>
            <span className="px-2.5 py-1 bg-indigo-500/20 text-indigo-300 font-bold rounded-lg border border-indigo-500/30">
              {a.role_title}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
export default MultiTechAssignmentPanel;
