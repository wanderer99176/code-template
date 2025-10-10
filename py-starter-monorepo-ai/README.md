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

- ✅ **Monorepo 架构**: pnpm workspace（高效的工作空间）+ Turborepo（智能增量构建，缓存优化）
- ✅ **类型安全**: 端到端类型支持，自动生成共享类型（从 FastAPI OpenAPI 到 TypeScript）
- ✅ **代码质量**: Ruff（比 Pylint 快 100 倍）+ ESLint + Prettier + Pre-commit Hooks（提交前自动检查）
- ✅ **快速工具**: `uv`（比 pip 快 10-100 倍）+ `pnpm`（比 npm 快 2 倍，节省 50% 磁盘空间）
- ✅ **任务运行**: Justfile（50+ 命令，比 Makefile 更现代）+ Makefile 兼容（传统工具支持）
- ✅ **文档完善**: API 文档（自动生成 OpenAPI/Swagger）+ ADR 架构决策记录 + 详细部署指南

### 🚀 生产就绪

- ✅ **云原生**: 完整的 Kubernetes Helm Charts（生产级配置）+ HPA 自动扩缩容（基于 CPU/内存）
- ✅ **IaC**: OpenTofu/Terraform AWS 基础设施代码（一键部署 VPC、EKS、RDS、ElastiCache、S3 等）
- ✅ **CI/CD**: GitHub Actions 流水线（自动化测试、构建、部署）+ 多环境支持（dev/staging/prod）
- ✅ **安全**: Kubernetes 网络策略 + IRSA（IAM 角色）+ Secrets Manager + SSL/TLS 自动证书
- ✅ **可观测性**: 结构化日志（JSON 格式）+ Metrics（Prometheus）+ Tracing（Jaeger）+ Alerts（告警规则）

## 📦 包含的服务

### 核心服务

1. **Backend (FastAPI)** ✅ 完整实现
   - RESTful API（符合 REST 规范的 API 接口）
   - JWT 认证（JSON Web Token 身份验证）
   - SQLModel ORM（类型安全的数据库操作）
   - Alembic 迁移（数据库版本控制和迁移）
   - ARQ 异步任务（基于 Redis 的后台任务队列）
   - Redis 缓存（高性能缓存层）

2. **Frontend (Nuxt)** ✅ 完整实现
   - SSR/SSG 支持（服务端渲染/静态站点生成）
   - Nuxt UI 组件库（开箱即用的 UI 组件）
   - Pinia 状态管理（Vue 官方推荐的状态管理）
   - TypeScript（完整的类型支持）

3. **ML API (YOLOv8)** ✅ 完整实现
   - 目标检测（实时物体识别和定位）
   - GPU 加速（CUDA 加速推理）
   - 模型管理（模型版本控制和热更新）

4. **Audio API (Whisper)** ✅ 完整实现
   - 语音转文字（高精度语音识别）
   - 多语言支持（支持 100+ 种语言）
   - 实时处理（流式音频处理）

5. **Scraper (Scrapy)** ✅ 完整实现
   - 分布式爬取（支持大规模并发爬取）
   - 反爬虫策略（User-Agent 轮换、代理池等）
   - 数据清洗（自动化数据提取和清洗）

### 基础设施

- **PostgreSQL**: 主数据库（关系型数据持久化存储）
- **Redis**: 缓存 + 消息队列（高性能键值存储和任务队列）
- **MinIO**: 对象存储（S3 兼容的文件存储服务）
- **Prometheus**: 指标收集（时序数据库，收集应用指标）
- **Grafana**: 可视化（监控数据可视化仪表板）
- **Loki**: 日志聚合（类 Prometheus 的日志系统）
- **Jaeger**: 分布式追踪（微服务调用链路追踪）

## 🚀 快速开始

### 前置要求

确保已安装以下工具（括号内为推荐安装方式）：

