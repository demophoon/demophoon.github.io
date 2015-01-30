#!/usr/bin/env python
from setuptools import setup

setup(
    name="demophoon.github.io",
    version="1.0.0",
    author="Britt Gresham",
    author_email="brittcgresham@gmail.com",
    description=("My personal blog website"),
    license="MIT",
    install_requires=[
        'pelican',
        'markdown',
        'ghp-import',
    ],
)
