from fastapi.testclient import TestClient

from app.main import app


def test_health_and_capabilities() -> None:
    with TestClient(app) as client:
        live = client.get("/health/live")
        ready = client.get("/health/ready")
        capabilities = client.get("/v1/capabilities")

    assert live.status_code == 200
    assert live.json()["status"] == "ok"
    assert ready.status_code == 200
    assert ready.json()["status"] == "ready"
    assert capabilities.status_code == 200
    body = capabilities.json()
    assert body["team_os"] is True
    assert body["single_runner_queue"] is True
    assert body["media_production"] is True
