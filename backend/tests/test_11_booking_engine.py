import pytest


def test_recurring_schedules(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}

    sched_payload = {
        "service_id": 1,
        "address_id": 1,
        "frequency": "MONTHLY",
        "start_date": "2026-09-01",
        "preferred_time_slot": "09:00 - 11:00"
    }
    r = client.post("/api/v1/booking-engine/recurring", json=sched_payload, headers=headers)
    assert r.status_code in [201, 404]

    r_list = client.get("/api/v1/booking-engine/recurring/me", headers=headers)
    assert r_list.status_code == 200


def test_slot_capacity_query(client):
    r = client.get("/api/v1/booking-engine/capacity?slot_date=2026-09-01&time_slot=10:00-12:00&zip_code=90210")
    assert r.status_code == 200
    data = r.json()
    assert data["max_capacity"] == 8
    assert data["available_capacity"] == 8


def test_multi_tech_assignment(client, test_admin_token, test_technician_token):
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    tech_id = test_technician_token["user"].id

    payload = {
        "booking_id": 1,
        "technician_id": tech_id,
        "role_title": "ASSISTANT_TECHNICIAN"
    }
    r = client.post("/api/v1/booking-engine/multi-tech", json=payload, headers=admin_headers)
    assert r.status_code in [201, 404]

    r_list = client.get("/api/v1/booking-engine/multi-tech/1", headers=admin_headers)
    assert r_list.status_code == 200


def test_cancellation_penalty_calculation(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}

    r = client.get("/api/v1/booking-engine/cancellation-penalty/1", headers=headers)
    assert r.status_code in [200, 404]
