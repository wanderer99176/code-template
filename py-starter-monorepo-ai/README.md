# 企业级全栈 AI 应用 Monorepo 项目模板

这是一个基于 **Cookiecutter** 的企业级全栈项目模板，包含完整的现代化技术栈和最佳实践。

## 🌟 特点

### 核心功能

- 🏗️ **Monorepo 架构**: 使用 pnpm workspace + Turbo 管理多个服务
- 🚀 **FastAPI 后端**: 高性能异步 API + SQLModel + Alembic
- 🎨 **Nuxt 3 前端**: 现代化 Vue 3 应用 + Nuxt UI + Tailwind CSS
- 🤖 **AI 服务**: YOLOv8 目标检测 + Whisper 语音识别
- 🕷️ **网络爬虫**: Scrapy 分布式爬虫
- 🐳 **完整 DevOps**: Docker + Kubernetes + Helm + OpenTofu
- 📊 **监控体系**: Prometheus + Grafana + Loki + Jaeger
- 🔒 **安全扫描**: Trivy + Dependabot
- 🔄 **CI/CD**: GitHub Actions 完整流水线

### 技术亮点

- ✅ **类型安全**: TypeScript + Python 类型提示 + 自动生成共享类型
- ✅ **代码质量**: Ruff + ESLint + Prettier + pre-commit hooks
- ✅ **测试完整**: Pytest + Vitest + Playwright E2E
- ✅ **文档齐全**: API 文档 + 架构决策记录 + 部署指南
- ✅ **性能优化**: Redis 缓存 + 连接池 + Gzip 压缩
- ✅ **可观测性**: 结构化日志 + 指标监控 + 分布式追踪

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

```bash
# 运行自动化设置脚本
bash scripts/setup.sh
```

这将自动完成：
1. ✅ 检查所有依赖
2. ✅ 安装 Node.js 依赖
3. ✅ 设置 Python 环境
4. ✅ 配置 pre-commit
5. ✅ 创建环境变量文件
6. ✅ 启动基础设施服务
7. ✅ 运行数据库迁移

### 启动开发环境

```bash
# 启动所有服务
pnpm dev

# 访问应用
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

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
│   │   ├── dev.yml           # 开发环境
│   │   └── monitoring.yml    # 监控套件
│   ├── kubernetes/            # K8s + Helm
│   │   ├── helm-charts/
│   │   └── core-infra/
│   └── tofu/                  # OpenTofu (Terraform)
├── packages/                  # 共享包
│   ├── shared-types/         # TypeScript 类型
│   ├── ui-kit/               # UI 组件库
│   ├── eslint-config-custom/ # ESLint 配置
│   └── tsconfig-custom/      # TypeScript 配置
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
├── .gitignore
├── .pre-commit-config.yaml
├── docker-compose.yml         # 完整应用栈
├── package.json              # pnpm workspace
├── pnpm-workspace.yaml
├── pyproject.toml            # 根 Python 配置
├── tsconfig.base.json
├── turbo.json                # Turbo 配置
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

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

### 添加新功能

```bash
# 1. 在 backend 添加新端点
cd services/backend/src/<package_name>/features
mkdir new_feature
# 创建 router.py, schemas.py, services.py

# 2. 注册路由
# 在 api/v1/router.py 中导入并注册

# 3. 生成类型
pnpm codegen

# 4. 在 frontend 使用新类型
# import type { NewFeature } from '@project/shared-types'
```

### 运行测试

```bash
# 所有测试
pnpm test

# Backend 测试
pnpm test:backend

# Frontend 测试
pnpm test:frontend

# E2E 测试
pnpm test:e2e
```

### 代码检查

```bash
# 运行所有检查
pnpm lint

# 自动修复
pnpm lint:fix

# 格式化代码
pnpm format
```

## 🐳 部署

### Docker Compose

```bash
# 开发环境
docker-compose up -d

# 生产环境
docker-compose -f docker-compose.prod.yml up -d
```

### Kubernetes

```bash
# 部署后端
helm install backend ./infra/kubernetes/helm-charts/backend

# 部署前端
helm install frontend ./infra/kubernetes/helm-charts/frontend
```

详见 [部署手册]({{ cookiecutter.project_slug }}/docs/deployment.md)

## 📊 已完成功能

### ✅ 已实现（100%核心功能）

- [x] 完整的 Monorepo 结构
- [x] 根目录配置文件
- [x] GitHub CI/CD 工作流
- [x] 完整的项目文档
- [x] 基础设施 Docker Compose
- [x] 监控套件配置
- [x] 项目自动化脚本
- [x] 共享包（TypeScript）
- [x] Backend 服务完整代码
- [x] Frontend 服务完整代码
- [x] ML API 服务
- [x] Audio API 服务
- [x] Scraper 服务
- [x] 数据库集成
- [x] API 端点示例
- [x] Dockerfile 和部署配置

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

**⚠️ 重要提示**

这是一个模板项目，包含了大量的配置和示例代码。请根据实际需求：

1. 📝 修改配置文件
2. 🔒 更改密钥和密码
3. 🎨 定制 UI 和样式
4. 🔧 添加业务逻辑
5. ✅ 完善测试用例

**祝您开发愉快！🚀**
