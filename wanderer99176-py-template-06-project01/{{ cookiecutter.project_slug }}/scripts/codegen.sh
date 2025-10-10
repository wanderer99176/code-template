#!/usr/bin/env bash

# 代码生成脚本
# 从 FastAPI 后端生成 OpenAPI 规范并转换为 TypeScript 类型

set -e

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}🔄 开始生成共享类型...${NC}"

# 1. 确保后端虚拟环境存在
if [ ! -d "services/backend/.venv" ]; then
    echo -e "${YELLOW}⚠️  后端虚拟环境不存在，请先运行 setup.sh${NC}"
    exit 1
fi

# 2. 启动后端服务器（临时）
echo -e "${BLUE}📡 启动临时后端服务器...${NC}"
cd services/backend
source .venv/bin/activate

# 在后台启动服务器
uvicorn {{ cookiecutter.package_name }}.main:app --host 0.0.0.0 --port 8000 &
SERVER_PID=$!

# 等待服务器启动
echo "⏳ 等待服务器就绪..."
sleep 5

# 3. 下载 OpenAPI 规范
echo -e "${BLUE}📥 下载 OpenAPI 规范...${NC}"
cd ../..
curl -s http://localhost:8000/openapi.json > packages/shared-types/openapi.json

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ OpenAPI 规范下载成功${NC}"
else
    echo "❌ 下载失败"
    kill $SERVER_PID
    exit 1
fi

# 4. 关闭临时服务器
echo "🛑 关闭临时服务器..."
kill $SERVER_PID

# 5. 生成 TypeScript 类型
echo -e "${BLUE}🔨 生成 TypeScript 类型...${NC}"
cd packages/shared-types

# 使用 openapi-typescript 生成类型
pnpm exec openapi-typescript openapi.json -o types.ts

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ TypeScript 类型生成成功${NC}"
else
    echo "❌ 类型生成失败"
    exit 1
fi

# 6. 格式化生成的代码
echo -e "${BLUE}🎨 格式化代码...${NC}"
pnpm exec prettier --write types.ts

cd ../..

echo ""
echo -e "${GREEN}🎉 代码生成完成！${NC}"
echo ""
echo "生成的文件:"
echo "  - packages/shared-types/openapi.json"
echo "  - packages/shared-types/types.ts"
echo ""

