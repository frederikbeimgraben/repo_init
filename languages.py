"""
Just a little config file for the languages.
"""

import languages

languages = {
    "python": {
        "name": languages.python.Python.name,
        "args": languages.python.Python.kwargs,
        "class": languages.python.Python,
    }
}