- **Python**: 3.11.9（使用 pyenv 或官方安装包）
- **Node.js**: 20.x（使用 nvm 或官方安装包）
- **pnpm**: 8.x（`npm install -g pnpm` 或 `brew install pnpm`）
- **uv**: 最新版本（`pip install uv` 或 `brew install uv`）
- **Docker**: 最新版本（Docker Desktop 或 Docker Engine）
- **Git**: 最新版本（版本控制系统）

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
├── .github/                    # GitHub 配置目录
│   ├── workflows/              # GitHub Actions 工作流目录
│   │   ├── ci-cd.yml          # 主 CI/CD 流水线（测试、构建、部署自动化）
│   │   └── dependabot.yml     # Dependabot 配置（自动更新依赖并创建 PR）
│   ├── ISSUE_TEMPLATE/        # Issue 模板目录
│   │   ├── bug_report.md      # Bug 报告模板（统一问题反馈格式）
│   │   └── feature_request.md # 功能请求模板（统一需求提交格式）
│   └── pull_request_template.md # PR 模板（统一代码审查格式）
│
├── docs/                       # 项目文档目录
│   ├── adr/                   # 架构决策记录（Architecture Decision Records）
│   │   ├── 001-monorepo-architecture.md  # 为什么选择 Monorepo 架构
│   │   └── README.md          # ADR 索引和说明
│   ├── setup-guide.md         # 环境搭建指南（详细的开发环境配置步骤）
│   └── deployment.md          # 部署手册（生产环境部署完整指南）
│
├── infra/                     # 基础设施即代码（Infrastructure as Code）
│   ├── docker-compose/        # Docker Compose 编排配置
│   │   ├── dev.yml           # 开发环境（PostgreSQL, Redis, MinIO, Mailhog）
│   │   ├── monitoring.yml    # 监控套件（Prometheus, Grafana, Loki, Jaeger, Promtail）
│   │   ├── prometheus/       # Prometheus 配置目录
│   │   │   └── prometheus.yml # Prometheus 抓取配置（定义监控目标和规则）
│   │   ├── loki/             # Loki 日志系统配置
│   │   │   └── local-config.yaml # Loki 本地配置（日志存储和查询设置）
│   │   └── promtail/         # Promtail 日志采集器配置
│   │       └── config.yml    # Promtail 配置（定义日志采集源和标签）
│   │
│   ├── kubernetes/            # Kubernetes 生产部署配置
│   │   ├── helm-charts/      # Helm Charts 包管理
│   │   │   ├── backend/      # 后端服务 Helm Chart
│   │   │   │   ├── Chart.yaml          # Chart 元数据（名称、版本、描述）
│   │   │   │   ├── values.yaml         # 默认配置值（副本数、资源限制等）
│   │   │   │   └── templates/          # Kubernetes 资源模板
│   │   │   │       ├── _helpers.tpl    # 模板辅助函数（标签、名称生成）
│   │   │   │       ├── deployment.yaml # Deployment 资源（Pod 部署配置）
│   │   │   │       ├── service.yaml    # Service 资源（服务发现和负载均衡）
│   │   │   │       ├── ingress.yaml    # Ingress 资源（外部访问和 HTTPS）
│   │   │   │       └── hpa.yaml        # HPA 资源（水平自动扩缩容）
│   │   │   └── frontend/     # 前端服务 Helm Chart（结构同 backend）
│   │   │
│   │   └── core-infra/       # 核心基础设施 Kubernetes 配置
│   │       ├── namespace.yaml         # 命名空间（资源隔离和组织）
│   │       ├── postgres.yaml          # PostgreSQL 数据库（StatefulSet + PVC）
│   │       ├── redis.yaml             # Redis 缓存（StatefulSet + PVC）
│   │       ├── secrets.yaml           # 密钥管理（数据库密码、API 密钥等）
│   │       ├── configmap.yaml         # 配置管理（环境变量、应用配置）
│   │       ├── cert-manager.yaml      # Cert-Manager 配置（自动 HTTPS 证书）
│   │       └── network-policies.yaml  # 网络策略（Pod 间通信安全控制）
│   │
│   └── tofu/                  # OpenTofu (Terraform) AWS 云基础设施
│       ├── main.tf           # 主配置文件（Provider 和 Backend 配置）
│       ├── variables.tf      # 变量定义（可配置参数，如区域、实例类型）
│       ├── outputs.tf        # 输出值（集群端点、数据库地址等）
│       ├── vpc.tf            # VPC 网络配置（子网、路由表、NAT Gateway）
│       ├── eks.tf            # EKS 集群配置（Kubernetes 控制平面和节点组）
│       ├── rds.tf            # RDS 数据库配置（PostgreSQL Multi-AZ）
│       ├── elasticache.tf    # ElastiCache 配置（Redis 集群）
│       ├── s3.tf             # S3 存储桶配置（应用数据和 ML 模型存储）
│       └── README.md         # Terraform 使用指南（部署步骤和成本估算）
│
├── packages/                  # 共享包目录（Monorepo 内部复用）
│   ├── shared-types/         # TypeScript 共享类型定义
│   │   ├── index.ts          # 类型导出入口（API 响应、请求类型等）
│   │   ├── package.json      # 包配置（依赖和构建脚本）
│   │   ├── tsconfig.json     # TypeScript 配置
│   │   └── README.md         # 包使用说明
│   │
│   ├── ui-kit/               # Vue UI 组件库
│   │   ├── src/
│   │   │   ├── components/   # UI 组件目录
│   │   │   │   ├── Button.vue # 按钮组件（可复用的按钮样式）
│   │   │   │   └── Card.vue   # 卡片组件（容器组件）
│   │   │   ├── utils/        # 工具函数
│   │   │   │   ├── colors.ts  # 颜色工具（Hex/RGB 转换等）
│   │   │   │   └── formatters.ts # 格式化工具（货币、日期、文件大小）
│   │   │   └── index.ts      # 组件库导出入口
│   │   ├── package.json      # 包配置
│   │   ├── tsconfig.json     # TypeScript 配置
│   │   └── README.md         # 组件库使用文档
│   │
│   ├── eslint-config-custom/ # 共享 ESLint 配置包
│   │   ├── index.js          # ESLint 规则配置（代码风格统一）
│   │   └── package.json      # 包配置
│   │
│   └── tsconfig-custom/      # 共享 TypeScript 配置包
│       ├── base.json         # 基础 TS 配置（严格模式、路径别名等）
│       └── package.json      # 包配置
│
├── scripts/                   # 项目自动化脚本
│   ├── setup.sh              # 环境初始化脚本（检查依赖、安装、配置）
│   ├── codegen.sh            # 类型生成脚本（OpenAPI → TypeScript）
│   └── db-backup.sh          # 数据库备份脚本（自动备份到 S3）
│
├── services/                  # 微服务目录
│   ├── backend/              # FastAPI 后端 API 服务 ✅
│   │   ├── src/              # 源代码目录
│   │   │   └── <package_name>/
│   │   │       ├── __init__.py      # 包初始化
│   │   │       ├── main.py          # FastAPI 应用入口
│   │   │       ├── api/             # API 路由层
│   │   │       │   └── v1/          # API v1 版本
│   │   │       │       ├── router.py         # 路由聚合
│   │   │       │       └── endpoints/        # 端点实现
│   │   │       │           ├── auth.py       # 认证端点（登录、注册）
│   │   │       │           ├── users.py      # 用户端点（CRUD）
│   │   │       │           └── health.py     # 健康检查端点
│   │   │       ├── core/            # 核心功能模块
│   │   │       │   ├── config.py    # 配置管理（环境变量、设置）
│   │   │       │   └── logging.py   # 日志配置（结构化日志）
│   │   │       └── db/              # 数据库层
│   │   │           ├── base.py      # 数据库基类和元数据
│   │   │           └── session.py   # 数据库会话管理
│   │   ├── Dockerfile        # Docker 镜像构建文件
│   │   ├── pyproject.toml    # Python 项目配置（依赖、工具设置）
│   │   └── README.md         # 后端服务文档
│   │
│   ├── frontend/             # Nuxt.js 前端应用 ✅
│   │   ├── pages/            # 页面目录（自动路由）
│   │   │   └── index.vue     # 首页组件
│   │   ├── app.vue           # 根组件（全局布局）
│   │   ├── nuxt.config.ts    # Nuxt 配置（模块、插件、运行时）
│   │   ├── Dockerfile        # Docker 镜像构建文件
│   │   ├── package.json      # 前端依赖配置
│   │   └── README.md         # 前端服务文档
│   │
│   ├── ml-api/               # YOLOv8 机器学习 API 服务 ✅
│   │   ├── src/              # 源代码目录
│   │   │   └── main.py       # FastAPI ML 服务（目标检测接口）
│   │   └── pyproject.toml    # Python 项目配置（含 YOLOv8 依赖）
│   │
│   ├── audio-api/            # Whisper 语音识别 API 服务 ✅
│   │   ├── src/              # 源代码目录
│   │   │   └── main.py       # FastAPI Audio 服务（语音转文字接口）
│   │   └── pyproject.toml    # Python 项目配置（含 Whisper 依赖）
│   │
│   └── scraper/              # Scrapy 网络爬虫服务 ✅
│       ├── <scraper_name>/   # Scrapy 项目目录
│       │   ├── spiders/      # 爬虫脚本目录
│       │   │   └── example_spider.py # 示例爬虫（可复制修改）
│       │   └── settings.py   # Scrapy 配置（中间件、管道、并发）
│       ├── scrapy.cfg        # Scrapy 项目配置
│       └── README.md         # 爬虫服务文档
│
├── data/                      # 数据目录（用于本地数据处理）
│   ├── raw/                  # 原始数据目录（爬取或导入的原始数据）
│   │   └── .gitkeep          # 保持目录存在的占位文件
│   └── processed/            # 处理后数据目录（清洗、转换后的数据）
│       └── .gitkeep          # 保持目录存在的占位文件
│
├── .gitignore                # Git 忽略文件配置（排除 node_modules, __pycache__ 等）
├── .dockerignore             # Docker 构建忽略配置（减小镜像体积）
├── .pre-commit-config.yaml   # Pre-commit hooks 配置（提交前自动检查代码质量）
├── .prettierrc               # Prettier 配置（代码格式化规则）
├── .editorconfig             # EditorConfig 配置（统一编辑器设置）
├── docker-compose.yml         # Docker Compose 主配置（完整应用栈编排）
├── justfile                  # Just 任务运行器（50+ 个开发、部署、维护命令）
├── Makefile                  # Make 兼容文件（传统构建工具支持）
├── package.json              # pnpm workspace 根配置（工作空间和脚本）
├── pnpm-workspace.yaml       # pnpm workspace 配置（定义工作空间包）
├── pyproject.toml            # Python 根项目配置（全局 Python 工具设置）
├── tsconfig.base.json        # TypeScript 基础配置（所有 TS 项目继承）
├── turbo.json                # Turborepo 配置（增量构建和缓存策略）
├── CHANGELOG.md              # 变更日志（版本更新记录）
├── CONTRIBUTING.md           # 贡献指南（如何参与项目开发）
├── LICENSE                   # 开源许可证（MIT License）
└── README.md                 # 项目主文档（项目概览和快速开始）
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
# 应用核心配置（命名空间、数据库、Redis、Secrets、ConfigMap 等）
kubectl apply -f infra/kubernetes/core-infra/

