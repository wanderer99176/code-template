#!/usr/bin/env bash

# 模板重命名脚本
# 将旧的命名方式改为新的语义化命名

set -e

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Python Starter Templates 重命名工具${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# 定义重命名映射
declare -A RENAME_MAP=(
    ["wanderer99176-py-template-01-mvp"]="py-starter-minimal"
    ["wanderer99176-py-template-02-small"]="py-starter-cli"
    ["wanderer99176-py-template-03-medium"]="py-starter-api"
    ["wanderer99176-py-template-05-enterprise"]="py-starter-enterprise"
    ["wanderer99176-py-template-06-project01"]="py-starter-monorepo-ai"
)

# 获取当前目录
CURRENT_DIR=$(pwd)

echo -e "${YELLOW}当前目录: ${CURRENT_DIR}${NC}"
echo ""
echo -e "${YELLOW}即将执行以下重命名操作:${NC}"
echo ""

# 显示重命名计划
for old_name in "${!RENAME_MAP[@]}"; do
    new_name="${RENAME_MAP[$old_name]}"
    if [ -d "$old_name" ]; then
        echo -e "  ${GREEN}✓${NC} $old_name → $new_name"
    else
        echo -e "  ${YELLOW}⚠${NC} $old_name (不存在，跳过)"
    fi
done

echo ""
read -p "是否继续？[y/N] " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}操作已取消${NC}"
    exit 0
fi

echo ""
echo -e "${BLUE}开始重命名...${NC}"
echo ""

# 执行重命名
SUCCESS_COUNT=0
SKIP_COUNT=0

for old_name in "${!RENAME_MAP[@]}"; do
    new_name="${RENAME_MAP[$old_name]}"
    
    if [ -d "$old_name" ]; then
        echo -e "${BLUE}重命名:${NC} $old_name → $new_name"
        mv "$old_name" "$new_name"
        ((SUCCESS_COUNT++))
        echo -e "${GREEN}✓ 完成${NC}"
    else
        echo -e "${YELLOW}⚠ 跳过:${NC} $old_name (目录不存在)"
        ((SKIP_COUNT++))
    fi
    echo ""
done

echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✓ 重命名完成！${NC}"
echo ""
echo -e "  成功: ${GREEN}${SUCCESS_COUNT}${NC} 个"
echo -e "  跳过: ${YELLOW}${SKIP_COUNT}${NC} 个"
echo ""
echo -e "${BLUE}下一步:${NC}"
echo -e "  1. 检查重命名结果: ${YELLOW}ls -la${NC}"
echo -e "  2. 更新 Git 仓库: ${YELLOW}git add . && git commit -m 'refactor: rename templates to semantic names'${NC}"
echo -e "  3. 推送到远程: ${YELLOW}git push${NC}"
echo ""
echo -e "${BLUE}========================================${NC}"

