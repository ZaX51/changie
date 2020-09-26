from datetime import datetime
import os
from .utils import write_file, read_file
from .changelog_generator import ChangelogGenerator

CHANGELOG_FILE_NAME = 'CHANGELOG.md';
CHANGELOG_ITEM_PREFIX = 'chg';
CHANGELOG_ITEM_EXTENSION = '.md';

def create_changelog_item(message):
    write_file(f'{CHANGELOG_ITEM_PREFIX}_{datetime.now().timestamp()}{CHANGELOG_ITEM_EXTENSION}', message)

    print('File added')

def update_changelog(version):
    changelog_items_names = __get_changelog_items_names()

    if len(changelog_items_names) == 0:
        print('Empty changelog for new version')
        return

    changelog_generator = ChangelogGenerator()

    changelog_generator.generate(version, __get_changelog_items(changelog_items_names))

    __update_changelog(changelog_generator.get_changelog())
    __remove_changelog_items(changelog_items_names)

    print('Changelog updated')

def __get_changelog_items_names():
    return list(filter(
        lambda file_name: file_name.startswith(CHANGELOG_ITEM_PREFIX) and file_name.endswith(CHANGELOG_ITEM_EXTENSION),
        os.listdir(os.getcwd())
    ))

def __get_changelog_items(changelog_items_names):
    return list(map(lambda file_name: read_file(file_name), changelog_items_names))

def __update_changelog(new_version_changelog):
    current_changelog = ''

    try:
        current_changelog = read_file(CHANGELOG_FILE_NAME)
    except FileNotFoundError:
        print('CHANGELOG.md not found, creating file')
    finally:
        updated_changelog = new_version_changelog + '\n' + current_changelog
        write_file(CHANGELOG_FILE_NAME, updated_changelog)

def __remove_changelog_items(file_names):
    for filename in file_names:
        os.remove(filename)