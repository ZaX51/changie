from changie.changelog_item_builder import ItemType
from .utils import write_file, read_file
from .changelog_builder import ChangelogBuilder
from .config import Config, ConfigKey
from .changelog_items_repository import ChangelogItemsRepository


def create_changelog_item(message: str, type: str):
    config = Config()
    config.load()
    repository = ChangelogItemsRepository(config)

    return repository.add(message, ItemType(type))


def preview_changelog(version: str):
    config = Config()
    config.load()
    repository = ChangelogItemsRepository(config)

    return __construct_changelog(version, repository.get_all())


def update_changelog(version: str):
    config = Config()
    config.load()
    repository = ChangelogItemsRepository(config)

    __update_changelog(
        config.get(ConfigKey.ChangelogFileName),
        __construct_changelog(version, repository.get_all()),
    )

    repository.remove_all()


def __construct_changelog(version: str, items):
    builder = ChangelogBuilder()

    builder.add_header(version)
    builder.add_changes_list(items)

    return builder.get()


def __update_changelog(changelog_file_name: str, new_version_changelog: str):
    current_changelog = ""

    try:
        current_changelog = read_file(changelog_file_name)
    except FileNotFoundError:
        print("CHANGELOG.md not found, creating file")
    finally:
        updated_changelog = new_version_changelog + "\n" + current_changelog
        write_file(changelog_file_name, updated_changelog)
