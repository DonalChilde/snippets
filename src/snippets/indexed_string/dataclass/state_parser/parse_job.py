####################################################
#                                                  #
# src/snippets/indexed_string/dataclass/state_parser/parse_job.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-05-07T11:30:50-07:00            #
# Last Modified: 2023-06-26T22:54:24.729751+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Iterable, TypeVar

from snippets.indexed_string.dataclass.indexed_string import IndexedStringProtocol
from snippets.indexed_string.dataclass.state_parser.parse_indexed_strings import (
    parse_indexed_strings,
)
from snippets.indexed_string.dataclass.state_parser.state_parser_protocols import (
    ParseManagerProtocol,
)

T = TypeVar("T")


def parse_job(
    indexed_strings: Iterable[IndexedStringProtocol],
    manager: ParseManagerProtocol[T],
) -> T | None:
    manager.result_handler().initialize(manager.ctx)
    for parse_result in parse_indexed_strings(
        indexed_strings=indexed_strings, manager=manager
    ):
        manager.result_handler().handle_result(parse_result)
    manager.result_handler().finalize(manager.ctx)
    return manager.result_handler().result_data()
