"""FastAPI main application."""

from __future__ import annotations

from fastapi import FastAPI

from radiant_server import __version__

app = FastAPI(
    title="Radiant API",
    description="Backend API for Radiant Meshtastic administration platform",
    version=__version__,
)


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Radiant API", "version": __version__}


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}
