from __future__ import annotations

from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import AsyncIterator

from fastapi import FastAPI

from ai_platform_contracts import ResourceClass


VERSION = "0.1.0-dev"


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    app.state.started_at = datetime.now(timezone.utc)
    app.state.ready = True
    try:
        yield
    finally:
        app.state.ready = False


app = FastAPI(
    title="Lokale AI Control API",
    version=VERSION,
    lifespan=lifespan,
)


@app.get("/health/live")
def live() -> dict[str, str]:
    return {"status": "ok", "version": VERSION}


@app.get("/health/ready")
def ready() -> dict[str, object]:
    return {
        "status": "ready" if getattr(app.state, "ready", False) else "starting",
        "version": VERSION,
        "started_at": getattr(app.state, "started_at", None),
    }


@app.get("/v1/capabilities")
def capabilities() -> dict[str, object]:
    return {
        "team_os": True,
        "parallel_by_default": True,
        "single_runner_queue": True,
        "media_production": True,
        "resource_classes": [resource.value for resource in ResourceClass],
    }
