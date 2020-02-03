import click
from datetime import datetime
import os

@click.group()
def main():
    pass

@main.command()
@click.option('-m', '--message', default='', help='message')
def add(message):
    create_changelog_item(message)

def create_changelog_item(message):
    write_file('chg_{}.md'.format(datetime.now().timestamp()), message)

@main.command()
@click.option('-v', '--version', default='New version', help='message')
def generate(version):
    new_changelog = '## {}\n\n'.format(version)
    should_update = False

    for filename in os.listdir(os.getcwd()):
        name, file_extension = os.path.splitext(filename)
        if file_extension == '.md' and filename.startswith('chg'):
            should_update = True

            new_changelog += '* {}\n'.format(read_file(filename))
            os.remove(filename)
    
    if should_update == True:
        current_changelog = read_file('CHANGELOG.md')
        new_changelog += '\n'+ current_changelog

        write_file('CHANGELOG.md', new_changelog)
        

def read_file(file):
    with open(file, 'r') as f:
        return f.read()

def write_file(file, s):
    with open(file, 'w+') as f:
        return f.write(s)