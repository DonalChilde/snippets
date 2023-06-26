####################################################
#                                                  #
#   src/snippets/indexed_string/dataclass/index_strings.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-04-15T16:11:15-07:00            #
# Last Modified: 2023-06-26T22:54:24.731503+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Callable, Iterable, Iterator

from snippets.indexed_string.dataclass.indexed_string import (
    IndexedString,
    IndexedStringProtocol,
)


def index_strings(
    strings: Iterable[str],
    factory: Callable[[int, str], IndexedStringProtocol] = IndexedString,
    index_start=0,
) -> Iterator[IndexedStringProtocol]:
    """
    Enumerate a string iterable, yield an `IndexedStringProtocol`.

    Args:
        strings: An iterable of strings.
        factory: The factory used to make an indexed string. Defaults to IndexedStringDC.
        index_start: Defaults to 0.

    Yields:
        The indexed strings.
    """
    for idx, txt in enumerate(strings, start=index_start):
        indexed_string = factory(idx, txt)
        yield indexed_string
