####################################################
#                                                  #
#          src/snippets/datetime/datetime.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-01T17:30:00-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

import logging
from dataclasses import dataclass
from datetime import date, timedelta
from typing import List, Sequence, Tuple

from ..collection.distance_in_wrapped_list import distance_in_wrapped_list
from ..filter.filter import simple_filter

#### setting up logger ####
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


@dataclass
class WeekBoundry:
    start_of_week: date
    end_of_week: date


@dataclass
class MonthBoundry:
    start_of_month: date
    end_of_month: date


def range_of_dates(start_date: date, end_date: date) -> List[date]:
    """
    Creates a list of dates between a start and end date, inclusive.

    If start_date is after end_date, the list will count backwards in time.

    Args:
        start_of_range: The start date.
        end_of_range: The end date
    Returns
        The list of dates inclusive.
    """

    # https://stackoverflow.com/a/24637447/105844

    # forwards
    if start_date <= end_date:
        date_count = (end_date - start_date).days + 1
        return [start_date + timedelta(days=x) for x in range(0, date_count)]
    # backwards
    date_count = (start_date - end_date).days + 1
    return [start_date - timedelta(days=x) for x in range(0, date_count)]


def month_boundries(date_value: date) -> MonthBoundry:
    raise NotImplementedError


def week_boundries(
    date_value: date, week_starts_on: int = 7, iso: bool = True
) -> WeekBoundry:
    """
    Find the first and last day of the week that contains a specific date.

    Python standard days of the week have a range of 0 - 6, with 0 being Monday.
    Iso standard days of the week have a range of 1 - 7, with 1 being Monday.

    Args:
        date_value: The date contained in a week.
        week_starts_on: _Index first day of the week. Defaults to 7.
        iso: Use iso week indexing. Defaults to True.

    Returns:
        The beginning and ending dates that make up the week.
    """
    if iso:
        if 1 > week_starts_on > 7:
            raise ValueError(
                f"week_stars_on must be an int between 1 and 7 when iso = True, "
                f"got {week_starts_on}"
            )
    else:
        if 0 > week_starts_on > 6:
            raise ValueError(
                f"week_stars_on must be an int between 0 and 6 when iso = False, "
                f"got {week_starts_on}"
            )
    bow_distance = 0
    # bow_not_found = True
    date_to_check = date_value
    while True:
        date_to_check = date_to_check - timedelta(days=bow_distance)
        if iso:
            check_dow = date_to_check.isoweekday()
        else:
            check_dow = date_to_check.weekday()
        if check_dow == week_starts_on:
            break
        bow_distance += 1
    return WeekBoundry(date_to_check, date_to_check + timedelta(days=6))


def beginning_of_week(
    date_value: date, week_starts_on: int = 7, iso: bool = True
) -> date:
    """
    Find the first day of the week which contains date_.

    Python standard days of the week have a range of 0 - 6, with 0 being Monday.
    Iso standard days of the week have a range of 1 - 7, with 1 being Monday.

    :param date_: Date reference to find the first day of the week.
    :param week_starts_on: Index first day of the week, defaults to 7, Sunday
    :param iso: Use iso week index. Defaults to ``True``.
    :raises ValueError: Invalid `week_starts_on` value.
    :return: The first day of the week that contains `date_`
    """
    logging.debug(
        "beginning_of_week(date_=%s, week_starts_on=%s, iso=%s)",
        date_value,
        week_starts_on,
        iso,
    )
    if iso:
        dow_index = date_value.isoweekday() - 1
        dow_int = [1, 2, 3, 4, 5, 6, 7]
    else:
        dow_index = date_value.weekday()
        dow_int = [0, 1, 2, 3, 4, 5, 6]
    if week_starts_on not in dow_int:
        raise ValueError(f"week_starts_on of {week_starts_on} is not valid. iso={iso}")
    distance, _ = distance_in_wrapped_list(
        dow_int, dow_index, -1, simple_filter(week_starts_on)
    )
    new_date = date_value - timedelta(hours=24 * distance)  # type: ignore
    return new_date


def end_of_week(date_: date, week_starts_on: int = 7, iso: bool = True) -> date:
    """
    Find the last day of the week which contains date_.

    Python standard days of the week have a range of 0 - 6, with 0 being Monday.
    Iso standard days of the week have a range of 1 - 7, with 1 being Monday.

    :param date_: Date reference to find the last day of the week.
    :param week_starts_on: Index first day of the week, defaults to 7, Sunday
    :param iso: Use iso week index. Defaults to ``True``.
    :raises ValueError: Invalid `week_starts_on` value.
    :return: The last day of the week that contains `date_`
    """
    logging.debug(
        "end_of_week(date_=%s, week_starts_on=%s, iso=%s)", date_, week_starts_on, iso
    )
    s_o_w = beginning_of_week(date_value=date_, week_starts_on=week_starts_on, iso=iso)
    e_o_w = s_o_w + timedelta(hours=24 * 6)
    return e_o_w


# def pad_to_end_of_week(date_: date) -> date:
#     dow_index = 6 - date_.weekday()
#     new_date = date_ + timedelta(hours=24 * dow_index)
#     return new_date


# def iso_date_now(tz=dateutil.tz.UTC):
#     return datetime.now(tz).date().isoformat()


# def tz_aware_utcnow() -> datetime:
#     """
#     Enforce adding timezone to utcnow. Use this over utcnow.

#     https://docs.python.org/3/library/datetime.html#datetime.datetime.now

#     :return: A datetime representing a timezone aware :func:`datetime.utcnow`
#     """
#     return datetime.now(tz.UTC)  # type: ignore
