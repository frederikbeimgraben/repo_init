"""
Abstract models for Languages and Templates
"""

from abc import ABC, abstractclassmethod, abstractstaticmethod
from functools import cached_property
import os
from typing import Dict, List, Tuple, Any

class Template(ABC):
    """
    A template containing a template path and a list of variables.
    """

    template_path: str
    variables: Dict[str, str]
    parent: 'Language'
    target: str = None
    kwargs: Dict[str, Any]

    def __init__(self, **kwargs):
        """
        Initialize the Template
        """
        
        self.kwargs = kwargs

        for key, value in kwargs.items():
            setattr(self, key, value)

    @abstractclassmethod
    def bake_template(self) -> str:
        """
        Gets the template.

        Parameters
        ----------
            project_name: The name of the project. (Tuple[str, str])
            version: The version of the project. (str)
        """

        pass


class ReplTemplate(Template):
    """
    Template class for Python.
    """

    def read_file(self, target: str = None) -> str:
        """
        Gets the template.

        Parameters
        ----------
            project_name: The name of the project. (Tuple[str, str])
            version: The version of the project. (str)
        """

        # Read file contents
        with open(target if target else self.template_path, "r") as file:
            contents = file.read()

        return contents

    def bake_template(self) -> str:
        """
        Gets the template.

        Parameters
        ----------
            project_name: The name of the project. (Tuple[str, str])
            version: The version of the project. (str)
        """

        # Read file contents
        contents = self.read_file()

        # Replace variables
        for key, value in self.variables.items():
            assert key in self.kwargs or key in self.parent.templates, f"{key} is not a valid variable."
            if key in self.kwargs:
                contents = contents.replace(value, self.kwargs[key])
            else:
                contents = contents.replace(value, self.read_file(self.parent.templates[key].template_path))
        return contents


class Language(ABC):
    """
    Language class
    """

    project_name: Tuple[str, str]
    kwargs: Dict[str, str] = {}
    args: Dict[str, Dict[str, Any]] = {}

    def __init__(self, **kwargs):
        """
        Initializes the language class.

        Parameters
        ----------
            project_name: The name of the project. (Name + folder_name) (Tuple[str, str])
            version: The language version for the project. (str)
        """

        # Set the kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    @abstractstaticmethod
    def get_folder_name(str):
        """
        Gets the folder name for the language.

        Parameters
        ----------
            str: The string to get the folder name for. (str)
        """

        pass

    @cached_property
    @abstractclassmethod
    def templates(self) -> List[Template]:
        """
        Gets the templates for the language.

        Returns
        -------
            templates: The templates for the language. (Dict[str, Template])
        """

        pass