"""Main CLI entry point for {{ cookiecutter.project_name }}."""

import click


@click.group()
@click.version_option(version="{{ cookiecutter.first_version }}")
def cli():
    """{{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}"""
    pass


@cli.command()
@click.option("--name", default="World", help="Name to greet")
def hello(name: str):
    """Say hello to someone."""
    click.echo(f"Hello, {name}!")


if __name__ == "__main__":
    cli()
