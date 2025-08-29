import pytest
from pydantic import ValidationError
from src.api.models.user import User
from src.api.models.place import Place
from src.api.models.itinerary import Itinerary
from uuid import uuid4
from datetime import datetime

# User model validator tests
def test_user_email_validator():
    with pytest.raises(ValidationError):
        User(id=uuid4(), name="Test", email="not-an-email")
    user = User(id=uuid4(), name="Test", email="test@example.com")
    assert user.email == "test@example.com"

import factory

class PlaceFactory(factory.Factory):
    class Meta:
        model = Place
    id = factory.LazyFunction(uuid4)
    name = "Test Place"
    country_code = "US"
    lat = 0.0
    lon = 0.0

class ItineraryFactory(factory.Factory):
    class Meta:
        model = Itinerary
    id = factory.LazyFunction(uuid4)
    title = "Trip"
    traveler_type = "solo"
    days = 5
    places = []
    created_at = factory.LazyFunction(datetime.utcnow)
    updated_at = factory.LazyFunction(datetime.utcnow)

@pytest.mark.parametrize("country_code,valid", [
    ("US", True),
    ("SG", True),
    ("XX", True),
    ("A1", False),
    ("USA", False),
    ("us", False),
])
def test_place_country_code_validation(country_code, valid):
    if valid:
        place = PlaceFactory(country_code=country_code)
        assert place.country_code == country_code
    else:
        with pytest.raises(ValidationError):
            PlaceFactory(country_code=country_code)

@pytest.mark.parametrize("days,valid", [
    (1, True),
    (60, True),
    (0, False),
    (-1, False),
    (61, False),
])
def test_itinerary_days_validation(days, valid):
    if valid:
        itinerary = ItineraryFactory(days=days)
        assert itinerary.days == days
    else:
        with pytest.raises(ValidationError):
            ItineraryFactory(days=days)
