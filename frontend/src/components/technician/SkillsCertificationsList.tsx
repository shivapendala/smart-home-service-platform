import React, { useState, useEffect } from 'react';
import { Award, CheckCircle2, ShieldCheck, Star } from 'lucide-react';
import api from '../../services/api';

interface Skill {
  id: number;
  skill_name: string;
  category_name: string;
  proficiency_level: string;
  years_experience: number;
  is_certified: boolean;
}

interface Certification {
  id: number;
  certification_title: string;
  issuing_authority: string;
  license_number: string;
  verification_status: string;
}

export const SkillsCertificationsList: React.FC = () => {
  const [skills, setSkills] = useState<Skill[]>([]);
  const [certs, setCerts] = useState<Certification[]>([]);

  useEffect(() => {
    api.get('/technicians/management/skills/me').then((r) => setSkills(r.data)).catch(() => {});
    api.get('/technicians/management/certifications/me').then((r) => setCerts(r.data)).catch(() => {});
  }, []);

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-6">
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <h2 className="text-xl font-bold text-slate-100 flex items-center gap-2">
          <Award className="w-5 h-5 text-indigo-400" /> Skills & Certified Credentials
        </h2>
      </div>

      <div className="space-y-6">
        <div>
          <h3 className="text-sm font-semibold text-slate-400 uppercase mb-3">Verified Skills Matrix</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {skills.map((s) => (
              <div key={s.id} className="p-3 bg-slate-950/60 border border-slate-800 rounded-xl flex items-center justify-between">
                <div>
                  <h4 className="font-semibold text-slate-200 text-sm">{s.skill_name}</h4>
                  <span className="text-xs text-slate-500">{s.category_name} • {s.years_experience} yrs exp</span>
                </div>
                <span className="px-2.5 py-1 text-xs bg-indigo-500/20 text-indigo-300 font-bold rounded-lg border border-indigo-500/30">
                  {s.proficiency_level}
                </span>
              </div>
            ))}
          </div>
        </div>

        <div>
          <h3 className="text-sm font-semibold text-slate-400 uppercase mb-3">Trade Certifications</h3>
          <div className="space-y-3">
            {certs.map((c) => (
              <div key={c.id} className="p-4 bg-slate-950/60 border border-slate-800 rounded-xl flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <ShieldCheck className="w-6 h-6 text-emerald-400" />
                  <div>
                    <h4 className="font-semibold text-slate-200 text-sm">{c.certification_title}</h4>
                    <p className="text-xs text-slate-500">{c.issuing_authority} • License #{c.license_number}</p>
                  </div>
                </div>
                <span className="px-3 py-1 bg-emerald-500/20 text-emerald-400 text-xs font-bold rounded-full border border-emerald-500/30">
                  {c.verification_status}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
export default SkillsCertificationsList;
