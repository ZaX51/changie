import click
from changie.changelog_item_builder import ItemType
from .changie import update_changelog, create_changelog_item, preview_changelog


@click.group()
def main():
    pass


@main.command()
@click.option("-m", "--message", required=True, help="Message")
@click.option(
    "-t",
    "--type",
    default=ItemType.Added.value,
    type=click.Choice(list(map(lambda x: x.value, ItemType))),
)
def add(message: str, type: str):
    name = create_changelog_item(message, type)
    print(f"File {name} added")


@main.command()
@click.option("-v", "--version", default="0.0.0", help="Release version")
def preview(version: str):
    print(preview_changelog(version))


@main.command()
@click.option("-v", "--version", default="0.0.0", help="Release version")
def update(version: str):
    update_changelog(version)
    print("Changelog updated")
