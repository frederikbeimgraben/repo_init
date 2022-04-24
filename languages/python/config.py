"""
Language configuration for Python.
"""

import os
from argparse import ArgumentParser

here = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_PATH = os.path.join(here, "templates")


# Subcommand: python
ARGS = {
    "project_name": {
        "help": "The name of the project.",
        "nargs": 1,
        "type": [str],
        "default": None,
        "required": True,
        "flags": ["project_name"],
        "positional": True,
    },
    "version": {
        "help": "The Python Version of the Project.",
        "nargs": 1,
        "type": [str, int],
        "default": "3.8",
        "required": False,
        "flags": ["--version", "-v"],
        "positional": False,
    },
    "env_type": {
        "help": "The type of environment to create.",
        "nargs": 1,
        "type": ["venv", "conda"],
        "default": "venv",
        "required": False,
        "flags": ["--env-type", "-e"],
        "positional": False,
    },
    "gitignore": {
        "help": "Don't create a .gitignore file.",
        "nargs": 0,
        "type": [bool],
        "default": True,
        "required": False,
        "flags": ["--no-gitignore", "-g"],
        "positional": False,
    },
    "description": {
        "help": "The description of the project.",
        "nargs": 1,
        "type": [str],
        "default": 'A Python project.',
        "required": False,
        "flags": ["--description", "-d"],
        "positional": False,
    }
}

TEMPLATES = {
    "README.md": {
        "template_path": os.path.join(TEMPLATE_PATH, "readme.md.template"),
        "variables": {
            "project_name": "{{project_name}}",
            "version": "{{version}}",
            "env_type": "{{env_type}}"
        },
        "location": "README.md",
    },
    "requirements.txt": {
        "template_path": os.path.join(TEMPLATE_PATH, "requirements.txt.template"),
        "variables": {
            "version": "{{version}}"
        },
        "location": "requirements.txt",
    },
    "setup.py": {
        "template_path": os.path.join(TEMPLATE_PATH, "setup.py.template"),
        "variables": {
            "project_name": "{{project_name}}",
            "version": "{{version}}",
            "description": "{{description}}",
        },
        "location": "setup.py",
    },
    ".gitignore": {
        "template_path": os.path.join(TEMPLATE_PATH, "gitignore.template"),
        "variables": {},
        "location": ".gitignore",
    },
    "script.py.md.template": {
        "template_path": os.path.join(TEMPLATE_PATH, "script.py.md.template"),
        "variables": {},
        "location": None,
    },
    "init.py.md.template": {
        "template_path": os.path.join(TEMPLATE_PATH, "init.py.md.template"),
        "variables": {},
        "location": None,
    },
    "module.py.md.template": {
        "template_path": os.path.join(TEMPLATE_PATH, "module.py.md.template"),
        "variables": {},
        "location": None,
    },
    "STYLE.md": {
        "template_path": os.path.join(TEMPLATE_PATH, "style.md.template"),
        "variables": {
            "script.py.md.template": "{{script.py}}",
            "module.py.md.template": "{{module.py}}",
            "init.py.md.template": "{{init.py}}",
        },
        "location": "STYLE.md",
    },
    "ENVIRONMENT.md": {
        "template_path": os.path.join(TEMPLATE_PATH, "env.conda.md.template"),
        "variables": {
            "env_type": "{{env_type}}",
            "version": "{{version}}",
            "project_name": "{{project_name}}",
        },
        "location": "ENVIRONMENT.md",
    },
    "environment.yml": {
        "template_path": os.path.join(TEMPLATE_PATH, "env.yml.template"),
        "variables": {
            "version": "{{version}}",
        },
        "location": "environment.yml",
    },
    "main.py": {
        "template_path": os.path.join(TEMPLATE_PATH, "main.py.template"),
        "variables": {
            "project_name": "{{project_name}}",
        },
        "location": "main.py",
    },
}

