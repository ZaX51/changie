from datetime import datetime
from os import listdir, getcwd, remove
from .utils import write_file, read_file
from .config import Config

class ChangelogItemsRepository:
    def __init__(self, config: Config):
        self.config = config

    def add(self, message):
        item_prefix = self.config.config['ChangelogItemPrefix']
        item_extension = self.config.config['ChangelogItemExtension']

        write_file(f'{item_prefix}_{datetime.now().timestamp()}{item_extension}', message)

    def get_all(self):
        item_prefix = self.config.config['ChangelogItemPrefix']
        item_extension = self.config.config['ChangelogItemExtension']

        items = []

        for file_name in listdir(getcwd()):
            if not (file_name.startswith(item_prefix) and file_name.endswith(item_extension)):
                continue

            items.append(read_file(file_name))

        return items

    def remove_all(self):
        item_prefix = self.config.config['ChangelogItemPrefix']
        item_extension = self.config.config['ChangelogItemExtension']

        for file_name in listdir(getcwd()):
            if file_name.startswith(item_prefix) and file_name.endswith(item_extension):
                remove(file_name)