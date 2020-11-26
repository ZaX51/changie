from enum import Enum


class ItemType(Enum):
    Added = "added"
    Changed = "changed"
    Deprecated = "deprecated"
    Removed = "removed"
    Fixed = "fixed"
    Security = "security"


class ChangelogItemBuilder:
    def __init__(self):
        self.__item = {}

    def add_message(self, message: str):
        self.__item["message"] = message

    def add_type(self, type: ItemType):
        self.__item["type"] = type.value

    def get(self):
        return self.__item
