import pytest


def test_inventory_and_van_transfer(client, test_admin_token, test_technician_token):
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}
    tech_headers = {"Authorization": f"Bearer {test_technician_token['token']}"}
    tech_id = test_technician_token["user"].id

    # 1. Create spare part
    part_payload = {
        "sku": "AC-CAP-45MFD",
        "part_name": "45 MFD Dual Run Capacitor",
        "category_name": "HVAC Spare Parts",
        "cost_price": 12.50,
        "selling_price": 35.00,
        "reorder_threshold": 5,
        "initial_warehouse_stock": 50
    }
    r_part = client.post("/api/v1/inventory/parts", json=part_payload, headers=admin_headers)
    assert r_part.status_code == 201
    part_id = r_part.json()["id"]

    # 2. List parts
    r_list = client.get("/api/v1/inventory/parts", headers=tech_headers)
    assert r_list.status_code == 200
    assert len(r_list.json()) >= 1

    # 3. Transfer to van
    trans_payload = {
        "technician_id": tech_id,
        "spare_part_id": part_id,
        "quantity": 5
    }
    r_trans = client.post("/api/v1/inventory/transfer-van", json=trans_payload, headers=admin_headers)
    assert r_trans.status_code == 200
    assert r_trans.json()["quantity_in_van"] == 5

    # 4. Check van inventory
    r_van = client.get("/api/v1/inventory/van/me", headers=tech_headers)
    assert r_van.status_code == 200
    assert len(r_van.json()) == 1

    # 5. Record usage
    usage_payload = {
        "booking_id": 1,
        "spare_part_id": part_id,
        "quantity_used": 1
    }
    r_use = client.post("/api/v1/inventory/use-part", json=usage_payload, headers=tech_headers)
    assert r_use.status_code == 201
    assert r_use.json()["quantity_used"] == 1
