import React from 'react';
import { Link } from 'react-router-dom';
import { 
  Wrench, 
  Wind, 
  Flame, 
  Droplet, 
  Zap, 
  Home, 
  ArrowRight, 
  Clock, 
  Star, 
  UserCheck 
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export const HomePage: React.FC = () => {
  const { user } = useAuth();

  const servicesList = [
    {
      id: 1,
      title: 'AC Repair & Cooling',
      icon: Wind,
      desc: 'Deep jet cleaning, gas leak refills, compressor replacements, and complete seasonal cooling maintenance.',
      tag: 'AC & HVAC'
    },
    {
      id: 2,
      title: 'Plumbing & Fitting',
      icon: Droplet,
      desc: 'Accurate leak detection, high-pressure line clearings, faucet installations, and emergency pipe fixes.',
      tag: 'Plumbing'
    },
    {
      id: 3,
      title: 'Electrical Upgrades',
      icon: Zap,
      desc: 'Short circuit diagnosis, DB box setups, main wiring installation, and smart home appliance connections.',
      tag: 'Electrical'
    },
    {
      id: 4,
      title: 'Washing Machine Fix',
      icon: Wrench,
      desc: 'Front-load and top-load motor servicing, drum balancing, drainage pump replacement, and noise reduction.',
      tag: 'Appliance'
    },
    {
      id: 5,
      title: 'Refrigerator Service',
      icon: Flame,
      desc: 'Thermostat replacement, ice maker repairs, gas charging, and sealed system diagnostic checkups.',
      tag: 'Refrigeration'
    },
    {
      id: 6,
      title: 'Full Home Maintenance',
      icon: Home,
      desc: 'Comprehensive final-inspection home maintenance packages matching enterprise safety & quality guidelines.',
      tag: 'Full Service'
    }
  ];

  return (
    <div style={{ maxWidth: '1240px', margin: '0 auto', padding: '3rem 1.5rem' }}>
      
      {/* Top Banner / Hero matching the Reference Image Section Header */}
      <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
        <span className="eyebrow-tag">OUR SERVICES</span>
        <h1 className="section-title">
          Tailored Home Service Solutions
        </h1>
        <p className="section-subtitle">
          From quick home repair support to highly customizable maintenance packages, we deploy certified technicians that drive results.
        </p>

        {!user && (
          <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem', flexWrap: 'wrap' }}>
            <Link to="/register" className="btn btn-primary">
              Book Service Now <ArrowRight size={18} />
            </Link>
            <Link to="/register?role=TECHNICIAN" className="btn btn-secondary">
              Join as Technician <UserCheck size={18} />
            </Link>
          </div>
        )}
      </div>

      {/* Cards Grid matching the Reference Image Cards */}
      <div className="grid-3" style={{ marginBottom: '5rem' }}>
        {servicesList.map((service) => {
          const IconComponent = service.icon;
          return (
            <div key={service.id} className="card" style={{ padding: '2rem 1.75rem', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
              <div>
                <div className="icon-box">
                  <IconComponent size={24} />
                </div>
                <h3 style={{ fontSize: '1.35rem', fontWeight: 700, color: '#0f172a', marginBottom: '0.75rem' }}>
                  {service.title}
                </h3>
                <p style={{ color: '#64748b', fontSize: '0.95rem', lineHeight: '1.6', marginBottom: '1.75rem' }}>
                  {service.desc}
                </p>
              </div>

              <div>
                <Link to="/services" className="btn btn-outline" style={{ width: 'auto', display: 'inline-flex' }}>
                  Learn More
                </Link>
              </div>
            </div>
          );
        })}
      </div>

      {/* Additional Features Section matching light clean card layout */}
      <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <span className="eyebrow-tag">WHY CHOOSE US</span>
        <h2 style={{ fontSize: '2rem', fontWeight: 800, color: '#0f172a', marginBottom: '1rem' }}>
          Built for Quality & Speed
        </h2>
        <p style={{ color: '#64748b', fontSize: '1rem', maxWidth: '600px', margin: '0 auto 2.5rem auto' }}>
          Transparent pricing, verified background checks, and instant dispatch tracking for your home.
        </p>
      </div>

      <div className="grid-3">
        <div className="card" style={{ padding: '2rem' }}>
          <div className="icon-box">
            <Zap size={24} />
          </div>
          <h4 style={{ fontSize: '1.15rem', fontWeight: 700, color: '#0f172a', marginBottom: '0.5rem' }}>
            Instant Dispatch
          </h4>
          <p style={{ color: '#64748b', fontSize: '0.9rem', lineHeight: '1.6' }}>
            Smart matching system assigns qualified certified technicians in under 5 minutes.
          </p>
        </div>

        <div className="card" style={{ padding: '2rem' }}>
          <div className="icon-box">
            <Clock size={24} />
          </div>
          <h4 style={{ fontSize: '1.15rem', fontWeight: 700, color: '#0f172a', marginBottom: '0.5rem' }}>
            Real-Time Tracking
          </h4>
          <p style={{ color: '#64748b', fontSize: '0.9rem', lineHeight: '1.6' }}>
            Track technician dispatch status, arrival countdowns, and completion stages live.
          </p>
        </div>

        <div className="card" style={{ padding: '2rem' }}>
          <div className="icon-box">
            <Star size={24} />
          </div>
          <h4 style={{ fontSize: '1.15rem', fontWeight: 700, color: '#0f172a', marginBottom: '0.5rem' }}>
            Verified Quality
          </h4>
          <p style={{ color: '#64748b', fontSize: '0.9rem', lineHeight: '1.6' }}>
            All technicians are background-checked and customer-rated for transparent high standards.
          </p>
        </div>
      </div>

    </div>
  );
};
