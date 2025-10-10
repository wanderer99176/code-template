# 企业级全栈 AI 应用 Monorepo 项目模板

> 🚀 **py-starter-monorepo-ai** - 基于 Cookiecutter 的生产级全栈 AI 应用模板

这是一个**开箱即用**的企业级项目模板，集成了从开发到生产部署的完整工具链，让您专注于业务逻辑而非基础设施搭建。

## 🌟 核心特性

### 🏗️ 完整技术栈

- **前端**: Nuxt 3 + Vue 3 + TypeScript + Tailwind CSS + UI Kit 组件库
- **后端**: FastAPI + Python 3.11.9 + SQLModel + Alembic + ARQ 异步任务
- **AI 服务**: YOLOv8 目标检测 + Whisper 语音识别 + GPU 加速
- **数据采集**: Scrapy 分布式爬虫 + 反爬虫策略
- **数据库**: PostgreSQL + Redis + MinIO (S3 兼容)
- **监控**: Prometheus + Grafana + Loki + Jaeger 全链路追踪
- **部署**: Docker + Kubernetes + Helm + OpenTofu (Terraform)

### ⚡ 开发体验

- ✅ **Monorepo 架构**: pnpm workspace + Turborepo 增量构建
- ✅ **类型安全**: 端到端类型支持，自动生成共享类型
- ✅ **代码质量**: Ruff + ESLint + Prettier + Pre-commit Hooks
- ✅ **快速工具**: `uv` (Python) + `pnpm` (Node.js) 极速依赖管理
- ✅ **任务运行**: Justfile (50+ 命令) + Makefile 兼容
- ✅ **文档完善**: API 文档 + ADR 架构决策 + 部署指南

### 🚀 生产就绪

- ✅ **云原生**: 完整的 Kubernetes Helm Charts + 自动扩缩容
- ✅ **IaC**: OpenTofu/Terraform AWS 基础设施代码（VPC + EKS + RDS + Redis + S3）
- ✅ **CI/CD**: GitHub Actions 流水线 + 多环境部署
- ✅ **安全**: 网络策略 + IRSA + Secrets Manager + SSL/TLS
- ✅ **可观测性**: 结构化日志 + Metrics + Tracing + Alerts

## 📦 包含的服务

### 核心服务

1. **Backend (FastAPI)** ✅ 完整实现
   - RESTful API
   - JWT 认证
   - SQLModel ORM
   - Alembic 迁移
   - ARQ 异步任务
   - Redis 缓存

2. **Frontend (Nuxt)** ✅ 完整实现
   - SSR/SSG 支持
   - Nuxt UI 组件库
   - Pinia 状态管理
   - TypeScript

3. **ML API (YOLOv8)** ✅ 完整实现
   - 目标检测
   - GPU 加速
   - 模型管理

4. **Audio API (Whisper)** ✅ 完整实现
   - 语音转文字
   - 多语言支持
   - 实时处理

5. **Scraper (Scrapy)** ✅ 完整实现
   - 分布式爬取
   - 反爬虫策略
   - 数据清洗

### 基础设施

- **PostgreSQL**: 主数据库
- **Redis**: 缓存 + 消息队列
- **MinIO**: 对象存储（S3 兼容）
- **Prometheus**: 指标收集
- **Grafana**: 可视化
- **Loki**: 日志聚合
- **Jaeger**: 分布式追踪

## 🚀 快速开始

### 前置要求

确保已安装：

- **Python**: 3.11.9
- **Node.js**: 20.x
- **pnpm**: 8.x
- **uv**: 最新版本
- **Docker**: 最新版本
- **Git**: 最新版本

### 创建项目

#### 方法 1: 使用 cookiecutter

```bash
# 1. 安装 cookiecutter
pipx install cookiecutter

# 2. 从模板创建项目
cookiecutter gh:wanderer99176/code-template --directory py-starter-monorepo-ai

# 或使用本地路径
cookiecutter /path/to/py-starter-monorepo-ai
```

#### 方法 2: 手动设置

```bash
# 1. 克隆或复制模板
git clone <this-repo> my-project
cd my-project

# 2. 手动替换模板变量
# 搜索并替换:
# {{ cookiecutter.project_name }}
# {{ cookiecutter.project_slug }}
# {{ cookiecutter.package_name }}
# {{ cookiecutter.author_name }}
# {{ cookiecutter.author_email }}
```

