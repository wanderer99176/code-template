# 环境搭建指南

本指南将帮助您从零开始搭建 {{ cookiecutter.project_name }} 的开发环境。

## 📋 前置要求

### 必需软件

#### Windows 用户

```PowerShell
# 1. 安装 Chocolatey (如果尚未安装)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# 2. 使用 Chocolatey 安装系统软件
choco install -y git python nodejs docker-desktop

# 3. 关闭管理员 PowerShell，打开一个普通的 Git Bash 终端
```

```Bash
# 4. 安装 pipx (用于管理 Python 工具)
pip install pipx
pipx ensurepath

# 5. 使用 pipx 安装 Python 工具
pipx install uv
pipx install cookiecutter
pipx install pre-commit
pipx install gibo

# 6. 安装 pnpm (Node.js 包管理器)
npm install -g pnpm@8

# 7. 验证安装
python --version    # 应该是 {{ cookiecutter.python_version }}
node --version      # 应该是 {{ cookiecutter.node_version }}
pnpm --version      # 应该是 8.x
uv --version
docker --version
```

#### macOS 用户

```bash
# 1. 安装 Homebrew (如果尚未安装)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. 安装必需软件
brew install python@3.11 node@20 git
brew install --cask docker

# 3. 安装 Python 工具
pip3 install pipx
pipx ensurepath
pipx install uv
pipx install pre-commit

# 4. 安装 pnpm
npm install -g pnpm@8

# 5. 启动 Docker Desktop
open -a Docker
```

#### Linux 用户 (Ubuntu/Debian)

```bash
# 1. 更新系统
sudo apt update && sudo apt upgrade -y

# 2. 安装 Python 3.11
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install -y python3.11 python3.11-venv python3.11-dev python3-pip

# 3. 安装 Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# 4. 安装 Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker

# 5. 安装 Python 工具
pip3 install pipx
pipx ensurepath
pipx install uv
pipx install pre-commit

# 6. 安装 pnpm
npm install -g pnpm@8
```

## 🚀 项目搭建

### 1. 克隆或创建项目

如果您是从模板创建新项目：

```bash
# 使用 cookiecutter 创建项目
cookiecutter gh:{{ cookiecutter.github_username }}/py-template-06-project01

# 或者从本地模板创建
cookiecutter /path/to/template
```

如果是克隆现有项目：

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
```

### 2. 初始化项目

```bash
# 运行自动化初始化脚本
bash scripts/setup.sh
```

或者手动执行以下步骤：

```bash
# 1. 安装 Node.js 依赖
pnpm install

# 2. 设置 pre-commit hooks
pre-commit install

# 3. 生成 .gitignore 文件 (如果使用 gibo)
gibo dump Python Node VisualStudioCode JetBrains Windows macOS Linux > .gitignore

# 4. 为每个 Python 服务创建虚拟环境并安装依赖

# Backend
cd services/backend
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
cd ../..

{% if cookiecutter.enable_ml_api == 'yes' -%}
# ML API
cd services/ml-api
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
cd ../..
{% endif -%}

{% if cookiecutter.enable_audio_api == 'yes' -%}
# Audio API
cd services/audio-api
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
cd ../..
{% endif -%}

{% if cookiecutter.enable_scraper == 'yes' -%}
# Scraper
cd services/scraper
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
cd ../..
{% endif -%}
```

### 3. 配置环境变量

```bash
# 1. 复制环境变量模板
cp services/backend/.env.example services/backend/.env
cp services/frontend/.env.example services/frontend/.env

# 2. 编辑 .env 文件，填入实际配置
# Backend
nano services/backend/.env

# Frontend
nano services/frontend/.env
```

**Backend .env 示例：**

```env
# 数据库配置
DATABASE_URL=postgresql://{{ cookiecutter.database_user }}:your_password@localhost:5432/{{ cookiecutter.database_name }}

# Redis 配置
REDIS_URL=redis://localhost:6379/0

# JWT 密钥 (使用 openssl rand -hex 32 生成)
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS 配置
BACKEND_CORS_ORIGINS=["http://localhost:3000"]

# S3/MinIO 配置
S3_ENDPOINT_URL=http://localhost:9000
S3_ACCESS_KEY_ID=minioadmin
S3_SECRET_ACCESS_KEY=minioadmin
S3_BUCKET_NAME={{ cookiecutter.project_slug }}-uploads

# 邮件配置 (可选)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
EMAILS_FROM_EMAIL=noreply@{{ cookiecutter.domain_name }}
```

**Frontend .env 示例：**

```env
# API 端点
NUXT_PUBLIC_API_BASE_URL=http://localhost:8000
NUXT_PUBLIC_WS_URL=ws://localhost:8000

