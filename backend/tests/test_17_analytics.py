import pytest


def test_analytics_dashboard_and_export(client, test_admin_token):
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}

    # 1. Fetch executive dashboard
    r_dash = client.get("/api/v1/analytics/dashboard", headers=admin_headers)
    assert r_dash.status_code == 200
    data = r_dash.json()
    assert "revenue_summary" in data
    assert "top_technicians" in data
    assert "category_breakdown" in data

    # 2. Export CSV
    export_payload = {
        "report_type": "REVENUE_MARGIN",
        "start_date": "2026-08-01",
        "end_date": "2026-08-25"
    }
    r_csv = client.post("/api/v1/analytics/export-csv", json=export_payload, headers=admin_headers)
    assert r_csv.status_code == 200
    assert "text/csv" in r_csv.headers["content-type"]
    assert "Gross Revenue" in r_csv.text
