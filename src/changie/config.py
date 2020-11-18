import configparser

def get_config():
    config = configparser.ConfigParser()

    config['Changie'] = {
        'ChangelogFileName': 'CHANGELOG.md',
        'ChangelogItemPrefix': 'chg',
        'ChangelogItemExtension': '.md'
    }

    config.read('.changierc')

    return config['Changie']