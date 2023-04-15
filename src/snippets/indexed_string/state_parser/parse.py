####################################################
#                                                  #
# src/snippets/indexed_string/state_parser/parse.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-04-15T16:05:58-07:00            #
# Last Modified: 2023-04-15T23:08:58.642309+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
import logging
from typing import Any, Iterable, Iterator, Sequence

from snippets.indexed_string.indexed_string_protocol import IndexedStringProtocol
from snippets.indexed_string.state_parser.parse_exception import ParseException
from snippets.indexed_string.state_parser.state_parser_protocols import (
    IndexedStringParserProtocol,
    ParseManagerProtocol,
    ParseResultProtocol,
)

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


# def parse_indexed_strings(
#     indexed_strings: Iterable[IndexedStringProtocol],
#     manager: ParseManagerProtocol,
# ) -> Iterable[ParseResultProtocol]:
#     pass


def parse_indexed_strings(
    indexed_strings: Iterable[IndexedStringProtocol],
    manager: ParseManagerProtocol,
) -> Iterator[ParseResultProtocol]:
    current_state = "start"
    for indexed_string in indexed_strings:
        try:
            parse_result = parse_indexed_string(
                indexed_string=indexed_string,
                parsers=manager.expected_parsers(current_state),
                ctx=manager.ctx,
            )
            # manager.handle_result(parse_result=parse_result)
            current_state = parse_result.current_state
            yield parse_result
        except ParseException as error:
            logger.error("%s", error)
            raise error


def parse_indexed_string(
    indexed_string: IndexedStringProtocol,
    parsers: Sequence[IndexedStringParserProtocol],
    ctx: dict[str, Any],
) -> ParseResultProtocol:
    for parser in parsers:
        try:
            parse_result = parser.parse(indexed_string=indexed_string, ctx=ctx)
            logger.info("\n\tPARSED %r->%r", parser.__class__.__name__, indexed_string)
            return parse_result
        except ParseException as error:
            logger.info(
                "\n\tFAILED %r->%r\n\t%r",
                parser.__class__.__name__,
                indexed_string,
                error,
            )
    raise ParseException(f"No parser found for {indexed_string!r}\nTried {parsers!r}")
