import React, { useState, useEffect } from 'react';
import { Users, Wrench, FileText, CheckCircle, Activity, Plus, Trash2, X } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { authService, catalogService } from '../../services/api';
import { User, Category, ServiceItem } from '../../types';

export const AdminDashboard: React.FC = () => {
  const { user } = useAuth();
  const [activeTab, setActiveTab] = useState<'technicians' | 'catalog'>('technicians');
  
  // Technicians state
  const [technicians, setTechnicians] = useState<User[]>([]);
  const [techLoading, setTechLoading] = useState(true);

  // Catalog state
  const [categories, setCategories] = useState<Category[]>([]);
  const [services, setServices] = useState<ServiceItem[]>([]);
  const [catalogLoading, setCatalogLoading] = useState(false);

  // Create Service Modal state
  const [showModal, setShowModal] = useState(false);
  const [newServiceName, setNewServiceName] = useState('');
  const [newServiceDesc, setNewServiceDesc] = useState('');
  const [newServicePrice, setNewServicePrice] = useState<number>(49);
  const [newServiceDuration, setNewServiceDuration] = useState<number>(60);
  const [newServiceCatId, setNewServiceCatId] = useState<number>(1);
  const [submitLoading, setSubmitLoading] = useState(false);

  useEffect(() => {
    fetchTechnicians();
    fetchCatalog();
  }, []);

  const fetchTechnicians = async () => {
    try {
      const list = await authService.getTechnicians();
      setTechnicians(list);
    } catch (err) {
      console.error('Failed to load technicians:', err);
    } finally {
      setTechLoading(false);
    }
  };

  const fetchCatalog = async () => {
    setCatalogLoading(true);
    try {
      const [catList, serviceList] = await Promise.all([
        catalogService.getCategories(),
        catalogService.getServices()
      ]);
      setCategories(catList);
      setServices(serviceList);
      if (catList.length > 0) setNewServiceCatId(catList[0].id);
    } catch (err) {
      console.error('Failed to load catalog:', err);
    } finally {
      setCatalogLoading(false);
    }
  };

  const handleCreateService = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitLoading(true);
    try {
      await catalogService.createService({
        category_id: newServiceCatId,
        name: newServiceName,
        description: newServiceDesc,
        base_price: Number(newServicePrice),
        duration_minutes: Number(newServiceDuration),
        is_active: true
      });
      setShowModal(false);
      setNewServiceName('');
      setNewServiceDesc('');
      await fetchCatalog();
    } catch (err) {
      alert('Failed to create service item.');
    } finally {
      setSubmitLoading(false);
    }
  };

  const handleDeleteService = async (id: number) => {
    if (window.confirm('Are you sure you want to delete this service item?')) {
      try {
        await catalogService.deleteService(id);
        await fetchCatalog();
      } catch (err) {
        alert('Failed to delete service.');
      }
    }
  };

  return (
    <div style={{ padding: '2rem 3rem' }}>
      {/* Admin Header */}
      <div className="glass-panel" style={{ padding: '2rem 2.5rem', marginBottom: '2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <span className="role-badge admin" style={{ marginBottom: '0.5rem' }}>Platform Control Center</span>
          <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#ffffff' }}>
            System Administration Dashboard
          </h1>
          <p style={{ color: '#94a3b8', fontSize: '0.95rem' }}>
            Administrator: <strong style={{ color: '#f43f5e' }}>{user?.full_name}</strong> ({user?.email})
          </p>
        </div>

        <div style={{ display: 'flex', gap: '0.75rem' }}>
          <button className="btn btn-secondary" style={{ padding: '0.65rem 1.25rem' }}>
            <FileText size={16} /> Export System Report
          </button>
        </div>
      </div>

      {/* Metrics Row */}
      <div className="grid-3" style={{ marginBottom: '2rem' }}>
        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Registered Technicians</span>
            <Wrench size={20} color="#10b981" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#ffffff', marginTop: '0.5rem' }}>
            {technicians.length}
          </div>
          <span style={{ fontSize: '0.8rem', color: '#10b981' }}>Active technician accounts</span>
        </div>

        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>Catalog Services</span>
            <Activity size={20} color="#06b6d4" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#ffffff', marginTop: '0.5rem' }}>
            {services.length}
          </div>
          <span style={{ fontSize: '0.8rem', color: '#06b6d4' }}>Total active service items</span>
        </div>

        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ color: '#94a3b8', fontWeight: 600, fontSize: '0.9rem' }}>System Status</span>
            <CheckCircle size={20} color="#10b981" />
          </div>
          <div style={{ fontSize: '1.25rem', fontWeight: 700, color: '#10b981', marginTop: '0.75rem', display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
            All Services Operational
          </div>
          <span style={{ fontSize: '0.8rem', color: '#64748b' }}>FastAPI Backend & DB Healthy</span>
        </div>
      </div>

      {/* Section Tabs */}
      <div style={{ display: 'flex', gap: '1rem', marginBottom: '1.5rem' }}>
        <button
          onClick={() => setActiveTab('technicians')}
          className={`btn ${activeTab === 'technicians' ? 'btn-primary' : 'btn-secondary'}`}
          style={{ padding: '0.6rem 1.25rem' }}
        >
          <Users size={16} /> Technician Directory
        </button>
        <button
          onClick={() => setActiveTab('catalog')}
          className={`btn ${activeTab === 'catalog' ? 'btn-primary' : 'btn-secondary'}`}
          style={{ padding: '0.6rem 1.25rem' }}
        >
          <Wrench size={16} /> Service Catalog Manager
        </button>
      </div>

      {/* Tab 1: Technician Directory */}
      {activeTab === 'technicians' && (
        <div className="glass-panel" style={{ padding: '2rem' }}>
          <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#ffffff', marginBottom: '1.25rem' }}>
            Registered Platform Technicians
          </h3>

          {techLoading ? (
            <div style={{ textAlign: 'center', color: '#94a3b8', padding: '2rem' }}>Loading technicians...</div>
          ) : technicians.length === 0 ? (
            <div style={{ padding: '2.5rem', textAlign: 'center', background: 'rgba(15, 23, 42, 0.4)', borderRadius: '12px' }}>
              <p style={{ color: '#94a3b8' }}>No technician accounts registered yet.</p>
            </div>
          ) : (
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', color: '#f8fafc', fontSize: '0.9rem' }}>
                <thead>
                  <tr style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.1)', color: '#94a3b8' }}>
                    <th style={{ padding: '0.75rem 1rem' }}>ID</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Name</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Email</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Specialization</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Experience</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Rating</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Status</th>
                  </tr>
                </thead>
                <tbody>
                  {technicians.map((t) => (
                    <tr key={t.id} style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.05)' }}>
                      <td style={{ padding: '0.75rem 1rem', color: '#64748b' }}>#{t.id}</td>
                      <td style={{ padding: '0.75rem 1rem', fontWeight: 600 }}>{t.full_name}</td>
                      <td style={{ padding: '0.75rem 1rem', color: '#94a3b8' }}>{t.email}</td>
                      <td style={{ padding: '0.75rem 1rem', color: '#06b6d4' }}>{t.specialization || 'General'}</td>
                      <td style={{ padding: '0.75rem 1rem' }}>{t.experience_years} Yrs</td>
                      <td style={{ padding: '0.75rem 1rem', color: '#f59e0b' }}>{t.rating} ★</td>
                      <td style={{ padding: '0.75rem 1rem' }}>
                        <span className="role-badge technician">Active</span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}

      {/* Tab 2: Service Catalog Manager */}
      {activeTab === 'catalog' && (
        <div className="glass-panel" style={{ padding: '2rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#ffffff' }}>
              Service Catalog & Upfront Pricing Manager
            </h3>
            <button onClick={() => setShowModal(true)} className="btn btn-primary" style={{ padding: '0.5rem 1.25rem' }}>
              <Plus size={16} /> Add New Service
            </button>
          </div>

          {catalogLoading ? (
            <div style={{ textAlign: 'center', color: '#94a3b8', padding: '2rem' }}>Loading catalog items...</div>
          ) : (
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', color: '#f8fafc', fontSize: '0.9rem' }}>
                <thead>
                  <tr style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.1)', color: '#94a3b8' }}>
                    <th style={{ padding: '0.75rem 1rem' }}>ID</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Service Name</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Category</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Base Price</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Duration</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Status</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {services.map((s) => (
                    <tr key={s.id} style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.05)' }}>
                      <td style={{ padding: '0.75rem 1rem', color: '#64748b' }}>#{s.id}</td>
                      <td style={{ padding: '0.75rem 1rem', fontWeight: 600 }}>{s.name}</td>
                      <td style={{ padding: '0.75rem 1rem', color: '#06b6d4' }}>
                        {categories.find(c => c.id === s.category_id)?.name || 'General'}
                      </td>
                      <td style={{ padding: '0.75rem 1rem', color: '#10b981', fontWeight: 700 }}>
                        ${s.base_price.toFixed(2)}
                      </td>
                      <td style={{ padding: '0.75rem 1rem', color: '#94a3b8' }}>{s.duration_minutes} Mins</td>
                      <td style={{ padding: '0.75rem 1rem' }}>
                        <span style={{
                          padding: '0.2rem 0.6rem',
                          borderRadius: '9999px',
                          fontSize: '0.75rem',
                          fontWeight: 700,
                          background: s.is_active ? 'rgba(16, 185, 129, 0.15)' : 'rgba(244, 63, 94, 0.15)',
                          color: s.is_active ? '#10b981' : '#f43f5e'
                        }}>
                          {s.is_active ? 'Active' : 'Disabled'}
                        </span>
                      </td>
                      <td style={{ padding: '0.75rem 1rem' }}>
                        <button
                          onClick={() => handleDeleteService(s.id)}
                          style={{ background: 'transparent', border: 'none', color: '#f43f5e', cursor: 'pointer', padding: '0.25rem' }}
                        >
                          <Trash2 size={16} />
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}

      {/* Add New Service Modal */}
      {showModal && (
        <div style={{
          position: 'fixed',
          top: 0, left: 0, right: 0, bottom: 0,
          background: 'rgba(0,0,0,0.7)',
          display: 'flex', justifyContent: 'center', alignItems: 'center',
          zIndex: 1000,
          padding: '1.5rem'
        }}>
          <div className="glass-panel" style={{ width: '100%', maxWidth: '500px', padding: '2rem', position: 'relative' }}>
            <button
              onClick={() => setShowModal(false)}
              style={{ position: 'absolute', right: '1.25rem', top: '1.25rem', background: 'transparent', border: 'none', color: '#94a3b8', cursor: 'pointer' }}
            >
              <X size={20} />
            </button>

            <h3 style={{ fontSize: '1.35rem', fontWeight: 800, color: '#ffffff', marginBottom: '1.25rem' }}>
              Add New Service Item
            </h3>

            <form onSubmit={handleCreateService}>
              <div className="form-group">
                <label className="form-label">Category</label>
                <select
                  className="form-select"
                  value={newServiceCatId}
                  onChange={(e) => setNewServiceCatId(Number(e.target.value))}
                >
                  {categories.map(c => (
                    <option key={c.id} value={c.id}>{c.icon} {c.name}</option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label className="form-label">Service Name</label>
                <input
                  type="text"
                  className="form-input"
                  placeholder="e.g. AC Gas Refill & Pressure Check"
                  value={newServiceName}
                  onChange={(e) => setNewServiceName(e.target.value)}
                  required
                />
              </div>

              <div className="form-group">
                <label className="form-label">Description</label>
                <textarea
                  className="form-textarea"
                  rows={3}
                  placeholder="Describe service inclusions..."
                  value={newServiceDesc}
                  onChange={(e) => setNewServiceDesc(e.target.value)}
                  required
                />
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
                <div className="form-group">
                  <label className="form-label">Base Price ($)</label>
                  <input
                    type="number"
                    step="0.01"
                    min="1"
                    className="form-input"
                    value={newServicePrice}
                    onChange={(e) => setNewServicePrice(Number(e.target.value))}
                    required
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">Duration (Mins)</label>
                  <input
                    type="number"
                    min="15"
                    step="15"
                    className="form-input"
                    value={newServiceDuration}
                    onChange={(e) => setNewServiceDuration(Number(e.target.value))}
                    required
                  />
                </div>
              </div>

              <button
                type="submit"
                className="btn btn-primary"
                disabled={submitLoading}
                style={{ width: '100%', marginTop: '1rem', padding: '0.85rem' }}
              >
                {submitLoading ? 'Creating...' : 'Create Service Item'}
              </button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
