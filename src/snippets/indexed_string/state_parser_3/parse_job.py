####################################################
#                                                  #
# src/snippets/indexed_string/state_parser_3/parse_job.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-05-07T11:30:50-07:00            #
# Last Modified: 2023-06-25T16:27:56.954383+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Any, Iterable, TypeVar

from snippets.indexed_string.indexed_string_td import IndexedString
from snippets.indexed_string.state_parser_3.parse_indexed_strings import (
    parse_indexed_strings,
)
from snippets.indexed_string.state_parser_3.state_parser_protocols import (
    ParseResult,
    ParserLookupProtocol,
    ResultHandlerProtocol,
)

T = TypeVar("T")


def parse_job(
    indexed_strings: Iterable[IndexedString],
    parser_lookup: ParserLookupProtocol,
    result_handler: ResultHandlerProtocol,
    ctx: dict[str, Any] | None = None,
) -> list[ParseResult] | None:
    with result_handler:
        for parse_result in parse_indexed_strings(
            indexed_strings=indexed_strings, parser_lookup=parser_lookup, ctx=ctx
        ):
            result_handler.handle_result(parse_result=parse_result, ctx=ctx)
    return result_handler.data
