
from fastapi import APIRouter, Depends
from sqlalchemy import text
from src.api.db import get_session, engine
import subprocess
import time
from loguru import logger

router = APIRouter()

@router.get("/v1/health/live", tags=["health"])
def health_live():
    return {"status": "live"}

@router.get("/v1/health/ready", tags=["health"])
async def health_ready(session=Depends(get_session)):
    start = time.time()
    # DB connectivity
    try:
        result = await session.exec(text("SELECT 1"))
        db_ok = result.first() == 1
    except Exception as e:
        db_ok = False
    db_time = time.time() - start

    # Pool metrics
    pool = engine.sync_engine.pool
    pool_metrics = {
        "size": pool.size(),
        "checked_out": pool.checkedout(),
        "overflow": pool.overflow(),
        "timeout": pool._timeout
    }

    # Migration status
    try:
        heads = subprocess.check_output([
            "poetry", "run", "alembic", "heads"
        ], cwd="anchorRepo/apps/api", text=True)
        migration_status = heads.strip()
    except Exception as e:
        migration_status = str(e)

    # Log request_id, SQL timings
    request_id = None
    try:
        from fastapi import Request
        request = session._request if hasattr(session, "_request") else None
        if request:
            request_id = request.headers.get("X-Request-ID")
    except Exception:
        pass
    logger.info({
        "request_id": request_id,
        "db_time": db_time,
        "slow_query": db_time > 0.25
    })

    return {
        "db_ok": db_ok,
        "db_time": db_time,
        "pool": pool_metrics,
        "migration_status": migration_status
    }
