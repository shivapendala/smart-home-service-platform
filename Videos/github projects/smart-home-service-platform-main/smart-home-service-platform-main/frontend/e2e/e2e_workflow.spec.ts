import { test, expect } from '@playwright/test';

test.describe('Smart Home Service Platform E2E Workflow', () => {
  const API_BASE = 'http://localhost:8000/api';

  test('Complete Customer -> Admin -> Technician -> Review Workflow', async ({ request, page }) => {
    const timestamp = Date.now();
    const customerEmail = `e2e_cust_${timestamp}@example.com`;
    const techEmail = `e2e_tech_${timestamp}@example.com`;
    const adminEmail = `e2e_admin_${timestamp}@example.com`;
    const password = 'Password123!';

    // 1. Register Customer, Technician, Admin via API
    const custReg = await request.post(`${API_BASE}/auth/register`, {
      data: { email: customerEmail, password, full_name: 'E2E Customer', role: 'CUSTOMER' }
    });
    expect(custReg.status()).toBe(201);

    const techReg = await request.post(`${API_BASE}/auth/register`, {
      data: { email: techEmail, password, full_name: 'E2E Tech', role: 'TECHNICIAN', specialization: 'AC Repair' }
    });
    expect(techReg.status()).toBe(201);
    const techUser = await techReg.json();

    const adminReg = await request.post(`${API_BASE}/auth/register`, {
      data: { email: adminEmail, password, full_name: 'E2E Admin', role: 'ADMIN' }
    });
    expect(adminReg.status()).toBe(201);

    // 2. Customer Login & Get Token
    const custLogin = await request.post(`${API_BASE}/auth/login`, {
      data: { email: customerEmail, password }
    });
    expect(custLogin.status()).toBe(200);
    const custToken = (await custLogin.json()).access_token;

    // 3. Browse Services Catalog
    const servicesRes = await request.get(`${API_BASE}/services`);
    expect(servicesRes.status()).toBe(200);
    const services = await servicesRes.json();
    expect(services.length).toBeGreaterThan(0);
    const selectedService = services[0];

    // 4. Create Booking
    const bookingRes = await request.post(`${API_BASE}/bookings`, {
      headers: { Authorization: `Bearer ${custToken}` },
      data: {
        service_id: selectedService.id,
        problem_description: 'E2E test cooling issue',
        scheduled_date: new Date(Date.now() + 86400000).toISOString().split('T')[0],
        scheduled_time: '10:00 AM',
        new_address: { street_address: '100 E2E St', city: 'Metropolis', zip_code: '90210' }
      }
    });
    expect(bookingRes.status()).toBe(201);
    const booking = await bookingRes.json();
    expect(booking.status).toBe('PENDING');

    // 5. Admin Login & Assign Technician
    const adminLogin = await request.post(`${API_BASE}/auth/login`, {
      data: { email: adminEmail, password }
    });
    const adminToken = (await adminLogin.json()).access_token;

    const assignRes = await request.patch(`${API_BASE}/bookings/${booking.id}/assign`, {
      headers: { Authorization: `Bearer ${adminToken}` },
      data: { technician_id: techUser.id }
    });
    expect(assignRes.status()).toBe(200);
    expect((await assignRes.json()).status).toBe('ASSIGNED');

    // 6. Technician Login & Complete Job Workflow
    const techLogin = await request.post(`${API_BASE}/auth/login`, {
      data: { email: techEmail, password }
    });
    const techToken = (await techLogin.json()).access_token;

    // Accept -> On The Way -> Start -> Complete
    const acceptRes = await request.post(`${API_BASE}/technicians/jobs/${booking.id}/action`, {
      headers: { Authorization: `Bearer ${techToken}` },
      form: { action: 'ACCEPT' }
    });
    expect(acceptRes.status()).toBe(200);

    const otwRes = await request.post(`${API_BASE}/technicians/jobs/${booking.id}/action`, {
      headers: { Authorization: `Bearer ${techToken}` },
      form: { action: 'ON_THE_WAY' }
    });
    expect(otwRes.status()).toBe(200);

    const startRes = await request.post(`${API_BASE}/technicians/jobs/${booking.id}/action`, {
      headers: { Authorization: `Bearer ${techToken}` },
      form: { action: 'START' }
    });
    expect(startRes.status()).toBe(200);

    const completeRes = await request.post(`${API_BASE}/technicians/jobs/${booking.id}/action`, {
      headers: { Authorization: `Bearer ${techToken}` },
      form: { action: 'COMPLETE' }
    });
    expect(completeRes.status()).toBe(200);
    expect((await completeRes.json()).status).toBe('COMPLETED');

    // 7. Customer Reviews Completed Service
    const reviewRes = await request.post(`${API_BASE}/reviews`, {
      headers: { Authorization: `Bearer ${custToken}` },
      data: { booking_id: booking.id, rating: 5, comment: 'Outstanding E2E service!' }
    });
    expect(reviewRes.status()).toBe(201);
    expect((await reviewRes.json()).rating).toBe(5);
  });
});
