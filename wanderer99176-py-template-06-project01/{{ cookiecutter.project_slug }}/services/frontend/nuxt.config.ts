// Nuxt 配置文件
// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  // 开发工具
  devtools: { enabled: true },
  
  // TypeScript 配置
  typescript: {
    strict: true,
    typeCheck: true,
  },
  
  // 模块
  modules: [
    '@nuxt/ui',
    '@pinia/nuxt',
  ],
  
  // 运行时配置
  runtimeConfig: {
    // 服务端环境变量
    // serverKey: '',
    
    // 客户端环境变量 (暴露给前端)
    public: {
      apiBaseUrl: process.env.NUXT_PUBLIC_API_BASE_URL || 'http://localhost:8000',
      wsUrl: process.env.NUXT_PUBLIC_WS_URL || 'ws://localhost:8000',
      siteUrl: process.env.NUXT_PUBLIC_SITE_URL || 'http://localhost:3000',
      siteName: process.env.NUXT_PUBLIC_SITE_NAME || '{{ cookiecutter.project_name }}',
    },
  },
  
  // 应用配置
  app: {
    head: {
      title: '{{ cookiecutter.project_name }}',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: '{{ cookiecutter.description }}' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      ],
    },
  },
  
  // CSS 配置
  css: [
    '~/assets/css/main.css',
  ],
  
  // Tailwind CSS 配置
  tailwindcss: {
    cssPath: '~/assets/css/main.css',
    configPath: 'tailwind.config',
  },
  
  // 构建配置
  build: {
    transpile: [],
  },
  
  // Nitro 服务器配置
  nitro: {
    compressPublicAssets: true,
  },
  
  // 实验性功能
  experimental: {
    payloadExtraction: false,
  },
  
  // 兼容性日期
  compatibilityDate: '2024-01-10',
})

