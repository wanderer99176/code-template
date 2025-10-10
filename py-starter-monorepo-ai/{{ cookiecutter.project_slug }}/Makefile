# Makefile - 传统 make 命令支持
# 推荐使用 just，这里保留 Makefile 是为了兼容性

.PHONY: help init dev build test lint clean

# 默认目标
.DEFAULT_GOAL := help

# 帮助信息
help:
	@echo "可用命令:"
	@echo "  make init          - 初始化项目"
	@echo "  make dev           - 启动开发环境"
	@echo "  make build         - 构建所有服务"
	@echo "  make test          - 运行测试"
	@echo "  make lint          - 运行 linters"
	@echo "  make format        - 格式化代码"
	@echo "  make clean         - 清理构建产物"
	@echo ""
	@echo "推荐使用 just 命令获得更好的体验: just --list"

# 初始化
init:
	chmod +x scripts/*.sh
	./scripts/setup.sh

# 开发
dev:
	docker-compose -f infra/docker-compose/dev.yml up -d
	pnpm install
	pnpm dev

# 构建
build:
	pnpm build
	cd services/backend && uv sync
	cd services/ml-api && uv sync
	cd services/audio-api && uv sync

# 测试
test:
	pnpm test
	cd services/backend && uv run pytest
	cd services/ml-api && uv run pytest
	cd services/audio-api && uv run pytest

# Lint
lint:
	pnpm lint
	cd services/backend && uv run ruff check .
	cd services/ml-api && uv run ruff check .
	cd services/audio-api && uv run ruff check .

# 格式化
format:
	pnpm format
	cd services/backend && uv run ruff format .
	cd services/ml-api && uv run ruff format .
	cd services/audio-api && uv run ruff format .

# 清理
clean:
	pnpm clean
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true

