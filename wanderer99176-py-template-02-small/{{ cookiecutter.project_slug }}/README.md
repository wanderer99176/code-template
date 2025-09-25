# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## 🚀 Installation

### From PyPI (when published)

```bash
pip install {{ cookiecutter.project_slug }}
```

### From Source

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
pip install -e .
```

## 📖 Usage

### Command Line Interface

{{ cookiecutter.project_name }} provides a simple CLI tool:

```bash
# Show help
{{ cookiecutter.package_name }} --help

# Show version
{{ cookiecutter.package_name }} --version

# Run a command
{{ cookiecutter.package_name }} hello --name "World"
```

### As a Python Library

You can also import and use {{ cookiecutter.project_name }} in your Python code:

```python
from {{ cookiecutter.package_name }}.main import cli

# Use the CLI programmatically
cli(["hello", "--name", "Python"])
```

## 📁 Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/
│   └── {{ cookiecutter.package_name }}/
│       ├── __init__.py
│       └── main.py          # CLI entry point
├── tests/
│   ├── __init__.py
│   └── test_main.py         # Test suite
├── .gitignore
├── pyproject.toml           # Project configuration
└── README.md               # This file
```

## 🛠️ Development

### Prerequisites

- Python {{ cookiecutter.python_version }} or higher
- pip or uv package manager

### Setup Development Environment

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

3. Install in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

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

## 📝 Features

- **Simple CLI Interface**: Easy-to-use command line tool
- **Modular Design**: Clean separation of concerns
- **Test Coverage**: Comprehensive test suite
- **Modern Python**: Uses latest Python features and best practices

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the {{ cookiecutter.license }} License.
