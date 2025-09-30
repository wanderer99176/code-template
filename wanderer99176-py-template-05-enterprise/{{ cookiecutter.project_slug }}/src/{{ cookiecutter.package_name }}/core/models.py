"""业务实体模型。"""

from pydantic import BaseModel


class User(BaseModel):
    """用户业务模型。"""
    id: int
    name: str
    email: str


class Task(BaseModel):
    """任务业务模型。"""
    id: int
    title: str
    description: str
    completed: bool = False