# 站点配置
NUXT_PUBLIC_SITE_URL=http://localhost:3000
NUXT_PUBLIC_SITE_NAME={{ cookiecutter.project_name }}
```

### 4. 启动基础设施服务

```bash
# 启动 PostgreSQL, Redis, MinIO
docker-compose -f infra/docker-compose/dev.yml up -d

# 查看服务状态
docker-compose -f infra/docker-compose/dev.yml ps

# 查看日志
docker-compose -f infra/docker-compose/dev.yml logs -f
```

访问服务：
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379
- **MinIO Console**: http://localhost:9001 (minioadmin/minioadmin)

### 5. 初始化数据库

```bash
# 进入 backend 目录
cd services/backend
source .venv/bin/activate

# 运行数据库迁移
alembic upgrade head

# 创建初始数据 (可选)
python scripts/seed_db.py

cd ../..
```

### 6. 启动开发服务器

```bash
# 方式 1: 使用 Turbo 同时启动所有服务
pnpm dev

# 方式 2: 分别启动各个服务

# 终端 1: 启动后端
pnpm dev:backend
# 或
cd services/backend && source .venv/bin/activate && uvicorn {{ cookiecutter.package_name }}.main:app --reload

# 终端 2: 启动前端
pnpm dev:frontend
# 或
cd services/frontend && pnpm dev
```

访问应用：
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs (Swagger)**: http://localhost:8000/docs
- **API Docs (ReDoc)**: http://localhost:8000/redoc

## 🧪 运行测试

```bash
# 运行所有测试
pnpm test

# 运行后端测试
pnpm test:backend
cd services/backend && pytest -v

# 运行前端测试
pnpm test:frontend
cd services/frontend && pnpm test

# 运行 E2E 测试
pnpm test:e2e
cd services/frontend && pnpm test:e2e

# 测试覆盖率
cd services/backend && pytest --cov --cov-report=html
# 打开 htmlcov/index.html 查看详细报告
```

## 🔍 代码检查和格式化

```bash
# 运行所有检查
pnpm lint

# 自动修复问题
pnpm lint:fix

# 格式化代码
pnpm format

# 类型检查
pnpm typecheck

# 手动运行 pre-commit hooks
pre-commit run --all-files
```

## 🐳 Docker 开发

```bash
# 构建所有服务的 Docker 镜像
docker-compose build

# 启动所有服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止所有服务
docker-compose down

# 停止并清理数据卷
docker-compose down -v
```

## 🔧 常见问题

### Python 版本问题

如果系统中有多个 Python 版本：

```bash
# 使用 pyenv 管理 Python 版本
curl https://pyenv.run | bash

# 安装 Python 3.11.9
pyenv install {{ cookiecutter.python_version }}

# 设置项目使用的 Python 版本
pyenv local {{ cookiecutter.python_version }}
```

### Node.js 版本问题

如果需要多个 Node.js 版本：

```bash
# 使用 nvm 管理 Node.js 版本
# Windows: 下载 nvm-windows from https://github.com/coreybutler/nvm-windows/releases

# macOS/Linux:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# 安装 Node.js 20
nvm install 20
nvm use 20
```

### 数据库连接失败

```bash
# 检查 Docker 容器状态
docker-compose -f infra/docker-compose/dev.yml ps

# 重启数据库
docker-compose -f infra/docker-compose/dev.yml restart postgres

# 查看数据库日志
docker-compose -f infra/docker-compose/dev.yml logs postgres
```

### 端口被占用

```bash
# Windows: 查找占用端口的进程
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux: 查找并终止进程
lsof -ti:8000 | xargs kill -9
```

### 依赖安装失败

```bash
# 清理缓存后重新安装

# Python
rm -rf services/backend/.venv
cd services/backend && uv venv && uv pip install -e ".[dev]"

# Node.js
rm -rf node_modules pnpm-lock.yaml
pnpm install
```

## 📚 下一步

- 阅读 [README.md](../README.md) 了解项目概述
- 查看 [CONTRIBUTING.md](../CONTRIBUTING.md) 学习如何贡献代码
- 阅读 [deployment.md](deployment.md) 了解部署流程
- 查看 [adr/](adr/) 目录了解架构决策

## 💡 有用的命令

```bash
# 生成类型定义
pnpm codegen

# 创建新的数据库迁移
cd services/backend && alembic revision --autogenerate -m "描述"

# 查看所有可用脚本
pnpm run

# 更新所有依赖
pnpm update -r

# 清理所有构建产物
pnpm clean
```

## 🆘 获取帮助

如果遇到问题：

1. 查看 [文档](.)
2. 搜索 [GitHub Issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues)
3. 在 [Discussions](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/discussions) 中提问
4. 发送邮件至 {{ cookiecutter.author_email }}

祝您开发愉快！🎉

