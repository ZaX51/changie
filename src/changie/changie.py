from datetime import datetime
from changie.change_file_builder import ChangeType
from .utils import write_file, read_file
from .changelog_builder import ChangelogBuilder
from .config import Config, ConfigKey
from .change_files_repository import ChangeFilesRepository


class Changie:
    def __init__(self, config: Config, repository: ChangeFilesRepository):
        self.config = config
        self.repository = repository

    def create_changelog_item(self, message: str, type: str):
        return self.repository.add(message, ChangeType(type))

    def preview_changelog(self, version: str):
        return self.__construct_changelog(version, self.repository.get_all())

    def update_changelog(self, version: str):
        self.__update_changelog(
            self.config.get(ConfigKey.ChangelogFileName),
            self.__construct_changelog(version, self.repository.get_all()),
        )

        self.repository.remove_all()

    def __construct_changelog(self, version: str, items):
        builder = ChangelogBuilder()

        builder.add_header(version, datetime.now())
        builder.add_changes_list(items)

        return builder.get()

    def __update_changelog(self, changelog_file_name: str, new_version_changelog: str):
        current_changelog = ""

        try:
            current_changelog = read_file(changelog_file_name)
        except FileNotFoundError:
            print("CHANGELOG.md not found, creating file")
        finally:
            updated_changelog = new_version_changelog + "\n" + current_changelog
            write_file(changelog_file_name, updated_changelog)
