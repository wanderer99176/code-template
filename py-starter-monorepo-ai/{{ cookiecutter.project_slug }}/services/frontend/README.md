# {{ cookiecutter.project_name }} Frontend

基于 Nuxt 3 的现代化前端应用。

## 技术栈

- **框架**: Nuxt 3
- **UI 库**: Nuxt UI + Tailwind CSS
- **状态管理**: Pinia
- **类型检查**: TypeScript
- **测试**: Vitest + Playwright

## 快速开始

```bash
# 安装依赖
pnpm install

# 启动开发服务器
pnpm dev

# 构建生产版本
pnpm build

# 预览生产版本
pnpm preview
```

## 项目结构

```
services/frontend/
├── assets/           # 静态资源（CSS、图片等）
├── components/       # Vue 组件
├── composables/      # 组合式函数
├── layouts/          # 布局组件
├── pages/            # 页面（自动路由）
├── plugins/          # Nuxt 插件
├── public/           # 公共静态文件
├── server/           # 服务端 API 和中间件
├── stores/           # Pinia 状态管理
├── tests/            # 测试文件
├── app.vue           # 根组件
├── nuxt.config.ts    # Nuxt 配置
├── tailwind.config.ts # Tailwind 配置
└── tsconfig.json     # TypeScript 配置
```

## 开发指南

### 添加新页面

在 `pages/` 目录下创建文件即可自动生成路由：

```
pages/
├── index.vue          → /
├── about.vue          → /about
└── users/
    ├── index.vue      → /users
    └── [id].vue       → /users/:id
```

### 使用 API

```vue
<script setup lang="ts">
const config = useRuntimeConfig()
const { data, error } = await useFetch(`${config.public.apiBaseUrl}/api/v1/users`)
</script>
```

### 状态管理

```typescript
// stores/user.ts
export const useUserStore = defineStore('user', () => {
  const user = ref(null)
  
  async function fetchUser() {
    // ...
  }
  
  return { user, fetchUser }
})
```

## 测试

```bash
# 单元测试
pnpm test

# E2E 测试
pnpm test:e2e
```

## 部署

### Docker

```bash
docker build -t {{ cookiecutter.project_slug }}-frontend .
docker run -p 3000:3000 {{ cookiecutter.project_slug }}-frontend
```

### Vercel/Netlify

```bash
# 生成静态站点
pnpm generate
```

## 相关资源

- [Nuxt 3 文档](https://nuxt.com/)
- [Nuxt UI 文档](https://ui.nuxt.com/)
- [Tailwind CSS 文档](https://tailwindcss.com/)

