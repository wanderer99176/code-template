{% raw %}<template>
  <UContainer>
    <div class="py-20">
      <!-- Hero Section -->
      <div class="text-center">
        <h1 class="text-5xl font-bold mb-4">
          欢迎使用 {{ siteName }}
        </h1>
        <p class="text-xl text-gray-600 mb-8">
          {{ description }}
        </p>
        <div class="flex gap-4 justify-center">
          <UButton size="lg" to="/docs">
            查看文档
          </UButton>
          <UButton size="lg" variant="outline" to="/api/docs">
            API 文档
          </UButton>
        </div>
      </div>

      <!-- Features -->
      <div class="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8">
        <UCard v-for="feature in features" :key="feature.title">
          <template #header>
            <div class="flex items-center gap-3">
              <UIcon :name="feature.icon" class="w-6 h-6" />
              <h3 class="text-lg font-semibold">{{ feature.title }}</h3>
            </div>
          </template>
          <p class="text-gray-600">{{ feature.description }}</p>
        </UCard>
      </div>

      <!-- Stats -->
      <div class="mt-20 grid grid-cols-1 md:grid-cols-4 gap-8 text-center">
        <div v-for="stat in stats" :key="stat.label">
          <div class="text-4xl font-bold text-primary">{{ stat.value }}</div>
          <div class="text-gray-600 mt-2">{{ stat.label }}</div>
        </div>
      </div>
    </div>
  </UContainer>
</template>

<script setup lang="ts">
// 页面元数据
definePageMeta({
  layout: 'default',
})

// 运行时配置
const config = useRuntimeConfig()
const siteName = config.public.siteName
const description = '{% endraw %}{{ cookiecutter.description }}{% raw %}'

// 功能列表
const features = [
  {
    icon: 'i-heroicons-rocket-launch',
    title: '高性能',
    description: '基于 FastAPI 和 Nuxt 3，提供极致的性能体验',
  },
  {
    icon: 'i-heroicons-shield-check',
    title: '类型安全',
    description: 'TypeScript + Python 类型提示，保证代码质量',
  },
  {
    icon: 'i-heroicons-cube',
    title: 'Monorepo',
    description: '统一的代码仓库，便于管理和协作',
  },
  {
    icon: 'i-heroicons-cpu-chip',
    title: 'AI 集成',
    description: '内置 YOLOv8 和 Whisper，轻松构建 AI 应用',
  },
  {
    icon: 'i-heroicons-cloud',
    title: '云原生',
    description: 'Docker + Kubernetes，支持容器化部署',
  },
  {
    icon: 'i-heroicons-chart-bar',
    title: '可观测性',
    description: 'Prometheus + Grafana，完整的监控体系',
  },
]

// 统计数据
const stats = [
  { value: '10+', label: '服务组件' },
  { value: '100%', label: '类型安全' },
  { value: '< 200ms', label: 'API 响应' },
  { value: '99.9%', label: '可用性' },
]
</script>
{% endraw %}
