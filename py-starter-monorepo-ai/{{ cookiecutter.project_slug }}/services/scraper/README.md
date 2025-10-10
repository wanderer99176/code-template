# {{ cookiecutter.project_name }} Scraper

基于 Scrapy 的网络爬虫服务。

## 快速开始

```bash
# 安装依赖
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"

# 运行爬虫
scrapy crawl example

# 输出到文件
scrapy crawl example -o output.json
```

## 创建新爬虫

```bash
# 使用模板创建
scrapy genspider my_spider example.com

# 手动创建
# 在 spiders/ 目录下创建 Python 文件
```

## 配置

编辑 `settings.py` 修改爬虫配置：

- `CONCURRENT_REQUESTS`: 并发请求数
- `DOWNLOAD_DELAY`: 下载延迟
- `USER_AGENT`: User-Agent
- `ITEM_PIPELINES`: 数据处理管道

## 分布式爬虫

使用 Scrapy-Redis 实现分布式：

```python
# settings.py
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
REDIS_URL = "redis://localhost:6379/1"
```

## 数据存储

在 `pipelines.py` 中实现数据存储逻辑：

```python
class PostgresPipeline:
    def process_item(self, item, spider):
        # 保存到 PostgreSQL
        return item
```

## 相关资源

- [Scrapy 文档](https://docs.scrapy.org/)
- [Scrapy-Redis](https://github.com/rmax/scrapy-redis)

