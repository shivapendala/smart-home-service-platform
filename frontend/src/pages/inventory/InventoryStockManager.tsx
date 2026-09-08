import React, { useState, useEffect } from 'react';
import { Package, Truck, AlertTriangle, Plus, RefreshCw } from 'lucide-react';
import api from '../../services/api';

interface SparePart {
  id: number;
  sku: string;
  part_name: string;
  category_name: string;
  cost_price: number;
  selling_price: number;
  reorder_threshold: number;
}

export const InventoryStockManager: React.FC = () => {
  const [parts, setParts] = useState<SparePart[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    api.get('/inventory/parts')
      .then((r) => setParts(r.data))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-10 space-y-8">
      <div className="border-b border-slate-800 pb-6 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-extrabold bg-gradient-to-r from-orange-400 via-amber-400 to-yellow-300 bg-clip-text text-transparent">
            Central Warehouse & Van Inventory
          </h1>
          <p className="text-slate-400 mt-1 text-sm">
            Stock check-in/out, reorder thresholds, SKU tracking, and technician van inventory audits.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
          <span className="text-xs uppercase font-semibold text-slate-400">Total Unique SKUs</span>
          <h2 className="text-3xl font-black text-slate-100 mt-2">{parts.length}</h2>
          <span className="text-xs text-slate-500">Active catalog items</span>
        </div>
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
          <span className="text-xs uppercase font-semibold text-slate-400">Reorder Alerts</span>
          <h2 className="text-3xl font-black text-amber-400 mt-2">1 Item Low</h2>
          <span className="text-xs text-slate-500">Below threshold level</span>
        </div>
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
          <span className="text-xs uppercase font-semibold text-slate-400">Van Inventory Assigned</span>
          <h2 className="text-3xl font-black text-emerald-400 mt-2">12 Vans</h2>
          <span className="text-xs text-slate-500">Active mobile stock</span>
        </div>
      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4">
        <h2 className="text-xl font-bold text-slate-100">Spare Parts Catalog</h2>

        {loading ? (
          <div className="flex justify-center py-12">
            <RefreshCw className="w-8 h-8 animate-spin text-amber-500" />
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="border-b border-slate-800 text-slate-400 text-xs uppercase">
                  <th className="py-3 px-4">SKU</th>
                  <th className="py-3 px-4">Part Name</th>
                  <th className="py-3 px-4">Category</th>
                  <th className="py-3 px-4">Cost Price</th>
                  <th className="py-3 px-4">Retail Price</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {parts.map((p) => (
                  <tr key={p.id} className="hover:bg-slate-800/40">
                    <td className="py-4 px-4 font-mono text-amber-400 font-bold">{p.sku}</td>
                    <td className="py-4 px-4 font-semibold text-slate-100">{p.part_name}</td>
                    <td className="py-4 px-4 text-slate-400">{p.category_name}</td>
                    <td className="py-4 px-4 text-slate-400">${p.cost_price.toFixed(2)}</td>
                    <td className="py-4 px-4 font-bold text-emerald-400">${p.selling_price.toFixed(2)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};
export default InventoryStockManager;
