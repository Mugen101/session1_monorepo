import json
import pytest
from pathlib import Path
from src.api.models.itinerary import Itinerary
from src.api.models.place import Place
from src.api.models.user import User

def test_openapi_paths_and_operations():
    openapi = json.loads(Path("openapi.json").read_text())
    paths = openapi["paths"]
    # Check all expected paths
    for path in ["/v1/itineraries/", "/v1/itineraries/{id}"]:
        assert path in paths
    # Check operations
    assert "post" in paths["/v1/itineraries/"]
    assert "get" in paths["/v1/itineraries/"]
    assert "get" in paths["/v1/itineraries/{id}"]
    assert "patch" in paths["/v1/itineraries/{id}"]
    assert "delete" in paths["/v1/itineraries/{id}"]

def test_openapi_schemas_required_properties():
    openapi = json.loads(Path("openapi.json").read_text())
    schemas = openapi["components"]["schemas"]
    for model, required in {
        "Itinerary": ["id", "title", "traveler_type", "days", "places", "created_at", "updated_at"],
        "Place": ["id", "name", "country_code", "lat", "lon"],
        "User": ["id", "name", "email"],
    }.items():
        assert model in schemas
        for prop in required:
            assert prop in schemas[model]["properties"]
            assert prop in schemas[model]["required"]
