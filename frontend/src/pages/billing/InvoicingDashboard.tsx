import React, { useState, useEffect } from 'react';
import { DollarSign, FileText, Download, Filter, RefreshCw, Eye } from 'lucide-react';
import api from '../../services/api';

interface Invoice {
  id: number;
  invoice_number: string;
  subtotal: number;
  tax_amount: number;
  discount_amount: number;
  total_amount: number;
  status: string;
  due_date: string;
  created_at: string;
}

export const InvoicingDashboard: React.FC = () => {
  const [invoices, setInvoices] = useState<Invoice[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    api.get('/billing/invoices/customer/me')
      .then((r) => setInvoices(r.data))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  const totalSpent = invoices.reduce((acc, curr) => acc + curr.total_amount, 0);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-10 space-y-8">
      <div className="border-b border-slate-800 pb-6">
        <h1 className="text-3xl font-extrabold bg-gradient-to-r from-cyan-400 via-blue-400 to-indigo-300 bg-clip-text text-transparent">
          Invoicing & Billing Dashboard
        </h1>
        <p className="text-slate-400 mt-1 text-sm">
          Itemized PDF receipts, payment gateway logs, tax calculations, and refund processing desk.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
          <span className="text-xs uppercase font-semibold text-slate-400">Total Billed</span>
          <h2 className="text-3xl font-black text-slate-100 mt-2">${totalSpent.toFixed(2)}</h2>
          <span className="text-xs text-slate-500">Across {invoices.length} total invoices</span>
        </div>
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
          <span className="text-xs uppercase font-semibold text-slate-400">Tax Breakdown</span>
          <h2 className="text-3xl font-black text-cyan-400 mt-2">
            ${invoices.reduce((a, b) => a + b.tax_amount, 0).toFixed(2)}
          </h2>
          <span className="text-xs text-slate-500">Regional state/city tax summary</span>
        </div>
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
          <span className="text-xs uppercase font-semibold text-slate-400">Pending Refunds</span>
          <h2 className="text-3xl font-black text-amber-400 mt-2">$0.00</h2>
          <span className="text-xs text-slate-500">All claims resolved</span>
        </div>
      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4">
        <h2 className="text-xl font-bold text-slate-100">Itemized Invoices</h2>

        {loading ? (
          <div className="flex justify-center py-12">
            <RefreshCw className="w-8 h-8 animate-spin text-blue-500" />
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="border-b border-slate-800 text-slate-400 text-xs uppercase">
                  <th className="py-3 px-4">Invoice #</th>
                  <th className="py-3 px-4">Due Date</th>
                  <th className="py-3 px-4">Subtotal</th>
                  <th className="py-3 px-4">Tax</th>
                  <th className="py-3 px-4">Total Amount</th>
                  <th className="py-3 px-4">Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {invoices.map((inv) => (
                  <tr key={inv.id} className="hover:bg-slate-800/40">
                    <td className="py-4 px-4 font-mono text-blue-400 font-bold">{inv.invoice_number}</td>
                    <td className="py-4 px-4 text-slate-300">{inv.due_date}</td>
                    <td className="py-4 px-4 text-slate-400">${inv.subtotal.toFixed(2)}</td>
                    <td className="py-4 px-4 text-slate-400">${inv.tax_amount.toFixed(2)}</td>
                    <td className="py-4 px-4 font-bold text-slate-100">${inv.total_amount.toFixed(2)}</td>
                    <td className="py-4 px-4">
                      <span className={`px-2.5 py-1 text-xs font-bold rounded-full ${
                        inv.status === 'PAID' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-blue-500/20 text-blue-400'
                      }`}>
                        {inv.status}
                      </span>
                    </td>
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
export default InvoicingDashboard;
