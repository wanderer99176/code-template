"""{{ cookiecutter.project_name }} 的主 CLI 入口点。"""

import click


@click.group()
@click.version_option(version="{{ cookiecutter.first_version }}")
def cli():
    """{{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}"""
    pass


@cli.command()
@click.option("--name", default="World", help="要问候的名字")
def hello(name: str):
    """向某人问好。"""
    click.echo(f"Hello, {name}!")


if __name__ == "__main__":
    cli()
