import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_create_itinerary_missing_title():
    payload = {
        "traveler_type": "solo",
        "days": 5,
        "places": []
    }
    response = client.post("/itineraries/", json=payload)
    assert response.status_code == 422
    assert any(
        err["loc"] == ["body", "title"] and err["msg"] == "Field required"
        for err in response.json()["detail"]
    )
