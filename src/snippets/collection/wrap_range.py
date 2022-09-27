####################################################
#                                                  #
#          src/snippets/collection/wrap_range.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T13:57:18-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

"""
wrap_range makes an iterator that contains the values in a range.

The values can have an arbitrary start point, and direction, and will
wrap around so that all values are represented.
"""

import logging
from itertools import chain
from typing import Iterator

#### setting up logger ####
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def wrap_range(
    left_boundry: int, right_boundry: int, start_index: int, direction: int
) -> Iterator[int]:
    """Create a range of integer values that start somewhere between the beginning and end, wrapping around back to start.

    Example:
    e.g. wrap_range(0,10,6,1) = [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
         wrap_range(0,10,6,-1) = [6, 5, 4, 3, 2, 1, 0, 9, 8, 7]
         wrap_range(-2, 10, 6, -1) = [6, 5, 4, 3, 2, 1, 0, -1, -2, 9, 8, 7]

    Note:
        right_boundry mimics the behavior of :func:`range`,
        where range(0,10) = [0,1,2,3,4,5,6,7,8,9]

    Args:
        left_boundry: lower boundry of number line
        right_boundry: upper boundry of number line + 1
        start_index: starting value, must be  left_bound >= start_index < right_bound
        direction: a positive or negative integer, where positive integers increment
        to the right on the number line, and negative integers increment to the left.

    Raises:
        ValueError: direction cannot be zero
        ValueError: left_boundry cannot be greater than right_boundry

    Returns:
        An :class:`itertools.chain` linking two :func:`range` generators.

    """
    logger.debug(
        "wrap_range(left_boundry=%s, right_bound=%s, start_index=%s, direction=%s)",
        left_boundry,
        right_boundry,
        start_index,
        direction,
    )
    if direction == 0:
        raise ValueError("direction cannot be zero")
    if left_boundry > right_boundry:
        raise ValueError(
            f"left_bound {left_boundry} is greater than right_bound {right_boundry}"
        )
    range_generator = None
    if direction > 0:
        left_range = range(left_boundry, start_index)
        right_range = range(start_index, right_boundry)
        range_generator = chain(right_range, left_range)
    else:
        left_range = range(start_index, left_boundry - 1, -1)
        right_range = range(right_boundry - 1, start_index, -1)
        range_generator = chain(left_range, right_range)
    return range_generator
