####################################################
#                                                  #
#      src/snippets/argparse/help_on_error.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T08:30:10-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

"""
Change the :class:`argparse.ArgumentParser` exit on error behavior.

This subclassed :class:`ArgumentParser` will print the parser help instead of usage.

"""

from argparse import ArgumentParser
from sys import stderr


class ArgumentParserHelpOnError(ArgumentParser):
    """
    Print help instead of usage when encountering an error.

    https://stackoverflow.com/a/16942165
    """

    def error(self, message):
        self.print_help(stderr)
        # self.print_usage(stderr)
        self.exit(2, f"{self.prog}: error: {message}\n")
