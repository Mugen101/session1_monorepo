import pytest
from src.api.models.itinerary import Itinerary

@pytest.mark.asyncio
async def test_create_itinerary(db_session):
    itinerary = Itinerary(title="Test Trip", traveler_type="solo", days=2)
    db_session.add(itinerary)
    await db_session.commit()
    await db_session.refresh(itinerary)
    assert itinerary.id is not None
    assert itinerary.title == "Test Trip"

@pytest.mark.asyncio
async def test_query_itinerary(db_session):
    itinerary = Itinerary(title="Query Trip", traveler_type="family", days=4)
    db_session.add(itinerary)
    await db_session.commit()
    await db_session.refresh(itinerary)
    result = await db_session.exec(Itinerary.select().where(Itinerary.title == "Query Trip"))
    found = result.first()
    assert found is not None
    assert found.title == "Query Trip"
