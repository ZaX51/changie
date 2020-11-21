from datetime import datetime
import os
from .utils import write_file, read_file
from .changelog_generator import generate
from .config import Config
from .changelog_items_repository import ChangelogItemsRepository

def create_changelog_item(message):
    config = Config()
    config.load()
    repository = ChangelogItemsRepository(config)

    repository.add(message)

    print('File added')

def preview_changelog(version):
    config = Config()
    config.load()
    repository = ChangelogItemsRepository(config)

    print(generate(version, repository.get_all()))

def update_changelog(version):
    config = Config()
    config.load()
    repository = ChangelogItemsRepository(config)

    __update_changelog(config.config['ChangelogFileName'], generate(version, repository.get_all()))
    repository.remove_all()

    print('Changelog updated')

def __update_changelog(changelog_file_name, new_version_changelog):
    current_changelog = ''

    try:
        current_changelog = read_file(changelog_file_name)
    except FileNotFoundError:
        print('CHANGELOG.md not found, creating file')
    finally:
        updated_changelog = new_version_changelog + '\n' + current_changelog
        write_file(changelog_file_name, updated_changelog)
