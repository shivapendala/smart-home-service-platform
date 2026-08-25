import React, { useState } from 'react';
import { Download, FileSpreadsheet } from 'lucide-react';
import api from '../../services/api';

export const ReportExportModal: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [reportType, setReportType] = useState('REVENUE_MARGIN');

  if (!isOpen) return null;

  const handleExport = async () => {
    try {
      const response = await api.post(
        '/analytics/export-csv',
        {
          report_type: reportType,
          start_date: '2026-08-01',
          end_date: '2026-08-25'
        },
        { responseType: 'blob' }
      );

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `report_${reportType.toLowerCase()}.csv`);
      document.body.appendChild(link);
      link.click();
      onClose();
    } catch (err) {
      console.error('CSV Export Error', err);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
      <div className="bg-slate-900 border border-slate-800 w-full max-w-lg rounded-3xl p-6 shadow-2xl space-y-6">
        <div className="flex items-center gap-3">
          <div className="p-3 bg-emerald-500/10 border border-emerald-500/30 rounded-2xl">
            <FileSpreadsheet className="w-6 h-6 text-emerald-400" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-slate-100">Export Business Intelligence CSV</h2>
            <p className="text-xs text-slate-400">Download formatted financial and operational metrics.</p>
          </div>
        </div>

        <div className="space-y-4 text-sm">
          <div>
            <label className="block text-slate-400 mb-1">Select Report Type</label>
            <select
              value={reportType}
              onChange={(e) => setReportType(e.target.value)}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-100"
            >
              <option value="REVENUE_MARGIN">Revenue & Net Margin Report</option>
              <option value="TECH_EFFICIENCY">Technician Efficiency & Utilization</option>
              <option value="CATEGORY_HEATMAP">Service Category Heatmap</option>
            </select>
          </div>

          <div className="flex justify-end gap-3 pt-4 border-t border-slate-800">
            <button onClick={onClose} className="px-4 py-2 text-slate-400">Cancel</button>
            <button onClick={handleExport} className="inline-flex items-center gap-2 px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl">
              <Download className="w-4 h-4" /> Download CSV
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
export default ReportExportModal;
