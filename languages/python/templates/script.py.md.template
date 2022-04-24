#!/bin/python3

"""
This is a Script to create and start a Bar.
"""

# Imports
from typing import Dict
from .bar import Bar, quixify
from .foo import Foo, start_foo

# Parser
parser = argparse.ArgumentParser(description='Create and start a Bar.')
parser.add_argument('--foo-config', type=Dict, default=dict(), help='The Foo config.')
parser.add_argument('--bar-level', type=int, default=0, help='The Bar level.')

# Main
def main(args: Dict, level: int) -> None:
    """
    Main function.
    
    Parameters
    ----------
        args: The arguments. (Dict)
        level: The level of the bar. (int)
    """
    
    # Create the bar
    bar = Bar(level)
    
    # Create the foo
    foo = Foo(**args['foo_config'])
    
    # Quixify the foo
    qux = quixify(foo)
    
    # Set the qux
    bar.foo = qux
    
    # Start the bar
    start_foo(bar)


# Run
if __name__ == '__main__':
    # Parse the arguments
    args = parser.parse_args()
    
    # Run the main function
    main(vars(args), args.bar_level)