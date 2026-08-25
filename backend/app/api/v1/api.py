from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth, services, bookings, technicians, admin, notifications,
    customer_portal, technician_mgmt, booking_engine, payments_billing,
    communication, inventory, warranty_amc, support_tickets, analytics,
    ai_recommendations, audit_security, service_catalog, user_management,
    booking_fulfillment, technician_dispatch, admin_oversight, review_ratings,
    notification_core, workflow_automation, financial_reporting, vendor_management,
    fleet_logistics, customer_feedback, system_health, platform_governance, enterprise_integration
)

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(services.router, prefix="/services", tags=["Service Catalog"])
api_router.include_router(bookings.router, prefix="/bookings", tags=["Bookings"])
api_router.include_router(technicians.router, prefix="/technicians", tags=["Technician Management Core"])
api_router.include_router(admin.router, prefix="/admin", tags=["Admin Oversight"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["Notifications Core"])
api_router.include_router(customer_portal.router, prefix="/customer-portal", tags=["Customer Portal"])

# Enterprise Expansion Modules
api_router.include_router(technician_mgmt.router, prefix="/technicians/management", tags=["Technician Engine & Shifts"])
api_router.include_router(booking_engine.router, prefix="/booking-engine", tags=["Capacity & Subscriptions Engine"])
api_router.include_router(payments_billing.router, prefix="/billing", tags=["Payments, Invoicing & Refunds"])
api_router.include_router(communication.router, prefix="/communication", tags=["Live Chat & Messaging Center"])
api_router.include_router(inventory.router, prefix="/inventory", tags=["Warehouse & Van Inventory System"])
api_router.include_router(warranty_amc.router, prefix="/amc-warranty", tags=["AMC Plans & Warranty Claims"])
api_router.include_router(support_tickets.router, prefix="/support-tickets", tags=["Support & Ticketing Desk"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics & BI Engine"])
api_router.include_router(ai_recommendations.router, prefix="/ai", tags=["AI Diagnostics & Recommendations"])
api_router.include_router(audit_security.router, prefix="/security", tags=["Audit & Security System"])

# Governance & Fulfillment Modules
api_router.include_router(service_catalog.router, prefix="/catalog-ext", tags=["Service Catalog Ext"])
api_router.include_router(user_management.router, prefix="/users-ext", tags=["User Management Ext"])
api_router.include_router(booking_fulfillment.router, prefix="/fulfillment", tags=["Fulfillment Engine"])
api_router.include_router(technician_dispatch.router, prefix="/dispatch", tags=["Dispatch Center"])
api_router.include_router(admin_oversight.router, prefix="/oversight", tags=["Governance Oversight"])
api_router.include_router(review_ratings.router, prefix="/ratings", tags=["Ratings Desk"])
api_router.include_router(notification_core.router, prefix="/notify-core", tags=["Notification Core Services"])
api_router.include_router(workflow_automation.router, prefix="/workflows", tags=["Workflow Automation"])
api_router.include_router(financial_reporting.router, prefix="/financials", tags=["Financial Reporting"])
api_router.include_router(vendor_management.router, prefix="/vendors", tags=["Vendor Management"])
api_router.include_router(fleet_logistics.router, prefix="/fleet", tags=["Fleet Logistics"])
api_router.include_router(customer_feedback.router, prefix="/feedback", tags=["Customer Feedback"])
api_router.include_router(system_health.router, prefix="/health", tags=["System Health"])
api_router.include_router(platform_governance.router, prefix="/governance", tags=["Platform Governance"])
api_router.include_router(enterprise_integration.router, prefix="/integrations", tags=["Enterprise Integrations"])
