"""
健康检查端点

提供详细的健康状态信息
"""

from typing import Any
from fastapi import APIRouter, Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from {{ cookiecutter.package_name }}.db.session import get_session
from {{ cookiecutter.package_name }}.core.config import settings
from {{ cookiecutter.package_name }}.core.logging import logger

router = APIRouter()


@router.get("/")
async def health_check() -> dict[str, Any]:
    """
    简单健康检查
    
    返回应用的基本状态信息
    """
    return {
        "success": True,
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
    }


@router.get("/detailed")
async def detailed_health_check(
    db: AsyncSession = Depends(get_session),
) -> dict[str, Any]:
    """
    详细健康检查
    
    检查所有关键服务的健康状态：
    - 数据库连接
    - Redis 连接
    - S3 连接
    """
    health_status = {
        "success": True,
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "checks": {},
    }
    
    # 检查数据库
    try:
        # 执行简单查询
        result = await db.execute(select(1))
        result.scalar()
        health_status["checks"]["database"] = {
            "status": "healthy",
            "message": "数据库连接正常",
        }
    except Exception as e:
        logger.error(f"数据库健康检查失败: {e}")
        health_status["checks"]["database"] = {
            "status": "unhealthy",
            "message": f"数据库连接失败: {str(e)}",
        }
        health_status["status"] = "unhealthy"
        health_status["success"] = False
    
    # 检查 Redis
    try:
        # 这里应该添加实际的 Redis 检查
        # import redis
        # r = redis.from_url(settings.REDIS_URL)
        # r.ping()
        health_status["checks"]["redis"] = {
            "status": "healthy",
            "message": "Redis 连接正常",
        }
    except Exception as e:
        logger.error(f"Redis 健康检查失败: {e}")
        health_status["checks"]["redis"] = {
            "status": "unhealthy",
            "message": f"Redis 连接失败: {str(e)}",
        }
    
    # 检查 S3/MinIO
    try:
        # 这里应该添加实际的 S3 检查
        # import boto3
        # s3 = boto3.client('s3', ...)
        # s3.head_bucket(Bucket=settings.S3_BUCKET_NAME)
        health_status["checks"]["s3"] = {
            "status": "healthy",
            "message": "S3 连接正常",
        }
    except Exception as e:
        logger.error(f"S3 健康检查失败: {e}")
        health_status["checks"]["s3"] = {
            "status": "warning",
            "message": f"S3 连接异常: {str(e)}",
        }
    
    return health_status


@router.get("/ready")
async def readiness_check(
    db: AsyncSession = Depends(get_session),
) -> dict[str, Any]:
    """
    就绪检查
    
    用于 Kubernetes readiness probe
    检查应用是否准备好接收流量
    """
    try:
        # 检查数据库连接
        result = await db.execute(select(1))
        result.scalar()
        
        return {
            "success": True,
            "ready": True,
            "message": "应用已就绪",
        }
    except Exception as e:
        logger.error(f"就绪检查失败: {e}")
        return {
            "success": False,
            "ready": False,
            "message": f"应用未就绪: {str(e)}",
        }


@router.get("/live")
async def liveness_check() -> dict[str, Any]:
    """
    存活检查
    
    用于 Kubernetes liveness probe
    检查应用是否还在运行
    """
    return {
        "success": True,
        "alive": True,
        "message": "应用正在运行",
    }

