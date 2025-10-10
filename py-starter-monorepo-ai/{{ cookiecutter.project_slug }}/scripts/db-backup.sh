#!/usr/bin/env bash

# 数据库备份脚本
# 自动备份 PostgreSQL 数据库并上传到 S3
{% raw %}
set -e

# 配置
BACKUP_DIR="${BACKUP_DIR:-./backups}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="${BACKUP_DIR}/backup_${TIMESTAMP}.sql.gz"
RETENTION_DAYS="${RETENTION_DAYS:-7}"

# 从 .env 文件加载配置
if [ -f "services/backend/.env" ]; then
    source services/backend/.env
fi

# 数据库配置
DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"
DB_NAME="${DB_NAME:-{{ cookiecutter.database_name }}}"
DB_USER="${DB_USER:-{{ cookiecutter.database_user }}}"
DB_PASSWORD="${DB_PASSWORD}"

# S3 配置（可选）
S3_BUCKET="${S3_BUCKET}"
S3_PREFIX="${S3_PREFIX:-backups}"

# 颜色
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}🗄️  开始数据库备份...${NC}"
echo "数据库: $DB_NAME"
echo "时间戳: $TIMESTAMP"
echo ""

# 创建备份目录
mkdir -p "$BACKUP_DIR"

# 执行备份
echo -e "${BLUE}📦 正在备份数据库...${NC}"
PGPASSWORD="$DB_PASSWORD" pg_dump \
    -h "$DB_HOST" \
    -p "$DB_PORT" \
    -U "$DB_USER" \
    -d "$DB_NAME" \
    --no-owner \
    --no-acl \
    | gzip > "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    BACKUP_SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    echo -e "${GREEN}✅ 备份完成${NC}"
    echo "文件: $BACKUP_FILE"
    echo "大小: $BACKUP_SIZE"
else
    echo -e "${RED}❌ 备份失败${NC}"
    exit 1
fi

# 上传到 S3（如果配置了）
if [ -n "$S3_BUCKET" ]; then
    echo ""
    echo -e "${BLUE}☁️  上传到 S3...${NC}"
    
    aws s3 cp "$BACKUP_FILE" "s3://${S3_BUCKET}/${S3_PREFIX}/backup_${TIMESTAMP}.sql.gz"
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ 上传成功${NC}"
    else
        echo -e "${RED}⚠️  上传失败${NC}"
    fi
fi

# 清理旧备份
echo ""
echo -e "${BLUE}🧹 清理旧备份...${NC}"
find "$BACKUP_DIR" -name "backup_*.sql.gz" -type f -mtime +$RETENTION_DAYS -delete
echo -e "${GREEN}✅ 已删除 ${RETENTION_DAYS} 天前的备份${NC}"

# 如果配置了 S3，也清理 S3 中的旧备份
if [ -n "$S3_BUCKET" ]; then
    CUTOFF_DATE=$(date -d "$RETENTION_DAYS days ago" +%Y-%m-%d)
    aws s3 ls "s3://${S3_BUCKET}/${S3_PREFIX}/" | \
        awk '{print $4}' | \
        while read file; do
            FILE_DATE=$(echo "$file" | grep -oP '\d{8}' | head -1)
            FILE_DATE_FORMATTED=$(date -d "${FILE_DATE:0:4}-${FILE_DATE:4:2}-${FILE_DATE:6:2}" +%Y-%m-%d)
            if [[ "$FILE_DATE_FORMATTED" < "$CUTOFF_DATE" ]]; then
                aws s3 rm "s3://${S3_BUCKET}/${S3_PREFIX}/$file"
                echo "已删除 S3 中的旧备份: $file"
            fi
        done
fi

echo ""
echo -e "${GREEN}🎉 备份流程完成！${NC}"
echo ""

# 显示备份列表
echo "本地备份列表:"
ls -lh "$BACKUP_DIR"/backup_*.sql.gz | tail -5

if [ -n "$S3_BUCKET" ]; then
    echo ""
    echo "S3 备份列表:"
    aws s3 ls "s3://${S3_BUCKET}/${S3_PREFIX}/" | tail -5
fi

echo ""
{% endraw %}

