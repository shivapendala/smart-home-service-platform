from datetime import date, timedelta
import pytest
from fastapi import status
from app.models.user import User, UserRole


def test_admin_dashboard_stats(client, test_admin_token, test_customer_token):
    # Customer attempt on Admin stats -> 403 Forbidden
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    res1 = client.get("/api/admin/dashboard/stats", headers=cust_headers)
    assert res1.status_code == status.HTTP_403_FORBIDDEN

    # Admin attempt on Admin stats -> 200 OK with summary metrics
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    res2 = client.get("/api/admin/dashboard/stats", headers=admin_headers)
    assert res2.status_code == status.HTTP_200_OK
    data = res2.json()
    assert "total_customers" in data
    assert "total_technicians" in data
    assert "todays_bookings" in data
    assert "revenue_summary" in data


def test_payment_and_refund_workflow(client, test_customer_token, test_admin_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    service_id = client.get("/api/services").json()[0]["id"]

    # 1. Create booking
    booking_res = client.post("/api/bookings", json={
        "service_id": service_id,
        "problem_description": "Payment test booking",
        "scheduled_date": str(date.today() + timedelta(days=1)),
        "scheduled_time": "10:00 AM",
        "new_address": {"street_address": "111 Pay St", "city": "City", "zip_code": "10001"}
    }, headers=cust_headers)
    booking_id = booking_res.json()["id"]

    # 2. Process payment (Customer)
    pay_res = client.post("/api/payments", json={
        "booking_id": booking_id,
        "amount": 79.00,
        "payment_method": "CARD"
    }, headers=cust_headers)
    assert pay_res.status_code == status.HTTP_201_CREATED
    pay_data = pay_res.json()
    assert pay_data["status"] == "PAID"
    assert pay_data["amount"] == 79.00
    payment_id = pay_data["id"]

    # 3. Duplicate payment attempt -> 400 Bad Request
    dup_pay = client.post("/api/payments", json={
        "booking_id": booking_id,
        "amount": 79.00,
        "payment_method": "CARD"
    }, headers=cust_headers)
    assert dup_pay.status_code == status.HTTP_400_BAD_REQUEST

    # 4. Refund payment (Admin)
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    refund_res = client.post(f"/api/payments/{payment_id}/refund", headers=admin_headers)
    assert refund_res.status_code == status.HTTP_200_OK
    assert refund_res.json()["status"] == "REFUNDED"


def test_review_creation_and_duplicate_block(client, test_customer_token, test_technician_token, test_admin_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    service_id = client.get("/api/services").json()[0]["id"]

    # 1. Create booking
    booking_res = client.post("/api/bookings", json={
        "service_id": service_id,
        "problem_description": "Review test booking",
        "scheduled_date": str(date.today() + timedelta(days=1)),
        "scheduled_time": "10:00 AM",
        "new_address": {"street_address": "222 Star Ave", "city": "City", "zip_code": "10001"}
    }, headers=cust_headers)
    booking_id = booking_res.json()["id"]

    # Attempt review BEFORE booking is completed -> 400 Bad Request
    pre_review = client.post("/api/reviews", json={
        "booking_id": booking_id,
        "rating": 5,
        "comment": "Too early review"
    }, headers=cust_headers)
    assert pre_review.status_code == status.HTTP_400_BAD_REQUEST
    assert "COMPLETED" in pre_review.json()["detail"]

    # Transition booking to COMPLETED via technician workflow
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    tech_id = test_technician_token["user"].id
    client.patch(f"/api/bookings/{booking_id}/assign", json={"technician_id": tech_id}, headers=admin_headers)

    tech_headers = {"Authorization": f"Bearer {test_technician_token['token']}"}
    client.post(f"/api/technicians/jobs/{booking_id}/action", data={"action": "ACCEPT"}, headers=tech_headers)
    client.post(f"/api/technicians/jobs/{booking_id}/action", data={"action": "ON_THE_WAY"}, headers=tech_headers)
    client.post(f"/api/technicians/jobs/{booking_id}/action", data={"action": "START"}, headers=tech_headers)
    client.post(f"/api/technicians/jobs/{booking_id}/action", data={"action": "COMPLETE"}, headers=tech_headers)

    # Now post review -> 201 Created
    review_res = client.post("/api/reviews", json={
        "booking_id": booking_id,
        "rating": 5,
        "comment": "Excellent service! Very prompt and professional."
    }, headers=cust_headers)
    assert review_res.status_code == status.HTTP_201_CREATED
    assert review_res.json()["rating"] == 5

    # Duplicate review attempt -> 400 Bad Request
    dup_review = client.post("/api/reviews", json={
        "booking_id": booking_id,
        "rating": 4,
        "comment": "Second review"
    }, headers=cust_headers)
    assert dup_review.status_code == status.HTTP_400_BAD_REQUEST
    assert "already submitted a review" in dup_review.json()["detail"]


def test_complaint_ticketing_and_admin_resolution(client, test_customer_token, test_admin_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    service_id = client.get("/api/services").json()[0]["id"]

    # 1. Customer creates booking and complaint
    booking_res = client.post("/api/bookings", json={
        "service_id": service_id,
        "problem_description": "Complaint test booking",
        "scheduled_date": str(date.today() + timedelta(days=1)),
        "scheduled_time": "10:00 AM",
        "new_address": {"street_address": "333 Issue Rd", "city": "City", "zip_code": "10001"}
    }, headers=cust_headers)
    booking_id = booking_res.json()["id"]

    complaint_res = client.post("/api/complaints", json={
        "booking_id": booking_id,
        "subject": "Technician arrived 30 minutes late",
        "description": "The service was fine, but time window was missed."
    }, headers=cust_headers)
    assert complaint_res.status_code == status.HTTP_201_CREATED
    complaint_id = complaint_res.json()["id"]
    assert complaint_res.json()["status"] == "OPEN"

    # 2. Admin resolves complaint
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    resolve_res = client.patch(f"/api/complaints/{complaint_id}", json={
        "status": "RESOLVED",
        "resolution_notes": "Issued $10 goodwill credit voucher."
    }, headers=admin_headers)
    assert resolve_res.status_code == status.HTTP_200_OK
    assert resolve_res.json()["status"] == "RESOLVED"
    assert resolve_res.json()["resolution_notes"] == "Issued $10 goodwill credit voucher."
