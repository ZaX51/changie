from typing import Dict
from changie.change_file_builder import ChangeFileBuilder, ChangeType


def test_empty_file():
    builder = ChangeFileBuilder()
    empty_file = {}

    assert isinstance(builder.get(), Dict)
    assert builder.get() == empty_file


def test_add_message():
    builder = ChangeFileBuilder()
    file = {"message": "TEST"}

    builder.add_message(file["message"])

    assert builder.get() == file


def test_add_type():
    builder = ChangeFileBuilder()
    file_type = ChangeType.Added
    file = {"type": file_type.value}

    builder.add_type(file_type)

    assert builder.get() == file
