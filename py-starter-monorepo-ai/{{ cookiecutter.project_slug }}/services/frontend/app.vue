{% raw %}<template>
  <div>
    <!-- 导航栏 -->
    <UContainer>
      <header class="py-4">
        <nav class="flex items-center justify-between">
          <div class="text-2xl font-bold">{{ config.public.siteName }}</div>
          <div class="flex gap-4">
            <UButton to="/" variant="ghost">首页</UButton>
            <UButton to="/about" variant="ghost">关于</UButton>
          </div>
        </nav>
      </header>
    </UContainer>

    <!-- 主内容 -->
    <main>
      <NuxtPage />
    </main>

    <!-- 页脚 -->
    <UContainer>
      <footer class="py-8 text-center text-gray-600">
        <p>© 2025 {{ config.public.siteName }}. All rights reserved.</p>
      </footer>
    </UContainer>
  </div>
</template>

<script setup lang="ts">
// 获取运行时配置
const config = useRuntimeConfig()

// SEO 配置
useHead({
  title: config.public.siteName as string,
  meta: [
    { name: 'description', content: '{% endraw %}{{ cookiecutter.description }}{% raw %}' },
  ],
})
</script>
{% endraw %}
