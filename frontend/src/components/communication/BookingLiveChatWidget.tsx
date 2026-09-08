import React, { useState, useEffect } from 'react';
import { MessageSquare, Send, Paperclip, CheckCheck } from 'lucide-react';
import api from '../../services/api';

interface ChatWidgetProps {
  bookingId: number;
  recipientId: number;
}

export const BookingLiveChatWidget: React.FC<ChatWidgetProps> = ({ bookingId, recipientId }) => {
  const [messages, setMessages] = useState<any[]>([]);
  const [input, setInput] = useState('');

  const fetchChat = async () => {
    try {
      const res = await api.get(`/communication/chat/booking/${bookingId}`);
      setMessages(res.data);
    } catch (err) {
      console.error('Chat load error', err);
    }
  };

  useEffect(() => {
    fetchChat();
    const interval = setInterval(fetchChat, 5000);
    return () => clearInterval(interval);
  }, [bookingId]);

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;
    try {
      await api.post('/communication/chat', {
        booking_id: bookingId,
        recipient_id: recipientId,
        message_text: input
      });
      setInput('');
      fetchChat();
    } catch (err) {
      console.error('Send error', err);
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4 flex flex-col h-[450px]">
      <div className="flex items-center justify-between border-b border-slate-800 pb-3">
        <h3 className="text-lg font-bold text-slate-100 flex items-center gap-2">
          <MessageSquare className="w-5 h-5 text-blue-400" /> Technician Live Messaging
        </h3>
        <span className="flex items-center gap-1.5 text-xs text-emerald-400 font-semibold">
          <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" /> Active Session
        </span>
      </div>

      <div className="flex-1 overflow-y-auto space-y-3 p-2">
        {messages.map((m, idx) => (
          <div key={idx} className="flex flex-col space-y-1">
            <div className="max-w-[80%] bg-slate-800 border border-slate-700/60 p-3 rounded-2xl text-slate-200 text-xs self-start">
              {m.message_text}
            </div>
            <span className="text-[10px] text-slate-500">{m.created_at?.slice(11, 16)}</span>
          </div>
        ))}
      </div>

      <form onSubmit={handleSend} className="flex items-center gap-2 pt-2 border-t border-slate-800">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type message to assigned technician..."
          className="bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-xs text-slate-100 flex-1 focus:outline-none focus:border-blue-500"
        />
        <button type="submit" className="p-2.5 bg-blue-600 hover:bg-blue-500 text-white rounded-xl transition-all">
          <Send className="w-4 h-4" />
        </button>
      </form>
    </div>
  );
};
export default BookingLiveChatWidget;
