def test_dashboard(client, auth_headers):
    response = client.get("/dashboard/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert "total_farms" in data
    assert "by_crop" in data
