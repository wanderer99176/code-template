"""主 CLI 功能测试。"""

import pytest
from click.testing import CliRunner

from {{ cookiecutter.package_name }}.main import cli


def test_cli_help():
    """测试 CLI 帮助命令。"""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "{{ cookiecutter.project_name }}" in result.output


def test_cli_version():
    """测试 CLI 版本命令。"""
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "{{ cookiecutter.first_version }}" in result.output


def test_cli_hello():
    """测试 CLI hello 命令。"""
    runner = CliRunner()
    result = runner.invoke(cli, ["hello", "--name", "World"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.output
