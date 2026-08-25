import pytest
from fastapi import status


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["status"] == "healthy"
    assert "app_name" in data


def test_user_registration_customer(client):
    payload = {
        "email": "john@example.com",
        "password": "SecurePassword123!",
        "full_name": "John Doe",
        "phone": "+1234567890",
        "role": "CUSTOMER"
    }
    response = client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["email"] == "john@example.com"
    assert data["full_name"] == "John Doe"
    assert data["role"] == "CUSTOMER"
    assert "id" in data


def test_user_registration_technician(client):
    payload = {
        "email": "tech_dave@example.com",
        "password": "TechPassword123!",
        "full_name": "Dave Tech",
        "phone": "+9876543210",
        "role": "TECHNICIAN",
        "specialization": "Refrigerator Repair",
        "experience_years": 4,
        "bio": "Expert in home refrigeration systems."
    }
    response = client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["email"] == "tech_dave@example.com"
    assert data["role"] == "TECHNICIAN"
    assert data["specialization"] == "Refrigerator Repair"


def test_user_registration_duplicate_email(client):
    payload = {
        "email": "dup@example.com",
        "password": "Password123!",
        "full_name": "Duplicate User",
        "role": "CUSTOMER"
    }
    res1 = client.post("/api/v1/auth/register", json=payload)
    assert res1.status_code == status.HTTP_201_CREATED

    res2 = client.post("/api/v1/auth/register", json=payload)
    assert res2.status_code == status.HTTP_400_BAD_REQUEST
    assert "already exists" in res2.json()["detail"]


def test_user_login(client):
    # Register first
    reg_payload = {
        "email": "login_user@example.com",
        "password": "MySecretPassword123!",
        "full_name": "Login Tester",
        "role": "CUSTOMER"
    }
    client.post("/api/v1/auth/register", json=reg_payload)

    # Login with JSON
    login_payload = {
        "email": "login_user@example.com",
        "password": "MySecretPassword123!"
    }
    response = client.post("/api/v1/auth/login", json=login_payload)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert data["email"] == "login_user@example.com"


def test_user_login_invalid_password(client):
    reg_payload = {
        "email": "wrong_pass@example.com",
        "password": "CorrectPassword123!",
        "full_name": "Wrong Pass",
        "role": "CUSTOMER"
    }
    client.post("/api/v1/auth/register", json=reg_payload)

    login_payload = {
        "email": "wrong_pass@example.com",
        "password": "WrongPassword123!"
    }
    response = client.post("/api/v1/auth/login", json=login_payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_get_current_user_profile(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    response = client.get("/api/v1/auth/me", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["email"] == "customer@example.com"
    assert data["full_name"] == "Alice Customer"


def test_unauthorized_profile_access(client):
    response = client.get("/api/v1/auth/me")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
