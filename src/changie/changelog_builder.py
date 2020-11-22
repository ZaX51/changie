from datetime import datetime


class ChangelogBuilder:
    def __init__(self):
        self.changelog = ""

    def add_header(self, version):
        date = datetime.now().strftime("%m-%d-%Y")
        self.changelog += f"## {version} - {date}\n\n"

    def add_changes_list(self, items):
        self.changelog += "\n".join(map(lambda item: f"* {item}", items)) + "\n"

    def get(self):
        return self.changelog
