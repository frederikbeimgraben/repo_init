# Style conventions for {{PROJECTNAME}}

## Project Structure
```py
    ROOT
    │   README.md           # Readme
    │   LICENSE             # License
    |   STYLE.md            # Style Conventions
    |   ENVIRONMENT.md      # Environment Guide
    │   environment.yml     # Conda Environment
    │
    └───src                 # Source Code
        │   run.py          # Main script (to run without compilation)
        │   setup.py        # Setup Project (will later be exportable as .exe)
        │
        └───{{PROJECTNAME_LC}}
            ├───__init__.py # For importing the project
            ├───main.py     # Main script (to be used as the compiled executables entry point)
            │
            ├───...         # Subpackages
            ...
```
> For more information, consider the [pip documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

## Coding Style
### Example package \_\_init\_\_.py

```py
{{init.py}}
```

### Example Module File
A module file should have the following structure:

```py
{{module.py}}
```

### Example Script
```py
{{script.py}}
```

> For more information on general style guidelines, consider [PEP8](https://www.python.org/dev/peps/pep-0008/).

> Docstrings: [PEP257](https://www.python.org/dev/peps/pep-0257/).
>> Attributes and Parameters: [Google Style Guide](https://google.github.io/styleguide/pyguide.html?showone=Comments#Comments).

> Python Project Structure: [PyPA Project Structure Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
