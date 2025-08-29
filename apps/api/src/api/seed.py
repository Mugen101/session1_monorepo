from sqlmodel import select
from .db import get_session
from .models.itinerary import Itinerary


async def seed():
    async with get_session() as s:
        # idempotent seed
        result = await s.exec(select(Itinerary))
        count = len(result.all())
        if count == 0:
            s.add_all([
                Itinerary(title="SG Weekend", traveler_type="couple", days=3),
                Itinerary(title="Bali Family", traveler_type="family", days=5)
            ])
            await s.commit()

if __name__ == "__main__":
    import asyncio
    asyncio.run(seed())
