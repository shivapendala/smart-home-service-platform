import React, { useState, useEffect } from 'react';
import { Shield, Key, Eye, Lock, RefreshCw, Search } from 'lucide-react';
import api from '../../services/api';

interface AuditEntry {
  id: number;
  user_id?: number;
  action: string;
  entity_name: string;
  entity_id?: string;
  ip_address: string;
  created_at: string;
}

export const AuditLogViewer: React.FC = () => {
  const [logs, setLogs] = useState<AuditEntry[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    api.get('/security/logs')
      .then((r) => setLogs(r.data))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-10 space-y-8">
      <div className="border-b border-slate-800 pb-6 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-extrabold bg-gradient-to-r from-red-400 via-rose-400 to-pink-300 bg-clip-text text-transparent">
            Security Audit & RBAC Session Portal
          </h1>
          <p className="text-slate-400 mt-1 text-sm">
            Immutable system audit trails, JWT session revocation, IP whitelist policy management, and fine-grained RBAC matrix.
          </p>
        </div>
      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4">
        <h2 className="text-xl font-bold text-slate-100 flex items-center gap-2">
          <Shield className="w-5 h-5 text-rose-400" /> Audit Trail Logs
        </h2>

        {loading ? (
          <div className="flex justify-center py-12">
            <RefreshCw className="w-8 h-8 animate-spin text-rose-500" />
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="border-b border-slate-800 text-slate-400 text-xs uppercase">
                  <th className="py-3 px-4">Timestamp</th>
                  <th className="py-3 px-4">Action</th>
                  <th className="py-3 px-4">Entity Path</th>
                  <th className="py-3 px-4">Client IP</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {logs.map((log) => (
                  <tr key={log.id} className="hover:bg-slate-800/40">
                    <td className="py-3 px-4 text-xs font-mono text-slate-400">{log.created_at?.slice(0, 19)}</td>
                    <td className="py-3 px-4">
                      <span className="px-2.5 py-1 text-xs font-bold rounded-full bg-rose-500/20 text-rose-400 border border-rose-500/30">
                        {log.action}
                      </span>
                    </td>
                    <td className="py-3 px-4 text-slate-300 font-mono text-xs">{log.entity_name}</td>
                    <td className="py-3 px-4 text-slate-400 font-mono text-xs">{log.ip_address}</td>
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
export default AuditLogViewer;
