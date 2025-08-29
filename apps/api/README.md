# TravelG3n API

A FastAPI backend for TravelG3n.

## Development

```bash
# Install dependencies
poetry install

# Run development server
poetry run uvicorn src.api.main:app --reload

# Run tests
poetry run pytest

# Lint (optional)
poetry run ruff src/api
```

## Endpoints
- `/health`: Health check
- `/itineraries/`: List itineraries

## Settings
- See `src/api/config.py` for environment variables and settings.
