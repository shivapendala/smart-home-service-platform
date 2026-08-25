import pytest


def test_support_desk_workflow(client, test_customer_token, test_admin_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}

    # 1. Create support ticket
    tck_payload = {
        "subject": "Billing issue on booking #102",
        "category": "BILLING",
        "priority": "HIGH",
        "initial_comment": "I was charged twice for the capacitor spare part."
    }
    r_tck = client.post("/api/v1/support-tickets/tickets", json=tck_payload, headers=cust_headers)
    assert r_tck.status_code == 201
    data = r_tck.json()
    assert data["priority"] == "HIGH"
    tck_id = data["id"]

    # 2. Get customer tickets
    r_list = client.get("/api/v1/support-tickets/tickets/me", headers=cust_headers)
    assert r_list.status_code == 200
    assert len(r_list.json()) == 1

    # 3. Add comment
    cmt_payload = {
        "ticket_id": tck_id,
        "comment_text": "Agent assigned. Reviewing invoice transaction log.",
        "is_internal_note": True
    }
    r_cmt = client.post("/api/v1/support-tickets/comments", json=cmt_payload, headers=admin_headers)
    assert r_cmt.status_code == 201

    # 4. Update status
    r_stat = client.put(f"/api/v1/support-tickets/tickets/{tck_id}/status?new_status=RESOLVED", headers=admin_headers)
    assert r_stat.status_code == 200
    assert r_stat.json()["status"] == "RESOLVED"

    # 5. Customer CSAT Survey
    surv_payload = {
        "ticket_id": tck_id,
        "rating": 5,
        "feedback_notes": "Prompt resolution and polite agent!"
    }
    r_surv = client.post("/api/v1/support-tickets/survey", json=surv_payload, headers=cust_headers)
    assert r_surv.status_code == 201
    assert r_surv.json()["rating"] == 5
