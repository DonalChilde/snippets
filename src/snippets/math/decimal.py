from decimal import Decimal

from snippets.math.make_decimal_string import make_decimal_string


def make_decimal(whole: int = 0, fractional=0, exponent: int = 1) -> Decimal:
    return Decimal(
        make_decimal_string(whole=whole, fractional=fractional, exponent=exponent)
    )
