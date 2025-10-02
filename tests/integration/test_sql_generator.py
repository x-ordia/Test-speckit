import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sql_generator_integration():
    response = client.post("/orchestrate", json={"prompt": "Give me all the users in the database"})
    assert response.status_code == 200
    assert "SELECT" in response.json().get("result", "")
    assert "FROM users" in response.json().get("result", "")
