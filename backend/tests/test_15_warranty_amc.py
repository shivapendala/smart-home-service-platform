import pytest


def test_amc_plans_and_subscriptions(client, test_admin_token, test_customer_token):
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}

    # 1. Create plan
    plan_payload = {
        "plan_name": "Gold Comprehensive Home AMC",
        "tier": "GOLD_PREMIUM",
        "description": "Covers AC, Plumbing & Electrical with 4 free visits.",
        "annual_price": 299.99,
        "duration_months": 12,
        "covered_visits_per_year": 4,
        "discount_on_spare_parts": 15.0
    }
    r_plan = client.post("/api/v1/amc-warranty/plans", json=plan_payload, headers=admin_headers)
    assert r_plan.status_code == 201
    plan_id = r_plan.json()["id"]

    # 2. List plans
    r_list = client.get("/api/v1/amc-warranty/plans")
    assert r_list.status_code == 200
    assert len(r_list.json()) >= 1

    # 3. Customer subscribe
    sub_payload = {
        "amc_plan_id": plan_id,
        "start_date": "2026-09-01",
        "is_auto_renew": True
    }
    r_sub = client.post("/api/v1/amc-warranty/subscribe", json=sub_payload, headers=cust_headers)
    assert r_sub.status_code == 201
    sub_data = r_sub.json()
    assert sub_data["visits_remaining"] == 4
    sub_id = sub_data["id"]

    # 4. Check scheduled inspections
    r_insp = client.get(f"/api/v1/amc-warranty/inspections/{sub_id}", headers=cust_headers)
    assert r_insp.status_code == 200
    assert len(r_insp.json()) == 4
