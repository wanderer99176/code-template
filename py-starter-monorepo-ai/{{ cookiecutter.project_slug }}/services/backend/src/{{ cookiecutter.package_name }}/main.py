"""
FastAPI 应用主入口

配置和初始化 FastAPI 应用，包括：
- 中间件
- 路由
- 事件处理器
- 异常处理
- 文档配置
"""

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from {{ cookiecutter.package_name }}.core.config import settings
from {{ cookiecutter.package_name }}.core.logging import setup_logging, logger

# 设置日志
setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    应用生命周期管理
    
    启动时执行初始化，关闭时执行清理
    """
    # 启动时执行
    logger.info(f"🚀 启动 {settings.APP_NAME} v{settings.VERSION}")
    logger.info(f"📝 环境: {settings.ENVIRONMENT}")
    logger.info(f"📊 API 文档: http://{settings.HOST}:{settings.PORT}/docs")
    
    # 导入并初始化数据库（如果需要）
    # from {{ cookiecutter.package_name }}.db.session import init_db
    # await init_db()
    
    yield
    
    # 关闭时执行
    logger.info(f"👋 关闭 {settings.APP_NAME}")
    
    # 清理资源
    # await cleanup()


# 创建 FastAPI 应用实例
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
    docs_url="/docs" if settings.ENVIRONMENT != "production" else None,
    redoc_url="/redoc" if settings.ENVIRONMENT != "production" else None,
    lifespan=lifespan,
)


# ==================== 中间件配置 ====================

# CORS 中间件
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Gzip 压缩
app.add_middleware(GZipMiddleware, minimum_size=1000)

# 可信主机（生产环境）
if settings.ENVIRONMENT == "production":
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.ALLOWED_HOSTS or ["*"],
    )


# ==================== 异常处理 ====================

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    """HTTP 异常处理器"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": f"HTTP_{exc.status_code}",
                "message": exc.detail,
            },
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """请求验证错误处理器"""
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"],
        })
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "请求参数验证失败",
                "details": errors,
            },
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """通用异常处理器"""
    logger.exception(f"未处理的异常: {exc}")
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "服务器内部错误" if settings.ENVIRONMENT == "production" else str(exc),
            },
        },
    )


# ==================== 路由配置 ====================

@app.get("/", tags=["Root"])
async def root() -> dict[str, Any]:
    """根路径 - 健康检查"""
    return {
        "success": True,
        "message": f"欢迎使用 {settings.APP_NAME} API",
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "docs": f"/docs",
    }


@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, Any]:
    """健康检查端点"""
    return {
        "success": True,
        "status": "healthy",
        "version": settings.VERSION,
    }


@app.get("/ping", tags=["Health"])
async def ping() -> dict[str, str]:
    """简单的 ping 端点"""
    return {"ping": "pong"}


# 导入并注册 API 路由
from {{ cookiecutter.package_name }}.api.v1.router import api_router

app.include_router(api_router, prefix=settings.API_V1_PREFIX)


# ==================== 监控端点 ====================

if settings.ENABLE_METRICS:
    from starlette_prometheus import PrometheusMiddleware, metrics
    
    app.add_middleware(PrometheusMiddleware)
    app.add_route("/metrics", metrics)


# ==================== OpenTelemetry 追踪 ====================

if settings.ENABLE_TRACING:
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    
    FastAPIInstrumentor.instrument_app(app)


# ==================== 开发工具 ====================

if settings.ENVIRONMENT == "development":
    @app.get("/info", tags=["Development"])
    async def app_info() -> dict[str, Any]:
        """应用信息 (仅开发环境)"""
        return {
            "app_name": settings.APP_NAME,
            "version": settings.VERSION,
            "environment": settings.ENVIRONMENT,
            "database_url": settings.DATABASE_URL.split("@")[-1] if settings.DATABASE_URL else None,
            "redis_url": settings.REDIS_URL.split("@")[-1] if settings.REDIS_URL else None,
            "cors_origins": settings.BACKEND_CORS_ORIGINS,
            "debug": settings.DEBUG,
        }


# ==================== 主程序 ====================

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "{{ cookiecutter.package_name }}.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.ENVIRONMENT == "development",
        log_level=settings.LOG_LEVEL.lower(),
    )

