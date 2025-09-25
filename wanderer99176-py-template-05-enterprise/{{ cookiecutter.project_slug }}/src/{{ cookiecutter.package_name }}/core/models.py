"""Business entity models."""

from pydantic import BaseModel


class User(BaseModel):
    """User business model."""
    id: int
    name: str
    email: str


class Task(BaseModel):
    """Task business model."""
    id: int
    title: str
    description: str
    completed: bool = False
