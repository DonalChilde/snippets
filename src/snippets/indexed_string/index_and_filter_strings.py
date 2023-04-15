####################################################
#                                                  #
# src/snippets/indexed_string/index_and_filter_strings.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-04-15T16:11:28-07:00            #
# Last Modified: 2023-04-15T23:11:59.237542+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Callable, Iterable, Iterator

from snippets.indexed_string.indexed_string_dc import IndexedStringDC
from snippets.indexed_string.indexed_string_protocol import IndexedStringProtocol


def index_and_filter_strings(
    strings: Iterable[str],
    string_filter: Callable[[IndexedStringProtocol], bool],
    factory: Callable[[int, str], IndexedStringProtocol] = IndexedStringDC,
) -> Iterator[IndexedStringProtocol]:
    """Enumerate and filter string iterable, yield matches as IndexedStringProtocol"""
    for idx, txt in enumerate(strings):
        indexed_string = factory(idx, txt)
        if string_filter(indexed_string):
            yield indexed_string
