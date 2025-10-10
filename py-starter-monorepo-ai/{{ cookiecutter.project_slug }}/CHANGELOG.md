# Changelog

本文档记录项目的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### 新增
- 初始项目结构
- FastAPI 后端服务
- Nuxt 3 前端应用
{% if cookiecutter.enable_ml_api == 'yes' -%}
- YOLOv8 目标检测 API
{% endif -%}
{% if cookiecutter.enable_audio_api == 'yes' -%}
- Whisper 音频转录 API
{% endif -%}
{% if cookiecutter.enable_scraper == 'yes' -%}
- Scrapy 网络爬虫
{% endif -%}
- Docker 和 Kubernetes 配置
- CI/CD 流水线
- 完整的文档

## [{{ cookiecutter.version }}] - 2025-10-10

### 新增
- 项目初始化

[Unreleased]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/compare/v{{ cookiecutter.version }}...HEAD
[{{ cookiecutter.version }}]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/releases/tag/v{{ cookiecutter.version }}

