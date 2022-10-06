####################################################
#                                                  #
# src/snippets/string/clean_numbers.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-05T19:08:17-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################


def clean_int_str(value: str) -> str:
    # https://stackoverflow.com/questions/1249388/removing-all-non-numeric-characters-from-string-in-python
    cleaned = "".join(c for c in value if c.isdigit())
    return cleaned


def clean_float_str(value: str, decimal_sep: str = "."):
    cleaned = "".join(c for c in value if (c.isdigit() or c == decimal_sep))
    return cleaned
