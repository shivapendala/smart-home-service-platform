import React from 'react';
import { Wrench } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="footer">
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem', marginBottom: '0.5rem' }}>
        <Wrench size={16} color="#ef4444" />
        <span style={{ fontWeight: 700, color: '#0f172a' }}>Smart Home Service Platform</span>
      </div>
      <p>© {new Date().getFullYear()} Smart Home Service Platform. Certified Home Technicians & Instant Service Booking.</p>
    </footer>
  );
};
