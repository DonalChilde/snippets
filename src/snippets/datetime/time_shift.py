####################################################
#                                                  #
#      src/snippets/datetime/time_shift.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-09-08T04:29:01-07:00            #
# Last Modified: 2023-09-08T11:36:47.209240+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from datetime import datetime, timedelta, timezone


def time_shift(
    ref_datetime: datetime, shift: timedelta, *, utc_out: bool = False
) -> datetime:
    """
    Combine an aware datetime with a timedelta. Enforce utc manipulation.

    Args:
        ref_datetime: A timezone aware datetime
        shift: The change in time.
        utc_out: Return as UTC instead of original timezone. Defaults to False.

    Raises:
        ValueError: ref_datetime must be tz aware.

    Returns:
        The timeshifted ref_datetime.
    """
    if ref_datetime.tzinfo is None:
        raise ValueError(
            f"ref_datetime: {ref_datetime!r} must be tz aware. No tzinfo found"
        )
    ref_tz = ref_datetime.tzinfo
    utc_ref = ref_datetime.astimezone(timezone.utc)
    utc_delta = utc_ref + shift
    if utc_out:
        return utc_delta
    return utc_delta.astimezone(ref_tz)
