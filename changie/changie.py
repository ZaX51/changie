from datetime import datetime
import os
from .common import write_file, read_file

CHANGELOG_FILE_NAME = 'CHANGELOG.md';
CHANGELOG_ITEM_PREFIX = 'chg';
CHANGELOG_ITEM_EXTENSION = '.md';

class Changie(object):
    @staticmethod
    def create_changelog_item(message):
        write_file(f'{CHANGELOG_ITEM_PREFIX}_{datetime.now().timestamp()}{CHANGELOG_ITEM_EXTENSION}', message)

    @staticmethod
    def generate(version):
        files = os.listdir(os.getcwd())
        filtered_files = list(filter(lambda f: f.startswith(CHANGELOG_ITEM_PREFIX) and f.endswith(CHANGELOG_ITEM_EXTENSION), files))

        if len(filtered_files) == 0:
            print('No changelog items')
            return

        new_changelog = f'## {version}\n\n'
        for filename in filtered_files:
            changelog_item = read_file(filename)
            new_changelog += f'* {changelog_item}\n'
            os.remove(filename)
        
        current_changelog = read_file(CHANGELOG_FILE_NAME)
        new_changelog += f'\n{current_changelog}'

        write_file(CHANGELOG_FILE_NAME, new_changelog)
