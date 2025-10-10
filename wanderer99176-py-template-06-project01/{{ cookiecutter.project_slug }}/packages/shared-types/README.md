# @{{ cookiecutter.project_slug }}/shared-types

前后端共享的 TypeScript 类型定义包。

## 功能

- 🔄 从 FastAPI 的 OpenAPI 规范自动生成类型
- 📝 类型安全的 API 调用
- 🎯 避免前后端类型不一致
- 🚀 提高开发效率

## 使用方法

### 在前端使用

```typescript
import type { paths, components } from '@{{ cookiecutter.project_slug }}/shared-types'

// 使用 API 路径类型
type GetUsersResponse =
  paths['/api/v1/users']['get']['responses']['200']['content']['application/json']

// 使用组件类型
type User = components['schemas']['User']
```

### 生成类型

```bash
# 从根目录运行
pnpm codegen

# 或手动生成
cd packages/shared-types
pnpm generate
```

## 类型说明

### paths

包含所有 API 端点的类型定义，按照 OpenAPI 规范组织。

```typescript
// GET /api/v1/users/{id}
type GetUserParams = paths['/api/v1/users/{id}']['get']['parameters']['path']
type GetUserResponse = paths['/api/v1/users/{id}']['get']['responses']['200']['content']['application/json']
```

### components

包含所有数据模型的类型定义。

```typescript
type User = components['schemas']['User']
type CreateUserRequest = components['schemas']['CreateUserRequest']
```

### 通用类型

包含项目中常用的通用类型定义。

```typescript
import type { ApiResponse, PaginatedResponse, UserRole } from '@{{ cookiecutter.project_slug }}/shared-types'

// API 响应
const response: ApiResponse<User> = {
  success: true,
  data: { id: '1', name: 'John' }
}

// 分页响应
const users: PaginatedResponse<User> = {
  items: [],
  total: 100,
  page: 1,
  pageSize: 20,
  totalPages: 5
}

// 枚举
const role: UserRole = UserRole.Admin
```

## 开发指南

### 添加新类型

1. 在后端定义 Pydantic 模型
2. 运行 `pnpm codegen` 重新生成类型
3. 在前端使用新类型

### 自定义类型

对于不从后端生成的类型，可以直接在 `index.ts` 中定义：

```typescript
// index.ts
export interface CustomType {
  // ...
}
```

## 注意事项

- ⚠️ 不要手动编辑 `types.ts` 文件，它会被自动生成覆盖
- ⚠️ 确保后端 API 文档是最新的
- ⚠️ 类型生成前需要启动后端服务

## 相关链接

- [openapi-typescript](https://github.com/drwpow/openapi-typescript)
- [OpenAPI Specification](https://swagger.io/specification/)

