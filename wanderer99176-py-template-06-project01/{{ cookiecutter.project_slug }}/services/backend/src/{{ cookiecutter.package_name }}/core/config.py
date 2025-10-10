"""
应用配置

使用 Pydantic Settings 管理配置，支持从环境变量和 .env 文件加载
"""

from typing import Any, Literal
import secrets
from pydantic import (
    AnyHttpUrl,
    EmailStr,
    PostgresDsn,
    RedisDsn,
    field_validator,
    ValidationInfo,
)
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """应用配置类"""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )
    
    # ==================== 基本配置 ====================
    
    APP_NAME: str = "{{ cookiecutter.project_name }}"
    DESCRIPTION: str = "{{ cookiecutter.description }}"
    VERSION: str = "{{ cookiecutter.version }}"
    ENVIRONMENT: Literal["development", "staging", "production"] = "development"
    DEBUG: bool = False
    
    API_V1_PREFIX: str = "/api/v1"
    
    # ==================== 服务器配置 ====================
    
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 4
    
    # ==================== 日志配置 ====================
    
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    
    # ==================== 数据库配置 ====================
    
    DATABASE_URL: PostgresDsn | str
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 10
    DB_POOL_RECYCLE: int = 3600
    DB_ECHO: bool = False
    
    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: str | None, info: ValidationInfo) -> str:
        """组装数据库连接字符串"""
        if isinstance(v, str):
            return v
        raise ValueError("DATABASE_URL is required")
    
    # ==================== Redis 配置 ====================
    
    REDIS_URL: RedisDsn | str
    CACHE_EXPIRE: int = 3600  # 秒
    
    # ==================== JWT 认证配置 ====================
    
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    @field_validator("SECRET_KEY", mode="before")
    @classmethod
    def check_secret_key(cls, v: str | None) -> str:
        """检查密钥"""
        if not v or v == "changethis":
            return secrets.token_urlsafe(32)
        return v
    
    # ==================== CORS 配置 ====================
    
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []
    
    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str]:
        """解析 CORS 源"""
        if isinstance(v, str):
            import json
            return json.loads(v)
        return v
    
    # ==================== S3/MinIO 配置 ====================
    
    S3_ENDPOINT_URL: str | None = None
    AWS_REGION: str = "us-east-1"
    S3_ACCESS_KEY_ID: str
    S3_SECRET_ACCESS_KEY: str
    S3_BUCKET_NAME: str
    MAX_UPLOAD_SIZE: int = 10  # MB
    
    # ==================== 邮件配置 ====================
    
    SMTP_HOST: str | None = None
    SMTP_PORT: int = 587
    SMTP_USER: str | None = None
    SMTP_PASSWORD: str | None = None
    EMAILS_FROM_EMAIL: EmailStr | None = None
    EMAILS_FROM_NAME: str | None = None
    
    # ==================== 异步任务配置 ====================
    
    ARQ_REDIS_URL: RedisDsn | str | None = None
    
    # ==================== 安全配置 ====================
    
    ALLOWED_HOSTS: list[str] = ["*"]
    RATE_LIMIT_PER_MINUTE: int = 60
    
    # 超级管理员
    FIRST_SUPERUSER_EMAIL: EmailStr = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "changethis"
    
    # ==================== 监控配置 ====================
    
    ENABLE_METRICS: bool = True
    METRICS_PATH: str = "/metrics"
    ENABLE_TRACING: bool = False
    JAEGER_ENDPOINT: str | None = None
    
    # ==================== 第三方服务 ====================
    
    SENTRY_DSN: str | None = None
    
    # OAuth
    GOOGLE_CLIENT_ID: str | None = None
    GOOGLE_CLIENT_SECRET: str | None = None
    GITHUB_CLIENT_ID: str | None = None
    GITHUB_CLIENT_SECRET: str | None = None
    
    # ==================== 工具方法 ====================
    
    @property
    def database_url_sync(self) -> str:
        """同步数据库 URL"""
        url = str(self.DATABASE_URL)
        if url.startswith("postgresql+asyncpg://"):
            return url.replace("postgresql+asyncpg://", "postgresql://")
        return url
    
    @property
    def database_url_async(self) -> str:
        """异步数据库 URL"""
        url = str(self.DATABASE_URL)
        if url.startswith("postgresql://"):
            return url.replace("postgresql://", "postgresql+asyncpg://")
        return url
    
    @property
    def is_production(self) -> bool:
        """是否为生产环境"""
        return self.ENVIRONMENT == "production"
    
    @property
    def is_development(self) -> bool:
        """是否为开发环境"""
        return self.ENVIRONMENT == "development"


# 创建全局配置实例
settings = Settings()

