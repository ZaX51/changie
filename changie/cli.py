import click
from datetime import datetime

@click.group()
def main():
    pass

@main.command()
@click.option('-m', '--message', default='', help='message')
@click.option('-t', '--type', default='Added', help='message type', type=click.Choice(['Added', 'Changed'], case_sensitive=False))
def add(message, type):
    create_changelog_item(message, type)

def create_changelog_item(message, type):
    with open('chg_{}_{}.md'.format(datetime.now().timestamp(), type), 'w+') as f:
        f.write(message)
