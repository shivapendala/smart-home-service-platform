import pytest


def test_ai_diagnostics_and_pricing_estimator(client):
    # 1. Run diagnostic wizard
    diag_payload = {
        "appliance_type": "AC",
        "symptoms": ["No Cooling", "Water Leakage"],
        "appliance_age_years": 4
    }
    r_diag = client.post("/api/v1/ai/diagnose", json=diag_payload)
    assert r_diag.status_code == 200
    diag_data = r_diag.json()
    assert "Refrigerant" in diag_data["diagnosed_root_cause"] or "Drain" in diag_data["diagnosed_root_cause"]

    # 2. NLP Pricing Estimator
    price_payload = {
        "problem_description": "My split AC is leaking water and not cooling properly"
    }
    r_price = client.post("/api/v1/ai/estimate-pricing", json=price_payload)
    assert r_price.status_code == 200
    p_data = r_price.json()
    assert p_data["total_estimated_price"] > 0
    assert len(p_data["detected_keywords"]) >= 1

    # 3. Health risk score
    r_health = client.get("/api/v1/ai/health-risk?brand=Samsung&appliance_type=AC&age_years=6")
    assert r_health.status_code == 200
    h_data = r_health.json()
    assert h_data["failure_risk_percentage"] > 0
