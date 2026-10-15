from fastapi.testclient import TestClient
from paladgpt.main import app

client = TestClient(app)


def test_helth_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