# 或使用 Just 命令（推荐）
just k8s-apply

# 验证核心服务状态
kubectl get all -n {{ cookiecutter.kubernetes_namespace }}
```

**包含的核心资源**:
- Namespace（命名空间隔离）
- PostgreSQL StatefulSet（有状态数据库，持久化存储）
- Redis StatefulSet（缓存服务，持久化存储）
- Secrets（敏感信息，如数据库密码）
- ConfigMap（配置信息）
- Cert-Manager ClusterIssuer（自动 SSL/TLS 证书）
- NetworkPolicies（网络安全策略）

#### 2. 使用 Helm 部署服务

```bash
# 部署后端服务（包含 Deployment、Service、Ingress、HPA）
helm install backend ./infra/kubernetes/helm-charts/backend \
  --namespace {{ cookiecutter.kubernetes_namespace }} \
  --values ./infra/kubernetes/helm-charts/backend/values.yaml

# 部署前端服务
helm install frontend ./infra/kubernetes/helm-charts/frontend \
  --namespace {{ cookiecutter.kubernetes_namespace }}

# 或使用 Just 命令一键部署所有服务
just k8s-deploy
```

**Helm Chart 功能**:
- 自动创建 Deployment（应用部署）
- Service（服务发现）
- Ingress（外部访问，自动配置 HTTPS）
- HPA（水平自动扩缩容，2-10 副本）
- 健康检查（Liveness 和 Readiness Probe）
- 资源限制（CPU 和内存限制）

#### 3. 查看部署状态

```bash
# 查看所有 Pods（运行中的容器）
kubectl get pods -n {{ cookiecutter.kubernetes_namespace }}

