import httpx
import pytest
from fastapi import status
from src.api.main import app

@pytest.mark.asyncio
async def test_itineraries_contract():
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/itineraries/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []
