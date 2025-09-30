"""{{ cookiecutter.project_name }} 的核心应用程序逻辑。"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from {{ cookiecutter.package_name }}.models import HealthResponse


def get_app() -> FastAPI:
    """创建并配置 FastAPI 应用程序。"""
    app = FastAPI(
        title="{{ cookiecutter.project_name }}",
        description="{{ cookiecutter.project_short_description }}",
        version="{{ cookiecutter.first_version }}",
    )

    # 添加 CORS 中间件
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 添加路由
    @app.get("/", response_model=HealthResponse)
    async def root():
        """根端点。"""
        return HealthResponse(message="Hello from {{ cookiecutter.project_name }}!")

    @app.get("/health", response_model=HealthResponse)
    async def health():
        """健康检查端点。"""
        return HealthResponse(message="OK")

    return app
