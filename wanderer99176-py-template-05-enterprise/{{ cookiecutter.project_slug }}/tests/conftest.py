import pytest
from fastapi.testclient import TestClient
from {{ cookiecutter.package_name }}.__main__ import app


@pytest.fixture(scope="module")
def client():
    """Yield a TestClient for the FastAPI app."""
    with TestClient(app) as c:
        yield c
