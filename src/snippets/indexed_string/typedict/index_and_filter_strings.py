####################################################
#                                                  #
# src/snippets/indexed_string/typedict/index_and_filter_strings.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-04-15T16:11:28-07:00            #
# Last Modified: 2023-06-26T23:11:51.059632+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Callable, Iterable, Iterator

from snippets.indexed_string.typedict.indexed_string import IndexedString


def index_and_filter_strings(
    strings: Iterable[str],
    string_filter: Callable[[IndexedString], bool],
    factory: Callable[[int, str], IndexedString] | None = None,
    index_start=0,
) -> Iterator[IndexedString]:
    """
    Enumerate and filter a string iterable, yield matches as an `IndexedStringProtocol`

    Args:
        strings: An iterable of strings.
        string_filter: Used to test strings.
        factory: The factory used to make an indexed string. Defaults to IndexedStringDC.
        index_start: Defaults to 0.

    Yields:
        The matched indexed strings.
    """
    for idx, txt in enumerate(strings, start=index_start):
        if factory is None:
            indexed_string = IndexedString(idx=idx, txt=txt)
        else:
            indexed_string = factory(idx, txt)
        if string_filter(indexed_string):
            yield indexed_string