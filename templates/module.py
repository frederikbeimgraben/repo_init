"""
This module contains the Bar implementation.

Functions
---------
    quixify(foo: Foo) -> Foo

Classes
-------
    Bar: The Bar object.
"""


# Imports
from .foo import Foo
from baz import qux


# Global Variables
FOO_LEVEL: int = 1


# Functions
def quixify(foo: Foo) -> Foo:
    """
    Quixify a foo.

    Parameters
    ----------
        foo: Foo to quixify. (Foo)

    Returns
    -------
        Quixified foo. (Foo)
    """
    
    return qux.from_foo(foo)

# Classes
class Bar:
    """
    Bar object

    Attributes
    ----------
        level: The level of the bar. (int)
        foo: The foo of the bar. (Foo)
    
    Methods
    -------
        to_foo: Returns the bars foo and level. (Foo, int)
    """

    level: int
    foo: Foo

    def __init__(self, foo: Foo, level: int = FOO_LEVEL) -> None:
        """
        Initializes a bar.

        Parameters
        ----------
            foo: The foo of the bar. (Foo)
            level: The level of the bar. (int)
        """

        self.foo = foo
        self.level = level

    def to_foo(self) -> 'Foo':
        """
        Converts a bar to a foo.

        Parameters
        ----------
            level: The level of the bar. (int)

        Returns
        -------
            The foo of the bar and its level. (Foo, int)
        """

        return self.foo, self.level