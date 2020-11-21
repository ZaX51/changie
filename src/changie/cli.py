import click
from .changie import update_changelog, create_changelog_item, preview_changelog

@click.group()
def main():
    pass

@main.command()
@click.option('-m', '--message', default='Message', help='message')
def add(message):
    name = create_changelog_item(message)
    print(f'File {name} added')

@main.command()
@click.option('-v', '--version', default='New version', help='message')
def preview(version):
    print(preview_changelog(version))

@main.command()
@click.option('-v', '--version', default='New version', help='message')
def update(version):
    update_changelog(version)
    print('Changelog updated')
