"""业务流程服务。"""

from typing import List
from my_enterprise_project.core.models import User, Task


class UserService:
    """用户业务服务。"""
    
    def get_user(self, user_id: int) -> User:
        """根据ID获取用户。"""
        # 待办：实现实际的业务逻辑
        return User(id=user_id, name="John Doe", email="john@example.com")
    
    def get_users(self) -> List[User]:
        """获取所有用户。"""
        # 待办：实现实际的业务逻辑
        return [
            User(id=1, name="John Doe", email="john@example.com"),
            User(id=2, name="Jane Smith", email="jane@example.com"),
        ]


class TaskService:
    """任务业务服务。"""
    
    def get_task(self, task_id: int) -> Task:
        """根据ID获取任务。"""
        # 待办：实现实际的业务逻辑
        return Task(id=task_id, title="Sample Task", description="A sample task")
    
    def get_tasks(self) -> List[Task]:
        """获取所有任务。"""
        # 待办：实现实际的业务逻辑
        return [
            Task(id=1, title="Task 1", description="First task"),
            Task(id=2, title="Task 2", description="Second task"),
        ]
