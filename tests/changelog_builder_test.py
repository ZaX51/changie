from datetime import datetime
from changie.changelog_builder import ChangelogBuilder
from changie.changelog_item_builder import ItemType

mocked_changelog = """### Added
- ADDED 1
- ADDED 2

### Fixed
- FIXED 1

### Removed
- REMOVED 1

"""


def test_empty_changelog():
    builder = ChangelogBuilder()

    assert isinstance(builder.get(), str)
    assert builder.get() == ""


def test_add_header():
    builder = ChangelogBuilder()

    builder.add_header("1.0.0", datetime(2020, 12, 24, 17, 00))

    assert builder.get() == "## 1.0.0 - 24-12-2020\n\n"


def test_add_items():
    builder = ChangelogBuilder()
    items = [
        {"message": "ADDED 1", "type": ItemType.Added.value},
        {"message": "ADDED 2", "type": ItemType.Added.value},
        {"message": "FIXED 1", "type": ItemType.Fixed.value},
        {"message": "REMOVED 1", "type": ItemType.Removed.value},
    ]

    builder.add_changes_list(items)

    assert builder.get() == mocked_changelog
