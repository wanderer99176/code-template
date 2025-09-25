"""Main application entry point for {{ cookiecutter.project_name }}."""

import uvicorn
from fastapi import FastAPI

from {{ cookiecutter.package_name }}.core import get_app


def run_dev_server(host: str = "0.0.0.0", port: int = 8000, reload: bool = True) -> None:
    """Run the development server."""
    app = get_app()
    uvicorn.run(app, host=host, port=port, reload=reload)


if __name__ == "__main__":
    run_dev_server()
