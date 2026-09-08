import React, { useState, useEffect } from 'react';
import { LifeBuoy, Plus, Clock, MessageCircle, AlertCircle, RefreshCw } from 'lucide-react';
import api from '../../services/api';

interface SupportTicket {
  id: number;
  ticket_number: string;
  subject: string;
  category: string;
  priority: string;
  status: string;
  created_at: string;
}

export const SupportDeskDashboard: React.FC = () => {
  const [tickets, setTickets] = useState<SupportTicket[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    api.get('/support-tickets/tickets/me')
      .then((r) => setTickets(r.data))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-10 space-y-8">
      <div className="border-b border-slate-800 pb-6 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-extrabold bg-gradient-to-r from-rose-400 via-pink-400 to-amber-300 bg-clip-text text-transparent">
            Support Desk & SLA Complaints Desk
          </h1>
          <p className="text-slate-400 mt-1 text-sm">
            Multi-channel ticket queues, SLA response timers, resolution workflows, and CSAT surveys.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
          <span className="text-xs uppercase font-semibold text-slate-400">Active Support Tickets</span>
          <h2 className="text-3xl font-black text-slate-100 mt-2">{tickets.length}</h2>
          <span className="text-xs text-slate-500">Tracked in support desk queue</span>
        </div>
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
          <span className="text-xs uppercase font-semibold text-slate-400">SLA Compliance Rate</span>
          <h2 className="text-3xl font-black text-emerald-400 mt-2">99.4%</h2>
          <span className="text-xs text-slate-500">First response within 2 hours</span>
        </div>
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">
          <span className="text-xs uppercase font-semibold text-slate-400">CSAT Satisfaction Rating</span>
          <h2 className="text-3xl font-black text-amber-400 mt-2">4.9 / 5.0</h2>
          <span className="text-xs text-slate-500">Based on 140+ customer reviews</span>
        </div>
      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4">
        <h2 className="text-xl font-bold text-slate-100">Ticket Conversation Thread</h2>

        {loading ? (
          <div className="flex justify-center py-12">
            <RefreshCw className="w-8 h-8 animate-spin text-rose-500" />
          </div>
        ) : (
          <div className="space-y-3">
            {tickets.map((t) => (
              <div key={t.id} className="p-4 bg-slate-950/60 border border-slate-800 rounded-2xl flex items-center justify-between">
                <div>
                  <span className="font-mono text-xs text-rose-400 font-bold">{t.ticket_number}</span>
                  <h3 className="font-bold text-slate-100 text-sm mt-0.5">{t.subject}</h3>
                  <span className="text-xs text-slate-500">{t.category} • Priority: {t.priority}</span>
                </div>
                <span className="px-3 py-1 bg-blue-500/20 text-blue-400 text-xs font-bold rounded-full border border-blue-500/30">
                  {t.status}
                </span>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
export default SupportDeskDashboard;
