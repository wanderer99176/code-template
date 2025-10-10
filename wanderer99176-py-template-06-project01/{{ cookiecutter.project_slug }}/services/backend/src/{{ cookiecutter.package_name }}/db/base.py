"""
数据库基类

导入所有模型以便 Alembic 自动检测
"""

from sqlmodel import SQLModel

# 导入所有模型（用于 Alembic 自动迁移）
# from {{ cookiecutter.package_name }}.models.user import User
# from {{ cookiecutter.package_name }}.models.post import Post

__all__ = ["SQLModel"]

