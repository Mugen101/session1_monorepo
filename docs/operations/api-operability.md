# API Operability

## CORS
- Only allows requests from http://localhost:3000

## Rate Limiting
- POST, PATCH, DELETE: 30 requests/minute per IP (slowapi)

## Logging
- Structured JSON logging (loguru)
- Each request logs: request_id, path, method, status, latency
- OpenTelemetry fields: service.name, trace_id

## Middleware
- request_id generated per request

## Future
- OpenTelemetry integration planned

---

See main.py for implementation details.