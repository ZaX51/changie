from datetime import datetime
from itertools import groupby
from changie.changelog_item_builder import ItemType


class ChangelogBuilder:
    def __init__(self):
        self.changelog = ""

    def get(self):
        return self.changelog

    def add_header(self, version):
        date = datetime.now().strftime("%m-%d-%Y")
        self.changelog += f"## {version} - {date}\n\n"

    def add_changes_list(self, items):
        for type, changes in self.__group_changes_by_type(items).items():
            self.changelog += f"### {ItemType(type).name}\n"

            for c in changes:
                self.changelog += "- {message}\n".format(message=c["message"])

            self.changelog += "\n"

    def __group_changes_by_type(self, items):
        sorted_items = sorted(items, key=lambda el: el["type"])
        grouped_items = groupby(sorted_items, key=lambda el: el["type"])
        return dict((k, list(v)) for k, v in grouped_items)
