# ===== 依赖阶段 =====
FROM node:{{ cookiecutter.node_version }}-alpine AS deps

# 安装 pnpm
RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app

# 复制依赖文件
COPY package.json pnpm-lock.yaml* ./

# 安装依赖
RUN pnpm install --frozen-lockfile

# ===== 构建阶段 =====
FROM node:{{ cookiecutter.node_version }}-alpine AS builder

RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app

# 从依赖阶段复制 node_modules
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# 构建应用
RUN pnpm build

# ===== 运行阶段 =====
FROM node:{{ cookiecutter.node_version }}-alpine AS runner

WORKDIR /app

# 设置环境变量
ENV NODE_ENV=production \
    NUXT_HOST=0.0.0.0 \
    NUXT_PORT=3000

# 创建非 root 用户
RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 nuxt

# 复制构建产物
COPY --from=builder --chown=nuxt:nodejs /app/.output ./.output
COPY --from=builder --chown=nuxt:nodejs /app/public ./public

# 切换到非 root 用户
USER nuxt

# 暴露端口
EXPOSE 3000

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD node -e "require('http').get('http://localhost:3000/api/_health', (r) => {process.exit(r.statusCode === 200 ? 0 : 1)})"

# 启动命令
CMD ["node", ".output/server/index.mjs"]

