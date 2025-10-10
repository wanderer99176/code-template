# {{ cookiecutter.project_name }} Backend API

基于 FastAPI 的高性能异步 API 服务。

## 技术栈

- **框架**: FastAPI 0.109+
- **数据库**: PostgreSQL + SQLModel + Alembic
- **缓存**: Redis
- **异步任务**: ARQ
- **认证**: JWT (python-jose)
- **日志**: structlog
- **监控**: Prometheus + OpenTelemetry

## 项目结构

```
services/backend/
├── src/
│   └── {{ cookiecutter.package_name }}/
│       ├── api/                  # API 路由
│       │   └── v1/
│       │       ├── endpoints/    # 端点实现
│       │       └── router.py     # 路由汇总
│       ├── core/                 # 核心配置
│       │   ├── config.py         # 应用配置
│       │   ├── logging.py        # 日志配置
│       │   └── security.py       # 安全相关
│       ├── db/                   # 数据库
│       │   ├── base.py           # 基类
│       │   ├── models/           # 数据模型
│       │   └── session.py        # 会话管理
│       ├── features/             # 业务功能模块
│       │   └── todos/
│       │       ├── router.py     # 路由
│       │       ├── schemas.py    # 数据模型
│       │       └── services.py   # 业务逻辑
│       ├── main.py               # 应用入口
│       └── worker.py             # 异步任务
├── alembic/                      # 数据库迁移
│   ├── versions/
│   └── env.py
├── tests/                        # 测试
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── pyproject.toml                # 项目配置
├── Dockerfile                    # Docker 镜像
└── README.md                     # 本文件
```

## 快速开始

### 1. 安装依赖

```bash
# 创建虚拟环境
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 安装依赖
uv pip install -e ".[dev]"
```

### 2. 配置环境变量

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件
nano .env
```

### 3. 启动基础设施

```bash
# 启动 PostgreSQL, Redis, MinIO
docker-compose -f ../../infra/docker-compose/dev.yml up -d
```

### 4. 运行数据库迁移

```bash
# 创建迁移
alembic revision --autogenerate -m "Initial migration"

# 应用迁移
alembic upgrade head
```

### 5. 启动开发服务器

```bash
# 使用 uvicorn 直接运行
uvicorn {{ cookiecutter.package_name }}.main:app --reload --host 0.0.0.0 --port 8000

# 或使用 Python 模块运行
python -m {{ cookiecutter.package_name }}.main
```

访问：
- **API 文档 (Swagger)**: http://localhost:8000/docs
- **API 文档 (ReDoc)**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/api/v1/openapi.json

## 开发指南

### 添加新功能

1. 在 `features/` 目录下创建新模块
2. 定义数据模型 (`schemas.py`)
3. 实现业务逻辑 (`services.py`)
4. 创建路由端点 (`router.py`)
5. 在 `api/v1/router.py` 中注册路由

示例：

```python
# features/todos/schemas.py
from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    completed: bool = False

# features/todos/services.py
async def create_todo(db: AsyncSession, todo: TodoCreate):
    # 业务逻辑
    pass

# features/todos/router.py
from fastapi import APIRouter, Depends
router = APIRouter()

@router.post("/")
async def create_todo(todo: TodoCreate):
    # 调用 service
    pass
```

### 数据库迁移

```bash
# 创建新迁移
alembic revision --autogenerate -m "描述变更"

# 应用迁移
alembic upgrade head

# 回滚迁移
alembic downgrade -1

# 查看迁移历史
alembic history

# 查看当前版本
alembic current
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/unit/test_users.py

# 生成覆盖率报告
pytest --cov={{ cookiecutter.package_name }} --cov-report=html

# 打开覆盖率报告
open htmlcov/index.html
```

### 代码检查

```bash
# Ruff 检查
ruff check .

# Ruff 格式化
ruff format .

# 类型检查
mypy src
```

## API 设计

### 响应格式

所有 API 响应遵循统一格式：

```json
{
  "success": true,
  "data": {...},
  "error": null,
  "message": "操作成功"
}
```

错误响应：

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "错误描述",
    "details": {}
  }
}
```

### 分页

使用标准的分页参数：

```
GET /api/v1/users?page=1&page_size=20&sort_by=created_at&sort_order=desc
```

响应：

```json
{
  "success": true,
  "data": {
    "items": [...],
    "total": 100,
    "page": 1,
    "page_size": 20,
    "total_pages": 5
  }
}
```

### 认证

使用 JWT Bearer Token：

```
Authorization: Bearer <token>
```

## 部署

### Docker 部署

```bash
# 构建镜像
docker build -t {{ cookiecutter.project_slug }}-backend:latest .

# 运行容器
docker run -d \
  --name {{ cookiecutter.project_slug }}-backend \
  -p 8000:8000 \
  --env-file .env \
  {{ cookiecutter.project_slug }}-backend:latest
```

### 生产环境配置

```bash
# 使用 Gunicorn + Uvicorn Workers
gunicorn {{ cookiecutter.package_name }}.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --log-level info \
  --access-logfile - \
  --error-logfile -
```

## 监控

### Prometheus 指标

访问 `/metrics` 端点获取 Prometheus 格式的指标。

### 健康检查

- `/health` - 基本健康检查
- `/health/detailed` - 详细健康状态
- `/health/ready` - 就绪检查（K8s readiness probe）
- `/health/live` - 存活检查（K8s liveness probe）

## 性能优化

### 数据库优化

1. 使用索引
2. 启用连接池
3. 使用异步查询
4. 实现查询缓存

### API 优化

1. 使用 Redis 缓存
2. 启用 Gzip 压缩
3. 实现 API 限流
4. 使用异步任务处理耗时操作

## 故障排查

### 常见问题

1. **数据库连接失败**
   ```bash
   # 检查数据库是否运行
   docker-compose -f ../../infra/docker-compose/dev.yml ps postgres
   
   # 查看日志
   docker-compose -f ../../infra/docker-compose/dev.yml logs postgres
   ```

2. **导入错误**
   ```bash
   # 确保安装了依赖
   uv pip install -e ".[dev]"
   
   # 检查 PYTHONPATH
   export PYTHONPATH="${PYTHONPATH}:${PWD}/src"
   ```

3. **迁移失败**
   ```bash
   # 回滚迁移
   alembic downgrade -1
   
   # 删除迁移文件并重新创建
   rm alembic/versions/*.py
   alembic revision --autogenerate -m "Initial"
   ```

## 相关资源

- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [SQLModel 文档](https://sqlmodel.tiangolo.com/)
- [Alembic 文档](https://alembic.sqlalchemy.org/)
- [Pydantic 文档](https://docs.pydantic.dev/)

## 许可证

{{ cookiecutter.license }}

