"""Core application logic for {{ cookiecutter.project_name }}."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from {{ cookiecutter.package_name }}.models import HealthResponse


def get_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="{{ cookiecutter.project_name }}",
        description="{{ cookiecutter.project_short_description }}",
        version="{{ cookiecutter.first_version }}",
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Add routes
    @app.get("/", response_model=HealthResponse)
    async def root():
        """Root endpoint."""
        return HealthResponse(message="Hello from {{ cookiecutter.project_name }}!")

    @app.get("/health", response_model=HealthResponse)
    async def health():
        """Health check endpoint."""
        return HealthResponse(message="OK")

    return app
