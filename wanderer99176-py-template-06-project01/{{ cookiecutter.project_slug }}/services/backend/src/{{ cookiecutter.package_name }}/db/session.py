"""
数据库会话管理

配置数据库连接和会话管理
"""

from typing import AsyncGenerator
from sqlmodel import create_engine
from sqlmodel.ext.asyncio.session import AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker

from {{ cookiecutter.package_name }}.core.config import settings
from {{ cookiecutter.package_name }}.core.logging import logger


# 创建异步引擎
async_engine: AsyncEngine = AsyncEngine(
    create_engine(
        str(settings.DATABASE_URL),
        echo=settings.DB_ECHO,
        pool_size=settings.DB_POOL_SIZE,
        max_overflow=settings.DB_MAX_OVERFLOW,
        pool_recycle=settings.DB_POOL_RECYCLE,
        pool_pre_ping=True,  # 连接池预检查
    )
)

# 创建异步会话工厂
async_session_factory = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    获取数据库会话
    
    用作 FastAPI 依赖注入
    
    Yields:
        AsyncSession: 数据库会话
    """
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            logger.error(f"数据库会话错误: {e}")
            raise
        finally:
            await session.close()


async def init_db() -> None:
    """
    初始化数据库
    
    创建所有表（仅开发环境，生产环境使用 Alembic）
    """
    from {{ cookiecutter.package_name }}.db.base import SQLModel
    
    if settings.is_development:
        async with async_engine.begin() as conn:
            # 仅在开发环境自动创建表
            await conn.run_sync(SQLModel.metadata.create_all)
            logger.info("数据库表创建完成")


async def close_db() -> None:
    """关闭数据库连接"""
    await async_engine.dispose()
    logger.info("数据库连接已关闭")

