
from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from uuid import UUID, uuid4
from sqlalchemy import select, update as sql_update, delete as sql_delete
from ..models.itinerary import Itinerary
from ..models.itinerary_dto import ItineraryCreateDTO, ItineraryUpdateDTO
from ..db import get_session


from fastapi import APIRouter
from ..seed import seed

router = APIRouter(prefix="/v1/itineraries", tags=["itineraries"])

@router.post("/v1/seed", tags=["itineraries"])
async def trigger_seed():
    await seed()
    return {"status": "seeded"}

@router.post("/", response_model=Itinerary, status_code=status.HTTP_201_CREATED)
async def create_itinerary(dto: ItineraryCreateDTO, response: Response, session=Depends(get_session)):
    entity = dto.to_entity()
    session.add(entity)
    await session.commit()
    await session.refresh(entity)
    response.headers["Location"] = f"/v1/itineraries/{entity.id}"
    return entity

@router.get("/", response_model=list[Itinerary])
async def list_itineraries(request: Request, limit: int = 10, offset: int = 0, session=Depends(get_session)):
    result = await session.exec(select(Itinerary).offset(offset).limit(limit))
    items = result.all()
    total = await session.exec(select(Itinerary))
    count = len(total.all())
    request.scope["headers"].append((b"x-total-count", str(count).encode()))
    return items

@router.get("/{id}", response_model=Itinerary)
async def get_itinerary(id: UUID, session=Depends(get_session)):
    result = await session.exec(select(Itinerary).where(Itinerary.id == id))
    entity = result.first()
    if not entity:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return entity

@router.patch("/{id}", response_model=Itinerary)
async def update_itinerary(id: UUID, dto: ItineraryUpdateDTO, session=Depends(get_session)):
    result = await session.exec(select(Itinerary).where(Itinerary.id == id))
    entity = result.first()
    if not entity:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    dto.apply_to_entity(entity)
    await session.commit()
    await session.refresh(entity)
    return entity

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_itinerary(id: UUID, session=Depends(get_session)):
    result = await session.exec(select(Itinerary).where(Itinerary.id == id))
    entity = result.first()
    if not entity:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    await session.delete(entity)
    await session.commit()

router = APIRouter(prefix="/v1/itineraries", tags=["itineraries"])

@router.post("/", response_model=Itinerary, status_code=status.HTTP_201_CREATED)
@router.get("/", response_model=list[Itinerary])
@router.get("/{id}", response_model=Itinerary)
@router.patch("/{id}", response_model=Itinerary)
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
