from datetime import date, timedelta
import pytest
from fastapi import status


def test_notification_creation_and_triggers(client, test_customer_token, test_technician_token, test_admin_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    service_id = client.get("/api/services").json()[0]["id"]

    # 1. Customer creates booking -> triggers BOOKING_CREATED notification
    booking_res = client.post("/api/bookings", json={
        "service_id": service_id,
        "problem_description": "Notification test booking",
        "scheduled_date": str(date.today() + timedelta(days=1)),
        "scheduled_time": "10:00 AM",
        "new_address": {"street_address": "123 Notif St", "city": "City", "zip_code": "10001"}
    }, headers=cust_headers)
    booking_id = booking_res.json()["id"]

    notif_res1 = client.get("/api/notifications", headers=cust_headers)
    assert notif_res1.status_code == status.HTTP_200_OK
    data1 = notif_res1.json()
    assert data1["unread_count"] >= 1
    types = [n["type"] for n in data1["notifications"]]
    assert "BOOKING_CREATED" in types

    # 2. Admin assigns technician -> triggers TECHNICIAN_ASSIGNED for Customer & JOB_DISPATCH for Tech
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    tech_id = test_technician_token["user"].id
    client.patch(f"/api/bookings/{booking_id}/assign", json={"technician_id": tech_id}, headers=admin_headers)

    # Check Technician notifications
    tech_headers = {"Authorization": f"Bearer {test_technician_token['token']}"}
    tech_notif_res = client.get("/api/notifications", headers=tech_headers)
    assert tech_notif_res.status_code == status.HTTP_200_OK
    tech_types = [n["type"] for n in tech_notif_res.json()["notifications"]]
    assert "JOB_DISPATCH" in tech_types

    # 3. Technician actions -> trigger STATUS_ON_THE_WAY, etc.
    client.post(f"/api/technicians/jobs/{booking_id}/action", data={"action": "ACCEPT"}, headers=tech_headers)
    client.post(f"/api/technicians/jobs/{booking_id}/action", data={"action": "ON_THE_WAY"}, headers=tech_headers)

    notif_res2 = client.get("/api/notifications", headers=cust_headers)
    cust_types = [n["type"] for n in notif_res2.json()["notifications"]]
    assert "TECHNICIAN_ASSIGNED" in cust_types
    assert "STATUS_ON_THE_WAY" in cust_types


def test_mark_as_read_and_security_isolation(client, test_customer_token, test_technician_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    service_id = client.get("/api/services").json()[0]["id"]

    # Create booking to generate notification
    client.post("/api/bookings", json={
        "service_id": service_id,
        "problem_description": "Mark as read test",
        "scheduled_date": str(date.today() + timedelta(days=1)),
        "scheduled_time": "10:00 AM",
        "new_address": {"street_address": "456 Notif Ave", "city": "City", "zip_code": "10001"}
    }, headers=cust_headers)

    # Fetch customer notification ID
    notif_res = client.get("/api/notifications", headers=cust_headers)
    notifications = notif_res.json()["notifications"]
    assert len(notifications) > 0
    target_notif_id = notifications[0]["id"]

    # Technician attempts to mark Customer's notification as read -> 403 Forbidden
    tech_headers = {"Authorization": f"Bearer {test_technician_token['token']}"}
    forbidden_res = client.patch(f"/api/notifications/{target_notif_id}/read", headers=tech_headers)
    assert forbidden_res.status_code == status.HTTP_403_FORBIDDEN

    # Customer marks single notification as read -> 200 OK
    read_res = client.patch(f"/api/notifications/{target_notif_id}/read", headers=cust_headers)
    assert read_res.status_code == status.HTTP_200_OK
    assert read_res.json()["is_read"] is True

    # Customer marks all as read -> 200 OK
    read_all_res = client.patch("/api/notifications/read-all", headers=cust_headers)
    assert read_all_res.status_code == status.HTTP_200_OK

    after_res = client.get("/api/notifications", headers=cust_headers)
    assert after_res.json()["unread_count"] == 0
