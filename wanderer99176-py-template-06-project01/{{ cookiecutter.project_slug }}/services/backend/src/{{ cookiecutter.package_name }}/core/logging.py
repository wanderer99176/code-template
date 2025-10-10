"""
日志配置

使用 structlog 实现结构化日志
"""

import logging
import sys
from typing import Any

import structlog
from structlog.types import EventDict, Processor

from {{ cookiecutter.package_name }}.core.config import settings


def add_app_context(logger: Any, method_name: str, event_dict: EventDict) -> EventDict:
    """添加应用上下文信息"""
    event_dict["app"] = settings.APP_NAME
    event_dict["version"] = settings.VERSION
    event_dict["environment"] = settings.ENVIRONMENT
    return event_dict


def setup_logging() -> None:
    """设置日志配置"""
    
    # 配置标准库日志
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, settings.LOG_LEVEL),
    )
    
    # 配置 structlog
    processors: list[Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        add_app_context,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
    ]
    
    # 开发环境使用彩色输出
    if settings.is_development:
        processors.append(structlog.dev.ConsoleRenderer(colors=True))
    else:
        # 生产环境使用 JSON 格式
        processors.append(structlog.processors.JSONRenderer())
    
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )


# 创建全局 logger 实例
logger = structlog.get_logger()

