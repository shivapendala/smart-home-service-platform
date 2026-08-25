import React, { useState, useEffect } from 'react';
import { 
  Plus, Shield, Wrench, Calendar, AlertCircle, CheckCircle, 
  Trash2, Edit3, Cpu, RefreshCw, ChevronRight 
} from 'lucide-react';
import api from '../../services/api';

interface CustomerAppliance {
  id: number;
  brand: string;
  model_number: string;
  serial_number?: string;
  appliance_type: string;
  installation_year?: number;
  condition: string;
  notes?: string;
  room_location?: string;
}

export const CustomerApplianceManager: React.FC = () => {
  const [appliances, setAppliances] = useState<CustomerAppliance[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [isModalOpen, setIsModalOpen] = useState<boolean>(false);
  const [formData, setFormData] = useState({
    brand: '',
    model_number: '',
    serial_number: '',
    appliance_type: 'Split AC',
    installation_year: 2023,
    condition: 'EXCELLENT',
    notes: '',
    room_location: 'Living Room'
  });

  const fetchAppliances = async () => {
    setLoading(true);
    try {
      const res = await api.get('/customer-portal/appliances');
      setAppliances(res.data);
    } catch (err) {
      console.error('Failed to fetch appliances', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAppliances();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/customer-portal/appliances', formData);
      setIsModalOpen(false);
      fetchAppliances();
    } catch (err) {
      console.error('Error saving appliance', err);
    }
  };

  const handleDelete = async (id: number) => {
    if (!window.confirm('Remove this appliance from your registry?')) return;
    try {
      await api.delete(`/customer-portal/appliances/${id}`);
      fetchAppliances();
    } catch (err) {
      console.error('Delete failed', err);
    }
  };

  const getConditionBadge = (condition: string) => {
    switch (condition) {
      case 'EXCELLENT':
        return <span className="px-3 py-1 text-xs font-semibold rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">Excellent Condition</span>;
      case 'GOOD':
        return <span className="px-3 py-1 text-xs font-semibold rounded-full bg-blue-500/20 text-blue-400 border border-blue-500/30">Good</span>;
      case 'FAIR':
        return <span className="px-3 py-1 text-xs font-semibold rounded-full bg-amber-500/20 text-amber-400 border border-amber-500/30">Maintenance Due</span>;
      default:
        return <span className="px-3 py-1 text-xs font-semibold rounded-full bg-rose-500/20 text-rose-400 border border-rose-500/30">Critical Repair</span>;
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-10 space-y-8">
      {/* Header Banner */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-3xl font-extrabold bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400 bg-clip-text text-transparent">
            Household Appliance Registry
          </h1>
          <p className="text-slate-400 mt-1 text-sm">
            Track your smart appliances, monitor warranty deadlines, and schedule instant diagnostic repairs.
          </p>
        </div>
        <button
          onClick={() => setIsModalOpen(true)}
          className="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-medium px-5 py-2.5 rounded-xl shadow-lg shadow-blue-600/25 transition-all"
        >
          <Plus className="w-5 h-5" />
          Register New Appliance
        </button>
      </div>

      {/* Appliance Grid */}
      {loading ? (
        <div className="flex justify-center items-center py-20 text-slate-400">
          <RefreshCw className="w-8 h-8 animate-spin text-blue-500" />
        </div>
      ) : appliances.length === 0 ? (
        <div className="text-center py-16 bg-slate-900/50 border border-dashed border-slate-800 rounded-2xl p-8">
          <Cpu className="w-12 h-12 text-slate-600 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-slate-300">No Appliances Registered</h3>
          <p className="text-slate-500 text-sm max-w-md mx-auto mt-1">
            Register your air conditioners, refrigerators, and appliances to unlock automated maintenance alerts and express support.
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {appliances.map((item) => (
            <div
              key={item.id}
              className="bg-slate-900/80 backdrop-blur-xl border border-slate-800 hover:border-slate-700 rounded-2xl p-6 shadow-xl transition-all duration-300 flex flex-col justify-between"
            >
              <div>
                <div className="flex items-start justify-between mb-4">
                  <div>
                    <span className="text-xs uppercase font-bold tracking-wider text-blue-400">{item.brand}</span>
                    <h3 className="text-xl font-bold text-slate-100">{item.appliance_type}</h3>
                  </div>
                  {getConditionBadge(item.condition)}
                </div>

                <div className="space-y-2 text-sm text-slate-400 mb-6">
                  <div className="flex items-center justify-between border-b border-slate-800/60 pb-2">
                    <span>Model Number:</span>
                    <span className="font-mono text-slate-200">{item.model_number}</span>
                  </div>
                  <div className="flex items-center justify-between border-b border-slate-800/60 pb-2">
                    <span>Location:</span>
                    <span className="text-slate-200">{item.room_location || 'General'}</span>
                  </div>
                  <div className="flex items-center justify-between border-b border-slate-800/60 pb-2">
                    <span>Install Year:</span>
                    <span className="text-slate-200">{item.installation_year || 'N/A'}</span>
                  </div>
                  {item.notes && (
                    <p className="text-xs text-slate-500 pt-2 italic">
                      "{item.notes}"
                    </p>
                  )}
                </div>
              </div>

              <div className="flex items-center justify-between pt-4 border-t border-slate-800 gap-2">
                <button
                  onClick={() => handleDelete(item.id)}
                  className="p-2 text-slate-500 hover:text-rose-400 hover:bg-rose-500/10 rounded-lg transition-colors"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
                <button className="flex-1 inline-flex items-center justify-center gap-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold py-2 px-3 rounded-lg transition-colors">
                  <Wrench className="w-3.5 h-3.5" /> Book Diagnostic Service
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Registration Modal */}
      {isModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
          <div className="bg-slate-900 border border-slate-800 w-full max-w-lg rounded-2xl p-6 shadow-2xl space-y-6">
            <h2 className="text-xl font-bold text-slate-100">Register New Appliance</h2>
            <form onSubmit={handleSubmit} className="space-y-4 text-sm">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-slate-400 mb-1">Brand Name</label>
                  <input
                    type="text"
                    required
                    value={formData.brand}
                    onChange={(e) => setFormData({ ...formData, brand: e.target.value })}
                    placeholder="e.g. Samsung"
                    className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
                  />
                </div>
                <div>
                  <label className="block text-slate-400 mb-1">Appliance Type</label>
                  <select
                    value={formData.appliance_type}
                    onChange={(e) => setFormData({ ...formData, appliance_type: e.target.value })}
                    className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
                  >
                    <option value="Split AC">Split AC</option>
                    <option value="Double Door Refrigerator">Double Door Refrigerator</option>
                    <option value="Washing Machine">Washing Machine</option>
                    <option value="Water Heater / Geyser">Water Heater / Geyser</option>
                    <option value="Microwave Oven">Microwave Oven</option>
                  </select>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-slate-400 mb-1">Model Number</label>
                  <input
                    type="text"
                    required
                    value={formData.model_number}
                    onChange={(e) => setFormData({ ...formData, model_number: e.target.value })}
                    placeholder="e.g. RT28T3722S8"
                    className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
                  />
                </div>
                <div>
                  <label className="block text-slate-400 mb-1">Room Location</label>
                  <input
                    type="text"
                    value={formData.room_location}
                    onChange={(e) => setFormData({ ...formData, room_location: e.target.value })}
                    placeholder="e.g. Master Bedroom"
                    className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
                  />
                </div>
              </div>

              <div className="flex justify-end gap-3 pt-4 border-t border-slate-800">
                <button
                  type="button"
                  onClick={() => setIsModalOpen(false)}
                  className="px-4 py-2 text-slate-400 hover:text-slate-200 transition-colors"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-5 py-2 bg-blue-600 hover:bg-blue-500 text-white font-medium rounded-xl transition-all shadow-lg shadow-blue-600/30"
                >
                  Save Appliance
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
export default CustomerApplianceManager;
