import React, { useState, useEffect } from 'react';
import { Bell, X, Check, Mail, Smartphone } from 'lucide-react';
import api from '../../services/api';

interface CommLog {
  id: number;
  channel: string;
  destination: string;
  subject?: string;
  content: string;
  status: string;
  sent_at: string;
}

export const NotificationCenterDrawer: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [logs, setLogs] = useState<CommLog[]>([]);

  useEffect(() => {
    if (isOpen) {
      api.get('/communication/logs/me').then((r) => setLogs(r.data)).catch(() => {});
    }
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-y-0 right-0 z-50 w-full max-w-md bg-slate-900 border-l border-slate-800 p-6 shadow-2xl space-y-6 flex flex-col">
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <h2 className="text-xl font-bold text-slate-100 flex items-center gap-2">
          <Bell className="w-5 h-5 text-amber-400" /> Notifications & Alerts
        </h2>
        <button onClick={onClose} className="text-slate-500 hover:text-slate-200">
          <X className="w-5 h-5" />
        </button>
      </div>

      <div className="flex-1 overflow-y-auto space-y-3">
        {logs.map((log) => (
          <div key={log.id} className="p-4 bg-slate-950/60 border border-slate-800 rounded-2xl space-y-2 text-xs">
            <div className="flex items-center justify-between">
              <span className="font-bold text-slate-300 uppercase flex items-center gap-1">
                {log.channel === 'SMS' ? <Smartphone className="w-3.5 h-3.5 text-blue-400" /> : <Mail className="w-3.5 h-3.5 text-purple-400" />}
                {log.channel}
              </span>
              <span className="text-[10px] text-slate-500">{log.sent_at?.slice(0, 10)}</span>
            </div>
            <p className="text-slate-200 font-medium">{log.subject || 'Platform Alert'}</p>
            <p className="text-slate-400">{log.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
export default NotificationCenterDrawer;
