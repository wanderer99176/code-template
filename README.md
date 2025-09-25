# Wanderer's Code Templates

[![Cookiecutter](https://img.shields.io/badge/cookiecutter-%23d4a679.svg?style=for-the-badge&logo=cookiecutter&logoColor=white)](https://github.com/cookiecutter/cookiecutter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

这是一个由 `wanderer99176` 创建和维护的、用于快速启动高质量Python项目的 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 模板库。

本仓库采用 Monorepo 模式，集中管理了适用于不同规模和场景的项目模板，旨在将现代Python开发的最佳实践固化为可复用的脚手架。

## ✨ 核心理念与特性

所有模板均遵循以下现代、高效的开发理念：

* **现代化工具链**: 完全由 `pyproject.toml` 驱动，使用 `uv` 进行极致性能的环境和包管理。
* **最佳实践结构**: 默认采用 `src` 布局，从根源上避免常见的Python导入问题。
* **自动化与质量保证**: 内置 `Ruff` 进行代码格式化与检查，集成 `pytest` 进行测试，并提供了开箱即用的 `pre-commit` 钩子和 GitHub Actions CI/CD 工作流。
* **可扩展性**: 提供了从快速原型（MVP）到大型企业级应用（Enterprise）的多种模板，可以随项目的成长而平滑演进。
* **容器化就绪**: 中型及以上规模的模板均包含经过优化的 `Dockerfile`，为云原生部署做好了准备。

##  disponível Templates

本仓库目前包含以下可用模板：

| 模板目录名 | 描述与适用场景 |
| :--- | :--- |
| `wanderer99176-py-template-01-mvp` | **MVP版**: 用于快速原型、一次性脚本或个人实验。采用扁平布局，追求最快的启动速度。 |
| `wanderer99176-py-template-02-small`| **小型工具版**: 用于开发可分发的CLI工具或简单的功能库。引入了`src`布局和`tests`目录。 |
| `wanderer99176-py-template-03-medium`| **中型应用版**: 用于构建标准的Web应用、API服务或有一定规模的库。增加了CI/CD和Docker支持。 |
| `wanderer99176-py-template-05-enterprise`| **企业级版**: 用于大型、多人协作、长期维护的复杂项目。包含了完整的分层架构和所有工程化组件。 |

*(注：您可以根据实际情况添加或修改此列表)*

## 🚀 使用方法

### 前提条件
请确保您已经安装了 `cookiecutter` 命令行工具。
```bash
# 推荐使用 pipx
pipx install cookiecutter
```

### 生成新项目
使用 `cookiecutter` 命令指向本仓库，并使用 `--directory` (或 `-d`) 参数指定您想使用的具体模板。

#### 示例1：创建一个大型新项目
```bash
cookiecutter gh:wanderer99176/code-template -d wanderer99176-py-template-05-enterprise
```

#### 示例2：创建一个简单的CLI工具
```bash
cookiecutter gh:wanderer99176/code-template -d wanderer99176-py-template-02-small
```

接下来，只需根据终端的提示回答几个关于您新项目的问题，一个结构完整、配置齐全的项目目录就会被自动创建。

## 🔧 模板的维护与贡献

本模板库是一个持续演进的项目。当发现有可以改进的最佳实践时，可以直接修改本仓库中的模板文件并提交。

欢迎通过 [Issues](https://github.com/wanderer99176/code-template/issues) 或 [Pull Requests](https://github.com/wanderer99176/code-template/pulls) 提出改进建议。

## 📜 许可证

本模板库本身采用 [MIT License](LICENSE) 开源。# Wanderer's Code Templates

[![Cookiecutter](https://img.shields.io/badge/cookiecutter-%23d4a679.svg?style=for-the-badge&logo=cookiecutter&logoColor=white)](https://github.com/cookiecutter/cookiecutter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

这是一个由 `wanderer99176` 创建和维护的、用于快速启动高质量Python项目的 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 模板库。

本仓库采用 Monorepo 模式，集中管理了适用于不同规模和场景的项目模板，旨在将现代Python开发的最佳实践固化为可复用的脚手架。

## ✨ 核心理念与特性

所有模板均遵循以下现代、高效的开发理念：

* **现代化工具链**: 完全由 `pyproject.toml` 驱动，使用 `uv` 进行极致性能的环境和包管理。
* **最佳实践结构**: 默认采用 `src` 布局，从根源上避免常见的Python导入问题。
* **自动化与质量保证**: 内置 `Ruff` 进行代码格式化与检查，集成 `pytest` 进行测试，并提供了开箱即用的 `pre-commit` 钩子和 GitHub Actions CI/CD 工作流。
* **可扩展性**: 提供了从快速原型（MVP）到大型企业级应用（Enterprise）的多种模板，可以随项目的成长而平滑演进。
* **容器化就绪**: 中型及以上规模的模板均包含经过优化的 `Dockerfile`，为云原生部署做好了准备。

##  disponível Templates

本仓库目前包含以下可用模板：

| 模板目录名 | 描述与适用场景 |
| :--- | :--- |
| `wanderer99176-py-template-01-mvp` | **MVP版**: 用于快速原型、一次性脚本或个人实验。采用扁平布局，追求最快的启动速度。 |
| `wanderer99176-py-template-02-small`| **小型工具版**: 用于开发可分发的CLI工具或简单的功能库。引入了`src`布局和`tests`目录。 |
| `wanderer99176-py-template-03-medium`| **中型应用版**: 用于构建标准的Web应用、API服务或有一定规模的库。增加了CI/CD和Docker支持。 |
| `wanderer99176-py-template-05-enterprise`| **企业级版**: 用于大型、多人协作、长期维护的复杂项目。包含了完整的分层架构和所有工程化组件。 |

*(注：您可以根据实际情况添加或修改此列表)*

## 🚀 使用方法

### 前提条件
请确保您已经安装了 `cookiecutter` 命令行工具。
```bash
# 推荐使用 pipx
pipx install cookiecutter
```

### 生成新项目
使用 `cookiecutter` 命令指向本仓库，并使用 `--directory` (或 `-d`) 参数指定您想使用的具体模板。

#### 示例1：创建一个大型新项目
```bash
cookiecutter gh:wanderer99176/code-template -d wanderer99176-py-template-05-enterprise
```

#### 示例2：创建一个简单的CLI工具
```bash
cookiecutter gh:wanderer99176/code-template -d wanderer99176-py-template-02-small
```

接下来，只需根据终端的提示回答几个关于您新项目的问题，一个结构完整、配置齐全的项目目录就会被自动创建。

## 🔧 模板的维护与贡献

本模板库是一个持续演进的项目。当发现有可以改进的最佳实践时，可以直接修改本仓库中的模板文件并提交。

欢迎通过 [Issues](https://github.com/wanderer99176/code-template/issues) 或 [Pull Requests](https://github.com/wanderer99176/code-template/pulls) 提出改进建议。

## 📜 许可证

本模板库本身采用 [MIT License](LICENSE) 开源。