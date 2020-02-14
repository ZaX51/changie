import click
from .changie import Changie

@click.group()
def main():
    pass

@main.command()
@click.option('-m', '--message', default='', help='message')
def add(message):
    Changie.create_changelog_item(message)

@main.command()
@click.option('-v', '--version', default='New version', help='message')
def generate(version):
    Changie.generate(version)