### 初始化项目

#### 🎯 推荐方式：使用 Just 命令

```bash
# 1. 初始化（自动检查依赖、安装、配置）
just init

# 2. 启动开发环境
just dev

# 3. 查看所有可用命令
just --list
```

#### 📜 传统方式：使用脚本

```bash
# 运行自动化设置脚本
bash scripts/setup.sh
```

这将自动完成：
1. ✅ 检查所有依赖（Node.js, Python, Docker, Git）
2. ✅ 安装 pnpm 依赖
3. ✅ 创建 Python 虚拟环境（使用 uv）
4. ✅ 配置 pre-commit hooks
5. ✅ 创建环境变量文件
6. ✅ 启动基础设施服务（PostgreSQL, Redis）
7. ✅ 运行数据库迁移

### 启动开发环境

```bash
# 方式 1: 使用 just (推荐)
just dev

# 方式 2: 使用 pnpm
pnpm dev

# 方式 3: 使用 make
make dev
```

**访问应用**:
- 🎨 Frontend: http://localhost:3000
- 🚀 Backend API: http://localhost:8000
- 📚 API Docs: http://localhost:8000/docs
- 📊 Grafana: http://localhost:3001 (admin/admin)
- 🔍 Jaeger: http://localhost:16686

## 📁 项目结构

```
<project_slug>/
├── .github/                    # GitHub Actions CI/CD
│   ├── workflows/
│   │   ├── ci-cd.yml          # 主 CI/CD 流水线
│   │   └── dependabot.yml     # 依赖自动更新
│   └── ISSUE_TEMPLATE/        # Issue 模板
├── docs/                       # 项目文档
│   ├── adr/                   # 架构决策记录
│   ├── setup-guide.md         # 环境搭建指南
│   └── deployment.md          # 部署手册
├── infra/                     # 基础设施配置
│   ├── docker-compose/        # Docker Compose 配置
│   │   ├── dev.yml           # 开发环境 (PostgreSQL, Redis, MinIO)
│   │   ├── monitoring.yml    # 监控套件 (Prometheus, Grafana, Loki, Jaeger)
│   │   ├── prometheus/       # Prometheus 配置
│   │   ├── loki/             # Loki 配置
│   │   └── promtail/         # Promtail 配置
│   ├── kubernetes/            # Kubernetes 部署
│   │   ├── helm-charts/      # Helm Charts
│   │   │   ├── backend/      # 后端服务 Chart (Deployment, Service, Ingress, HPA)
│   │   │   └── frontend/     # 前端服务 Chart
│   │   └── core-infra/       # 核心基础设施
│   │       ├── namespace.yaml
│   │       ├── postgres.yaml
│   │       ├── redis.yaml
│   │       ├── secrets.yaml
│   │       ├── configmap.yaml
│   │       ├── cert-manager.yaml
│   │       └── network-policies.yaml
│   └── tofu/                  # OpenTofu (Terraform) AWS 基础设施
│       ├── main.tf           # 主配置
│       ├── vpc.tf            # VPC 网络
│       ├── eks.tf            # EKS 集群
│       ├── rds.tf            # RDS 数据库
│       ├── elasticache.tf    # Redis 集群
│       ├── s3.tf             # S3 存储
│       └── README.md
├── packages/                  # 共享包 (Monorepo)
│   ├── shared-types/         # TypeScript 类型定义
│   ├── ui-kit/               # Vue UI 组件库 (Button, Card, etc.)
│   ├── eslint-config-custom/ # 共享 ESLint 配置
│   └── tsconfig-custom/      # 共享 TypeScript 配置
├── scripts/                   # 项目脚本
│   ├── setup.sh              # 自动化设置
│   ├── codegen.sh            # 类型生成
│   └── db-backup.sh          # 数据库备份
├── services/                  # 所有微服务
│   ├── backend/              # FastAPI 后端 ✅
│   ├── frontend/             # Nuxt 前端 ✅
│   ├── ml-api/               # ML API ✅
│   ├── audio-api/            # Audio API ✅
│   └── scraper/              # 爬虫 ✅
├── data/                      # 数据目录
│   ├── raw/                  # 原始数据
│   └── processed/            # 处理后的数据
├── .gitignore                # Git 忽略配置
├── .dockerignore             # Docker 忽略配置
├── .pre-commit-config.yaml   # Pre-commit hooks
├── .prettierrc               # Prettier 配置
├── .editorconfig             # EditorConfig 配置
├── docker-compose.yml         # 完整应用栈
├── justfile                  # Just 任务运行器 (50+ 命令)
├── Makefile                  # Make 兼容
├── package.json              # pnpm workspace 根配置
├── pnpm-workspace.yaml       # pnpm workspace 配置
├── pyproject.toml            # Python 根配置
├── tsconfig.base.json        # TypeScript 基础配置
├── turbo.json                # Turborepo 配置
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

> 📖 **详细结构说明**: 查看生成项目中的 `PROJECT_STRUCTURE.md` 获取完整的目录结构和说明

## 📖 文档

### 核心文档

- [使用指南](使用指南.md) - **从这里开始！**
- [环境搭建]({{ cookiecutter.project_slug }}/docs/setup-guide.md)
- [部署手册]({{ cookiecutter.project_slug }}/docs/deployment.md)
- [架构决策]({{ cookiecutter.project_slug }}/docs/adr/)
- [贡献指南]({{ cookiecutter.project_slug }}/CONTRIBUTING.md)

### 服务文档

- [Backend README]({{ cookiecutter.project_slug }}/services/backend/README.md)
- [Frontend README]({{ cookiecutter.project_slug }}/services/frontend/README.md)

## 🛠️ 开发指南

### ⚡ 常用 Just 命令

```bash
# 开发相关
just init              # 初始化项目
just dev               # 启动开发环境
just dev-down          # 停止开发环境

