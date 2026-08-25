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
    reg_payload = {
        "email": "login_user@example.com",
        "password": "MySecretPassword123!",
        "full_name": "Login Tester",
        "role": "CUSTOMER"
    }
    client.post("/api/v1/auth/register", json=reg_payload)

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


def test_invalid_token(client):
    headers = {"Authorization": "Bearer invalid.token.value"}
    response = client.get("/api/v1/auth/me", headers=headers)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert "Could not validate credentials" in response.json()["detail"]


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


def test_role_authorization_admin_only(client, test_customer_token, test_admin_token):
    # Customer attempt on Admin endpoint should be 403 Forbidden
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    create_payload = {
        "category_id": 1,
        "name": "Admin Only Service",
        "description": "Requires admin role.",
        "base_price": 99.00
    }
    res1 = client.post("/api/v1/services/items", json=create_payload, headers=cust_headers)
    assert res1.status_code == status.HTTP_403_FORBIDDEN

    # Admin attempt on Admin endpoint should succeed 201 Created
    cat_res = client.get("/api/v1/services/categories")
    cat_id = cat_res.json()[0]["id"]
    create_payload["category_id"] = cat_id

    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    res2 = client.post("/api/v1/services/items", json=create_payload, headers=admin_headers)
    assert res2.status_code == status.HTTP_201_CREATED


def test_direct_api_auth_routes(client):
    # Test POST /api/auth/register
    reg_payload = {
        "email": "direct_api@example.com",
        "password": "DirectPassword123!",
        "full_name": "Direct Api User",
        "role": "CUSTOMER"
    }
    res1 = client.post("/api/auth/register", json=reg_payload)
    assert res1.status_code == status.HTTP_201_CREATED

    # Test POST /api/auth/login
    login_payload = {
        "email": "direct_api@example.com",
        "password": "DirectPassword123!"
    }
    res2 = client.post("/api/auth/login", json=login_payload)
    assert res2.status_code == status.HTTP_200_OK
    token = res2.json()["access_token"]

    # Test GET /api/auth/me
    headers = {"Authorization": f"Bearer {token}"}
    res3 = client.get("/api/auth/me", headers=headers)
    assert res3.status_code == status.HTTP_200_OK
    assert res3.json()["email"] == "direct_api@example.com"
