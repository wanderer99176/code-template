# {{ cookiecutter.project_name }}

[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yml)

{{ cookiecutter.project_short_description }}

## 🚀 Quick Start

### Prerequisites

- Python {{ cookiecutter.python_version }} or higher
- pip or uv package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
   cd {{ cookiecutter.project_slug }}
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Copy environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

### Running the Application

Start the development server:

```bash
# Using the CLI command
run-dev

# Or directly with uvicorn
uvicorn {{ cookiecutter.package_name }}.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive API docs**: http://localhost:8000/docs
- **Alternative API docs**: http://localhost:8000/redoc

## 📖 API Usage

### Health Check

```bash
curl http://localhost:8000/health
```

### Root Endpoint

```bash
curl http://localhost:8000/
```

## 📁 Project Structure

```
{{ cookiecutter.project_slug }}/
├── .github/
│   └── workflows/
│       └── ci.yml           # CI/CD configuration
├── scripts/
│   └── run_dev_server.sh    # Development server script
├── src/
│   └── {{ cookiecutter.package_name }}/
│       ├── __init__.py
│       ├── main.py          # FastAPI application
│       ├── core.py          # Core application logic
│       └── models.py        # Pydantic models
├── tests/
│   ├── __init__.py
│   └── test_core.py         # Test suite
├── .env.example             # Environment variables template
├── .gitignore
├── Dockerfile               # Container configuration
├── pyproject.toml           # Project configuration
└── README.md               # This file
```

## 🛠️ Development

### Running Tests

```bash
pytest
```

### Code Quality

This project uses `ruff` for linting and formatting:

```bash
# Check code style
ruff check .

# Format code
ruff format .
```

### Docker Support

Build and run with Docker:

```bash
# Build the image
docker build -t {{ cookiecutter.project_slug }} .

# Run the container
docker run -p 8000:8000 {{ cookiecutter.project_slug }}
```

## 📝 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Automatic API Documentation**: Interactive docs at `/docs`
- **Type Safety**: Full type hints with Pydantic models
- **Testing**: Comprehensive test suite with pytest
- **CI/CD**: GitHub Actions workflow for automated testing
- **Docker Support**: Containerized deployment ready
- **Environment Configuration**: Flexible configuration management

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the {{ cookiecutter.license }} License.
