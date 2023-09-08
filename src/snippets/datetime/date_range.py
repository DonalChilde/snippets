####################################################
#                                                  #
#       src/snippets/datetime/date_range.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-09-08T10:32:43-07:00            #
# Last Modified: 2023-09-08T17:35:34.512575+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################from datetime import date, datetime
from typing import Iterable


def date_range(
    start_date: date | datetime, end_date: date | datetime, *, inclusive: bool = True
) -> Iterable[date]:
    """Generate a range of dates."""
    # https://stackoverflow.com/a/32616832/105844
    if inclusive:
        extra = 1
    else:
        extra = 0
    if start_date < end_date:
        step = 1
    else:
        step = -1
    for ordinal in range(start_date.toordinal(), end_date.toordinal() + extra, step):
        yield date.fromordinal(ordinal)
