import httpx
import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/v1/health/live")
    assert response.status_code == 200
    assert response.json()["status"] == "live"
