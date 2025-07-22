def test_create_producer(client, auth_headers):
    response = client.post(
        "/producers/",
        json={"name": "João", "cpf_cnpj": "064.263.560-93"},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["name"] == "João"


def test_get_all_producers(client, auth_headers):
    response = client.get("/producers/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)


def test_update_producer(client, auth_headers):
    # Cria produtor
    response = client.post(
        "/producers/",
        json={"name": "Carlos", "cpf_cnpj": "942.945.380-74"},
        headers=auth_headers,
    )
    assert response.status_code == 200
    producer_id = response.json()["id"]

    # Atualiza
    response = client.put(
        f"/producers/{producer_id}",
        json={"name": "Carlos Silva", "cpf_cnpj": "081.061.110-40"},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Carlos Silva"


def test_delete_producer(client, auth_headers):
    # Cria produtor
    response = client.post(
        "/producers/",
        json={"name": "Delete Me", "cpf_cnpj": "843.606.070-91"},
        headers=auth_headers,
    )
    assert response.status_code == 200
    producer_id = response.json()["id"]

    # Deleta
    response = client.delete(
        f"/producers/{producer_id}",
        headers=auth_headers,
    )
    assert response.status_code == 204

    # Verifica remoção
    response = client.get("/producers/", headers=auth_headers)
    data = response.json()
    assert all(p["id"] != producer_id for p in data["data"])
