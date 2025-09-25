"""Tests for main CLI functionality."""

import pytest
from click.testing import CliRunner

from {{ cookiecutter.package_name }}.main import cli


def test_cli_help():
    """Test CLI help command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "{{ cookiecutter.project_name }}" in result.output


def test_cli_version():
    """Test CLI version command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "{{ cookiecutter.first_version }}" in result.output


def test_cli_hello():
    """Test CLI hello command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["hello", "--name", "World"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.output
