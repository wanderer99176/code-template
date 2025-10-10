# Dockerfile for {{ cookiecutter.project_name }}

# --- Stage 1: Builder ---
FROM python:{{ cookiecutter.python_version }}-slim AS builder
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:${PATH}"
WORKDIR /app
COPY pyproject.toml .
# 使用 --system 将包装在全局site-packages中，方便复制
RUN uv pip install --system --no-cache .

# --- Stage 2: Final ---
FROM python:{{ cookiecutter.python_version }}-slim

# 创建一个非root用户并切换
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /home/appuser/app

# 从构建阶段复制已安装的依赖
COPY --from=builder /usr/local/lib/python{{ cookiecutter.python_version }}/site-packages /usr/local/lib/python{{ cookiecutter.python_version }}/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# 复制源代码
COPY ./src/{{ cookiecutter.package_name }} ./{{ cookiecutter.package_name }}

# 更改文件所有权为新用户
RUN chown -R appuser:appuser /home/appuser/app

# 切换到非root用户
USER appuser

EXPOSE 8000
# 使用非特权端口 (>1024)
CMD ["uvicorn", "{{ cookiecutter.package_name }}.__main__:app", "--host", "0.0.0.0", "--port", "8000"]
