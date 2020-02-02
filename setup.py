#!/usr/bin/env python
import os

from setuptools import setup, find_packages

setup(
    name="changie",
    version="0.1.0",
    description="Changelog generator",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    author="Dawid Sołtysiak",
    install_requires=[
        "setuptools",
        "click"
    ],
    packages = find_packages(),
    entry_points={"console_scripts": ["changie = changie:main"]},
)