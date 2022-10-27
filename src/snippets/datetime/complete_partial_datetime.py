####################################################
#                                                  #
# src/snippets/datetime/complete_partial_datetime.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-27T10:37:56-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
import logging
from datetime import datetime, timedelta, tzinfo

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def complete_fwd_time(
    ref_datetime: datetime,
    partial_string: str,
    tz_info: tzinfo | None,
    strf: str = "%H:%M:%S",
) -> datetime:
    if ref_datetime.tzinfo is None and tzinfo is not ref_datetime.tzinfo:
        raise ValueError("tz_info must be None if ref_datetime.tzinfo is None.")
    partial = datetime.strptime(partial_string, strf)
    partial = partial.replace(
        year=ref_datetime.year,
        month=ref_datetime.month,
        day=ref_datetime.day,
        tzinfo=tz_info,
    )
    if partial < ref_datetime:
        increment = timedelta(days=1)
        logger.debug("adding %s to %s", increment, partial.isoformat())
        partial = partial + increment
    if partial < ref_datetime:
        raise ValueError(
            f"fwd time {partial.isoformat()} still shows as "
            f"less than ref {ref_datetime.isoformat()}"
        )
    return partial


def complete_fwd_mdt(
    ref_datetime: datetime,
    partial_string: str,
    tz_info: tzinfo | None,
    strf: str = "%m/%d %H:%M",
) -> datetime:
    if ref_datetime.tzinfo is None and tz_info is not ref_datetime.tzinfo:
        raise ValueError("tz must be None if ref_datetime.tzinfo is None.")

    partial = datetime.strptime(partial_string, strf)
    partial = partial.replace(
        year=ref_datetime.year,
        tzinfo=tz_info,
    )
    if partial < ref_datetime:
        logger.debug("adding one year to %s", partial.isoformat())
        partial = partial.replace(year=partial.year + 1)

    if partial < ref_datetime:
        raise ValueError(
            f"fwd time {partial.isoformat()} still shows as "
            f"less than ref {ref_datetime.isoformat()}"
        )
    return partial


# def complete_partial_datetime(ref_datetime: datetime, partial_string: str) -> datetime:
#     # 10/30 11:11
#     # 22:57
#     ref_tz = ref_datetime.tzinfo
#     if ref_tz:
#         ref_no_tz = ref_datetime.replace(tzinfo=None)
#     else:
#         ref_no_tz = ref_datetime
#     year_added = f"{ref_no_tz.year}/{partial_string}"
#     try:
#         partial = datetime.strptime(year_added, "%Y/%m/%d %H:%M")
#         # check if overlaps year, eg. 12/31-1/1
#         if partial < ref_no_tz:
#             partial = partial.replace(year=ref_no_tz.year + 1)
#     except ValueError as err:
#         logger.info("%s", err)
#         try:
#             partial = datetime.strptime(year_added, "%Y/%H:%M")
#             partial = partial.replace(month=ref_no_tz.month, day=ref_no_tz.day)
#             # check if overlaps day, eg. 2350-0230
#             if partial.time() < ref_no_tz.time():
#                 partial = partial + timedelta(days=1)
#             # check if overlaps year, eg. 12/31-1/1
#             if partial < ref_no_tz:
#                 partial = partial.replace(year=ref_no_tz.year + 1)
#         except ValueError as err_2:
#             _ = err_2
#             logger.error(
#                 "Failure to parse %s",
#                 partial_string,
#                 exc_info=True,
#             )
#             raise err_2
#     partial = partial.replace(tzinfo=ref_tz)
#     if partial < ref_datetime:
#         error = ValueError(
#             f"Partial string {partial_string} parsed as {partial.isoformat()} "
#             f"does not come after ref of {ref_datetime.isoformat()}"
#         )
#         logger.error(error)
#         raise error
#     return partial
