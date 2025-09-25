import pytest
from {{ cookiecutter.package_name }}.core.services import UserService, TaskService


class TestUserService:
    """Test UserService."""
    
    def test_get_user(self):
        """Test getting a user by ID."""
        service = UserService()
        user = service.get_user(1)
        assert user.id == 1
        assert user.name == "John Doe"
        assert user.email == "john@example.com"
    
    def test_get_users(self):
        """Test getting all users."""
        service = UserService()
        users = service.get_users()
        assert len(users) == 2
        assert users[0].id == 1
        assert users[1].id == 2


class TestTaskService:
    """Test TaskService."""
    
    def test_get_task(self):
        """Test getting a task by ID."""
        service = TaskService()
        task = service.get_task(1)
        assert task.id == 1
        assert task.title == "Sample Task"
        assert task.description == "A sample task"
    
    def test_get_tasks(self):
        """Test getting all tasks."""
        service = TaskService()
        tasks = service.get_tasks()
        assert len(tasks) == 2
        assert tasks[0].id == 1
        assert tasks[1].id == 2
