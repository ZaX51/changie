from datetime import datetime
import os
from .utils import write_file, read_file
from .changelog_generator import generate
from .config import get_config

def create_changelog_item(message):
    config = get_config()
    item_prefix = config['ChangelogItemPrefix']
    item_extension = config['ChangelogItemExtension']
    
    write_file(f'{item_prefix}_{datetime.now().timestamp()}{item_extension}', message)

    print('File added')

def preview_changelog(version):
    config = get_config()

    changelog_items_names = __get_changelog_items_names(
        config['ChangelogItemPrefix'],
        config['ChangelogItemExtension']
    )

    if len(changelog_items_names) == 0:
        print('Empty changelog')
        return

    print(generate(version, __get_changelog_items_content(changelog_items_names)))

def update_changelog(version):
    config = get_config()

    changelog_items_names = __get_changelog_items_names(
        config['ChangelogItemPrefix'],
        config['ChangelogItemExtension']
    )

    if len(changelog_items_names) == 0:
        print('Empty changelog')
        return

    __update_changelog(config['ChangelogFileName'], generate(version, __get_changelog_items_content(changelog_items_names)))
    __remove_changelog_items(changelog_items_names)

    print('Changelog updated')

def __get_changelog_items_names(item_prefix, item_extension):
    return list(filter(
        lambda file_name: file_name.startswith(item_prefix) and file_name.endswith(item_extension),
        os.listdir(os.getcwd())
    ))

def __get_changelog_items_content(changelog_items_names):
    return list(map(lambda file_name: read_file(file_name), changelog_items_names))

def __update_changelog(changelog_file_name, new_version_changelog):
    current_changelog = ''

    try:
        current_changelog = read_file(changelog_file_name)
    except FileNotFoundError:
        print('CHANGELOG.md not found, creating file')
    finally:
        updated_changelog = new_version_changelog + '\n' + current_changelog
        write_file(changelog_file_name, updated_changelog)

def __remove_changelog_items(file_names):
    for filename in file_names:
        os.remove(filename)