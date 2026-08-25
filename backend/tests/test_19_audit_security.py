import pytest


def test_audit_logs_and_security_ip_policies(client, test_admin_token):
    admin_headers = {"Authorization": f"Bearer {test_admin_token['token']}"}

    # 1. Fetch audit logs
    r_logs = client.get("/api/v1/security/logs", headers=admin_headers)
    assert r_logs.status_code == 200
    assert isinstance(r_logs.json(), list)

    # 2. Add IP policy
    ip_payload = {
        "ip_address_or_cidr": "192.168.1.100",
        "policy_type": "WHITELIST",
        "reason": "Office Admin Network"
    }
    r_pol = client.post("/api/v1/security/ip-policies", json=ip_payload, headers=admin_headers)
    assert r_pol.status_code == 201
    assert r_pol.json()["ip_address_or_cidr"] == "192.168.1.100"

    # 3. List IP policies
    r_list = client.get("/api/v1/security/ip-policies", headers=admin_headers)
    assert r_list.status_code == 200
    assert len(r_list.json()) >= 1
