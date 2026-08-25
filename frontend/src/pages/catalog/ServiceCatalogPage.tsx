import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Search, Clock, ArrowRight, Sparkles, Filter, Check } from 'lucide-react';
import { catalogService } from '../../services/api';
import { Category, ServiceItem } from '../../types';
import { useAuth } from '../../context/AuthContext';

export const ServiceCatalogPage: React.FC = () => {
  const [categories, setCategories] = useState<Category[]>([]);
  const [services, setServices] = useState<ServiceItem[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<number | null>(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(true);

  const { user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCatalog = async () => {
      setLoading(true);
      try {
        const [catData, serviceData] = await Promise.all([
          catalogService.getCategories(),
          catalogService.getServices(selectedCategory || undefined, searchQuery || undefined),
        ]);
        setCategories(catData);
        setServices(serviceData);
      } catch (err) {
        console.error('Failed to load catalog:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchCatalog();
  }, [selectedCategory, searchQuery]);

  const handleBookClick = () => {
    if (!user) {
      navigate('/login');
    } else {
      navigate('/customer-dashboard');
    }
  };

  return (
    <div style={{ padding: '2rem 3rem' }}>
      {/* Catalog Header */}
      <div className="glass-panel" style={{
        padding: '3rem 2.5rem',
        marginBottom: '2rem',
        background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%)',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: '#06b6d4', fontWeight: 600, fontSize: '0.88rem', marginBottom: '0.5rem' }}>
          <Sparkles size={16} /> Instant Online Booking & Upfront Pricing
        </div>
        <h1 style={{ fontSize: '2.25rem', fontWeight: 800, color: '#ffffff', marginBottom: '0.75rem' }}>
          Home Service Catalog
        </h1>
        <p style={{ color: '#94a3b8', fontSize: '1rem', maxWidth: '650px', marginBottom: '1.75rem' }}>
          Browse certified appliance repair, plumbing, and electrical services. All prices are upfront with no hidden diagnostic charges.
        </p>

        {/* Search Bar */}
        <div style={{ position: 'relative', maxWidth: '540px' }}>
          <input
            type="text"
            className="form-input"
            placeholder="Search services (e.g. AC Deep Cleaning, Leak Fix, Wiring)..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{ paddingLeft: '2.75rem', height: '50px', fontSize: '1rem', borderRadius: '12px' }}
          />
          <Search size={20} color="#64748b" style={{ position: 'absolute', left: '1rem', top: '50%', transform: 'translateY(-50%)' }} />
        </div>
      </div>

      {/* Category Tabs */}
      <div style={{
        display: 'flex',
        gap: '0.75rem',
        overflowX: 'auto',
        paddingBottom: '0.75rem',
        marginBottom: '2rem'
      }}>
        <button
          onClick={() => setSelectedCategory(null)}
          style={{
            padding: '0.65rem 1.25rem',
            borderRadius: '9999px',
            border: selectedCategory === null ? '1px solid #6366f1' : '1px solid rgba(255,255,255,0.1)',
            background: selectedCategory === null ? 'rgba(99, 102, 241, 0.2)' : 'rgba(30, 41, 59, 0.6)',
            color: selectedCategory === null ? '#818cf8' : '#94a3b8',
            fontWeight: 600,
            cursor: 'pointer',
            whiteSpace: 'nowrap',
            display: 'flex',
            alignItems: 'center',
            gap: '0.35rem'
          }}
        >
          <Filter size={14} /> All Categories
        </button>
        {categories.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setSelectedCategory(cat.id)}
            style={{
              padding: '0.65rem 1.25rem',
              borderRadius: '9999px',
              border: selectedCategory === cat.id ? '1px solid #06b6d4' : '1px solid rgba(255,255,255,0.1)',
              background: selectedCategory === cat.id ? 'rgba(6, 182, 212, 0.2)' : 'rgba(30, 41, 59, 0.6)',
              color: selectedCategory === cat.id ? '#38bdf8' : '#94a3b8',
              fontWeight: 600,
              cursor: 'pointer',
              whiteSpace: 'nowrap',
              display: 'flex',
              alignItems: 'center',
              gap: '0.4rem'
            }}
          >
            <span>{cat.icon}</span>
            <span>{cat.name}</span>
          </button>
        ))}
      </div>

      {/* Services Grid */}
      {loading ? (
        <div style={{ textAlign: 'center', color: '#94a3b8', padding: '4rem 0' }}>
          Loading service catalog...
        </div>
      ) : services.length === 0 ? (
        <div className="glass-panel" style={{ padding: '3rem', textAlign: 'center', color: '#94a3b8' }}>
          No services match your selected category or search filter.
        </div>
      ) : (
        <div className="grid-3">
          {services.map((service) => (
            <div key={service.id} className="glass-panel" style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '0.75rem' }}>
                  <h3 style={{ fontSize: '1.2rem', fontWeight: 700, color: '#f8fafc' }}>
                    {service.name}
                  </h3>
                  <span style={{
                    fontSize: '1.25rem',
                    fontWeight: 800,
                    color: '#10b981',
                    background: 'rgba(16, 185, 129, 0.15)',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '8px',
                    border: '1px solid rgba(16, 185, 129, 0.3)'
                  }}>
                    ${service.base_price.toFixed(2)}
                  </span>
                </div>

                <p style={{ color: '#94a3b8', fontSize: '0.9rem', marginBottom: '1.25rem', lineHeight: 1.5 }}>
                  {service.description}
                </p>
              </div>

              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', color: '#64748b', fontSize: '0.85rem', marginBottom: '1.25rem', paddingTop: '0.75rem', borderTop: '1px solid rgba(255,255,255,0.08)' }}>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                    <Clock size={14} color="#06b6d4" /> {service.duration_minutes} Mins Service
                  </span>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                    <Check size={14} color="#10b981" /> Verified Price
                  </span>
                </div>

                <button
                  onClick={() => handleBookClick()}
                  className="btn btn-primary"
                  style={{ width: '100%', padding: '0.7rem' }}
                >
                  Book Service <ArrowRight size={16} />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
