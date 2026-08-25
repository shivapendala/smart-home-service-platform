import React from 'react';
import { Printer, Download, X, FileText } from 'lucide-react';

interface InvoiceViewerProps {
  isOpen: boolean;
  onClose: () => void;
  invoice: any;
}

export const InvoiceViewerModal: React.FC<InvoiceViewerProps> = ({ isOpen, onClose, invoice }) => {
  if (!isOpen || !invoice) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
      <div className="bg-slate-900 border border-slate-800 w-full max-w-2xl rounded-3xl p-8 shadow-2xl space-y-6 relative">
        <button onClick={onClose} className="absolute right-6 top-6 text-slate-500 hover:text-slate-200">
          <X className="w-5 h-5" />
        </button>

        <div className="flex justify-between items-start border-b border-slate-800 pb-6">
          <div>
            <h2 className="text-2xl font-black text-slate-100">TAX INVOICE</h2>
            <p className="text-xs text-blue-400 font-mono mt-1">{invoice.invoice_number}</p>
          </div>
          <button onClick={() => window.print()} className="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs px-4 py-2 rounded-xl">
            <Printer className="w-4 h-4" /> Print / Save PDF
          </button>
        </div>

        <div className="grid grid-cols-2 gap-4 text-xs text-slate-400">
          <div>
            <span className="uppercase font-bold text-slate-500">Billed To</span>
            <p className="text-slate-200 font-semibold text-sm mt-1">Valued Smart Home Customer</p>
          </div>
          <div className="text-right">
            <span className="uppercase font-bold text-slate-500">Invoice Date & Status</span>
            <p className="text-slate-200 font-semibold text-sm mt-1">{invoice.created_at?.slice(0, 10)} • <span className="text-emerald-400">{invoice.status}</span></p>
          </div>
        </div>

        <div className="bg-slate-950/60 border border-slate-800 rounded-2xl p-4">
          <table className="w-full text-xs text-left">
            <thead>
              <tr className="border-b border-slate-800 text-slate-500 uppercase">
                <th className="py-2">Description</th>
                <th className="py-2">Qty</th>
                <th className="py-2">Unit Price</th>
                <th className="py-2 text-right">Total</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {invoice.items?.map((item: any, idx: number) => (
                <tr key={idx}>
                  <td className="py-2.5 text-slate-200">{item.item_description}</td>
                  <td className="py-2.5 text-slate-400">{item.quantity}</td>
                  <td className="py-2.5 text-slate-400">${item.unit_price}</td>
                  <td className="py-2.5 text-right font-semibold text-slate-200">${item.total_price}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="flex justify-end text-sm space-y-1 text-right">
          <div className="w-48 space-y-1">
            <div className="flex justify-between text-xs text-slate-400">
              <span>Subtotal:</span>
              <span>${invoice.subtotal}</span>
            </div>
            <div className="flex justify-between text-xs text-slate-400">
              <span>Tax Rate (8.5%):</span>
              <span>${invoice.tax_amount}</span>
            </div>
            <div className="flex justify-between font-extrabold text-slate-100 text-base border-t border-slate-800 pt-2">
              <span>Total Paid:</span>
              <span className="text-emerald-400">${invoice.total_amount}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default InvoiceViewerModal;
