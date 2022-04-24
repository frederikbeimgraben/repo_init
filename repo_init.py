"""
Script to initialize a new repo.

Arguments:
    repo_init <project_name> <language> [--no-gitignore] <language_args>
"""

import argparse
import os
from languages.python import Python
from languages import languages

BLUE = "\033[94m"
GREEN = "\033[92m"
CLEAN = "\033[0m"
ICON_SAVED = GREEN + "✓" + CLEAN

def print_written(file_path):
    print(f"{BLUE}{ICON_SAVED} {BLUE}{file_path}{CLEAN}")

def main():
    # Setup the parser
    parser = argparse.ArgumentParser(description="Initialize a new repo.")
    # Add the subparsers for the languages
    subparsers = parser.add_subparsers(title="Language", help=f"Selected Language", required=True, dest="language")
    for lang, lobj in languages.items():
        subparser = subparsers.add_parser(lang, help=f"{lang} Language")
        # Add the arguments for the languages
        for key, value in lobj.arguments.items():
            if value["positional"]:
                subparser.add_argument(
                    *value["flags"],
                    help=value["help"],
                    type=value["type"][0] if type(value["type"]) == type else None,
                    choices=value["type"] if str in [type(v) for v in value["type"]] else None,
                )
            elif value["type"][0] == bool:
                subparser.add_argument(
                    *value["flags"],
                    help=value["help"],
                    action="store_true" if value["default"] else "store_false",
                    required=value["required"],
                )
            else:
                subparser.add_argument(
                    *value["flags"],
                    dest=key,
                    help=value["help"],
                    default=value["default"],
                    type=value["type"][0] if type(value["type"]) == type else None,
                    choices=value["type"] if str in [type(v) for v in value["type"]] else None,
                    required=value["required"],
                )
    
    args = parser.parse_args()

    # Get the language
    language = languages[args.language]

    # Create the language object
    language_obj = language(**vars(args))

    # Get Templates
    templates = language_obj.templates


    print(args)
    # Bake templates
    for _, template in templates.items():
        if not template.target:
            continue
        if template.target == ".gitignore" and args.no_gitignore:
            continue
        baked = template.bake_template()
        # Get cwd
        cwd = os.getcwd()
        # Get file path
        file_path = os.path.join(cwd, template.target)
        # If the file exists in subfolders, create them if they don't exist
        if "/" in template.target:
            sub_dir = os.path.dirname(file_path)
            if not os.path.exists(sub_dir):
                os.makedirs(sub_dir)
        # Get Path relative to cwd
        rel_path = os.path.relpath(file_path, cwd)
        # Write file
        with open(file_path, "w") as f:
            f.write(baked)

        print_written(rel_path)