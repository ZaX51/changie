from enum import Enum


class ChangeType(Enum):
    Added = "added"
    Changed = "changed"
    Deprecated = "deprecated"
    Removed = "removed"
    Fixed = "fixed"
    Security = "security"


class ChangeFileBuilder:
    def __init__(self):
        self.__item = {}

    def get(self):
        return self.__item

    def add_message(self, message: str):
        self.__item["message"] = message

    def add_type(self, type: ChangeType):
        self.__item["type"] = type.value
