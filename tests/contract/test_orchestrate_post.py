from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_orchestrate_post_contract():
    response = client.post("/orchestrate", json={"prompt": "test prompt"})
    assert response.status_code == 200
    assert "result" in response.json()
