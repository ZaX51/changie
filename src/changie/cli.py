import click
from .changie import generate, create_changelog_item

@click.group()
def main():
    pass

@main.command()
@click.option('-m', '--message', default='', help='message')
def add(message):
    create_changelog_item(message)

@main.command()
@click.option('-v', '--version', default='New version', help='message')
def generate(version):
    generate(version)
