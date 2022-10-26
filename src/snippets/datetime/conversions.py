####################################################
#                                                  #
#      src/snippets/datetime/conversions.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-01T17:29:40-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

from datetime import timedelta

NANOS_PER_SECOND = 10e9


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


def timedelta_to_HHHMMSS(delta: timedelta) -> str:
    if delta.days < 0:
        sign = "-"
    else:
        sign = ""
    abs_delta = abs(delta)
    hours, rem = divmod(abs_delta, timedelta(hours=1))
    minutes, rem = divmod(rem, timedelta(minutes=1))
    seconds = int(rem.total_seconds())
    if abs_delta.microseconds:
        microseconds = f".{abs_delta.microseconds:06d}"
    else:
        microseconds = ""
    return f"{sign}{hours:01d}:{minutes:02d}:{seconds:02d}{microseconds}"


def timedelta_to_iso(delta: timedelta):
    if delta.days < 0:
        sign = "-"
    else:
        sign = ""
    abs_delta = abs(delta)
    years, rem = divmod(abs_delta, timedelta(days=365))
    days, rem = divmod(rem, timedelta(days=1))
    hours, rem = divmod(rem, timedelta(hours=1))
    minutes, rem = divmod(rem, timedelta(minutes=1))
    seconds = int(rem.total_seconds())
    return build_iso_duration(
        sign=sign,
        years=years,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        fractional_seconds=rem.microseconds,
        exponent=6,
    )
    # if abs_delta.microseconds:
    #     microseconds = f".{abs_delta.microseconds:06d}"
    # else:
    #     microseconds = ""
    # return (
    #     f"{sign}P{f'{years}Y' if years else '' }{f'{days}D' if days else ''}"
    #     f"T{f'{hours}H' if hours else ''}{f'{minutes}M'if minutes else ''}"
    #     f"{f'{seconds:01d}{microseconds}S'if (seconds or microseconds)else''}"
    # )


def build_iso_duration(
    sign: str = "",
    years: int = 0,
    days: int = 0,
    hours: int = 0,
    minutes: int = 0,
    seconds: int = 0,
    fractional_seconds: int = 0,
    exponent: int = 0,
):
    if fractional_seconds:
        frac_str = f".{fractional_seconds:0{exponent}}"
    else:
        frac_str = ""
    return (
        f"{sign}P{f'{years}Y' if years else '' }{f'{days}D' if days else ''}"
        f"T{f'{hours}H' if hours else ''}{f'{minutes}M'if minutes else ''}"
        f"{f'{seconds:01d}{frac_str}S'if (seconds or frac_str)else''}"
    )
