from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_create_veiculo():
    response = client.post("/veiculos", json={"nome": "Carro"})
    assert response.status_code == 200
    assert response.json()["nome"] == "Carro"

def test_get_veiculos():
    response = client.get("/veiculos")
    assert response.status_code == 200

def test_update_status():
    response = client.put("/veiculos/1", json={"status": "CONNECTADO"})
    assert response.status_code == 200
    assert response.json()["status"] == "CONNECTADO"

def test_delete_veiculo():
    response = client.delete("/veiculos/1")
    assert response.status_code == 200