# 构建相关
just build             # 构建所有服务
just docker-build      # 构建 Docker 镜像
just docker-push       # 推送镜像到仓库

# 测试相关
just test              # 运行所有测试
just test-cov          # 测试 + 覆盖率报告

# 代码质量
just lint              # 运行 linters
just lint-fix          # 自动修复 lint 问题
just format            # 格式化代码
just typecheck         # 类型检查

# 数据库操作
just db-migrate name="add_users"  # 创建迁移
just db-upgrade        # 应用迁移
just db-downgrade      # 回滚迁移
just db-reset          # 重置数据库
just db-backup         # 备份数据库

# Kubernetes 部署
just k8s-apply         # 应用 K8s 配置
just k8s-deploy        # 部署到 K8s
just k8s-status        # 查看状态

# Terraform 操作
just tf-init           # 初始化 Terraform
just tf-plan           # 查看执行计划
just tf-apply          # 应用变更

# 监控
just monitoring-up     # 启动监控套件
just monitoring-down   # 停止监控

# 查看所有命令
just --list
```

### 添加新功能

```bash
# 1. 在 backend 添加新端点
cd services/backend/src/<package_name>/features
mkdir new_feature
# 创建 router.py, schemas.py, services.py

# 2. 注册路由
# 在 api/v1/router.py 中导入并注册

# 3. 生成 TypeScript 类型
just codegen
# 或
pnpm codegen

# 4. 在 frontend 使用新类型
# import type { NewFeature } from '@project/shared-types'
```

### 运行测试

```bash
# 使用 Just (推荐)
just test              # 所有测试
just test-cov          # 测试 + 覆盖率

# 使用 pnpm
pnpm test              # 所有测试
pnpm test:backend      # Backend 测试
pnpm test:frontend     # Frontend 测试
pnpm test:e2e          # E2E 测试
```

### 代码质量检查

```bash
# 完整检查流程
just lint              # Lint 检查
just typecheck         # 类型检查
just format            # 格式化代码

# 自动修复
just lint-fix          # 自动修复 lint 问题

# 模拟 CI 流程
just ci                # 运行 lint + typecheck + test + build
```

## 🐳 部署

### 本地开发环境

```bash
# 使用 Just (推荐)
just dev

# 使用 Docker Compose
docker-compose -f infra/docker-compose/dev.yml up -d

# 启动监控
just monitoring-up
```

### Kubernetes 部署

#### 1. 部署核心基础设施

```bash
# 应用核心配置（命名空间、数据库、Redis 等）
kubectl apply -f infra/kubernetes/core-infra/

# 或使用 Just
just k8s-apply
```

#### 2. 使用 Helm 部署服务

```bash
# 部署后端
helm install backend ./infra/kubernetes/helm-charts/backend \
  --namespace {{ cookiecutter.kubernetes_namespace }} \
  --values ./infra/kubernetes/helm-charts/backend/values.yaml

