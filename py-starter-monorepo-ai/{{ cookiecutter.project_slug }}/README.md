# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## 项目概述

这是一个企业级全栈 AI 应用 Monorepo 项目，采用现代化的技术栈和最佳实践，包含：

- 🚀 **后端服务**: 基于 FastAPI 的高性能异步 API
- 🎨 **前端应用**: 基于 Nuxt 3 的现代化 Web 应用
- 🤖 **机器学习服务**: YOLOv8 目标检测 API
- 🎙️ **音频处理服务**: Fast-Whisper 语音转文字 API
- 🕷️ **网络爬虫**: 基于 Scrapy 的分布式爬虫
- 📊 **完整的监控**: Prometheus + Grafana + Loki + Jaeger
- 🔒 **安全扫描**: Trivy + Dependabot
- ☸️ **云原生部署**: Kubernetes + Helm + OpenTofu

## 技术栈

### 前端
- **框架**: Nuxt 3 + TypeScript
- **UI 库**: Nuxt UI + Tailwind CSS
- **状态管理**: Pinia
- **测试**: Vitest + Playwright

### 后端
- **框架**: FastAPI + Python {{ cookiecutter.python_version }}
- **数据库**: PostgreSQL + SQLModel + Alembic
- **缓存**: Redis + fastapi-cache2
- **异步任务**: ARQ
- **测试**: Pytest

### DevOps
- **容器化**: Docker + Docker Compose
- **编排**: Kubernetes + Helm
- **IaC**: OpenTofu (Terraform)
- **CI/CD**: GitHub Actions
- **监控**: Prometheus + Grafana + Loki + Jaeger

### 机器学习
{% if cookiecutter.enable_ml_api == 'yes' -%}
- **目标检测**: Ultralytics YOLOv8 + PyTorch
- **图像处理**: OpenCV + PIL
{% endif -%}
{% if cookiecutter.enable_audio_api == 'yes' -%}
- **语音识别**: Fast-Whisper
- **音频处理**: ffmpeg
{% endif -%}

## 快速开始

### 前置要求

- **Node.js**: {{ cookiecutter.node_version }}
- **Python**: {{ cookiecutter.python_version }}
- **pnpm**: 最新版本
- **uv**: 最新版本 (Python 包管理器)
- **Docker**: 最新版本
- **Docker Compose**: 最新版本

### 安装依赖

```bash
# 1. 克隆项目
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}

# 2. 安装 Node.js 依赖 (使用 pnpm workspace)
pnpm install

# 3. 为每个 Python 服务安装依赖
cd services/backend
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
cd ../..

{% if cookiecutter.enable_ml_api == 'yes' -%}
# 4. 安装 ML API 依赖
cd services/ml-api
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
cd ../..
{% endif -%}

{% if cookiecutter.enable_audio_api == 'yes' -%}
# 5. 安装 Audio API 依赖
cd services/audio-api
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
cd ../..
{% endif -%}

{% if cookiecutter.enable_scraper == 'yes' -%}
# 6. 安装爬虫依赖
cd services/scraper
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
cd ../..
{% endif -%}

# 7. 设置 pre-commit hooks
pre-commit install
```

### 本地开发环境

```bash
# 1. 复制环境变量配置文件
cp services/backend/.env.example services/backend/.env
cp services/frontend/.env.example services/frontend/.env

# 2. 启动基础设施服务 (PostgreSQL, Redis, MinIO)
docker-compose -f infra/docker-compose/dev.yml up -d

# 3. 等待数据库启动后，运行数据库迁移
cd services/backend
alembic upgrade head
cd ../..

# 4. 启动所有服务 (使用 Turbo)
pnpm dev
```

服务将在以下端口启动：
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Backend API Docs**: http://localhost:8000/docs
{% if cookiecutter.enable_ml_api == 'yes' -%}
- **ML API**: http://localhost:8001
{% endif -%}
{% if cookiecutter.enable_audio_api == 'yes' -%}
- **Audio API**: http://localhost:8002
{% endif -%}

