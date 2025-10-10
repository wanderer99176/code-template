"""
Scrapy 设置

详细配置请参考: https://docs.scrapy.org/en/latest/topics/settings.html
"""

BOT_NAME = "{{ cookiecutter.scraper_name }}"

SPIDER_MODULES = ["{{ cookiecutter.scraper_name }}.spiders"]
NEWSPIDER_MODULE = "{{ cookiecutter.scraper_name }}.spiders"

# 遵守 robots.txt 规则
ROBOTSTXT_OBEY = True

# 并发请求数
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# 下载延迟 (秒)
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True

# User-Agent
USER_AGENT = "{{ cookiecutter.project_name }} Bot/{{ cookiecutter.version }}"

# 中间件
DOWNLOADER_MIDDLEWARES = {
    "{{ cookiecutter.scraper_name }}.middlewares.{{ cookiecutter.scraper_name.title().replace('_', '') }}DownloaderMiddleware": 543,
}

SPIDER_MIDDLEWARES = {
    "{{ cookiecutter.scraper_name }}.middlewares.{{ cookiecutter.scraper_name.title().replace('_', '') }}SpiderMiddleware": 543,
}

# Item 处理管道
ITEM_PIPELINES = {
    "{{ cookiecutter.scraper_name }}.pipelines.{{ cookiecutter.scraper_name.title().replace('_', '') }}Pipeline": 300,
}

# 日志级别
LOG_LEVEL = "INFO"

# 请求头
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

# Scrapy-Redis 配置（分布式爬虫）
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# REDIS_URL = "redis://localhost:6379/1"

