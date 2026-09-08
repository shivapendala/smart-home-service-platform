from datetime import date, timedelta
import pytest
from fastapi import status
from app.models.user import User, UserRole
from app.core.security import create_access_token


@pytest.fixture
def second_customer_token(db_session):
    user = User(
        email="customer2@example.com",
        hashed_password="hashed_password_123",
        full_name="Bob Customer",
        role=UserRole.CUSTOMER,
        is_active=True
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    token = create_access_token(subject=user.id, role=user.role.value)
    return {"token": token, "user": user}


def test_booking_creation_workflow(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}

    # 1. Get valid service ID
    cat_res = client.get("/api/services")
    service_id = cat_res.json()[0]["id"]

    # 2. Customer creates booking with inline new address
    booking_payload = {
        "service_id": service_id,
        "problem_description": "AC is making loud rattling noise and not blowing cold air.",
        "scheduled_date": str(date.today() + timedelta(days=2)),
        "scheduled_time": "10:00 AM - 12:00 PM",
        "new_address": {
            "street_address": "456 Oak Avenue, Apt 4B",
            "city": "Metropolis",
            "state": "CA",
            "zip_code": "90210",
            "is_default": True
        }
    }
    response = client.post("/api/bookings", json=booking_payload, headers=headers)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["problem_description"] == "AC is making loud rattling noise and not blowing cold air."
    assert data["status"] == "PENDING"
    assert data["address"]["street_address"] == "456 Oak Avenue, Apt 4B"
    assert "status_history" in data
    assert len(data["status_history"]) >= 1
    assert data["status_history"][0]["new_status"] == "PENDING"


def test_booking_invalid_service(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    payload = {
        "service_id": 99999,  # Invalid service ID
        "problem_description": "Fix my appliance",
        "scheduled_date": str(date.today() + timedelta(days=1)),
        "scheduled_time": "02:00 PM - 04:00 PM",
        "new_address": {
            "street_address": "123 Main St",
            "city": "City",
            "zip_code": "10001"
        }
    }
    response = client.post("/api/bookings", json=payload, headers=headers)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Invalid service ID" in response.json()["detail"]


def test_booking_invalid_past_date(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    cat_res = client.get("/api/services")
    service_id = cat_res.json()[0]["id"]

    payload = {
        "service_id": service_id,
        "problem_description": "Past date test",
        "scheduled_date": str(date.today() - timedelta(days=5)),  # Past date
        "scheduled_time": "10:00 AM",
        "new_address": {
            "street_address": "123 Main St",
            "city": "City",
            "zip_code": "10001"
        }
    }
    response = client.post("/api/bookings", json=payload, headers=headers)
    # Pydantic schema or service level validation returns 422 or 400
    assert response.status_code in (status.HTTP_400_BAD_REQUEST, status.HTTP_422_UNPROCESSABLE_ENTITY)


def test_unauthorized_customer_booking_access(client, test_customer_token, second_customer_token):
    # Customer 1 creates a booking
    cust1_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    cat_res = client.get("/api/services")
    service_id = cat_res.json()[0]["id"]

    booking_payload = {
        "service_id": service_id,
        "problem_description": "Private issue for Customer 1",
        "scheduled_date": str(date.today() + timedelta(days=3)),
        "scheduled_time": "02:00 PM",
        "new_address": {
            "street_address": "789 Private Way",
            "city": "Metropolis",
            "zip_code": "90210"
        }
    }
    create_res = client.post("/api/bookings", json=booking_payload, headers=cust1_headers)
    booking_id = create_res.json()["id"]

    # Customer 2 attempts to read Customer 1's booking -> 403 Forbidden
    cust2_headers = {"Authorization": f"Bearer {second_customer_token['token']}"}
    read_res = client.get(f"/api/bookings/{booking_id}", headers=cust2_headers)
    assert read_res.status_code == status.HTTP_403_FORBIDDEN


def test_booking_cancellation_and_status_history(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    cat_res = client.get("/api/services")
    service_id = cat_res.json()[0]["id"]

    # 1. Create booking
    booking_payload = {
        "service_id": service_id,
        "problem_description": "Leaky faucet needing quick repair",
        "scheduled_date": str(date.today() + timedelta(days=2)),
        "scheduled_time": "09:00 AM",
        "new_address": {
            "street_address": "101 Water St",
            "city": "Metropolis",
            "zip_code": "90210"
        }
    }
    create_res = client.post("/api/bookings", json=booking_payload, headers=headers)
    booking_id = create_res.json()["id"]

    # 2. Cancel booking (PUT /api/bookings/{id}/cancel)
    cancel_res = client.put(f"/api/bookings/{booking_id}/cancel", headers=headers)
    assert cancel_res.status_code == status.HTTP_200_OK
    cancelled_data = cancel_res.json()
    assert cancelled_data["status"] == "CANCELLED"

    # 3. Check status history
    history = cancelled_data["status_history"]
    new_statuses = [h["new_status"] for h in history]
    assert "PENDING" in new_statuses
    assert "CANCELLED" in new_statuses


def test_strict_invalid_status_transition(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    cat_res = client.get("/api/services")
    service_id = cat_res.json()[0]["id"]

    booking_payload = {
        "service_id": service_id,
        "problem_description": "Strict transition test",
        "scheduled_date": str(date.today() + timedelta(days=4)),
        "scheduled_time": "11:00 AM",
        "new_address": {
            "street_address": "202 State St",
            "city": "Metropolis",
            "zip_code": "90210"
        }
    }
    create_res = client.post("/api/bookings", json=booking_payload, headers=headers)
    booking_id = create_res.json()["id"]

    # Try invalid direct transition from PENDING -> COMPLETED (Not allowed in state machine)
    invalid_payload = {"status": "COMPLETED"}
    transition_res = client.patch(f"/api/bookings/{booking_id}/status", json=invalid_payload, headers=headers)
    assert transition_res.status_code == status.HTTP_400_BAD_REQUEST
    assert "Invalid status transition" in transition_res.json()["detail"]
