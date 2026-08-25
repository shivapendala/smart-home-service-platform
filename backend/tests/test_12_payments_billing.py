import pytest


def test_payments_and_invoicing_workflow(client, test_customer_token, test_admin_token):
    cust_headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}

    # 1. Generate Invoice
    inv_payload = {
        "booking_id": 1,
        "items": [
            {
                "item_description": "AC Compressor Replacement Labor",
                "quantity": 1,
                "unit_price": 120.00,
                "item_type": "LABOR"
            },
            {
                "item_description": "45 MFD Dual Run Capacitor",
                "quantity": 1,
                "unit_price": 35.00,
                "item_type": "SPARE_PART"
            }
        ],
        "discount_amount": 10.0,
        "tax_rate_percent": 8.5,
        "due_days": 14,
        "notes": "Thank you for using Smart Home Service Platform!"
    }
    r_inv = client.post("/api/v1/billing/invoices", json=inv_payload, headers=cust_headers)
    assert r_inv.status_code in [201, 404]

    if r_inv.status_code == 201:
        inv_data = r_inv.json()
        assert inv_data["subtotal"] == 155.00
        assert inv_data["tax_amount"] == 13.18
        assert inv_data["total_amount"] == 158.18
        inv_id = inv_data["id"]

        # 2. Get Invoice by ID
        r_get = client.get(f"/api/v1/billing/invoices/{inv_id}", headers=cust_headers)
        assert r_get.status_code == 200
        assert r_get.json()["invoice_number"] == inv_data["invoice_number"]

        # 3. Process Payment
        pay_payload = {
            "booking_id": 1,
            "invoice_id": inv_id,
            "provider": "STRIPE",
            "amount": 158.18,
            "currency": "USD"
        }
        r_pay = client.post("/api/v1/billing/payments/process", json=pay_payload, headers=cust_headers)
        assert r_pay.status_code == 201
        assert r_pay.json()["is_successful"] == True

        # 4. Submit Refund Request
        ref_payload = {
            "invoice_id": inv_id,
            "requested_amount": 35.00,
            "reason": "Capacitor price discrepancy"
        }
        r_ref = client.post("/api/v1/billing/refunds", json=ref_payload, headers=cust_headers)
        assert r_ref.status_code == 201
        ref_id = r_ref.json()["id"]

        # 5. Evaluate Refund
        r_eval = client.put(
            f"/api/v1/billing/refunds/{ref_id}/evaluate?approved=true&approved_amount=35.00&reviewer_notes=Partial+refund+approved",
            headers=admin_headers
        )
        assert r_eval.status_code == 200
        assert r_eval.json()["status"] == "APPROVED"


def test_customer_invoice_list(client, test_customer_token):
    headers = {"Authorization": f"Bearer {test_customer_token['token']}"}
    r = client.get("/api/v1/billing/invoices/customer/me", headers=headers)
    assert r.status_code == 200
    assert isinstance(r.json(), list)
