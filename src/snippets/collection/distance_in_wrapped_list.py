####################################################
#                                                  #
#  src/snippets/collection/distance_in_wrapped_list.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T15:30:51-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Callable, NamedTuple, Sequence, TypeVar

from .wrap_range import wrap_range

T = TypeVar("T")

# TODO function to return all matches
class NoMatchException(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class MatchDistance(NamedTuple):
    distance: int
    match_index: int


def distance_in_wrapped_list(
    list_data: Sequence[T],
    start_index: int,
    direction: int,
    filter_function: Callable[[T], bool],
) -> MatchDistance:
    """
    Find the distance between a starting index, and the first matching object in a list.

    Search will wrap around the list.

    Args:
        list_data: Sequence to search
        start_index: Index to start from, must be a valid index to list_data.
        direction: A positive integer to start search to the right, negative for left.
            Zero is not allowed.
        filter_function: The filter function to define a match.
    Returns:
        :class:`MatchDistance` or None if no match found.

    Raises:
        ValueError - No match found
    """

    range_generator = wrap_range(0, len(list_data), start_index, direction)
    for distance, index in enumerate(range_generator):
        if filter_function(list_data[index]):
            return MatchDistance(distance, index)
    raise NoMatchException("No match found.")
