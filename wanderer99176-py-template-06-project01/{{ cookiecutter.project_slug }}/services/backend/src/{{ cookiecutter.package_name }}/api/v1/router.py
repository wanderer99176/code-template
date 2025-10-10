"""
API v1 路由汇总

将所有 v1 版本的 API 路由汇总到此处
"""

from fastapi import APIRouter

from {{ cookiecutter.package_name }}.api.v1.endpoints import (
    auth,
    users,
    health,
)

# 创建 API 路由器
api_router = APIRouter()

# 注册各个模块的路由
api_router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"],
)

api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"],
)

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["Users"],
)

