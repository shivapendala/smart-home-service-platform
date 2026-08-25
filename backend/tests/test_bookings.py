from datetime import date, timedelta
import pytest
from fastapi import status


def test_create_booking_flow(client, test_customer_token, test_technician_token):
    # 1. Get available service from catalog
    cat_res = client.get("/api/v1/services/items")
    service_id = cat_res.json()[0]["id"]

    # 2. Customer creates booking
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    booking_payload = {
        "service_id": service_id,
        "scheduled_date": str(date.today() + timedelta(days=2)),
        "scheduled_time_slot": "10:00 AM - 12:00 PM",
        "address_line": "123 Elm Street",
        "city": "Metropolis",
        "zip_code": "10001",
        "notes": "Ring doorbell upon arrival."
    }
    create_res = client.post("/api/v1/bookings/", json=booking_payload, headers=headers)
    assert create_res.status_code == status.HTTP_201_CREATED
    booking_data = create_res.json()
    assert booking_data["address_line"] == "123 Elm Street"
    assert booking_data["status"] in ["ASSIGNED", "PENDING"]
    assert "total_amount" in booking_data

    booking_id = booking_data["id"]

    # 3. Technician updates status to IN_PROGRESS
    tech_headers = {"Authorization": f"Bearer {test_technician_token['token']}"}
    status_payload = {"status": "IN_PROGRESS"}
    status_res = client.patch(f"/api/v1/bookings/{booking_id}/status", json=status_payload, headers=tech_headers)
    assert status_res.status_code == status.HTTP_200_OK
    assert status_res.json()["status"] == "IN_PROGRESS"

    # 4. Technician marks COMPLETED
    complete_payload = {"status": "COMPLETED"}
    complete_res = client.patch(f"/api/v1/bookings/{booking_id}/status", json=complete_payload, headers=tech_headers)
    assert complete_res.status_code == status.HTTP_200_OK
    assert complete_res.json()["status"] == "COMPLETED"


def test_list_my_bookings(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    res = client.get("/api/v1/bookings/my", headers=headers)
    assert res.status_code == status.HTTP_200_OK
    assert isinstance(res.json(), list)
