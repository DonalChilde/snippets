####################################################
#                                                  #
#          src/snippets/collection/search.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T15:30:51-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
import logging
from typing import Any, Callable, NamedTuple, Optional, Sequence, TypeVar

from .wrap_range import wrap_range

#### setting up logger ####
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

T = TypeVar("T")


class MatchDistance(NamedTuple):
    distance: int
    match_index: int


def distance_in_list(
    list_data: Sequence[Any],
    start_index: int,
    direction: int,
    filter_function: Callable[[Any], bool],
) -> Optional[MatchDistance]:
    """
    Find the distance between a starting index, and the first matching object in a list.

    Search will wrap around the list.

    Args:
        list_data: Sequence to search
        start_index: Index to start from
        direction: A positive integer to start search to the right, negative for left.
            Zero is not allowed.
        filter_function: The filter function to define a match.
    Returns:
        :class:`MatchDistance` or None if no match found.
    """
    logging.debug(
        "distance_in_list(list_data=%s, start_index=%s, direction=%s, filter_function=%s)",
        list_data,
        start_index,
        direction,
        filter_function,
    )
    logging.debug(
        "range_generator as list=%s",
        list(wrap_range(0, len(list_data), start_index, direction)),
    )
    range_generator = wrap_range(0, len(list_data), start_index, direction)
    for distance, index in enumerate(range_generator):
        if filter_function(list_data[index]):
            return MatchDistance(distance, index)
    return None
