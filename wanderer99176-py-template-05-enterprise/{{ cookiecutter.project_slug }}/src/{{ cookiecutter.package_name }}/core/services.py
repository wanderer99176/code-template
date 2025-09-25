"""Business process services."""

from typing import List
from {{ cookiecutter.package_name }}.core.models import User, Task


class UserService:
    """User business service."""
    
    def get_user(self, user_id: int) -> User:
        """Get user by ID."""
        # TODO: Implement actual business logic
        return User(id=user_id, name="John Doe", email="john@example.com")
    
    def get_users(self) -> List[User]:
        """Get all users."""
        # TODO: Implement actual business logic
        return [
            User(id=1, name="John Doe", email="john@example.com"),
            User(id=2, name="Jane Smith", email="jane@example.com"),
        ]


class TaskService:
    """Task business service."""
    
    def get_task(self, task_id: int) -> Task:
        """Get task by ID."""
        # TODO: Implement actual business logic
        return Task(id=task_id, title="Sample Task", description="A sample task")
    
    def get_tasks(self) -> List[Task]:
        """Get all tasks."""
        # TODO: Implement actual business logic
        return [
            Task(id=1, title="Task 1", description="First task"),
            Task(id=2, title="Task 2", description="Second task"),
        ]
