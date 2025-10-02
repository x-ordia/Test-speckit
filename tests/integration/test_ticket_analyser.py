import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ticket_analyser_integration():
    response = client.post("/orchestrate", json={"prompt": "My computer is not turning on"})
    assert response.status_code == 200
    assert "resolution" in response.json().get("result", "")
