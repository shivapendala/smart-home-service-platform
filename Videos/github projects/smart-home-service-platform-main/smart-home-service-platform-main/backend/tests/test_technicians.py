import io
from datetime import date, timedelta
import pytest
from fastapi import status
from app.models.user import User, UserRole
from app.core.security import create_access_token


@pytest.fixture
def second_technician_token(db_session):
    user = User(
        email="tech2@example.com",
        hashed_password="hashed_password_123",
        full_name="Edward Technician 2",
        role=UserRole.TECHNICIAN,
        specialization="Electrical Repair",
        experience_years=3,
        is_active=True
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    token = create_access_token(subject=user.id, role=user.role.value)
    return {"token": token, "user": user}


def test_technician_complete_workflow(client, test_customer_token, test_technician_token, test_admin_token):
    # 1. Customer creates booking
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    cat_res = client.get("/api/services")
    service_id = cat_res.json()[0]["id"]

    booking_payload = {
        "service_id": service_id,
        "problem_description": "Full workflow diagnostic test",
        "scheduled_date": str(date.today() + timedelta(days=1)),
        "scheduled_time": "10:00 AM - 12:00 PM",
        "new_address": {
            "street_address": "555 Workflow Way",
            "city": "Metropolis",
            "zip_code": "90210"
        }
    }
    create_res = client.post("/api/bookings", json=booking_payload, headers=cust_headers)
    booking_id = create_res.json()["id"]

    # 2. Admin assigns Technician 1 -> status becomes ASSIGNED
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    tech_id = test_technician_token["user"].id
    assign_res = client.patch(f"/api/bookings/{booking_id}/assign", json={"technician_id": tech_id}, headers=admin_headers)
    assert assign_res.status_code == status.HTTP_200_OK
    assert assign_res.json()["status"] == "ASSIGNED"

    tech1_headers = {"Authorization": f"Bearer {test_technician_token['token']}"}

    # 3. Technician ACCEPT -> ASSIGNED to ACCEPTED
    res_accept = client.post(f"/api/technicians/jobs/{booking_id}/action", data={"action": "ACCEPT"}, headers=tech1_headers)
    assert res_accept.status_code == status.HTTP_200_OK
    assert res_accept.json()["status"] == "ACCEPTED"

    # 4. Technician ON_THE_WAY -> ACCEPTED to ON_THE_WAY
    res_otw = client.post(f"/api/technicians/jobs/{booking_id}/action", data={"action": "ON_THE_WAY"}, headers=tech1_headers)
    assert res_otw.status_code == status.HTTP_200_OK
    assert res_otw.json()["status"] == "ON_THE_WAY"

    # 5. Technician START -> ON_THE_WAY to IN_PROGRESS
    res_start = client.post(f"/api/technicians/jobs/{booking_id}/action", data={"action": "START"}, headers=tech1_headers)
    assert res_start.status_code == status.HTTP_200_OK
    assert res_start.json()["status"] == "IN_PROGRESS"

    # 6. Technician COMPLETE -> IN_PROGRESS to COMPLETED
    res_complete = client.post(f"/api/technicians/jobs/{booking_id}/action", data={"action": "COMPLETE"}, headers=tech1_headers)
    assert res_complete.status_code == status.HTTP_200_OK
    assert res_complete.json()["status"] == "COMPLETED"


def test_technician_job_rejection(client, test_customer_token, test_technician_token, test_admin_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    service_id = client.get("/api/services").json()[0]["id"]
    create_res = client.post("/api/bookings", json={
        "service_id": service_id,
        "problem_description": "Job rejection test",
        "scheduled_date": str(date.today() + timedelta(days=2)),
        "scheduled_time": "02:00 PM",
        "new_address": {"street_address": "123 Reject Rd", "city": "City", "zip_code": "10001"}
    }, headers=cust_headers)
    booking_id = create_res.json()["id"]

    # Admin assigns tech
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    client.patch(f"/api/bookings/{booking_id}/assign", json={"technician_id": test_technician_token["user"].id}, headers=admin_headers)

    # Tech rejects job
    tech_headers = {"Authorization": f"Bearer {test_technician_token['token']}"}
    reject_res = client.post(f"/api/technicians/jobs/{booking_id}/action", data={"action": "REJECT"}, headers=tech_headers)
    assert reject_res.status_code == status.HTTP_200_OK
    data = reject_res.json()
    assert data["status"] == "PENDING"
    assert data["technician_id"] is None


def test_unrelated_technician_security_isolation(client, test_customer_token, test_technician_token, second_technician_token, test_admin_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    service_id = client.get("/api/services").json()[0]["id"]
    create_res = client.post("/api/bookings", json={
        "service_id": service_id,
        "problem_description": "Isolation test",
        "scheduled_date": str(date.today() + timedelta(days=2)),
        "scheduled_time": "02:00 PM",
        "new_address": {"street_address": "777 Isolated St", "city": "City", "zip_code": "10001"}
    }, headers=cust_headers)
    booking_id = create_res.json()["id"]

    # Admin assigns to Tech 1
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    client.patch(f"/api/bookings/{booking_id}/assign", json={"technician_id": test_technician_token["user"].id}, headers=admin_headers)

    # Tech 2 attempts to perform action on Tech 1's booking -> 403 Forbidden
    tech2_headers = {"Authorization": f"Bearer {second_technician_token['token']}"}
    action_res = client.post(f"/api/technicians/jobs/{booking_id}/action", data={"action": "ACCEPT"}, headers=tech2_headers)
    assert action_res.status_code == status.HTTP_403_FORBIDDEN
    assert "Security Violation" in action_res.json()["detail"]


def test_photo_upload_and_validation(client, test_customer_token, test_technician_token, test_admin_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    service_id = client.get("/api/services").json()[0]["id"]
    create_res = client.post("/api/bookings", json={
        "service_id": service_id,
        "problem_description": "Photo upload test",
        "scheduled_date": str(date.today() + timedelta(days=2)),
        "scheduled_time": "02:00 PM",
        "new_address": {"street_address": "888 Photo Ave", "city": "City", "zip_code": "10001"}
    }, headers=cust_headers)
    booking_id = create_res.json()["id"]

    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    client.patch(f"/api/bookings/{booking_id}/assign", json={"technician_id": test_technician_token["user"].id}, headers=admin_headers)

    tech_headers = {"Authorization": f"Bearer {test_technician_token['token']}"}

    # 1. Valid image upload (JPEG)
    fake_image_bytes = b"\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01" + b"\x00" * 100
    file_payload = {"file": ("before_repair.jpg", io.BytesIO(fake_image_bytes), "image/jpeg")}
    data_payload = {"photo_type": "BEFORE"}

    upload_res = client.post(f"/api/technicians/jobs/{booking_id}/photos", files=file_payload, data=data_payload, headers=tech_headers)
    assert upload_res.status_code == status.HTTP_201_CREATED
    photo_data = upload_res.json()
    assert photo_data["photo_type"] == "BEFORE"
    assert "photo_url" in photo_data

    # 2. Invalid file type upload (.txt) -> 400 Bad Request
    invalid_file = {"file": ("malicious.txt", io.BytesIO(b"Hello text file"), "text/plain")}
    invalid_res = client.post(f"/api/technicians/jobs/{booking_id}/photos", files=invalid_file, data=data_payload, headers=tech_headers)
    assert invalid_res.status_code == status.HTTP_400_BAD_REQUEST
    assert "Invalid file type" in invalid_res.json()["detail"]


def test_service_notes(client, test_customer_token, test_technician_token, test_admin_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    service_id = client.get("/api/services").json()[0]["id"]
    create_res = client.post("/api/bookings", json={
        "service_id": service_id,
        "problem_description": "Notes test",
        "scheduled_date": str(date.today() + timedelta(days=2)),
        "scheduled_time": "02:00 PM",
        "new_address": {"street_address": "999 Note St", "city": "City", "zip_code": "10001"}
    }, headers=cust_headers)
    booking_id = create_res.json()["id"]

    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    client.patch(f"/api/bookings/{booking_id}/assign", json={"technician_id": test_technician_token["user"].id}, headers=admin_headers)

    tech_headers = {"Authorization": f"Bearer {test_technician_token['token']}"}
    note_payload = {"note_text": "Replaced faulty capacitor and recharged gas."}
    note_res = client.post(f"/api/technicians/jobs/{booking_id}/notes", json=note_payload, headers=tech_headers)
    assert note_res.status_code == status.HTTP_201_CREATED
    assert note_res.json()["note_text"] == "Replaced faulty capacitor and recharged gas."
