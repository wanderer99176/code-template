"""Tests for core application logic."""

import pytest
from fastapi.testclient import TestClient

from {{ cookiecutter.package_name }}.core import get_app


@pytest.fixture
def client():
    """Create a test client."""
    app = get_app()
    return TestClient(app)


def test_root_endpoint(client):
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "{{ cookiecutter.project_name }}" in data["message"]


def test_health_endpoint(client):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "OK"
