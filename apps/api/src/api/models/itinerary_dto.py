from pydantic import BaseModel, Field
from typing import Annotated, Literal
from .place import Place


class ItineraryCreateDTO(BaseModel):
    title: Annotated[str, Field(min_length=3, max_length=80)]
    traveler_type: Literal["solo", "couple", "family", "business"]
    days: Annotated[int, Field(ge=1, le=60)]
    places: list[Place]
    model_config = {"extra": "forbid"}

    def to_entity(self):
        from .itinerary import Itinerary
        return Itinerary(
            title=self.title,
            traveler_type=self.traveler_type,
            days=self.days,
            # Add mapping for places if needed
        )


class ItineraryUpdateDTO(BaseModel):
    title: Annotated[str, Field(min_length=3, max_length=80)] | None = None
    traveler_type: Literal["solo", "couple", "family", "business"] | None = None
    days: Annotated[int, Field(ge=1, le=60)] | None = None
    places: list[Place] | None = None
    model_config = {"extra": "forbid"}

    def apply_to_entity(self, entity):
        if self.title is not None:
            entity.title = self.title
        if self.traveler_type is not None:
            entity.traveler_type = self.traveler_type
        if self.days is not None:
            entity.days = self.days
        # Add mapping for places if needed
        return entity
