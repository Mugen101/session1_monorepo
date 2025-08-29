import json
import pytest
from httpx import AsyncClient
from src.api.main import app

@pytest.mark.asyncio
async def test_golden_create_itinerary():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
            "title": "Trip",
            "traveler_type": "solo",
            "days": 5,
            "places": []
        }
        resp = await ac.post("/v1/itineraries/", json=payload)
        assert resp.status_code == 201

@pytest.mark.asyncio
async def test_golden_create_itinerary_bad_payload():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
            "traveler_type": "solo",
            "days": 0,
            "places": []
        }
        resp = await ac.post("/v1/itineraries/", json=payload)
        assert resp.status_code == 422
