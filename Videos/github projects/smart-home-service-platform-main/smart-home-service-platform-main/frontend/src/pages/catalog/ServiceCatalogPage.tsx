import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Search, Clock, ArrowRight, Filter, Check } from 'lucide-react';
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
    <div style={{ maxWidth: '1240px', margin: '0 auto', padding: '3rem 1.5rem' }}>
      {/* Catalog Header */}
      <div style={{ textAlign: 'center', marginBottom: '3.5rem' }}>
        <span className="eyebrow-tag">OUR SERVICES CATALOG</span>
        <h1 className="section-title">
          Professional Home Services
        </h1>
        <p className="section-subtitle">
          Browse certified appliance repair, plumbing, and electrical services with transparent upfront pricing and no hidden diagnostic fees.
        </p>

        {/* Search Bar */}
        <div style={{ position: 'relative', maxWidth: '560px', margin: '0 auto' }}>
          <input
            type="text"
            className="form-input"
            placeholder="Search services (e.g. AC Deep Cleaning, Pipe Leak Fix, Wiring)..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{ paddingLeft: '2.8rem', height: '52px', fontSize: '1rem', borderRadius: '12px' }}
          />
          <Search size={20} color="#94a3b8" style={{ position: 'absolute', left: '1rem', top: '50%', transform: 'translateY(-50%)' }} />
        </div>
      </div>

      {/* Category Tabs */}
      <div style={{
        display: 'flex',
        gap: '0.75rem',
        overflowX: 'auto',
        paddingBottom: '0.75rem',
        marginBottom: '2.5rem',
        justifyContent: 'center',
        flexWrap: 'wrap'
      }}>
        <button
          onClick={() => setSelectedCategory(null)}
          style={{
            padding: '0.65rem 1.35rem',
            borderRadius: '9999px',
            border: selectedCategory === null ? '1.5px solid #ef4444' : '1px solid #e2e8f0',
            background: selectedCategory === null ? 'rgba(239, 68, 68, 0.08)' : '#ffffff',
            color: selectedCategory === null ? '#ef4444' : '#64748b',
            fontWeight: 600,
            cursor: 'pointer',
            whiteSpace: 'nowrap',
            display: 'flex',
            alignItems: 'center',
            gap: '0.4rem',
            transition: 'all 0.2s'
          }}
        >
          <Filter size={14} /> All Categories
        </button>
        {categories.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setSelectedCategory(cat.id)}
            style={{
              padding: '0.65rem 1.35rem',
              borderRadius: '9999px',
              border: selectedCategory === cat.id ? '1.5px solid #ef4444' : '1px solid #e2e8f0',
              background: selectedCategory === cat.id ? 'rgba(239, 68, 68, 0.08)' : '#ffffff',
              color: selectedCategory === cat.id ? '#ef4444' : '#64748b',
              fontWeight: 600,
              cursor: 'pointer',
              whiteSpace: 'nowrap',
              display: 'flex',
              alignItems: 'center',
              gap: '0.4rem',
              transition: 'all 0.2s'
            }}
          >
            <span>{cat.icon}</span>
            <span>{cat.name}</span>
          </button>
        ))}
      </div>

      {/* Services Grid */}
      {loading ? (
        <div style={{ textAlign: 'center', color: '#64748b', padding: '4rem 0' }}>
          Loading service catalog...
        </div>
      ) : services.length === 0 ? (
        <div className="card" style={{ padding: '3rem', textAlign: 'center', color: '#64748b' }}>
          No services match your selected category or search filter.
        </div>
      ) : (
        <div className="grid-3">
          {services.map((service) => (
            <div key={service.id} className="card" style={{ padding: '2rem 1.75rem', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '0.75rem' }}>
                  <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#0f172a' }}>
                    {service.name}
                  </h3>
                  <span style={{
                    fontSize: '1.25rem',
                    fontWeight: 800,
                    color: '#ef4444',
                    background: 'rgba(239, 68, 68, 0.08)',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '8px',
                    border: '1px solid rgba(239, 68, 68, 0.2)'
                  }}>
                    ${service.base_price.toFixed(2)}
                  </span>
                </div>

                <p style={{ color: '#64748b', fontSize: '0.92rem', marginBottom: '1.5rem', lineHeight: '1.6' }}>
                  {service.description}
                </p>
              </div>

              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', color: '#94a3b8', fontSize: '0.85rem', marginBottom: '1.25rem', paddingTop: '0.75rem', borderTop: '1px solid #f1f5f9' }}>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '0.3rem', color: '#64748b' }}>
                    <Clock size={14} color="#ef4444" /> {service.duration_minutes} Mins Duration
                  </span>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '0.3rem', color: '#059669' }}>
                    <Check size={14} color="#059669" /> Transparent Price
                  </span>
                </div>

                <button
                  onClick={() => handleBookClick()}
                  className="btn btn-outline"
                  style={{ width: '100%', padding: '0.65rem' }}
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
