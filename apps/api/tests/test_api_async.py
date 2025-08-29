import pytest
from httpx import AsyncClient
from src.api.main import app
from uuid import uuid4

@pytest.mark.asyncio
async def test_create_and_get_itinerary():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
            "title": "Trip",
            "traveler_type": "solo",
            "days": 5,
            "places": []
        }
        resp = await ac.post("/v1/itineraries/", json=payload)
        assert resp.status_code == 201
        location = resp.headers["location"]
        get_resp = await ac.get(location)
        assert get_resp.status_code == 200
        data = get_resp.json()
        assert data["title"] == "Trip"

@pytest.mark.asyncio
async def test_create_itinerary_missing_title():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
            "traveler_type": "solo",
            "days": 5,
            "places": []
        }
        resp = await ac.post("/v1/itineraries/", json=payload)
        assert resp.status_code == 422
