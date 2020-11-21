import configparser

class Config:
    def load(self):
        config = configparser.ConfigParser()

        config['Changie'] = {
            'ChangelogFileName': 'CHANGELOG.md',
            'ChangelogItemPrefix': 'chg',
            'ChangelogItemExtension': '.md'
        }
        config.read('.changierc')

        self.config = config['Changie']

