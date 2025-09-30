import pytest
from {{ cookiecutter.package_name }}.core.services import UserService, TaskService


class TestUserService:
    """测试 UserService。"""
    
    def test_get_user(self):
        """测试根据ID获取用户。"""
        service = UserService()
        user = service.get_user(1)
        assert user.id == 1
        assert user.name == "John Doe"
        assert user.email == "john@example.com"
    
    def test_get_users(self):
        """测试获取所有用户。"""
        service = UserService()
        users = service.get_users()
        assert len(users) == 2
        assert users[0].id == 1
        assert users[1].id == 2


class TestTaskService:
    """测试 TaskService。"""
    
    def test_get_task(self):
        """测试根据ID获取任务。"""
        service = TaskService()
        task = service.get_task(1)
        assert task.id == 1
        assert task.title == "Sample Task"
        assert task.description == "A sample task"
    
    def test_get_tasks(self):
        """测试获取所有任务。"""
        service = TaskService()
        tasks = service.get_tasks()
        assert len(tasks) == 2
        assert tasks[0].id == 1
        assert tasks[1].id == 2