### 运行测试

```bash
# 运行所有测试
pnpm test

# 运行前端测试
pnpm test:frontend

# 运行后端测试
pnpm test:backend
```

### 构建生产版本

```bash
# 构建所有服务
pnpm build

# 构建 Docker 镜像
docker-compose build
```

## 项目结构

```
{{ cookiecutter.project_slug }}/
├── .github/                    # GitHub Actions CI/CD 配置
├── docs/                       # 项目文档
├── infra/                      # 基础设施配置
│   ├── docker-compose/         # Docker Compose 配置
│   ├── kubernetes/             # Kubernetes 和 Helm Charts
│   └── tofu/                   # OpenTofu (Terraform) 配置
├── packages/                   # 跨服务共享包
│   ├── shared-types/           # 共享 TypeScript 类型
│   ├── ui-kit/                 # 共享 UI 组件
│   ├── eslint-config-custom/   # ESLint 配置
│   └── tsconfig-custom/        # TypeScript 配置
├── scripts/                    # 项目脚本
├── services/                   # 所有微服务
│   ├── backend/                # FastAPI 后端
│   ├── frontend/               # Nuxt 前端
│   ├── ml-api/                 # 机器学习 API
│   ├── audio-api/              # 音频处理 API
│   └── scraper/                # 网络爬虫
├── .gitignore
├── .pre-commit-config.yaml     # pre-commit 钩子配置
├── package.json                # pnpm workspace 根配置
├── pnpm-workspace.yaml         # pnpm workspace 定义
├── pyproject.toml              # Python 项目配置
├── tsconfig.base.json          # TypeScript 基础配置
└── turbo.json                  # Turbo 任务编排配置
```

## 开发指南

### 代码规范

项目使用以下工具确保代码质量：

- **Python**: ruff (lint + format)
- **JavaScript/TypeScript**: ESLint + Prettier
- **Pre-commit**: 自动在提交前运行检查

```bash
# 手动运行代码检查
pnpm lint

# 自动修复问题
pnpm lint:fix

# 格式化代码
pnpm format
```

### 数据库迁移

```bash
# 创建新的迁移
cd services/backend
alembic revision --autogenerate -m "描述迁移内容"

# 应用迁移
alembic upgrade head

# 回滚迁移
alembic downgrade -1
```

### API 文档

后端 API 文档自动生成：
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 部署

### Docker 部署

```bash
# 构建镜像
docker-compose build

# 启动服务
docker-compose up -d
```

### Kubernetes 部署

```bash
# 使用 Helm 部署
cd infra/kubernetes/helm-charts

# 部署后端
helm install backend ./backend -n {{ cookiecutter.kubernetes_namespace }}

# 部署前端
helm install frontend ./frontend -n {{ cookiecutter.kubernetes_namespace }}
```

### 生产环境配置

1. 配置环境变量
2. 设置数据库连接
3. 配置对象存储 (S3/MinIO)
4. 设置 Redis 连接
5. 配置域名和 SSL 证书
6. 设置监控和日志收集

详细部署文档请参考 [docs/deployment.md](docs/deployment.md)

## 监控

{% if cookiecutter.enable_monitoring == 'yes' -%}
### 本地监控

```bash
# 启动监控套件
docker-compose -f infra/docker-compose/monitoring.yml up -d
```

访问：
- **Grafana**: http://localhost:3001 (admin/admin)
- **Prometheus**: http://localhost:9090
- **Jaeger**: http://localhost:16686

### 生产监控

生产环境使用 Prometheus Operator 部署完整的监控栈。
{% endif -%}

## 贡献指南

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何为项目做贡献。

## 许可证

本项目采用 {{ cookiecutter.license }} 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 作者

**{{ cookiecutter.author_name }}** - [{{ cookiecutter.author_email }}](mailto:{{ cookiecutter.author_email }})

## 致谢

感谢所有使用的开源项目和贡献者！

