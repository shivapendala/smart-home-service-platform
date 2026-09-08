import pytest
from fastapi import status


def test_list_categories_auto_seeds(client):
    response = client.get("/api/services/categories")
    assert response.status_code == status.HTTP_200_OK
    categories = response.json()
    assert len(categories) >= 5
    category_names = [c["name"] for c in categories]
    assert "AC Repair & Installation" in category_names
    assert "Plumbing" in category_names
    assert "TV Repair" in category_names


def test_customer_browsing_and_retrieval(client):
    # List services
    response = client.get("/api/services")
    assert response.status_code == status.HTTP_200_OK
    services = response.json()
    assert len(services) > 0
    
    first_service_id = services[0]["id"]
    
    # Retrieve single service details
    detail_res = client.get(f"/api/services/{first_service_id}")
    assert detail_res.status_code == status.HTTP_200_OK
    detail = detail_res.json()
    assert detail["id"] == first_service_id
    assert "name" in detail
    assert "base_price" in detail


def test_search_and_category_filter(client):
    # Category filter
    cat_res = client.get("/api/services/categories")
    category_id = cat_res.json()[0]["id"]
    
    cat_services_res = client.get(f"/api/services?category_id={category_id}")
    assert cat_services_res.status_code == status.HTTP_200_OK
    assert isinstance(cat_services_res.json(), list)

    # Keyword search
    search_res = client.get("/api/services?search=Installation")
    assert search_res.status_code == status.HTTP_200_OK
    results = search_res.json()
    assert len(results) > 0
    assert any("Installation" in s["name"] for s in results)


def test_admin_create_update_and_deactivate_service(client, test_admin_token):
    headers = {"Authorization": f"Bearer {test_admin_token['token']}"}

    # 1. Get categories
    cat_res = client.get("/api/services/categories")
    category_id = cat_res.json()[0]["id"]

    # 2. Create new service item (POST /api/services)
    create_payload = {
        "category_id": category_id,
        "name": "TV Wall Mounting & Cable Hiding",
        "description": "Professional TV bracket wall mounting up to 75 inch.",
        "base_price": 75.00,
        "duration_minutes": 60
    }
    create_res = client.post("/api/services", json=create_payload, headers=headers)
    assert create_res.status_code == status.HTTP_201_CREATED
    service_data = create_res.json()
    assert service_data["name"] == "TV Wall Mounting & Cable Hiding"
    assert service_data["base_price"] == 75.00

    service_id = service_data["id"]

    # 3. Update service item (PUT /api/services/{id})
    update_payload = {"base_price": 85.00, "duration_minutes": 75}
    update_res = client.put(f"/api/services/{service_id}", json=update_payload, headers=headers)
    assert update_res.status_code == status.HTTP_200_OK
    assert update_res.json()["base_price"] == 85.00

    # 4. Deactivate/delete service item (DELETE /api/services/{id})
    delete_res = client.delete(f"/api/services/{service_id}", headers=headers)
    assert delete_res.status_code == status.HTTP_204_NO_CONTENT


def test_unauthorized_modification_attempts(client, test_customer_token):
    # Customer trying to create service -> 403 Forbidden
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    create_payload = {
        "category_id": 1,
        "name": "Unauthorized Service",
        "description": "Hack attempt.",
        "base_price": 10.00,
        "duration_minutes": 30
    }
    res1 = client.post("/api/services", json=create_payload, headers=cust_headers)
    assert res1.status_code == status.HTTP_403_FORBIDDEN

    # Customer trying to update service -> 403 Forbidden
    res2 = client.put("/api/services/1", json={"base_price": 1.00}, headers=cust_headers)
    assert res2.status_code == status.HTTP_403_FORBIDDEN

    # Customer trying to delete service -> 403 Forbidden
    res3 = client.delete("/api/services/1", headers=cust_headers)
    assert res3.status_code == status.HTTP_403_FORBIDDEN
