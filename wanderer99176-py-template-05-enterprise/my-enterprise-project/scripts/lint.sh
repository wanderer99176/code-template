#!/bin/bash
# Linter运行脚本

set -e

echo ">>> Running linter..."
uv run ruff check .
echo "✅ Linting completed."
