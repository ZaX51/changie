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
    changelog_items = __get_changelog_items(changelog_items_names)

    if len(changelog_items) == 0:
        print('Empty changelog for new version')
        return

    new_version_changelog = __generate_new_version_changelog(version, changelog_items)

    __update_changelog(new_version_changelog)
    __remove_changelog_items(changelog_items_names)

    print('Changelog updated')

def __get_changelog_items_names():
    return list(filter(__is_changelog_item, __get_files_names_in_directory()))

def __get_changelog_items(changelog_items_names):
    return list(map(lambda f: read_file(f), changelog_items_names))

def __is_changelog_item(file_name: str):
    return file_name.startswith(CHANGELOG_ITEM_PREFIX) and file_name.endswith(CHANGELOG_ITEM_EXTENSION)

def __get_files_names_in_directory():
    return os.listdir(os.getcwd())

def __generate_new_version_changelog(version, changelog_items):
    changelog_generator = ChangelogGenerator()

    changelog_generator.generate(version, changelog_items)

    return changelog_generator.get_changelog()

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