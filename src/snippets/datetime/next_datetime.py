####################################################
#                                                  #
#       src/snippets/datetime/next_datetime.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-09-08T09:16:31-07:00            #
# Last Modified: 2023-09-08T17:35:04.623317+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from calendar import isleap
from datetime import date, datetime, time


def month_day(
    ref_date: date,
    month: int,
    day: int,
    *,
    future: bool = True,
    same_date_ok: bool = False,
) -> date:
    """Get the next occurrance of a month and day."""
    year = ref_date.year
    if same_date_ok and date_tuple(ref_date) == (year, month, day):
        return date(year, month, day)
    # handle leapyear extra day
    if month == 2 and day == 29:
        return next_leap_date(ref_date=ref_date, future=future)
    if future:
        if ref_date.month > month:
            year += 1
        if ref_date.month == month and ref_date.day >= day:
            year += 1
    else:
        if ref_date.month == month and ref_date.day <= day:
            year -= 1
        if ref_date.month < month:
            year -= 1
    return date(year, month, day)


def next_leap_year(
    year: int, *, future: bool = True, same_year_ok: bool = False
) -> int:
    """Find the next leap year, by default not including the provided year."""
    if same_year_ok and isleap(year):
        return year
    if future:
        increment = 1
    else:
        increment = -1
    year += increment
    while not isleap(year):
        year += increment
    return year


def next_leap_date(
    ref_date: date, *, future: bool = True, same_date_ok: bool = False
) -> date:
    """Find the next 02/29 date, by default not includng the provided date."""
    if same_date_ok and same_month_day(ref_date, 2, 29):
        return date(ref_date.year, 2, 29)
    result_year = 0
    if future:
        if isleap(ref_date.year) and ref_date.month <= 2 and ref_date.day < 29:
            result_year = ref_date.year
        result_year = next_leap_year(ref_date.year, future=True)
    if not future:
        if isleap(ref_date.year) and ref_date.month > 2:
            result_year = ref_date.year
        result_year = next_leap_year(ref_date.year, future=False)
    return date(result_year, 2, 29)


def same_month_day(ref_date: date, month: int, day: int) -> bool:
    """Check to see if a date has the same month and day."""
    return ref_date.month == month and ref_date.day == day


def date_tuple(ref_date: date) -> tuple[int, int, int]:
    """convert a date to a tuple of ints -> (year,month,day)"""
    return (ref_date.year, ref_date.month, ref_date.day)


def next_time(
    ref_datetime: datetime,
    new_time: time,
    *,
    future: bool = True,
    same_datetime_ok: bool = False,
) -> datetime:
    """
    Find the next occurance of a time of day, either future or past.

    Args:
        ref_datetime: _description_
        new_time: _description_
        future: _description_. Defaults to True.
        same_datetime_ok: _description_. Defaults to False.

    Raises:
        ValueError: _description_

    Returns:
        _description_
    """
    if ref_datetime.tzinfo != new_time.tzinfo:
        raise ValueError(
            f"Timezone info must match ref_datetime={ref_datetime!r}, new_time={new_time!r}"
        )
    if same_datetime_ok and ref_datetime.time() == new_time:
        return ref_datetime
    if future:
        if ref_datetime.time() < new_time:
            shifted_date = ref_datetime.date()
        shifted_date = datetime.fromordinal(ref_datetime.date().toordinal() + 1)
    else:
        if ref_datetime.time() > new_time:
            shifted_date = ref_datetime.date()
        shifted_date = datetime.fromordinal(ref_datetime.date().toordinal() - 1)
    return datetime.combine(shifted_date, new_time)
