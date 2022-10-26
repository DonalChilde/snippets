####################################################
#                                                  #
#    src/snippets/math/make_decimal_string.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-24T16:08:26-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################


def make_decimal_string(whole: int = 0, fractional=0, exponent: int = 1) -> str:
    exponent = abs(exponent)
    if exponent < len(str(fractional)):
        raise ValueError("exponent must be >= number of digits in fractional")
    return f"{whole}.{fractional:0{exponent}}"