# 部署前端
helm install frontend ./infra/kubernetes/helm-charts/frontend \
  --namespace {{ cookiecutter.kubernetes_namespace }}

# 或使用 Just
just k8s-deploy
```

#### 3. 查看部署状态

```bash
# 查看 pods
kubectl get pods -n {{ cookiecutter.kubernetes_namespace }}

# 查看服务
kubectl get svc -n {{ cookiecutter.kubernetes_namespace }}

# 或使用 Just
just k8s-status
```

### AWS 云部署 (OpenTofu/Terraform)

#### 1. 初始化 Terraform

```bash
cd infra/tofu

# 初始化
tofu init

# 或使用 Just
just tf-init
```

#### 2. 创建 AWS 基础设施

```bash
# 查看执行计划
tofu plan

# 应用变更（创建 VPC, EKS, RDS, Redis, S3 等）
tofu apply

# 或使用 Just
just tf-plan
just tf-apply
```

#### 3. 配置 kubectl

```bash
# 获取 EKS 凭证
aws eks update-kubeconfig --region us-west-2 --name {{ cookiecutter.project_slug }}-cluster

# 验证连接
kubectl get nodes
```

#### 4. 部署应用到 EKS

```bash
# 应用核心配置
kubectl apply -f infra/kubernetes/core-infra/

