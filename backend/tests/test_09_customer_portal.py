import pytest
from datetime import date


def test_customer_appliance_workflow(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}

    # 1. Register new appliance
    appliance_payload = {
        "brand": "Samsung",
        "model_number": "RT28T3722S8",
        "serial_number": "SN-9876543210",
        "appliance_type": "Double Door Refrigerator",
        "installation_year": 2022,
        "condition": "EXCELLENT",
        "notes": "Purchased in 2022, primary kitchen fridge.",
        "room_location": "Kitchen"
    }

    r_create = client.post("/api/v1/customer-portal/appliances", json=appliance_payload, headers=headers)
    assert r_create.status_code == 201
    data = r_create.json()
    assert data["brand"] == "Samsung"
    assert data["appliance_type"] == "Double Door Refrigerator"
    appliance_id = data["id"]

    # 2. List appliances
    r_list = client.get("/api/v1/customer-portal/appliances", headers=headers)
    assert r_list.status_code == 200
    assert len(r_list.json()) == 1

    # 3. Update appliance condition
    r_update = client.put(
        f"/api/v1/customer-portal/appliances/{appliance_id}",
        json={"condition": "FAIR", "notes": "Needs coil cleaning"},
        headers=headers
    )
    assert r_update.status_code == 200
    assert r_update.json()["condition"] == "FAIR"

    # 4. Delete appliance
    r_del = client.delete(f"/api/v1/customer-portal/appliances/{appliance_id}", headers=headers)
    assert r_del.status_code == 204


def test_loyalty_rewards_workflow(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}

    # 1. Fetch loyalty account (creates welcome bonus of 100 points)
    r_acc = client.get("/api/v1/customer-portal/loyalty", headers=headers)
    assert r_acc.status_code == 200
    acc_data = r_acc.json()
    assert acc_data["points_balance"] == 100
    assert acc_data["tier"] == "BRONZE"

    # 2. Redeem points (100 points)
    r_redeem = client.post("/api/v1/customer-portal/loyalty/redeem", json={"points_to_redeem": 100}, headers=headers)
    assert r_redeem.status_code == 200
    assert r_redeem.json()["points_balance"] == 0


def test_custom_quote_workflow(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}

    # Submit custom quote
    quote_payload = {
        "title": "Whole House Electrical Rewiring",
        "description": "3-bedroom apartment full rewiring and new distribution board installation."
    }
    r_quote = client.post("/api/v1/customer-portal/quotes", json=quote_payload, headers=headers)
    assert r_quote.status_code == 201
    assert r_quote.json()["status"] == "PENDING"

    # List quotes
    r_list = client.get("/api/v1/customer-portal/quotes", headers=headers)
    assert r_list.status_code == 200
    assert len(r_list.json()) == 1


def test_saved_payment_methods_workflow(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}

    card_payload = {
        "card_brand": "Visa",
        "last_four_digits": "4242",
        "expiration_month": 12,
        "expiration_year": 2028,
        "cardholder_name": "Alice Customer",
        "is_default": True
    }
    r_card = client.post("/api/v1/customer-portal/payment-methods", json=card_payload, headers=headers)
    assert r_card.status_code == 201
    assert r_card.json()["last_four_digits"] == "4242"

    r_list = client.get("/api/v1/customer-portal/payment-methods", headers=headers)
    assert r_list.status_code == 200
    assert len(r_list.json()) == 1
