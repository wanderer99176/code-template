import pytest
from fastapi.testclient import TestClient
from {{ cookiecutter.package_name }}.__main__ import app


@pytest.fixture(scope="module")
def client():
    """为 FastAPI 应用生成测试客户端。"""
    with TestClient(app) as c:
        yield c