# 查看服务（Service 和 Endpoints）
kubectl get svc -n {{ cookiecutter.kubernetes_namespace }}

# 查看 Ingress（外部访问入口）
kubectl get ingress -n {{ cookiecutter.kubernetes_namespace }}

# 查看 HPA 自动扩缩容状态
kubectl get hpa -n {{ cookiecutter.kubernetes_namespace }}

# 或使用 Just 命令一键查看
just k8s-status

# 查看 Pod 日志（排查问题）
kubectl logs -f deployment/backend -n {{ cookiecutter.kubernetes_namespace }}
```

### AWS 云部署 (OpenTofu/Terraform)

#### 1. 初始化 Terraform

```bash
cd infra/tofu

# 初始化 Terraform（下载 provider 插件）
tofu init

# 或使用 Just 命令
just tf-init
```

**初始化步骤**:
- 下载 AWS Provider（与 AWS API 交互）
- 配置 S3 后端（存储 Terraform 状态文件）
- 设置 DynamoDB 锁（防止并发修改）

#### 2. 创建 AWS 基础设施

```bash
# 查看执行计划（预览将要创建的资源，不会实际创建）
tofu plan

# 应用变更（实际创建基础设施）
# 将创建: VPC、EKS 集群、RDS 数据库、ElastiCache、S3 等
tofu apply

