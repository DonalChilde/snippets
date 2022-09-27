import logging
from itertools import chain
from typing import Iterator

#### setting up logger ####
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def wrap_range(
    left_bound: int, right_bound: int, start_index: int, direction: int
) -> Iterator[int]:
    """Create a range of integer values that start somewhere between the beginning and end, wrapping around back to start.

    e.g. wrap_range(0,10,6,1) = [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
         wrap_range(0,10,6,-1) = [6, 5, 4, 3, 2, 1, 0, 9, 8, 7]
         wrap_range(-2, 10, 6, -1) = [6, 5, 4, 3, 2, 1, 0, -1, -2, 9, 8, 7]

    note right_bound mimics the behavior of range(),
    where range(0,10) = [0,1,2,3,4,5,6,7,8,9]

    :param left_bound: lower boundry of number line
    :param right_bound: upper boundry of number line + 1
    :param start_index: starting value, must be  left_bound >= start_index < right_bound
    :param direction: a positive or negative integer, where positive integers increment
        to the right on the number line, and negative integers increment to the left.
    :raises ValueError: direction cannot be zero
    :raises ValueError: left_bound cannot be greater than right_bound
    :returns: Two range() generators chained by itertools.chain
    """
    logger.debug(
        "wrap_range(left_bound=%s, right_bound=%s, start_index=%s, direction=%s)",
        left_bound,
        right_bound,
        start_index,
        direction,
    )
    if direction == 0:
        raise ValueError("direction cannot be zero")
    if left_bound > right_bound:
        raise ValueError(
            f"left_bound {left_bound} is greater than right_bound {right_bound}"
        )
    range_generator = None
    if direction > 0:
        left_range = range(left_bound, start_index)
        right_range = range(start_index, right_bound)
        range_generator = chain(right_range, left_range)
    else:
        left_range = range(start_index, left_bound - 1, -1)
        right_range = range(right_bound - 1, start_index, -1)
        range_generator = chain(left_range, right_range)
    return range_generator


# TODO keep these as examples, suggest use more itertools
# def chunk(it, size):
#     """
#     https://stackoverflow.com/a/22045226
#     """
#     it = iter(it)
#     return iter(lambda: tuple(islice(it, size)), ())


# def chunk_pad(it, size, padval=None):
#     """
#     https://stackoverflow.com/a/22045226
#     """
#     it = chain(iter(it), repeat(padval))
#     return iter(lambda: tuple(islice(it, size)), (padval,) * size)


# def chunks(l, n):
#     """
#     https://stackoverflow.com/a/1751478
#     """
#     n = max(1, n)
#     return (l[i : i + n] for i in range(0, len(l), n))
