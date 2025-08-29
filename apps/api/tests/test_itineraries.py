
import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_create_and_list_itineraries(db_session):
    # Create itinerary via API
    payload = {
        "title": "API Trip",
        "traveler_type": "solo",
        "days": 2,
        "places": []
    }
    response = client.post("/v1/itineraries/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "API Trip"

    # List itineraries via API
    response = client.get("/v1/itineraries/")
    assert response.status_code == 200
    items = response.json()
    assert any(i["title"] == "API Trip" for i in items)