# 或使用 Just 命令
just tf-plan    # 查看计划
just tf-apply   # 应用变更
```

**创建的 AWS 资源**（约 15-20 分钟）:
- **网络层**: VPC、子网（公有/私有/数据库）、NAT Gateway、VPC Endpoints
- **计算层**: EKS 集群、Node Groups（一般节点 + GPU 节点）、Cluster Autoscaler
- **数据层**: RDS PostgreSQL（Multi-AZ）、ElastiCache Redis（集群模式）
- **存储层**: S3 存储桶（应用数据 + ML 模型）
- **安全层**: IAM 角色（IRSA）、Security Groups、Secrets Manager

#### 3. 配置 kubectl

```bash
# 获取 EKS 集群凭证（配置 kubeconfig）
aws eks update-kubeconfig --region us-west-2 --name {{ cookiecutter.project_slug }}-cluster

# 验证集群连接
kubectl get nodes

# 查看节点详情
kubectl describe nodes
```

#### 4. 部署应用到 EKS

```bash
# 应用核心基础设施配置
kubectl apply -f infra/kubernetes/core-infra/

# 使用 Helm 部署后端和前端服务
helm install backend ./infra/kubernetes/helm-charts/backend
helm install frontend ./infra/kubernetes/helm-charts/frontend

# 或使用 Just 命令一键部署
just k8s-apply
just k8s-deploy

# 获取 Ingress 地址（应用访问地址）
kubectl get ingress -n {{ cookiecutter.kubernetes_namespace }}
```

**部署后验证**:
```bash
# 检查所有 Pods 是否运行
kubectl get pods -n {{ cookiecutter.kubernetes_namespace }}

# 检查服务状态
kubectl get svc -n {{ cookiecutter.kubernetes_namespace }}

