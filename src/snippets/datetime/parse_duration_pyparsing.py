####################################################
#                                                  #
#  src/snippets/datetime/parse_duration_pyparsing.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-28T17:10:25-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

"""
    Various duration parsing strategies using pyparsing,

"""

from datetime import timedelta

from .duration import IsoDuration


def parse_iso_duration(duration_string: str) -> IsoDuration:
    pass


def parse_duration(parser, duration_string: str) -> timedelta:
    pass
