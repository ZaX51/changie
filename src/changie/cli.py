import click
from changie.changelog_item_builder import ItemType
from changie.changelog_items_repository import ChangelogItemsRepository
from changie.config import Config
from .changie import Changie

changie: Changie = None


@click.group()
@click.option("-c", "--config", "config_path", help="Config path")
def main(config_path: str = None):
    global changie

    config = Config()
    config.load(config_path)

    repository = ChangelogItemsRepository(config)

    changie = Changie(config, repository)


@main.command()
@click.option("-m", "--message", required=True, help="Message")
@click.option(
    "-t",
    "--type",
    default=ItemType.Added.value,
    type=click.Choice(list(map(lambda x: x.value, ItemType))),
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
