from datetime import timedelta
from typing import Dict

NANOS_PER_SECOND = 1000000000

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR


def seconds_to_nanoseconds(seconds: float) -> int:
    """Convert seconds to nanoseconds"""
    nanos = int(seconds * NANOS_PER_SECOND)
    return nanos


def nanoseconds_to_seconds(nanos: int) -> float:
    """
    Convert nanoseconds to seconds
    Args:
        nanos: Nanoseconds to convert.
    Returns:
        Seconds as a float.
    """
    seconds = nanos / NANOS_PER_SECOND
    return seconds


def duration_to_seconds_int(
    days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0
) -> int:
    day_seconds = days * 24 * 60 * 60
    hour_seconds = hours * 60 * 60
    minute_seconds = minutes * 60
    return day_seconds + hour_seconds + minute_seconds + seconds
