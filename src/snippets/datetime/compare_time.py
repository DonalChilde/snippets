####################################################
#                                                  #
#       src/snippets/datetime/compare_time.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-09-08T05:08:54-07:00            #
# Last Modified: 2023-09-08T12:11:03.022194+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from datetime import time


def compare_time(time_1: time, time_2: time, *, ignore_tz: bool = True) -> bool:
    """
    Compare two times, ignoring time zone.

    Args:
        time_1: First time value.
        time_2: Second time value.
        ignore_tz: Disregard timezone state during comparison. Defaults to True.

    Raises:
        ValueError: When not ignoring timezone state, raise value error if the two
            times have differing time zone states, e.g. None and UTC.

    Returns:
        comparison result
    """
    if ignore_tz:
        naive_time_1 = time_1.replace(tzinfo=None)
        naive_time_2 = time_2.replace(tzinfo=None)
        return naive_time_1 == naive_time_2
    matching_tz_aware_state = bool(time_1.tzinfo) == bool(time_2.tzinfo)
    if not matching_tz_aware_state:
        raise ValueError(
            f"Cannot compare two times with different timezone states. "
            f"time_1={time_1!r} time_2={time_2!r}"
        )
    return time_1 == time_2
