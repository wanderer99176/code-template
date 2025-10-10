# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## 🚀 Quick Start

This is a minimal viable product (MVP) template designed for rapid prototyping and idea validation.

### Prerequisites

- Python {{ cookiecutter.python_version }} or higher
- pip or uv package manager

### Installation

1. Clone or download this project
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -e .
   ```

### Usage

Run the main script directly:

```bash
python {{ cookiecutter.package_name }}.py
```

Or import and use in your own code:

```python
import {{ cookiecutter.package_name }}

# Your code here
```

## 📁 Project Structure

```
{{ cookiecutter.project_slug }}/
├── .gitignore
├── {{ cookiecutter.package_name }}.py    # Main script file
├── pyproject.toml                        # Project configuration
└── README.md                            # This file
```

## 🛠️ Development

This MVP template uses a flat layout structure for maximum simplicity:

- **Main script**: `{{ cookiecutter.package_name }}.py` - Start coding here!
- **Dependencies**: Defined in `pyproject.toml`
- **No complex structure** - Just start writing your code!

## 📝 Next Steps

1. Edit `{{ cookiecutter.package_name }}.py` to implement your idea
2. Add dependencies to `pyproject.toml` as needed
3. Test your script: `python {{ cookiecutter.package_name }}.py`
4. Iterate and refine your MVP

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
