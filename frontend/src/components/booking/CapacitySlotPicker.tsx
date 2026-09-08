import React, { useState, useEffect } from 'react';
import { Clock, Zap, AlertTriangle } from 'lucide-react';
import api from '../../services/api';

interface CapacitySlotPickerProps {
  selectedDate: string;
  zipCode: string;
  onSlotSelect: (slot: string) => void;
}

export const CapacitySlotPicker: React.FC<CapacitySlotPickerProps> = ({ selectedDate, zipCode, onSlotSelect }) => {
  const [selectedSlot, setSelectedSlot] = useState<string>('09:00 - 11:00');
  const slots = [
    { time: '08:00 - 10:00', density: 'High Demand', surge: 1.15, available: 2 },
    { time: '10:00 - 12:00', density: 'Optimal Availability', surge: 1.0, available: 6 },
    { time: '13:00 - 15:00', density: 'Optimal Availability', surge: 1.0, available: 5 },
    { time: '15:00 - 17:00', density: 'Filling Fast', surge: 1.10, available: 3 },
    { time: '17:00 - 19:00', density: 'Peak Surge', surge: 1.25, available: 1 }
  ];

  const handleSelect = (s: string) => {
    setSelectedSlot(s);
    onSlotSelect(s);
  };

  return (
    <div className="space-y-4">
      <h3 className="text-sm font-semibold text-slate-400 uppercase tracking-wider flex items-center gap-2">
        <Clock className="w-4 h-4 text-blue-400" /> Select Dispatch Time Slot
      </h3>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
        {slots.map((slot) => {
          const isSelected = selectedSlot === slot.time;
          return (
            <div
              key={slot.time}
              onClick={() => handleSelect(slot.time)}
              className={`cursor-pointer p-4 rounded-2xl border transition-all ${
                isSelected
                  ? 'bg-blue-600/10 border-blue-500 text-slate-100 ring-2 ring-blue-500/30'
                  : 'bg-slate-900 border-slate-800 text-slate-300 hover:border-slate-700'
              }`}
            >
              <div className="flex items-center justify-between">
                <span className="font-bold text-sm">{slot.time}</span>
                {slot.surge > 1.0 && (
                  <span className="flex items-center gap-1 text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30">
                    <Zap className="w-3 h-3" /> {slot.surge}x Surge
                  </span>
                )}
              </div>
              <div className="flex items-center justify-between text-xs text-slate-500 mt-2">
                <span>{slot.density}</span>
                <span className="font-semibold text-slate-400">{slot.available} slots left</span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
export default CapacitySlotPicker;
