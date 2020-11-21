class ChangelogBuilder:
    def __init__(self):
        self.changelog = ''

    def add_header(self, version):
        self.changelog += f'## {version}\n'

    def add_changes_list(self, items):
        self.changelog += '\n'.join(map(lambda item: f'* {item}', items)) + '\n'

    def get(self):
        return self.changelog