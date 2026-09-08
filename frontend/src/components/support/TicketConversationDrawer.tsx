import React, { useState } from 'react';
import { X, Send, Lock } from 'lucide-react';
import api from '../../services/api';

export const TicketConversationDrawer: React.FC<{ isOpen: boolean; onClose: () => void; ticketId: number }> = ({ isOpen, onClose, ticketId }) => {
  const [commentText, setCommentText] = useState('');

  if (!isOpen) return null;

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/support-tickets/comments', {
        ticket_id: ticketId,
        comment_text: commentText,
        is_internal_note: false
      });
      setCommentText('');
    } catch (err) {
      console.error('Comment error', err);
    }
  };

  return (
    <div className="fixed inset-y-0 right-0 z-50 w-full max-w-lg bg-slate-900 border-l border-slate-800 p-6 shadow-2xl space-y-6 flex flex-col">
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <h2 className="text-xl font-bold text-slate-100">Ticket Details & History</h2>
        <button onClick={onClose} className="text-slate-500 hover:text-slate-200">
          <X className="w-5 h-5" />
        </button>
      </div>

      <div className="flex-1 overflow-y-auto space-y-3">
        <div className="p-3 bg-slate-800 rounded-xl text-xs text-slate-200">
          Agent support thread active. SLA response guarantee under 2 hours.
        </div>
      </div>

      <form onSubmit={handleSend} className="flex gap-2 pt-2 border-t border-slate-800">
        <input
          type="text"
          value={commentText}
          onChange={(e) => setCommentText(e.target.value)}
          placeholder="Reply to ticket thread..."
          className="bg-slate-800 border border-slate-700 rounded-xl px-4 py-2 text-xs text-slate-100 flex-1"
        />
        <button type="submit" className="px-4 py-2 bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs rounded-xl">
          Reply
        </button>
      </form>
    </div>
  );
};
export default TicketConversationDrawer;
