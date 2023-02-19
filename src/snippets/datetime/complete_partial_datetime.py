####################################################
#                                                  #
# src/snippets/datetime/complete_partial_datetime.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-27T10:37:56-07:00            #
# Last Modified: 2023-02-19T17:16:13.360642+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
import datetime as DT
import logging
import time
from calendar import isleap
from datetime import datetime, timedelta, tzinfo

from snippets.datetime.datetime_from_struct_time import datetime_from_struct

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def get_future_time(reference_date: datetime, future_time: DT.time) -> datetime:
    if future_time.tzinfo is not None and reference_date.tzinfo != future_time.tzinfo:
        raise ValueError(
            f"If future_time has a tzinfo, it must match reference_date tzinfo."
            f" reference_date={reference_date!r}, future_time={future_time!r}",
        )
    if reference_date.time() <= future_time:
        # Time is later on the same day
        return reference_date.combine(reference_date.date(), future_time)
    # Time is on the next day
    reference_date = reference_date + timedelta(days=1)
    return reference_date.combine(reference_date.date(), future_time)


def complete_future_time(
    start: datetime,
    future: str,
    tz_info: tzinfo | None = None,
    strf: str = "%H:%M:%S",
) -> datetime:
    """Use this when only time is available."""
    if start.tzinfo is None and tz_info is not start.tzinfo:
        raise ValueError("tz_info must be None if ref_datetime.tzinfo is None.")
    parsed = time.strptime(future, strf)
    if tz_info is None:
        partial = datetime_from_struct(
            parsed,
            year=start.year,
            month=start.month,
            day=start.day,
            tz_info=None,
            aware=False,
        )
    else:
        partial = datetime_from_struct(
            parsed,
            year=start.year,
            month=start.month,
            day=start.day,
            tz_info=tz_info,
            aware=True,
        )
    if partial < start:
        increment = timedelta(days=1)
        logger.debug("adding %s to %s", increment, partial.isoformat())
        partial = partial + increment
    if partial < start:
        raise ValueError(
            f"fwd time {partial.isoformat()} still shows as "
            f"less than ref {start.isoformat()}"
        )
    return partial


def complete_future_mdt(
    start: datetime,
    future: str,
    tz_info: tzinfo | None = None,
    strf: str = "%m/%d %H:%M",
) -> datetime:
    """Use this when at least month and day are available, but year is missing."""
    if start.tzinfo is None and tz_info is not start.tzinfo:
        raise ValueError("tz_info must be None if ref_datetime.tzinfo is None.")
    # Use time.strptime because datetime.strptime will not parse 02/29 without a valid year
    parsed = time.strptime(future, strf)
    year = start.year
    if parsed.tm_mon == 2 and parsed.tm_mday == 29:
        # if the start year is not a leap year, find the next leap year.
        while not isleap(year):
            year += 1
    if tz_info is None:
        partial = datetime_from_struct(parsed, year=year, tz_info=tz_info, aware=False)
    else:
        partial = datetime_from_struct(parsed, year=year, tz_info=tz_info, aware=True)
    if partial < start:
        logger.debug("adding one year to %s", partial.isoformat())
        partial = partial.replace(year=partial.year + 1)

    if partial < start:
        raise ValueError(
            f"fwd time {partial.isoformat()} still shows as "
            f"less than ref {start.isoformat()}"
        )
    return partial
