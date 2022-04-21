# -----------------------------------------------------------------------------
# Purpose: Builds the default project.
# Author:  Frederik Beimgraben
# Created: 2022-04-21
# -----------------------------------------------------------------------------

# Imports
import argparse
import os
import shutil
from typing import Dict


# Functions
def insert_from_file(string: str, marker: str, file: str) -> str:
    """
    Inserts the contents of a file into a string.
    
    Parameters
    ----------
        string: The string to insert into. (str)
        marker: The marker to insert the file contents into. (str)
        file: The file to insert. (str)
    """

    # Check if the string contains the marker
    assert marker in string, 'Marker not found in string.'
    
    # Open the file
    with open(file, 'r') as f:
        # Read the file
        contents = f.read()
    
    # Insert the contents
    return string.replace(marker, contents)


def get_templates_path() -> str:
    """
    Gets the path to the templates directory.
    """

    # Get the path to the current file
    path = os.path.dirname(os.path.realpath(__file__))

    # Get the path to the templates directory
    templates_path = os.path.join(path, 'templates')

    # Return the templates path
    return templates_path


def make_fs_compatible(string: str) -> str:
    """
    Makes a string filesystem compatible.
    
    Parameters
    ----------
        string: The string to make filesystem compatible. (str)
    """

    # Replace characters unsupported by the filesystem
    string = string.replace('/', '_')
    string = string.replace('\\', '_')
    string = string.replace('.', '_')

    # Return the string
    return string


def make_env_md(env_name: str, env_path: str) -> str:
    """
    Makes a markdown string for an environment.
    
    Parameters
    ----------
        env_name: The name of the environment. (str)
        env_path: The path of the environment. (str)
        project_name: The name of the project. (str)
    """

    # Get the environment name
    env_name = env_name.lower().replace(' ', '_')

    # Replace characters unsupported by the filesystem
    env_name = make_fs_compatible(env_name)

    # Load the environment template
    with open(os.path.join(get_templates_path(), 'env.md'), 'r') as f:
        env_template = f.read()

    # Replace the template variables
    env_template = env_template.replace('{{PACKAGENAME_LC}}', env_name)

    # Return the environment template
    return env_template


def make_style_md(project_name: str, project_name_lc: str) -> str:
    """
    Makes a markdown string for the style.
    
    Parameters
    ----------
        project_name: The name of the project. (str)
        project_name_lc: The name of the project in lowercase. (str)
    """

    # Get the style template
    with open(os.path.join(get_templates_path(), 'style.md'), 'r') as f:
        style_template = f.read()

    # Replace the template variables
    style_template = style_template.replace('{{PACKAGENAME}}', project_name)
    style_template = style_template.replace('{{PACKAGENAME_LC}}', project_name_lc)

    # Insert Examples
    for example in ['init.py', 'module.py', 'script.py']:
        style_template = insert_from_file(style_template, '{{' + example + '}}', os.path.join(get_templates_path(), example))

    # Return the style template
    return style_template 


def make_readme_md(project_name: str) -> str:
    """
    Makes a markdown string for the readme.
    
    Parameters
    ----------
        project_name: The name of the project. (str)
    """

    # Get the readme template
    with open(os.path.join(get_templates_path(), 'readme.md'), 'r') as f:
        readme_template = f.read()

    # Replace the template variables
    readme_template = readme_template.replace('{{PACKAGENAME}}', project_name)

    # Return the readme template
    return readme_template


def make_env_yml(env_name: str, pyversion: str) -> str:
    """
    Makes a string for an environment.
    
    Parameters
    ----------
        env_name: The name of the environment. (str)
    """

    # Get the environment name
    env_name = env_name.lower().replace(' ', '_')

    # Replace characters unsupported by the filesystem
    env_name = make_fs_compatible(env_name)

    # Load the environment template
    with open(os.path.join(get_templates_path(), 'environment.yml'), 'r') as f:
        env_yml = f.read()

    # Insert into the environment template
    env_yml = insert_from_file(env_yml, '{{PROJECTNAME}}', env_name)
    env_yml = insert_from_file(env_yml, '{{PYVERSION}}', pyversion)

    # Return the environment template
    return env_yml


def build_project(project_name: str) -> None:
    """
    Builds the project.
    
    Parameters
    ----------
        project_name: The name of the project. (str)
        project_path: The path of the project. (str)
        project_files: The files of the project. (Dict[str, str])
    """

    # Determine the project dir name from the project short name
    project_dir_name = project_name.lower().replace(' ', '_')

    # Replace characters unsupported by the filesystem
    project_dir_name = make_fs_compatible(project_dir_name)

    # Get cwd
    cwd = os.getcwd()

    # Get the project path (cwd/project_dir_name)
    project_path = cwd

    # If the cwd is in the same directory as build.py, change to ./build
    if cwd == os.path.dirname(os.path.realpath(__file__)):
        # Create a build directory if it doesn't exist
        if not os.path.exists('./build'):
            os.mkdir('./build')
        os.chdir(os.path.join(cwd, 'build'))

        project_path = os.path.join(cwd, project_dir_name)


    # Create the project directory
    os.mkdir(project_path)

    # Change to the project directory
    os.chdir(project_path)

    # Create ENVIRONMENT.md
    with open('ENVIRONMENT.md', 'w') as f:
        f.write(make_env_md(project_name, project_path))

    # Create STYLE.md
    with open('STYLE.md', 'w') as f:
        f.write(make_style_md(project_name, project_dir_name))

    # Create README.md
    with open('README.md', 'w') as f:
        f.write(make_readme_md(project_name))

    # Create environment.yml
    with open('environment.yml', 'w') as f:
        f.write(make_env_yml(project_name, '3.7'))

    # Create src directory
    os.mkdir('src')

    # Create src/{project_dir_name} directory
    os.mkdir(os.path.join('src', project_dir_name))

    # Copy .gitignore
    shutil.copy(os.path.join(get_templates_path(), '.gitignore'), '.')

    # Done
    print('Done!')


# Execute the build script
if __name__ == '__main__':
    # Parse the arguments
    parser = argparse.ArgumentParser(description='Builds a project.')
    parser.add_argument('project_name', type=str, help='The name of the project.')
    # Python version
    parser.add_argument('--pyversion', type=str, default='3.10', help='The python version to use.')
    # Environment name (optional)
    parser.add_argument('--envname', type=str, default='', help='The name of the environment.')
    # Parse the arguments
    args = parser.parse_args()

    project_name = args.project_name
    pyversion = args.pyversion
    env_name = args.envname if args.envname != '' else project_name

    # Build the project
    build_project(project_name)
