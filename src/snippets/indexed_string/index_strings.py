####################################################
#                                                  #
#   src/snippets/indexed_string/index_strings.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-04-15T16:11:15-07:00            #
# Last Modified: 2023-04-15T23:11:59.238130+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Callable, Iterable, Iterator

from snippets.indexed_string.indexed_string_dc import IndexedStringDC
from snippets.indexed_string.indexed_string_protocol import IndexedStringProtocol


def index_strings(
    strings: Iterable[str],
    factory: Callable[[int, str], IndexedStringProtocol] = IndexedStringDC,
) -> Iterator[IndexedStringProtocol]:
    """Enumerate strings and yield as IndexedStringProtocol"""
    for idx, txt in enumerate(strings):
        indexed_string = factory(idx, txt)
        yield indexed_string
