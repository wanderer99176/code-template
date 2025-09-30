"""{{ cookiecutter.project_name }} 的 Pydantic 模型。"""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """健康检查响应模型。"""
    
    message: str
