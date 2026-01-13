"""Test server API."""

from __future__ import annotations

from fastapi.testclient import TestClient

from radiant_server.api.main import app

client = TestClient(app)


def test_root() -> None:
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Radiant API"


def test_health() -> None:
    """Test health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
