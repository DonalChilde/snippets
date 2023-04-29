####################################################
#                                                  #
#     src/snippets/filter/filtered_enumerate.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-04-29T08:32:51-07:00            #
# Last Modified: 2023-04-29T15:36:05.235313+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Callable, Iterable, Tuple, TypeVar

T = TypeVar("T")


class FilteredEnumerate:
    def __init__(self) -> None:
        """Enumerate values, return filtered enumerated values.

        Keeps a count of values enumerated.
        """
        self.counter = 0

    def __call__(
        self, sieve: Callable[[T], bool], values: Iterable[T]
    ) -> Iterable[Tuple[int, T]]:
        for idx, value in enumerate(values):
            self.counter += 1
            if not sieve(value):
                continue
            yield idx, value
