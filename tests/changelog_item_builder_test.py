from typing import Dict
from changie.changelog_item_builder import ChangelogItemBuilder, ItemType


def test_empty_item():
    builder = ChangelogItemBuilder()
    empty_item = {}

    assert isinstance(builder.get(), Dict)
    assert builder.get() == empty_item


def test_add_message():
    builder = ChangelogItemBuilder()
    item = {"message": "TEST"}

    builder.add_message(item["message"])

    assert builder.get() == item


def test_add_type():
    builder = ChangelogItemBuilder()
    item_type = ItemType.Added
    item = {"type": item_type.value}

    builder.add_type(item_type)

    assert builder.get() == item
