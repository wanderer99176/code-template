from fastapi.testclient import TestClient


def test_health_check(client: TestClient):
    """测试健康检查端点。"""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root_endpoint(client: TestClient):
    """测试根端点。"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
