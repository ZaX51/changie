import configparser

class Config:
    def load(self):
        config = configparser.ConfigParser()

        config['Changie'] = {
            'ChangelogFileName': 'CHANGELOG.md',
            'ChangelogItemPrefix': 'chg',
            'ChangelogItemExtension': '.md',
            'ChangelogItemsPath': 'chg_items'
        }
        config.read('.changierc')

        self.__config = config['Changie']

    def get_changelog_file_name(self):
        return self.__config['ChangelogFileName']

    def get_changelog_item_prefix(self):
        return self.__config['ChangelogItemPrefix']

    def get_changelog_item_extension(self):
        return self.__config['ChangelogItemExtension']

    def get_changelog_items_path(self):
        return self.__config['ChangelogItemsPath']

