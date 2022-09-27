####################################################
#                                                  #
#    src/snippets/argparse/readable_directory.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T09:12:49-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

"""
Action to check if an argument is a valid path to a directory.

This subclassed :class:`argparse.Action` will error if the argument
is not a valid directory path.
"""

import os
from argparse import Action
from pathlib import Path


class ReadableDirectory(Action):
    """
    Ensure the cmd line argument is a valid path to a directory.

    :class:`argparse.Action` to ensure cmd line argument is a valid path to a directory.
    Checks for :func:Path.is_dir, exists, and :func:`os.access`. Will error on fail.

    This probably works, needs some testing the next time i do an argparse
    script.
    TODO Things to check:
      - how does this interact with type=pathlib.Path
      - using parser.error instead of raise argparse.ArgumentError(self, ...)

    Example:
        # TODO add example
    # TODO This needs some picking apart and some testing.


    https://stackoverflow.com/a/11415816

    """

    def __call__(self, parser, namespace, values, option_string=None):
        dir_path: Path
        try:
            dir_path = Path(values).resolve(strict=True)
            if not dir_path.is_dir():
                parser.error(f"{dir_path} is not a directory")
            if os.access(dir_path, os.R_OK):
                setattr(namespace, self.dest, dir_path)
            else:
                parser.error(f"{dir_path} is not a readable directory")
        except FileNotFoundError:
            parser.error(f"{dir_path} is not a valid path")
