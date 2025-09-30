"""核心应用程序逻辑测试。"""

import pytest
from fastapi.testclient import TestClient

from {{ cookiecutter.package_name }}.core import get_app


@pytest.fixture
def client():
    """创建测试客户端。"""
    app = get_app()
    return TestClient(app)


def test_root_endpoint(client):
    """测试根端点。"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "{{ cookiecutter.project_name }}" in data["message"]


def test_health_endpoint(client):
    """测试健康检查端点。"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "OK"
