import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { Navbar } from './components/layout/Navbar';
import { MobileBottomNav } from './components/layout/MobileBottomNav';
import { Footer } from './components/layout/Footer';
import { ProtectedRoute } from './components/common/ProtectedRoute';

import { HomePage } from './pages/HomePage';
import { LoginPage } from './pages/auth/LoginPage';
import { RegisterPage } from './pages/auth/RegisterPage';
import { ServiceCatalogPage } from './pages/catalog/ServiceCatalogPage';
import { CustomerDashboard } from './pages/dashboard/CustomerDashboard';
import { TechnicianDashboard } from './pages/dashboard/TechnicianDashboard';
import { AdminDashboard } from './pages/dashboard/AdminDashboard';

// Enterprise Expansion Pages
import CustomerApplianceManager from './pages/customer/CustomerApplianceManager';
import LoyaltyRewardsPortal from './pages/customer/LoyaltyRewardsPortal';
import ShiftScheduler from './pages/technician/ShiftScheduler';
import ZoneCoverageManager from './pages/technician/ZoneCoverageManager';
import InvoicingDashboard from './pages/billing/InvoicingDashboard';
import InventoryStockManager from './pages/inventory/InventoryStockManager';
import AMCPlanCatalog from './pages/amc/AMCPlanCatalog';
import SubscriptionManager from './pages/amc/SubscriptionManager';
import SupportDeskDashboard from './pages/support/SupportDeskDashboard';
import ExecutiveAnalyticsDashboard from './pages/analytics/ExecutiveAnalyticsDashboard';
import AuditLogViewer from './pages/admin/AuditLogViewer';

export const App: React.FC = () => {
  return (
    <AuthProvider>
      <Router>
        <div className="app-container">
          <Navbar />
          <main className="main-content">
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/services" element={<ServiceCatalogPage />} />
              <Route path="/login" element={<LoginPage />} />
              <Route path="/register" element={<RegisterPage />} />
              <Route path="/amc-plans" element={<AMCPlanCatalog />} />

              {/* Customer Routes */}
              <Route
                path="/customer-dashboard"
                element={
                  <ProtectedRoute allowedRoles={['CUSTOMER']}>
                    <CustomerDashboard />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/customer/appliances"
                element={
                  <ProtectedRoute allowedRoles={['CUSTOMER']}>
                    <CustomerApplianceManager />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/customer/loyalty"
                element={
                  <ProtectedRoute allowedRoles={['CUSTOMER']}>
                    <LoyaltyRewardsPortal />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/customer/amc"
                element={
                  <ProtectedRoute allowedRoles={['CUSTOMER']}>
                    <SubscriptionManager />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/customer/invoices"
                element={
                  <ProtectedRoute allowedRoles={['CUSTOMER']}>
                    <InvoicingDashboard />
                  </ProtectedRoute>
                }
              />

              {/* Technician Routes */}
              <Route
                path="/technician-dashboard"
                element={
                  <ProtectedRoute allowedRoles={['TECHNICIAN']}>
                    <TechnicianDashboard />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/technician/shifts"
                element={
                  <ProtectedRoute allowedRoles={['TECHNICIAN']}>
                    <ShiftScheduler />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/technician/zones"
                element={
                  <ProtectedRoute allowedRoles={['TECHNICIAN']}>
                    <ZoneCoverageManager />
                  </ProtectedRoute>
                }
              />

              {/* Admin & Management Routes */}
              <Route
                path="/admin-dashboard"
                element={
                  <ProtectedRoute allowedRoles={['ADMIN']}>
                    <AdminDashboard />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/inventory"
                element={
                  <ProtectedRoute allowedRoles={['ADMIN']}>
                    <InventoryStockManager />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/support-desk"
                element={
                  <ProtectedRoute allowedRoles={['ADMIN', 'CUSTOMER']}>
                    <SupportDeskDashboard />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/analytics"
                element={
                  <ProtectedRoute allowedRoles={['ADMIN']}>
                    <ExecutiveAnalyticsDashboard />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/audit-logs"
                element={
                  <ProtectedRoute allowedRoles={['ADMIN']}>
                    <AuditLogViewer />
                  </ProtectedRoute>
                }
              />
            </Routes>
          </main>
          <Footer />
          <MobileBottomNav />
        </div>
      </Router>
    </AuthProvider>
  );
};

export default App;
