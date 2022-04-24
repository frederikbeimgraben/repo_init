"""
Build the package.

Scripts:
    repo_init.py:
        Initializes a new repo.
        python repo_init.py <project_name> <language> [--at <path>] [--no-gitignore] <language_args>
"""

from setuptools import setup, find_packages
import os

# Get the packaage path
here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="repo_init",
    version="0.1.0",
    author="Frederik Beimgraben",
    author_email="beimgraben8@gmail.com",
    packages=find_packages(),
    description="Python Module for default repo initialization.",
    long_description=open(os.path.join(here, "README.md")).read(),
    long_description_content_type="text/markdown",
    url="github.com/frederikbeimgraben/default_repo_init",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "repo_init = repo_init:main",
        ],
    }
)