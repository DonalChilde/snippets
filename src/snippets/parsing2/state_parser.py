import logging
from pathlib import Path
from typing import Callable, Iterable, Sequence

from snippets.parsing2 import state_parser_protocols as spp
from snippets.parsing2.parse_exception import ParseException
from snippets.parsing.indexed_string import IndexedString

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def parse_file(
    file_path: Path,
    ctx: spp.ParseContext,
    skipper: Callable[[spp.IndexedString], bool] | None = None,
):
    with open(file_path, encoding="utf-8") as file:
        try:
            parse_lines(file, ctx=ctx, skipper=skipper)
        except ParseException as error:
            logger.error("%s Failed to parse %r", file_path, error)
            raise error


def parse_lines(
    lines: Iterable[str],
    ctx: spp.ParseContext,
    skipper: Callable[[spp.IndexedString], bool] | None = None,
):
    state = "start"
    for line_number, line in enumerate(lines):
        indexed_string = IndexedString(idx=line_number, txt=line)
        if skipper is not None and not skipper(indexed_string):
            continue
        try:
            parse_result = parse_line(
                indexed_string=indexed_string,
                parsers=ctx.expected_parsers.parsers_from_state(state),
            )
            ctx.result_handler.handle_result(parse_result=parse_result)
            state = parse_result.new_state
        except ParseException as error:
            logger.error("%s", error)
            raise error


def parse_line(
    indexed_string: IndexedString, parsers: Sequence[spp.IndexedStringParser]
) -> spp.ParseResult:
    for parser in parsers:
        try:
            parse_result = parser.parse(indexed_string=indexed_string)
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
