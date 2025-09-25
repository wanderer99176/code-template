"""Pydantic models for {{ cookiecutter.project_name }}."""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health check response model."""
    
    message: str
