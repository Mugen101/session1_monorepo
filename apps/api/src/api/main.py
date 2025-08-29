
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from loguru import logger
import time
import uuid
from .config import get_settings
from .routers import health, itineraries


def create_app():
    settings = get_settings()
    app = FastAPI(title=settings.app_name)
    app.include_router(health.router)
    app.include_router(itineraries.router)

    # Restrict CORS to localhost:3000
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Rate limiting: 30/min for POST/PATCH/DELETE per IP
    limiter = Limiter(key_func=get_remote_address)
    app.state.limiter = limiter
    app.add_exception_handler(429, _rate_limit_exceeded_handler)

    @app.middleware("http")
    async def add_request_id_and_logging(request: Request, call_next):
        request_id = str(uuid.uuid4())
        start_time = time.time()
        response = None
        try:
            response = await call_next(request)
        finally:
            process_time = time.time() - start_time
            log_data = {
                "request_id": request_id,
                "path": request.url.path,
                "method": request.method,
                "status": response.status_code if response else None,
                "latency": process_time,
                "service.name": "travelg3n-api",
                "trace_id": request.headers.get("x-trace-id", request_id),
            }
            logger.info(log_data)
            response.headers["X-Request-ID"] = request_id
        return response

    # Apply rate limit to POST/PATCH/DELETE
    from fastapi.routing import APIRoute
    for route in app.routes:
        if isinstance(route, APIRoute) and route.methods & {"POST", "PATCH", "DELETE"}:
            route.endpoint = limiter.limit("30/minute")(route.endpoint)
    return app

app = create_app()
