from datetime import datetime
import os
from .utils import write_file, read_file
from .config import Config

class ChangelogItemsRepository:
    def __init__(self, config: Config):
        self.config = config

    def add(self, message):
        file_name = '{prefix}_{timestamp}{extension}'.format(
            prefix = self.config.get_changelog_item_prefix(),
            timestamp = datetime.now().timestamp(),
            extension = self.config.get_changelog_item_extension()
        )

        write_file(self.__get_file_path(file_name), message)

        return file_name

    def get_all(self):
        items = []

        for file_name in self.__get_items_dir():
            if not self.__is_changelog_item(file_name):
                continue

            items.append(read_file(self.__get_file_path(file_name)))

        return items

    def remove_all(self):
        for file_name in self.__get_items_dir():
            if self.__is_changelog_item(file_name):
                os.remove(self.__get_file_path(file_name))

    def __is_changelog_item(self, file_name):
        return file_name.startswith(self.config.get_changelog_item_prefix()) and file_name.endswith(self.config.get_changelog_item_extension())

    def __get_items_dir(self):
        return os.listdir(os.path.join(os.getcwd(), self.config.get_changelog_items_path()))

    def __get_file_path(self, file_name):
        return os.path.join(os.getcwd(), self.config.get_changelog_items_path(), file_name)
