import React, { useState, useEffect } from 'react';
import { MapPin, Plus, Navigation, Trash2, CheckCircle2 } from 'lucide-react';
import api from '../../services/api';

interface ServiceZone {
  id: number;
  zone_name: string;
  zip_code: string;
  city: string;
  state: string;
  radius_km: number;
  is_primary_zone: boolean;
}

export const ZoneCoverageManager: React.FC = () => {
  const [zones, setZones] = useState<ServiceZone[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [formData, setFormData] = useState({
    zone_name: 'Metro Center Zone',
    zip_code: '90210',
    city: 'Los Angeles',
    state: 'CA',
    radius_km: 15.0,
    is_primary_zone: true
  });

  const fetchZones = async () => {
    setLoading(true);
    try {
      const res = await api.get('/technicians/management/zones/me');
      setZones(res.data);
    } catch (err) {
      console.error('Failed to fetch zones', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchZones();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/technicians/management/zones', formData);
      fetchZones();
    } catch (err) {
      console.error('Zone save failed', err);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-10 space-y-8">
      <div className="border-b border-slate-800 pb-6">
        <h1 className="text-3xl font-extrabold bg-gradient-to-r from-teal-400 via-emerald-400 to-green-300 bg-clip-text text-transparent">
          Geo-Fence Service Zones
        </h1>
        <p className="text-slate-400 mt-1 text-sm">
          Define assigned zip codes, geographic bounding boxes, and travel radius limits for dispatch matching.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl space-y-6">
          <h2 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <MapPin className="w-5 h-5 text-teal-400" /> Add Service Zone
          </h2>

          <form onSubmit={handleSubmit} className="space-y-4 text-sm">
            <div>
              <label className="block text-slate-400 mb-1">Zone Name</label>
              <input
                type="text"
                required
                value={formData.zone_name}
                onChange={(e) => setFormData({ ...formData, zone_name: e.target.value })}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100"
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-slate-400 mb-1">Zip Code</label>
                <input
                  type="text"
                  required
                  value={formData.zip_code}
                  onChange={(e) => setFormData({ ...formData, zip_code: e.target.value })}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100 font-mono"
                />
              </div>
              <div>
                <label className="block text-slate-400 mb-1">Radius (km)</label>
                <input
                  type="number"
                  value={formData.radius_km}
                  onChange={(e) => setFormData({ ...formData, radius_km: Number(e.target.value) })}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100"
                />
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-slate-400 mb-1">City</label>
                <input
                  type="text"
                  required
                  value={formData.city}
                  onChange={(e) => setFormData({ ...formData, city: e.target.value })}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100"
                />
              </div>
              <div>
                <label className="block text-slate-400 mb-1">State</label>
                <input
                  type="text"
                  required
                  value={formData.state}
                  onChange={(e) => setFormData({ ...formData, state: e.target.value })}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-slate-100"
                />
              </div>
            </div>

            <button
              type="submit"
              className="w-full inline-flex items-center justify-center gap-2 bg-gradient-to-r from-teal-600 to-emerald-600 hover:from-teal-500 hover:to-emerald-500 text-white font-semibold py-3 rounded-xl shadow-lg shadow-teal-600/30 transition-all"
            >
              <Plus className="w-5 h-5" /> Add Geo-Zone
            </button>
          </form>
        </div>

        <div className="lg:col-span-2 space-y-4">
          <h2 className="text-xl font-bold text-slate-100">Covered Zip-Code Regions</h2>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {zones.map((z) => (
              <div key={z.id} className="bg-slate-900 border border-slate-800 rounded-2xl p-6 space-y-3">
                <div className="flex items-center justify-between">
                  <h3 className="font-bold text-slate-100 text-lg">{z.zone_name}</h3>
                  <span className="px-3 py-1 bg-teal-500/20 text-teal-400 border border-teal-500/30 text-xs font-mono font-bold rounded-full">
                    {z.zip_code}
                  </span>
                </div>
                <p className="text-slate-400 text-xs flex items-center gap-2">
                  <Navigation className="w-4 h-4 text-teal-400" /> {z.city}, {z.state} ({z.radius_km} km radius)
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
export default ZoneCoverageManager;
