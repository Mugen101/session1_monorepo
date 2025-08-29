
from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4

class Place(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True, min_length=1, max_length=80)
    country_code: str = Field(index=True, min_length=2, max_length=2)
    lat: float
    lon: float
