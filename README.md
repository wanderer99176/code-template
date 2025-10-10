# Wanderer's Python Templates

[![Cookiecutter](https://img.shields.io/badge/cookiecutter-template-blue)](https://github.com/cookiecutter/cookiecutter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

这是一个由 `wanderer99176` 创建和维护的、用于快速启动高质量Python项目的 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 模板库。

本仓库采用 Monorepo 模式，集中管理了适用于不同规模和场景的项目模板，旨在将现代Python开发的最佳实践固化为可复用的脚手架。

## ✨ 核心理念与特性

所有模板均遵循以下现代、高效的开发理念：

  * **现代化工具链**: 完全由 `pyproject.toml` 驱动，使用 `uv` 进行极致性能的环境和包管理。
  * **最佳实践结构**: 采用 `src` 布局（Minimal版除外），从根源上避免常见的Python导入问题。
  * **自动化与质量保证**: 内置 `Ruff` 进行代码格式化与检查，集成 `pytest` 进行测试，并提供了开箱即用的 `pre-commit` 钩子和 GitHub Actions CI/CD 工作流。
  * **可扩展性**: 提供了从快速原型（Minimal）到大型全栈应用（Monorepo AI）的多种模板，可以随项目的成长而平滑演进。
  * **容器化就绪**: 中型及以上规模的模板均包含经过优化的 `Dockerfile`，为云原生部署做好了准备。

## 📦 模板概要 (Available Templates)

本仓库目前包含以下可用模板：

| 模板名称 | 描述与适用场景 | 核心特性 |
| :--- | :--- | :--- |
| `py-starter-minimal` | **最小化**: 用于快速原型、一次性脚本或个人实验。采用扁平布局，追求最快的启动速度。 | 单文件、快速启动 |
| `py-starter-cli`| **CLI工具**: 用于开发可分发的命令行工具或简单的功能库。引入了`src`布局和`tests`目录。 | src布局、测试框架 |
| `py-starter-api`| **API应用**: 用于构建标准的Web应用、REST API服务或有一定规模的库。增加了CI/CD和Docker支持。 | CI/CD、Docker、FastAPI |
| `py-starter-enterprise`| **企业级**: 用于大型、多人协作、长期维护的复杂项目。包含了完整的分层架构和所有工程化组件。 | 完整架构、文档齐全 |
| `py-starter-monorepo-ai`| **🔥 全栈AI Monorepo**: 企业级全栈AI应用，包含FastAPI后端、Nuxt前端、ML/Audio API、爬虫、完整DevOps和监控体系。 | Monorepo、微服务、AI集成、K8s |

## 🚀 快速开始：使用模板

### 前提条件

请确保您已经安装了 `cookiecutter` 命令行工具。

```bash
# 推荐使用 pipx
pipx install cookiecutter
```

### 生成新项目

根据您的项目需求，选择并运行以下对应命令：

#### **模板一：Minimal（最小化）**

用于快速原型或一次性脚本，最快启动。

```bash
cookiecutter gh:wanderer99176/code-template --directory py-starter-minimal
```

#### **模板二：CLI（命令行工具）**

用于创建可分发的CLI工具或小型库。

```bash
cookiecutter gh:wanderer99176/code-template --directory py-starter-cli
```

#### **模板三：API（Web应用）**

用于构建包含CI/CD和Docker的标准API应用。

```bash
cookiecutter gh:wanderer99176/code-template --directory py-starter-api
```

#### **模板四：Enterprise（企业级）**

用于启动复杂的、企业级的应用程序。

```bash
cookiecutter gh:wanderer99176/code-template --directory py-starter-enterprise
```

#### **模板五：Monorepo AI（全栈AI应用）🔥**

用于构建包含多个服务的大型全栈AI应用，支持微服务架构和云原生部署。

```bash
cookiecutter gh:wanderer99176/code-template --directory py-starter-monorepo-ai
```

**模板五特性：**
- 🏗️ **Monorepo架构**: pnpm workspace + Turbo 统一管理
- 🚀 **后端服务**: FastAPI + SQLModel + Alembic + Redis + ARQ
- 🎨 **前端应用**: Nuxt 3 + TypeScript + Nuxt UI + Tailwind CSS
- 🤖 **AI服务**: YOLOv8目标检测 + Whisper语音识别
- 🕷️ **爬虫服务**: Scrapy分布式爬虫
- 🐳 **DevOps**: Docker Compose + Kubernetes + Helm + OpenTofu
- 📊 **监控体系**: Prometheus + Grafana + Loki + Jaeger
- 🔒 **安全扫描**: Trivy + Dependabot
- 🔄 **CI/CD**: GitHub Actions完整流水线
- 📝 **详尽文档**: 环境搭建、部署、ADR等

**创建后的步骤：**

```bash
# 1. 进入项目目录
cd <your-project-name>

# 2. 运行自动化设置脚本
bash scripts/setup.sh

# 3. 启动开发环境
pnpm dev
```

详细使用指南请查看：`py-starter-monorepo-ai/使用指南.md`

---

接下来，只需根据终端的提示回答几个关于您新项目的问题，一个结构完整、配置齐全的项目目录就会被自动创建。

## 📊 模板对比

| 特性 | Minimal | CLI | API | Enterprise | **Monorepo AI** |
|:---|:---:|:---:|:---:|:---:|:---:|
| 项目结构 | 扁平 | src布局 | src布局 | 分层架构 | **Monorepo多服务** |
| 依赖管理 | pyproject.toml | pyproject.toml + uv | pyproject.toml + uv | pyproject.toml + uv | **pnpm + uv** |
| 测试框架 | ❌ | ✅ pytest | ✅ pytest | ✅ pytest + coverage | **✅ pytest + Vitest + Playwright** |
| 代码规范 | ❌ | ✅ Ruff | ✅ Ruff | ✅ Ruff + pre-commit | **✅ Ruff + ESLint + Prettier** |
| CI/CD | ❌ | ❌ | ✅ GitHub Actions | ✅ GitHub Actions | **✅ 完整CI/CD流水线** |
| Docker | ❌ | ❌ | ✅ Dockerfile | ✅ Dockerfile | **✅ Docker Compose + K8s** |
| 文档 | 基础 | README | README + API docs | 完整文档 | **✅ 完整文档 + ADR** |
| 数据库 | ❌ | ❌ | 可选 | ✅ | **✅ PostgreSQL + Redis** |
| API框架 | ❌ | ❌ | ✅ FastAPI | ✅ FastAPI | **✅ FastAPI + Nuxt** |
| 监控 | ❌ | ❌ | ❌ | 基础 | **✅ 完整监控栈** |
| 适用规模 | 个人实验 | 小工具 | 中型项目 | 大型项目 | **🔥 企业级全栈** |

## 🔧 模板的维护与贡献

本模板库是一个持续演进的项目。当发现有可以改进的最佳实践时，可以直接修改本仓库中的模板文件并提交。

欢迎通过 [Issues](https://github.com/wanderer99176/code-template/issues) 或 [Pull Requests](https://github.com/wanderer99176/code-template/pulls) 提出改进建议。

## 💡 使用建议

### 如何选择合适的模板？

1. **快速验证想法** → 使用 `py-starter-minimal`
2. **开发CLI工具** → 使用 `py-starter-cli`
3. **构建Web API** → 使用 `py-starter-api`
4. **大型企业项目** → 使用 `py-starter-enterprise`
5. **全栈AI微服务** → 使用 `py-starter-monorepo-ai` 🔥

### 模板升级路径

```
Minimal → CLI → API → Enterprise → Monorepo AI
```

项目可以随着需求增长，逐步迁移到更高级的模板。

## 📚 相关资源

- [Cookiecutter 文档](https://cookiecutter.readthedocs.io/)
- [uv 快速入门](https://github.com/astral-sh/uv)
- [Ruff 配置指南](https://docs.astral.sh/ruff/)
- [FastAPI 最佳实践](https://fastapi.tiangolo.com/)
- [Nuxt 3 文档](https://nuxt.com/)
- [Turborepo 指南](https://turbo.build/repo)

## 📜 许可证

本模板库本身采用 [MIT License](LICENSE) 开源。

使用这些模板生成的项目，其许可证由您在创建时选择决定。

---

**⭐ 如果这个项目对您有帮助，欢迎 Star！**

Made with ❤️ by wanderer99176
