import React, { useState, useEffect } from 'react';
import { Calendar, Clock, Plus, CheckCircle, RefreshCw } from 'lucide-react';
import api from '../../services/api';

interface Shift {
  id: number;
  day_of_week: string;
  shift_start: string;
  shift_end: string;
  break_start?: string;
  break_end?: string;
  is_active: boolean;
  max_jobs_per_shift: number;
}

export const ShiftScheduler: React.FC = () => {
  const [shifts, setShifts] = useState<Shift[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [formData, setFormData] = useState({
    day_of_week: 'MONDAY',
    shift_start: '08:00',
    shift_end: '17:00',
    break_start: '12:00',
    break_end: '13:00',
    max_jobs_per_shift: 6
  });

  const fetchShifts = async () => {
    setLoading(true);
    try {
      const res = await api.get('/technicians/management/shifts/me');
      setShifts(res.data);
    } catch (err) {
      console.error('Failed to fetch shifts', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchShifts();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/technicians/management/shifts', formData);
      fetchShifts();
    } catch (err) {
      console.error('Shift creation failed', err);
    }
  };

  const days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'];

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-10 space-y-8">
      <div className="border-b border-slate-800 pb-6">
        <h1 className="text-3xl font-extrabold bg-gradient-to-r from-emerald-400 via-teal-400 to-cyan-300 bg-clip-text text-transparent">
          Shift Roster & Work Availability
        </h1>
        <p className="text-slate-400 mt-1 text-sm">
          Set up weekly working hours, break schedules, and maximum job capacity limits per shift.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Roster Config Form */}
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl space-y-6">
          <h2 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <Clock className="w-5 h-5 text-emerald-400" /> Configure Shift Day
          </h2>

          <form onSubmit={handleSubmit} className="space-y-4 text-sm">
            <div>
              <label className="block text-slate-400 mb-1">Day of Week</label>
              <select
                value={formData.day_of_week}
                onChange={(e) => setFormData({ ...formData, day_of_week: e.target.value })}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2.5 text-slate-100 focus:outline-none focus:border-emerald-500"
              >
                {days.map((d) => (
                  <option key={d} value={d}>{d}</option>
                ))}
              </select>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-slate-400 mb-1">Shift Start</label>
                <input
                  type="time"
                  value={formData.shift_start}
                  onChange={(e) => setFormData({ ...formData, shift_start: e.target.value })}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100"
                />
              </div>
              <div>
                <label className="block text-slate-400 mb-1">Shift End</label>
                <input
                  type="time"
                  value={formData.shift_end}
                  onChange={(e) => setFormData({ ...formData, shift_end: e.target.value })}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100"
                />
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-slate-400 mb-1">Break Start</label>
                <input
                  type="time"
                  value={formData.break_start}
                  onChange={(e) => setFormData({ ...formData, break_start: e.target.value })}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100"
                />
              </div>
              <div>
                <label className="block text-slate-400 mb-1">Break End</label>
                <input
                  type="time"
                  value={formData.break_end}
                  onChange={(e) => setFormData({ ...formData, break_end: e.target.value })}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100"
                />
              </div>
            </div>

            <div>
              <label className="block text-slate-400 mb-1">Max Jobs Per Shift</label>
              <input
                type="number"
                min={1}
                max={12}
                value={formData.max_jobs_per_shift}
                onChange={(e) => setFormData({ ...formData, max_jobs_per_shift: Number(e.target.value) })}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100"
              />
            </div>

            <button
              type="submit"
              className="w-full inline-flex items-center justify-center gap-2 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-semibold py-3 rounded-xl shadow-lg shadow-emerald-600/30 transition-all"
            >
              <Plus className="w-5 h-5" /> Save Shift Roster
            </button>
          </form>
        </div>

        {/* Shift Roster Grid */}
        <div className="lg:col-span-2 space-y-4">
          <h2 className="text-xl font-bold text-slate-100">Weekly Working Roster</h2>

          {loading ? (
            <div className="flex justify-center py-12">
              <RefreshCw className="w-8 h-8 animate-spin text-emerald-500" />
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {days.map((d) => {
                const shift = shifts.find((s) => s.day_of_week === d);
                return (
                  <div
                    key={d}
                    className={`p-5 rounded-2xl border ${
                      shift
                        ? 'bg-slate-900/80 border-emerald-500/30 text-slate-100'
                        : 'bg-slate-950/50 border-slate-800/80 text-slate-500'
                    }`}
                  >
                    <div className="flex items-center justify-between mb-3">
                      <span className="font-bold uppercase tracking-wider text-sm">{d}</span>
                      {shift ? (
                        <span className="px-2.5 py-0.5 text-xs rounded-full bg-emerald-500/20 text-emerald-400 font-semibold border border-emerald-500/30">
                          Active Shift
                        </span>
                      ) : (
                        <span className="text-xs italic text-slate-600">Day Off</span>
                      )}
                    </div>

                    {shift ? (
                      <div className="space-y-1 text-xs text-slate-300">
                        <p>Hours: <span className="font-mono text-emerald-400">{shift.shift_start} - {shift.shift_end}</span></p>
                        {shift.break_start && (
                          <p>Break: <span className="font-mono text-slate-400">{shift.break_start} - {shift.break_end}</span></p>
                        )}
                        <p className="text-slate-400 pt-1">Capacity: {shift.max_jobs_per_shift} max jobs</p>
                      </div>
                    ) : (
                      <p className="text-xs text-slate-600">No shift scheduled</p>
                    )}
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
export default ShiftScheduler;
