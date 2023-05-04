import click
from changie.change_file_builder import ChangeType
from changie.change_files_repository import ChangeFilesRepository
from changie.config import Config
from .changie import Changie

changie: Changie = None


@click.group()
@click.option("-c", "--config", "config_path", help="Config path")
def main(config_path: str = None):
    global changie

    config = Config()
    config.load(config_path)

    repository = ChangeFilesRepository(config)

    changie = Changie(config, repository)


@main.command()
@click.option("-m", "--message", required=True, help="Message")
@click.option(
    "-t",
    "--type",
    default=ChangeType.Added.value,
    type=click.Choice(list(map(lambda x: x.value, ChangeType))),
    help="Message type",
    show_default=True,
)
def add(message: str, type: str):
    name = changie.create_changelog_item(message, type)
    print(f"File {name} added")


@main.command()
@click.option(
    "-v",
    "--version",
    default="0.0.0",
    help="Release version",
    show_default=True,
)
def preview(version: str):
    print(changie.preview_changelog(version))


@main.command()
@click.option(
    "-v",
    "--version",
    default="0.0.0",
    help="Release version",
    show_default=True,
)
def update(version: str):
    changie.update_changelog(version)
    print("Changelog updated")
