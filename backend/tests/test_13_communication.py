import pytest


def test_live_chat_and_template_workflow(client, test_customer_token, test_technician_token, test_admin_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    tech_id = test_technician_token["user"].id
    cust_id = test_customer_token["user"].id

    # 1. Send chat message
    chat_payload = {
        "booking_id": 1,
        "recipient_id": tech_id,
        "message_text": "Hello, when will you arrive?"
    }
    r_chat = client.post("/api/v1/communication/chat", json=chat_payload, headers=cust_headers)
    assert r_chat.status_code == 201
    assert r_chat.json()["message_text"] == "Hello, when will you arrive?"

    # 2. Get chat history
    r_hist = client.get("/api/v1/communication/chat/booking/1", headers=cust_headers)
    assert r_hist.status_code == 200
    assert len(r_hist.json()) == 1

    # 3. Create notification template
    tmpl_payload = {
        "template_key": "BOOKING_CONFIRM_SMS",
        "channel": "SMS",
        "title_template": "Booking Confirmed",
        "body_template": "Your booking #{booking_id} is scheduled for {date}."
    }
    r_tmpl = client.post("/api/v1/communication/templates", json=tmpl_payload, headers=admin_headers)
    assert r_tmpl.status_code == 201

    # 4. Dispatch message
    disp_payload = {
        "recipient_user_id": cust_id,
        "template_key": "BOOKING_CONFIRM_SMS",
        "template_params": {"booking_id": 101, "date": "Tomorrow at 10 AM"}
    }
    r_disp = client.post("/api/v1/communication/dispatch", json=disp_payload, headers=admin_headers)
    assert r_disp.status_code == 201
    assert r_disp.json()["status"] == "SENT"
