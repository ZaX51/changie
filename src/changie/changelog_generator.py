class ChangelogGenerator:
    def __init__(self):
        self.__changelog = ''

    def get_changelog(self):
        return self.__changelog

    def generate(self, version, changelog_items):
        self.__generate_header(version)
        self.__generate_items_list(changelog_items)

    def __generate_header(self, version):
        self.__changelog += f'## {version}\n\n'

    def __generate_items_list(self, changelog_items):
        for item in changelog_items:
            self.__changelog += f'* {item}\n'
