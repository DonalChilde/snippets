from decimal import Decimal


def make_decimal(whole: int = 0, fractional=0, exponent: int = 1) -> Decimal:
    return Decimal(
        make_decimal_string(whole=whole, fractional=fractional, exponent=exponent)
    )


def make_decimal_string(whole: int = 0, fractional=0, exponent: int = 1) -> str:
    exponent = abs(exponent)
    if exponent < len(str(fractional)):
        raise ValueError("exponent must be >= number of digits in fractional")
    return f"{whole}.{fractional:0{exponent}}"
