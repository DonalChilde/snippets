from datetime import timedelta
from decimal import Decimal
from typing import TypedDict


class DurationDict(TypedDict):
    years: int
    days: int
    hours: int
    minutes: int
    seconds: Decimal


def split_timedelta(delta: timedelta) -> DurationDict:
    """
    Split a time delta to a dict of years, days, hours, minutes, seconds, microseconds.

    https://stackoverflow.com/a/17847006/105844

    Args:
        delta: The timedelta to split
    Returns:
        A dict of the times in the timedelta
    """
    abs_delta = abs(delta)
    years, rem = divmod(abs_delta, timedelta(days=365))
    days, rem = divmod(rem, timedelta(days=1))
    hours, rem = divmod(rem, timedelta(hours=1))
    minutes, rem = divmod(rem, timedelta(minutes=1))
    seconds = Decimal(rem.total_seconds())
    return DurationDict(
        years=years, days=days, hours=hours, minutes=minutes, seconds=seconds
    )
