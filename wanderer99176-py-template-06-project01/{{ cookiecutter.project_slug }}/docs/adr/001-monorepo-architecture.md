# ADR 001: Monorepo 架构决策

**状态**: 已接受  
**日期**: 2025-10-10  
**决策者**: {{ cookiecutter.author_name }}

## 上下文

{{ cookiecutter.project_name }} 是一个包含多个服务和应用的企业级全栈项目，包括：

- 前端应用 (Nuxt)
- 后端 API (FastAPI)
- 机器学习服务 (YOLOv8)
- 音频处理服务 (Whisper)
- 网络爬虫 (Scrapy)
- 共享包和工具库

我们需要选择一个合适的代码仓库组织结构，以支持：

1. 代码共享和重用
2. 统一的依赖管理
3. 协调的版本发布
4. 一致的 CI/CD 流程
5. 良好的开发体验

## 决策

我们决定采用 **Monorepo** 架构，使用以下技术栈：

- **pnpm workspace**: 管理 Node.js/TypeScript 包
- **Turbo**: 高性能任务编排和缓存
- **uv**: Python 包管理
- **Docker Compose / Kubernetes**: 服务编排

## 备选方案

### 1. Multirepo (多仓库)

**优点:**
- 代码隔离，独立部署
- 权限控制更细粒度
- 构建更快（单个服务）

**缺点:**
- 代码共享困难，需要发布 npm/PyPI 包
- 依赖管理复杂，版本同步困难
- CI/CD 配置重复
- 跨服务重构困难

### 2. Monorepo (单仓库)

**优点:**
- ✅ 代码共享简单，直接引用
- ✅ 统一的依赖管理
- ✅ 原子化提交，跨服务重构容易
- ✅ 统一的 CI/CD 配置
- ✅ 更好的开发体验

**缺点:**
- 仓库体积较大
- 需要工具支持（Turbo, pnpm workspace）
- 权限控制粗粒度

## 理由

我们选择 Monorepo 的主要理由：

### 1. 代码共享和类型安全

**问题**: 前后端需要共享类型定义（如 API 接口、数据模型）

**Monorepo 解决方案**:
```typescript
// packages/shared-types/index.ts
export interface User {
  id: string
  email: string
  name: string
}

// services/backend - 自动生成
// services/frontend - 直接导入
import type { User } from '@{{ cookiecutter.project_slug }}/shared-types'
```

### 2. 依赖管理

**问题**: 多个服务使用相同的依赖，版本不一致导致问题

**Monorepo 解决方案**:
```json
// 根目录 package.json
{
  "devDependencies": {
    "typescript": "^5.3.3",  // 所有服务共享
    "prettier": "^3.2.5"
  }
}
```

### 3. 协调发布

**问题**: 功能需要同时更新前后端，版本同步困难

**Monorepo 解决方案**:
- 一个 PR 包含所有相关变更
- 一次提交，原子化部署
- 使用 Changesets 管理版本

### 4. CI/CD 效率

**问题**: 每个服务都需要配置 CI/CD，重复且难以维护

**Monorepo 解决方案**:
```yaml
# .github/workflows/ci-cd.yml
# 一个工作流，智能地只测试和构建变更的服务
jobs:
  test-backend:
    if: contains(github.event.head_commit.modified, 'services/backend')
  test-frontend:
    if: contains(github.event.head_commit.modified, 'services/frontend')
```

### 5. 开发体验

**Monorepo 提供**:
- ✅ 一键安装所有依赖: `pnpm install`
- ✅ 一键启动所有服务: `pnpm dev`
- ✅ 一键运行所有测试: `pnpm test`
- ✅ 一键代码检查: `pnpm lint`
- ✅ 智能缓存: Turbo 缓存构建结果

## 技术栈选择

### pnpm workspace

**理由**:
- 比 npm/yarn 更快、更节省磁盘空间
- 严格的依赖解析，避免幽灵依赖
- 支持 workspace protocol

```yaml
# pnpm-workspace.yaml
packages:
  - 'services/*'
  - 'packages/*'
```

### Turbo

**理由**:
- 智能任务编排，只运行必要的任务
- 增量构建，缓存结果
- 并行执行，充分利用 CPU

```json
// turbo.json
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],  // 自动处理依赖顺序
      "outputs": ["dist/**", ".next/**"]
    }
  }
}
```

### uv (Python)

**理由**:
- 比 pip 快 10-100 倍
- 统一的依赖管理
- 支持 lockfile

## 项目结构

```
{{ cookiecutter.project_slug }}/
├── packages/              # 共享包
│   ├── shared-types/      # TypeScript 类型
│   ├── ui-kit/            # UI 组件库
│   └── ...
├── services/              # 微服务
│   ├── backend/           # FastAPI
│   ├── frontend/          # Nuxt
│   └── ...
├── infra/                 # 基础设施
│   ├── docker-compose/
│   ├── kubernetes/
│   └── tofu/
├── scripts/               # 脚本
├── .github/workflows/     # CI/CD
├── package.json           # 根 package.json
├── pnpm-workspace.yaml    # pnpm workspace
└── turbo.json             # Turbo 配置
```

## 实施计划

### 阶段 1: 基础设施 (已完成)
- ✅ 创建 Monorepo 结构
- ✅ 配置 pnpm workspace
- ✅ 配置 Turbo
- ✅ 设置 pre-commit hooks

### 阶段 2: 服务迁移 (进行中)
- 🔄 迁移后端服务
- 🔄 迁移前端应用
- 🔄 创建共享包

### 阶段 3: CI/CD (待定)
- ⏳ 设置智能 CI/CD
- ⏳ 配置增量部署
- ⏳ 设置监控和告警

## 预期收益

### 量化指标

- **开发效率**: 提升 30-40%（减少重复配置和代码）
- **构建速度**: 提升 50-70%（Turbo 缓存）
- **依赖安装**: 提升 60-80%（pnpm）
- **代码重用**: 提升 40-50%（共享包）

### 定性收益

- ✅ 更好的代码一致性
- ✅ 更容易的跨服务重构
- ✅ 更快的 Bug 修复（一次 PR 修复所有服务）
- ✅ 更好的新成员入职体验
- ✅ 更统一的技术栈

## 潜在风险和缓解措施

### 风险 1: 仓库体积过大

**缓解**:
- 使用 Git LFS 存储大文件
- 定期清理 Git 历史
- 使用浅克隆: `git clone --depth 1`

### 风险 2: CI/CD 构建时间长

**缓解**:
- 使用 Turbo 增量构建
- 利用 GitHub Actions 缓存
- 智能地只测试变更的服务

### 风险 3: 权限控制粗粒度

**缓解**:
- 使用 CODEOWNERS 文件
- 设置分支保护规则
- 使用 Dependabot 分组更新

## 成功标准

1. ✅ 新服务可以在 1 天内集成
2. ✅ CI/CD 运行时间 < 15 分钟
3. ✅ 依赖安装时间 < 2 分钟
4. ✅ 开发者满意度 > 8/10
5. ✅ Bug 修复周期缩短 30%

## 参考资料

- [Google 的 Monorepo 实践](https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository)
- [Monorepo.tools](https://monorepo.tools/)
- [Turbo 文档](https://turbo.build/)
- [pnpm workspace](https://pnpm.io/workspaces)

## 修订历史

- 2025-10-10: 初始版本，决定采用 Monorepo 架构

