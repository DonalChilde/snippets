####################################################
#                                                  #
# src/snippets/indexed_string/state_parser/parse_indexed_string.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-04-16T09:11:27-07:00            #
# Last Modified: 2023-04-22T15:59:58.362776+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
import logging
from typing import Any, Sequence

from snippets.indexed_string.indexed_string_protocol import IndexedStringProtocol
from snippets.indexed_string.state_parser.parse_exception import (
    ParseAllFail,
    ParseException,
    ParseJobFail,
    SingleParserFail,
)
from snippets.indexed_string.state_parser.state_parser_protocols import (
    IndexedStringParserProtocol,
    ParseResultProtocol,
)

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def parse_indexed_string(
    indexed_string: IndexedStringProtocol,
    parsers: Sequence[IndexedStringParserProtocol],
    ctx: dict[str, Any],
) -> ParseResultProtocol:
    """
    Parse an indexed string based on a list of possible parsers.

    The failure of an individual parser should raise a `ParseException`. This does not
    represent a failure of the parse job as a whole, unless none of the parses
    successfully match.

    Args:
        indexed_string: An indexed string to parse.
        parsers: A sequence of parsers to try.
        ctx: A store for arbitrary information needed to parse.

    Raises:
        SingleParserFail: Signals the failure of a parser.
        ParseJobFail: Signals the failure of the parse job as a whole.
        ParseAllFail: Signals the failure of all parsers.

    Returns:
        The result of a successful parse.
    """
    for parser in parsers:
        try:
            parse_result = parser.parse(indexed_string=indexed_string, ctx=ctx)
            return parse_result
        except SingleParserFail as error:
            logger.info(
                "\n\tFAILED %r->%r\n\t%r",
                error.parser.__class__.__name__,
                error.indexed_string,
                error,
            )
        except ParseJobFail as error:
            logger.info("Parse Job failed %s", error)
            raise error
    raise ParseAllFail(
        f"No parser found for {indexed_string!r}\nTried {parsers!r}",
        parsers=parsers,
        indexed_string=indexed_string,
    )
