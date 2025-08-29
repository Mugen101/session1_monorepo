
from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4

class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True, min_length=1, max_length=80)
    email: str = Field(index=True)
