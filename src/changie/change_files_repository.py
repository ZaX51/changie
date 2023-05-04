from datetime import datetime
import os
import yaml
from .utils import write_file, read_file
from .config import Config, ConfigKey
from .change_file_builder import ChangeFileBuilder, ChangeType


class ChangeFilesRepository:
    def __init__(self, config: Config):
        self.config = config

    def add(self, message: str, type: ChangeType):
        file_name = "{prefix}_{timestamp}{extension}".format(
            prefix=self.config.get(ConfigKey.ChangeFilePrefix),
            timestamp=datetime.now().timestamp(),
            extension=self.config.get(ConfigKey.ChangeFileExtension),
        )

        builder = ChangeFileBuilder()
        builder.add_message(message)
        builder.add_type(type)

        write_file(
            self.__get_file_path(file_name),
            yaml.dump(builder.get(), Dumper=yaml.Dumper),
        )

        return file_name

    def get_all(self):
        items = []

        for file_name in self.__get_files_dir():
            if not self.__is_change_file(file_name):
                continue

            items.append(
                yaml.load(
                    read_file(self.__get_file_path(file_name)), Loader=yaml.Loader
                )
            )

        return items

    def remove_all(self):
        for file_name in self.__get_files_dir():
            if self.__is_change_file(file_name):
                os.remove(self.__get_file_path(file_name))

    def __is_change_file(self, file_name: str):
        return file_name.startswith(
            self.config.get(ConfigKey.ChangeFilePrefix)
        ) and file_name.endswith(self.config.get(ConfigKey.ChangeFileExtension))

    def __get_files_dir(self):
        return os.listdir(
            os.path.join(os.getcwd(), self.config.get(ConfigKey.ChangeFilesPath))
        )

    def __get_file_path(self, file_name: str):
        return os.path.join(
            os.getcwd(), self.config.get(ConfigKey.ChangeFilesPath), file_name
        )
