# Makefile for {{ cookiecutter.project_name }}

.PHONY: help install lint format test run build clean

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	@echo ">>> Creating venv and syncing dependencies..."
	uv venv --python {{ cookiecutter.python_version }}
	uv pip sync pyproject.toml --extra dev
	@echo "✅ Done."

lint: ## Run linter
	@echo ">>> Running linter..."
	uv run ruff check .

format: ## Format code
	@echo ">>> Formatting code..."
	uv run ruff format .

test: ## Run tests
	@echo ">>> Running tests..."
	uv run pytest

run: ## Start the application
	@echo ">>> Starting the application..."
	uv run run-app

build: ## Build package
	@echo ">>> Building package..."
	uv run python -m build

clean: ## Clean up temporary files
	@echo ">>> Cleaning up..."
	rm -rf .venv dist build *.egg-info .pytest_cache .coverage
	find . -type d -name "__pycache__" -exec rm -r {} +