# 查看应用日志
kubectl logs -f deployment/backend -n {{ cookiecutter.kubernetes_namespace }}
```

### 成本估算 (AWS)

基础配置月成本约 **$633-873**（us-west-2 区域）:
- **EKS 集群**: $73（控制平面固定费用）
- **EC2 实例**: $190-430（含可选的 GPU 节点）
  - 一般节点: 3 × t3.large @ ~$63/月
  - GPU 节点: 1 × g4dn.xlarge @ ~$240/月（可选）
- **RDS PostgreSQL**: $120（db.t3.medium Multi-AZ）
- **ElastiCache Redis**: $100（cache.t3.medium × 2 节点）
- **NAT Gateway**: $100（3 个可用区，每个 ~$33/月）
- **数据传输**: $50（估算值，实际取决于流量）
- **其他**: EBS 存储、S3、CloudWatch 日志等

> 💡 **成本优化建议**：开发/测试环境可使用单 AZ、关闭 GPU、使用 Spot 实例等方式降低成本至 $300-400/月

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
- **框架**: Nuxt 3.8+（基于 Vue 3 + Vite 的全栈框架）
- **UI**: Tailwind CSS（实用优先的 CSS 框架）+ UI Kit 组件库（自定义 Vue 组件）
- **状态**: Pinia（Vue 官方状态管理库）
- **类型**: TypeScript 5.3+（静态类型检查）
- **工具**: ESLint（代码检查）+ Prettier（代码格式化）

### 后端技术
- **框架**: FastAPI 0.104+（高性能 Python Web 框架）
- **ORM**: SQLModel（结合 Pydantic 和 SQLAlchemy 的 ORM）
- **迁移**: Alembic（数据库迁移工具）
- **任务队列**: ARQ（基于 Redis 的异步任务队列）
- **验证**: Pydantic V2（数据验证和序列化）
- **工具**: Ruff（极速 Python Linter）+ MyPy（静态类型检查）

### AI/ML 技术
- **目标检测**: YOLOv8（Ultralytics 最新目标检测模型）
- **语音识别**: Whisper（OpenAI 开源语音识别模型）
- **加速**: CUDA（NVIDIA GPU 加速，可选）

### DevOps 技术
- **容器**: Docker（容器化）+ Docker Compose（本地编排）
- **编排**: Kubernetes（生产环境容器编排）+ Helm（K8s 包管理器）
- **IaC**: OpenTofu（开源 Terraform 分支，基础设施即代码）
- **CI/CD**: GitHub Actions（持续集成/持续部署）
- **监控**: Prometheus（指标）+ Grafana（可视化）+ Loki（日志）+ Jaeger（追踪）

### 数据库 & 存储
- **关系型**: PostgreSQL 16（最新版关系型数据库）
- **缓存**: Redis 7（内存数据库，缓存和消息队列）
- **对象存储**: MinIO（开源 S3 兼容对象存储）

---

## 📝 快速参考

### 环境要求
```bash
Python: 3.11.9          # Python 运行环境（后端、AI 服务）
Node.js: 20.x           # Node.js 运行环境（前端）
pnpm: 8.x               # JavaScript 包管理器（快速、节省空间）
Docker: 24.x+           # 容器运行环境
uv: latest              # Python 包管理器（替代 pip，更快）
```

### 端口映射
| 服务 | 端口 | 说明 |
|-----|------|-----|
| Frontend | 3000 | Nuxt 前端应用 |
| Backend API | 8000 | FastAPI 后端服务 |
| PostgreSQL | 5432 | 主数据库 |
| Redis | 6379 | 缓存和消息队列 |
| MinIO | 9000 | 对象存储服务 |
| MinIO Console | 9001 | MinIO 管理控制台 |
| Grafana | 3001 | 监控可视化面板 |
| Prometheus | 9090 | 指标数据收集 |
| Jaeger UI | 16686 | 分布式追踪界面 |
| Loki | 3100 | 日志聚合服务 |

### 环境变量
主要环境变量（`.env` 文件）：
```bash
# === 数据库配置 ===
DATABASE_URL=postgresql://user:pass@localhost:5432/db  # PostgreSQL 连接字符串

# === Redis 配置 ===
REDIS_URL=redis://localhost:6379/0  # Redis 连接字符串（0 为数据库编号）

# === JWT 认证 ===
SECRET_KEY=your-secret-key  # JWT 签名密钥（生产环境必须修改为强密码）
ALGORITHM=HS256               # JWT 加密算法
ACCESS_TOKEN_EXPIRE_MINUTES=30  # Token 过期时间（分钟）

# === AWS 配置（可选，用于生产环境）===
AWS_ACCESS_KEY_ID=xxx         # AWS 访问密钥 ID
AWS_SECRET_ACCESS_KEY=xxx     # AWS 访问密钥
AWS_REGION=us-west-2          # AWS 区域

# === 应用配置 ===
ENVIRONMENT=development       # 运行环境: development, staging, production
LOG_LEVEL=INFO                # 日志级别: DEBUG, INFO, WARNING, ERROR
CORS_ORIGINS=http://localhost:3000  # 允许的跨域来源
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
- **使用 Spot Instances**：降低 EC2 成本 50-90%（适用于非关键工作负载）
- **配置自动扩缩容**：HPA（水平 Pod 自动扩缩容）+ Cluster Autoscaler（节点自动扩缩容）
- **启用 S3 生命周期策略**：自动将旧数据迁移到更便宜的存储类（IA, Glacier）
- **使用 VPC Endpoints**：避免 NAT Gateway 费用，减少数据传输成本
- **定期审查资源**：删除未使用的资源（EBS 卷、快照、负载均衡器等）
- **使用预留实例**：长期运行的服务可节省 30-75% 成本
- **优化容器镜像**：使用多阶段构建和精简基础镜像减少存储成本

---

**🚀 开始您的企业级全栈 AI 应用开发之旅！**

有问题？查看 [使用指南](使用指南.md) 或提交 Issue。
