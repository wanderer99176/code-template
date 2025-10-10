#!/usr/bin/env bash

# {{ cookiecutter.project_name }} 项目初始化脚本
# 此脚本自动执行项目设置的所有步骤

set -e  # 遇到错误立即退出

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# 打印欢迎消息
print_header() {
    echo ""
    echo "╔════════════════════════════════════════════════════════════╗"
    echo "║                                                            ║"
    echo "║        {{ cookiecutter.project_name }} 项目初始化        ║"
    echo "║                                                            ║"
    echo "╚════════════════════════════════════════════════════════════╝"
    echo ""
}

# 检查命令是否存在
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# 检查前置条件
check_prerequisites() {
    print_info "检查前置条件..."
    
    local missing_deps=()
    
    # 检查 Node.js
    if command_exists node; then
        NODE_VERSION=$(node -v)
        print_success "Node.js: $NODE_VERSION"
    else
        missing_deps+=("Node.js")
    fi
    
    # 检查 pnpm
    if command_exists pnpm; then
        PNPM_VERSION=$(pnpm -v)
        print_success "pnpm: v$PNPM_VERSION"
    else
        missing_deps+=("pnpm")
    fi
    
    # 检查 Python
    if command_exists python3; then
        PYTHON_VERSION=$(python3 --version)
        print_success "$PYTHON_VERSION"
    else
        missing_deps+=("Python 3")
    fi
    
    # 检查 uv
    if command_exists uv; then
        UV_VERSION=$(uv --version)
        print_success "$UV_VERSION"
    else
        missing_deps+=("uv")
    fi
    
    # 检查 Docker
    if command_exists docker; then
        DOCKER_VERSION=$(docker --version)
        print_success "$DOCKER_VERSION"
    else
        print_warning "Docker 未安装 (可选)"
    fi
    
    # 检查 pre-commit
    if command_exists pre-commit; then
        PRECOMMIT_VERSION=$(pre-commit --version)
        print_success "$PRECOMMIT_VERSION"
    else
        missing_deps+=("pre-commit")
    fi
    
    # 如果有缺失的依赖，提示安装
    if [ ${#missing_deps[@]} -ne 0 ]; then
        print_error "缺少以下依赖："
        for dep in "${missing_deps[@]}"; do
            echo "  - $dep"
        done
        echo ""
        print_info "请参考 docs/setup-guide.md 安装缺失的依赖"
        exit 1
    fi
    
    echo ""
}

# 安装 Node.js 依赖
install_node_dependencies() {
    print_info "安装 Node.js 依赖..."
    
    if [ -f "pnpm-lock.yaml" ]; then
        pnpm install --frozen-lockfile
    else
        pnpm install
    fi
    
    print_success "Node.js 依赖安装完成"
    echo ""
}

# 设置 Python 环境
setup_python_env() {
    local service=$1
    local service_path="services/$service"
    
    if [ ! -d "$service_path" ]; then
        print_warning "服务目录不存在: $service_path"
        return
    fi
    
    print_info "设置 $service Python 环境..."
    
    cd "$service_path"
    
    # 创建虚拟环境
    if [ ! -d ".venv" ]; then
        uv venv
        print_success "虚拟环境创建完成"
    else
        print_info "虚拟环境已存在"
    fi
    
    # 激活虚拟环境并安装依赖
    source .venv/bin/activate
    uv pip install -e ".[dev]"
    deactivate
    
    print_success "$service Python 环境设置完成"
    cd - > /dev/null
    echo ""
}

# 设置所有 Python 服务
setup_all_python_services() {
    print_info "设置所有 Python 服务..."
    echo ""
    
    # 后端
    setup_python_env "backend"
    
    {% if cookiecutter.enable_ml_api == 'yes' -%}
    # ML API
    setup_python_env "ml-api"
    {% endif -%}
    
    {% if cookiecutter.enable_audio_api == 'yes' -%}
    # Audio API
    setup_python_env "audio-api"
    {% endif -%}
    
    {% if cookiecutter.enable_scraper == 'yes' -%}
    # Scraper
    setup_python_env "scraper"
    {% endif -%}
}

# 设置 pre-commit hooks
setup_pre_commit() {
    print_info "设置 pre-commit hooks..."
    
    pre-commit install
    
    print_success "pre-commit hooks 设置完成"
    echo ""
}

# 复制环境变量文件
setup_env_files() {
    print_info "设置环境变量文件..."
    
    # Backend
    if [ -f "services/backend/.env.example" ] && [ ! -f "services/backend/.env" ]; then
        cp services/backend/.env.example services/backend/.env
        print_success "已创建 services/backend/.env"
    fi
    
    # Frontend
    if [ -f "services/frontend/.env.example" ] && [ ! -f "services/frontend/.env" ]; then
        cp services/frontend/.env.example services/frontend/.env
        print_success "已创建 services/frontend/.env"
    fi
    
    {% if cookiecutter.enable_ml_api == 'yes' -%}
    # ML API
    if [ -f "services/ml-api/.env.example" ] && [ ! -f "services/ml-api/.env" ]; then
        cp services/ml-api/.env.example services/ml-api/.env
        print_success "已创建 services/ml-api/.env"
    fi
    {% endif -%}
    
    {% if cookiecutter.enable_audio_api == 'yes' -%}
    # Audio API
    if [ -f "services/audio-api/.env.example" ] && [ ! -f "services/audio-api/.env" ]; then
        cp services/audio-api/.env.example services/audio-api/.env
        print_success "已创建 services/audio-api/.env"
    fi
    {% endif -%}
    
    print_warning "请编辑 .env 文件填入实际配置"
    echo ""
}

# 启动基础设施服务
start_infrastructure() {
    if ! command_exists docker; then
        print_warning "Docker 未安装，跳过基础设施服务启动"
        return
    fi
    
    print_info "是否启动基础设施服务 (PostgreSQL, Redis, MinIO)? [y/N]"
    read -r response
    
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        print_info "启动基础设施服务..."
        docker-compose -f infra/docker-compose/dev.yml up -d
        print_success "基础设施服务启动完成"
        echo ""
        print_info "等待服务就绪..."
        sleep 5
    fi
}

# 运行数据库迁移
run_migrations() {
    if [ ! -f "services/backend/.env" ]; then
        print_warning "Backend .env 文件不存在，跳过数据库迁移"
        return
    fi
    
    print_info "是否运行数据库迁移? [y/N]"
    read -r response
    
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        print_info "运行数据库迁移..."
        cd services/backend
        source .venv/bin/activate
        alembic upgrade head
        deactivate
        cd - > /dev/null
        print_success "数据库迁移完成"
        echo ""
    fi
}

# 生成共享类型
generate_types() {
    print_info "是否生成共享 TypeScript 类型? [y/N]"
    read -r response
    
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        if [ -f "scripts/codegen.sh" ]; then
            print_info "生成共享类型..."
            bash scripts/codegen.sh
            print_success "类型生成完成"
            echo ""
        else
            print_warning "codegen.sh 脚本不存在"
        fi
    fi
}

# 打印完成消息
print_completion() {
    echo ""
    echo "╔════════════════════════════════════════════════════════════╗"
    echo "║                                                            ║"
    echo "║                🎉 项目初始化完成！                         ║"
    echo "║                                                            ║"
    echo "╚════════════════════════════════════════════════════════════╝"
    echo ""
    print_info "下一步："
    echo ""
    echo "  1. 编辑环境变量文件:"
    echo "     - services/backend/.env"
    echo "     - services/frontend/.env"
    echo ""
    echo "  2. 启动开发服务器:"
    echo "     pnpm dev"
    echo ""
    echo "  3. 访问应用:"
    echo "     - Frontend: http://localhost:3000"
    echo "     - Backend API: http://localhost:8000"
    echo "     - API Docs: http://localhost:8000/docs"
    echo ""
    echo "  4. 查看文档:"
    echo "     - docs/setup-guide.md"
    echo "     - docs/deployment.md"
    echo "     - README.md"
    echo ""
    print_success "祝您开发愉快！🚀"
    echo ""
}

# 主函数
main() {
    print_header
    check_prerequisites
    install_node_dependencies
    setup_all_python_services
    setup_pre_commit
    setup_env_files
    start_infrastructure
    run_migrations
    generate_types
    print_completion
}

# 运行主函数
main

