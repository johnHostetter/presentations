"""
Set up the 'soft' computing Python library.
"""

from setuptools import setup

setup(
    name="presentations",
    version="1.0",
    author="John Wesley Hostetter",
    author_email="jhostetter16@gmail.com",
    packages=[
        "src.manim_presentation",
        "src.oral_proposal",
        "YACS",
        "unit_tests"
    ],
)