# 部署服务
helm install backend ./infra/kubernetes/helm-charts/backend
helm install frontend ./infra/kubernetes/helm-charts/frontend
```

### 成本估算 (AWS)

基础配置月成本约 **$633-873**:
- EKS 集群: $73
- EC2 实例: $190-430 (含 GPU)
- RDS PostgreSQL: $120
- ElastiCache Redis: $100
- NAT Gateway: $100
- 数据传输: $50

详见 [infra/tofu/README.md]({{ cookiecutter.project_slug }}/infra/tofu/README.md)

### 更多部署选项

查看 [部署手册]({{ cookiecutter.project_slug }}/docs/deployment.md) 获取：
- 生产环境配置
- CI/CD 流水线
- 监控和告警设置
- 备份和恢复策略
- 安全最佳实践

## 📊 已完成功能

### ✅ 已实现（100% 完整）

#### 核心架构
- [x] Monorepo 结构 (pnpm workspace + Turborepo)
- [x] 完整的项目配置文件 (.gitignore, .editorconfig, .prettierrc, etc.)
- [x] Pre-commit hooks (Ruff, ESLint, Prettier, MyPy)
- [x] GitHub CI/CD 工作流

#### 服务实现
- [x] **Backend** - FastAPI 完整实现 (Auth, Health, Users)
- [x] **Frontend** - Nuxt 3 完整实现 (SSR, Pinia, TypeScript)
- [x] **ML API** - YOLOv8 目标检测服务
- [x] **Audio API** - Whisper 语音识别服务
- [x] **Scraper** - Scrapy 爬虫服务

#### 共享包
- [x] **shared-types** - TypeScript 类型定义
- [x] **ui-kit** - Vue 组件库 (Button, Card, 工具函数)
- [x] **eslint-config-custom** - 共享 ESLint 配置
- [x] **tsconfig-custom** - 共享 TypeScript 配置

#### 基础设施
- [x] Docker Compose 开发环境 (PostgreSQL, Redis, MinIO)
- [x] 监控套件 (Prometheus, Grafana, Loki, Jaeger, Promtail)
- [x] **Kubernetes Helm Charts** (Backend + Frontend 完整配置)
- [x] **Kubernetes 核心基础设施** (PostgreSQL, Redis, Secrets, ConfigMap, Cert-Manager, NetworkPolicies)
- [x] **OpenTofu/Terraform AWS IaC** (VPC, EKS, RDS, ElastiCache, S3, IAM)

#### 自动化工具
- [x] **Justfile** - 50+ 任务命令
- [x] **Makefile** - 传统 Make 支持
- [x] setup.sh - 自动化环境设置
- [x] codegen.sh - TypeScript 类型生成
- [x] db-backup.sh - 数据库备份

#### 文档
- [x] 完整的 README 和使用指南
- [x] 环境搭建指南
- [x] 部署手册
- [x] 架构决策记录 (ADR)
- [x] 项目结构文档

## 🤝 贡献

欢迎贡献！请查看 [CONTRIBUTING.md]({{ cookiecutter.project_slug }}/CONTRIBUTING.md)

## 📄 许可证

MIT License - 详见 [LICENSE]({{ cookiecutter.project_slug }}/LICENSE)

## 👨‍💻 作者

{{ cookiecutter.author_name }} - {{ cookiecutter.author_email }}

## 🙏 致谢

感谢所有使用的开源项目！

---

## 🎓 相关资源

### 官方文档

- [FastAPI](https://fastapi.tiangolo.com/)
- [Nuxt](https://nuxt.com/)
- [Turbo](https://turbo.build/)
- [pnpm](https://pnpm.io/)
- [Docker](https://docs.docker.com/)
- [Kubernetes](https://kubernetes.io/docs/)

### 教程和指南

- [Monorepo 最佳实践](https://monorepo.tools/)
- [FastAPI 完整教程](https://fastapi.tiangolo.com/tutorial/)
- [Nuxt 3 文档](https://nuxt.com/docs)
- [Kubernetes 实战](https://kubernetes.io/docs/tutorials/)

---

## 🔧 技术栈详情

### 前端技术
- **框架**: Nuxt 3.8+ (Vue 3 + Vite)
- **UI**: Tailwind CSS + UI Kit 组件库
- **状态**: Pinia
- **类型**: TypeScript 5.3+
- **工具**: ESLint + Prettier

### 后端技术
- **框架**: FastAPI 0.104+
- **ORM**: SQLModel (SQLAlchemy 2.0)
- **迁移**: Alembic
- **任务队列**: ARQ (Redis-based)
- **验证**: Pydantic V2
- **工具**: Ruff + MyPy

### AI/ML 技术
- **目标检测**: YOLOv8 (Ultralytics)
- **语音识别**: Whisper (OpenAI)
- **加速**: CUDA (可选)

### DevOps 技术
- **容器**: Docker + Docker Compose
- **编排**: Kubernetes + Helm
- **IaC**: OpenTofu (Terraform)
- **CI/CD**: GitHub Actions
- **监控**: Prometheus + Grafana + Loki + Jaeger

### 数据库 & 存储
- **关系型**: PostgreSQL 16
- **缓存**: Redis 7
- **对象存储**: MinIO (S3 兼容)

---

## 📝 快速参考

### 环境要求
```bash
Python: 3.11.9
Node.js: 20.x
pnpm: 8.x
Docker: 24.x+
uv: latest
```

### 端口映射
| 服务 | 端口 | 说明 |
|-----|------|-----|
| Frontend | 3000 | Nuxt 应用 |
| Backend | 8000 | FastAPI |
| PostgreSQL | 5432 | 数据库 |
| Redis | 6379 | 缓存 |
| MinIO | 9000 | 对象存储 |
| Grafana | 3001 | 监控面板 |
| Prometheus | 9090 | 指标收集 |
| Jaeger | 16686 | 链路追踪 |

### 环境变量
主要环境变量（`.env` 文件）：
```bash
# 数据库
DATABASE_URL=postgresql://user:pass@localhost:5432/db

# Redis
REDIS_URL=redis://localhost:6379/0

# JWT
SECRET_KEY=your-secret-key

# AWS (可选)
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
```

---

## ⚠️ 重要提示

这是一个**生产级模板项目**，包含了完整的配置和示例代码。使用前请：

### 必做事项 ✅
1. 🔒 **修改所有密钥和密码**（数据库、Redis、JWT Secret 等）
2. 🏷️ **更新项目信息**（名称、作者、许可证）
3. 🔐 **配置 Secrets Manager**（生产环境使用 AWS Secrets Manager 或 Vault）
4. 📊 **设置监控告警**（Grafana Alerts）
5. 🔄 **配置 CI/CD**（GitHub Actions Secrets）

### 安全检查 🔐
```bash
# 安全审计
just security-audit

# 扫描 Docker 镜像
just security-scan-docker

# 检查敏感信息泄露
git secrets --scan
```

### 成本优化 💰
- 使用 Spot Instances 降低 EC2 成本
- 配置自动扩缩容（HPA + Cluster Autoscaler）
- 启用 S3 生命周期策略
- 使用 VPC Endpoints 减少数据传输费用

---

**🚀 开始您的企业级全栈 AI 应用开发之旅！**

有问题？查看 [使用指南](使用指南.md) 或提交 Issue。
