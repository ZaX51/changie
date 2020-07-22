from datetime import datetime
import os
from .utils import write_file, read_file

CHANGELOG_FILE_NAME = 'CHANGELOG.md';
CHANGELOG_ITEM_PREFIX = 'chg';
CHANGELOG_ITEM_EXTENSION = '.md';

def create_changelog_item(message):
    write_file(f'{CHANGELOG_ITEM_PREFIX}_{datetime.now().timestamp()}{CHANGELOG_ITEM_EXTENSION}', message)

def generate(version):
    changelog_items_file_names = __get_changelog_items_file_names()

    if len(changelog_items_file_names) == 0:
        print('Empty changelog for new version')
        return

    new_version_changelog = __generate_new_version_changelog(version, changelog_items_file_names)
    
    __update_changelog(new_version_changelog)

def __get_changelog_items_file_names():
    files_names = os.listdir(os.getcwd())
    return list(filter(lambda f: f.startswith(CHANGELOG_ITEM_PREFIX) and f.endswith(CHANGELOG_ITEM_EXTENSION), files_names))

def __generate_new_version_changelog(version, filtered_files):
    new_version_changelog = f'## {version}\n\n'

    for filename in filtered_files:
        changelog_item = read_file(filename)
        new_version_changelog += f'* {changelog_item}\n'
        os.remove(filename)
    
    return new_version_changelog

def __update_changelog(new_version_changelog):
    current_changelog = read_file(CHANGELOG_FILE_NAME)
    new_version_changelog += f'\n{current_changelog}'

    write_file(CHANGELOG_FILE_NAME, new_version_changelog)
