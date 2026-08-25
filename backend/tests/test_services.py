import pytest
from fastapi import status


def test_list_categories_auto_seeds(client):
    response = client.get("/api/v1/services/categories")
    assert response.status_code == status.HTTP_200_OK
    categories = response.json()
    assert len(categories) >= 5
    category_names = [c["name"] for c in categories]
    assert "AC Repair & Maintenance" in category_names
    assert "Plumbing Services" in category_names


def test_list_services(client):
    response = client.get("/api/v1/services/items")
    assert response.status_code == status.HTTP_200_OK
    services = response.json()
    assert len(services) > 0
    first_service = services[0]
    assert "base_price" in first_service
    assert "duration_minutes" in first_service


def test_search_services(client):
    response = client.get("/api/v1/services/items?search=Leak")
    assert response.status_code == status.HTTP_200_OK
    results = response.json()
    assert any("Leak" in s["name"] or "leak" in s["description"] for s in results)


def test_admin_create_and_update_service(client, test_admin_token):
    headers = {"Authorization": f"Bearer {test_admin_token['token']}"}

    # 1. Get categories
    cat_res = client.get("/api/v1/services/categories")
    category_id = cat_res.json()[0]["id"]

    # 2. Create new service item
    create_payload = {
        "category_id": category_id,
        "name": "Emergency Drain Flushing",
        "description": "High pressure water jetting for clogged main lines.",
        "base_price": 150.00,
        "duration_minutes": 90
    }
    create_res = client.post("/api/v1/services/items", json=create_payload, headers=headers)
    assert create_res.status_code == status.HTTP_201_CREATED
    service_data = create_res.json()
    assert service_data["name"] == "Emergency Drain Flushing"
    assert service_data["base_price"] == 150.00

    service_id = service_data["id"]

    # 3. Update service item price
    update_payload = {"base_price": 165.00}
    update_res = client.put(f"/api/v1/services/items/{service_id}", json=update_payload, headers=headers)
    assert update_res.status_code == status.HTTP_200_OK
    assert update_res.json()["base_price"] == 165.00


def test_customer_cannot_create_service(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    create_payload = {
        "category_id": 1,
        "name": "Unauthorized Service",
        "description": "Hack attempt.",
        "base_price": 10.00,
        "duration_minutes": 30
    }
    response = client.post("/api/v1/services/items", json=create_payload, headers=headers)
    assert response.status_code == status.HTTP_403_FORBIDDEN
