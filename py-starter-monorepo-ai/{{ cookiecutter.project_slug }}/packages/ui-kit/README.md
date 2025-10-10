# @{{ cookiecutter.project_slug }}/ui-kit

共享 UI 组件库，提供可在整个应用中复用的 Vue 组件。

## 安装

```bash
pnpm add @{{ cookiecutter.project_slug }}/ui-kit
```

## 使用

### Button 组件

```vue
<script setup>
import { Button } from '@{{ cookiecutter.project_slug }}/ui-kit'
</script>

<template>
  <Button variant="primary" size="md" @click="handleClick">
    点击我
  </Button>
</template>
```

### Card 组件

```vue
<script setup>
import { Card } from '@{{ cookiecutter.project_slug }}/ui-kit'
</script>

<template>
  <Card shadow hoverable>
    <template #header>
      卡片标题
    </template>
    
    <p>卡片内容</p>
    
    <template #footer>
      卡片底部
    </template>
  </Card>
</template>
```

### 工具函数

```ts
import { formatCurrency, formatDate, formatFileSize } from '@{{ cookiecutter.project_slug }}/ui-kit'

const price = formatCurrency(1234.56) // "$1,234.56"
const date = formatDate(new Date()) // "December 10, 2023"
const size = formatFileSize(1024 * 1024) // "1 MB"
```

## 组件列表

- `Button` - 按钮组件
- `Card` - 卡片容器组件
- `Input` - 输入框组件（待实现）
- `Modal` - 模态框组件（待实现）
- `Spinner` - 加载动画组件（待实现）

## 开发

```bash
# 开发模式
pnpm dev

# 构建
pnpm build

# 类型检查
pnpm typecheck

# Lint
pnpm lint
```

