"""
Python Module for default repo initialization.
"""

NAME = ["python", "python3"]

from ast import arguments
from functools import cached_property
from typing import List
from model import ReplTemplate, Language
from .config import TEMPLATE_PATH, ARGS, TEMPLATES


class Python(Language):
    """
    Python Language
    """

    arguments = ARGS

    def __init__(self, **kwargs):
        """
        Initialize the Python Language
        """

        for key, value in ARGS.items():
            if key in kwargs:
                setattr(self, key, kwargs[key])
            elif not value["required"]:
                setattr(self, key, value["default"])
            else:
                raise ValueError(f"{key} is required.")
        
        self.kwargs = kwargs
    
    @cached_property
    def templates(self) -> List[ReplTemplate]:
        """
        Gets the templates.
        """
        return {
            key: ReplTemplate(
                template_path=value["template_path"],
                variables=value["variables"],
                parent=self,
                target=value["location"],
                args=ARGS,
                **self.kwargs,
            ) for key, value in TEMPLATES.items()
        }

    def get_folder_name(str):
        """
        Gets the folder name for the language.

        Parameters
        ----------
            str: The string to get the folder name for. (str)
        """
        return str.lower().replace(" ", "_").replace("-", "_")

    