import pytest
from datetime import date


def test_technician_shifts_workflow(client, test_technician_token):
    headers = {"Authorization": f"Bearer {test_technician_token['token']}"}

    # 1. Create shift
    shift_payload = {
        "day_of_week": "MONDAY",
        "shift_start": "08:00:00",
        "shift_end": "17:00:00",
        "break_start": "12:00:00",
        "break_end": "13:00:00",
        "is_active": True,
        "max_jobs_per_shift": 5
    }
    r = client.post("/api/v1/technicians/management/shifts", json=shift_payload, headers=headers)
    assert r.status_code == 201
    data = r.json()
    assert data["day_of_week"] == "MONDAY"
    assert data["max_jobs_per_shift"] == 5

    # 2. Get shifts
    r_list = client.get("/api/v1/technicians/management/shifts/me", headers=headers)
    assert r_list.status_code == 200
    assert len(r_list.json()) == 1


def test_technician_zones_workflow(client, test_technician_token):
    headers = {"Authorization": f"Bearer {test_technician_token['token']}"}

    zone_payload = {
        "zone_name": "Downtown Central",
        "zip_code": "90210",
        "city": "Los Angeles",
        "state": "CA",
        "radius_km": 10.0,
        "is_primary_zone": True
    }
    r = client.post("/api/v1/technicians/management/zones", json=zone_payload, headers=headers)
    assert r.status_code == 201
    assert r.json()["zip_code"] == "90210"

    r_list = client.get("/api/v1/technicians/management/zones/me", headers=headers)
    assert r_list.status_code == 200
    assert len(r_list.json()) == 1


def test_skills_certifications_workflow(client, test_technician_token):
    headers = {"Authorization": f"Bearer {test_technician_token['token']}"}

    # Add skill
    skill_payload = {
        "skill_name": "Inverter AC Diagnostics",
        "category_name": "HVAC",
        "proficiency_level": "EXPERT",
        "years_experience": 4,
        "is_certified": True
    }
    r_skill = client.post("/api/v1/technicians/management/skills", json=skill_payload, headers=headers)
    assert r_skill.status_code == 201
    assert r_skill.json()["proficiency_level"] == "EXPERT"

    # Get skills
    r_s_list = client.get("/api/v1/technicians/management/skills/me", headers=headers)
    assert r_s_list.status_code == 200
    assert len(r_s_list.json()) == 1

    # Add cert
    cert_payload = {
        "certification_title": "Master HVAC Technician",
        "issuing_authority": "EPA National",
        "license_number": "EPA-9988776655",
        "issue_date": "2021-05-10",
        "expiry_date": "2028-05-10"
    }
    r_cert = client.post("/api/v1/technicians/management/certifications", json=cert_payload, headers=headers)
    assert r_cert.status_code == 201
    assert r_cert.json()["license_number"] == "EPA-9988776655"

    # Get certs
    r_c_list = client.get("/api/v1/technicians/management/certifications/me", headers=headers)
    assert r_c_list.status_code == 200
    assert len(r_c_list.json()) == 1


def test_emergency_dispatch_workflow(client, test_customer_token, test_admin_token, test_technician_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    tech_id = test_technician_token["user"].id

    # Enqueue emergency dispatch
    dispatch_payload = {
        "booking_id": 1,
        "priority": "CRITICAL_EMERGENCY",
        "dispatch_reason": "Major gas leak warning in kitchen area",
        "response_sla_minutes": 15
    }
    r = client.post("/api/v1/technicians/management/emergency-dispatch", json=dispatch_payload, headers=cust_headers)
    assert r.status_code == 201
    d_data = r.json()
    assert d_data["priority"] == "CRITICAL_EMERGENCY"
    dispatch_id = d_data["id"]

    # Pending queue
    r_queue = client.get("/api/v1/technicians/management/emergency-dispatch/pending", headers=admin_headers)
    assert r_queue.status_code == 200
    assert len(r_queue.json()) >= 1

    # Assign technician
    r_assign = client.put(f"/api/v1/technicians/management/emergency-dispatch/{dispatch_id}/assign/{tech_id}", headers=admin_headers)
    assert r_assign.status_code == 200
    assert r_assign.json()["is_dispatched"] == True


def test_payouts_workflow(client, test_admin_token, test_technician_token):
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    tech_headers = {"Authorization": f"Bearer {test_technician_token['token']}"}
    tech_id = test_technician_token["user"].id

    payout_payload = {
        "technician_id": tech_id,
        "period_start": "2026-08-01",
        "period_end": "2026-08-15",
        "gross_earnings": 1500.0,
        "platform_commission": 300.0,
        "payout_method": "DIRECT_DEPOSIT"
    }
    r = client.post("/api/v1/technicians/management/payouts", json=payout_payload, headers=admin_headers)
    assert r.status_code == 201
    p_data = r.json()
    assert p_data["net_payout"] == 1200.0
    payout_id = p_data["id"]

    # List payouts
    r_p_list = client.get("/api/v1/technicians/management/payouts", headers=tech_headers)
    assert r_p_list.status_code == 200

    # Process payout
    r_proc = client.put(
        f"/api/v1/technicians/management/payouts/{payout_id}/process?reference_number=REF-889900",
        headers=admin_headers
    )
    assert r_proc.status_code == 200
    assert r_proc.json()["status"] == "PAID"
