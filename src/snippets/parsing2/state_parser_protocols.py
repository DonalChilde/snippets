from typing import Protocol, Sequence


class IndexedString(Protocol):
    idx: int
    txt: str


class ParsedIndexedString(Protocol):
    source: IndexedString


class ParseResult(Protocol):
    new_state: str
    parsed_data: ParsedIndexedString


class IndexedStringParser(Protocol):
    """Parse an IndexedString.

    Raise ParseException on a parse error. Pass any additional information
    required in the kwargs. A successful parse also determines the new state of the
    parse job.
    """

    def parse(self, indexed_string: IndexedString, **kwargs) -> ParseResult:
        """foo"""


class ResultHandler(Protocol):
    """Do something with the result of a successful parse.

    Pass in any necessary instructions or objects in the kwargs, e.g. an object
    for accumulation of data, or a database connection.
    """

    def handle_result(self, parse_result: ParseResult, **kwargs):
        ...


class ExpectedParsers(Protocol):
    """Get a list of parsers expected to match the next string.

    The state string is usually obtained during the previous parse, where a successful
    parse determines the new state of the parse job.
    """

    def parsers_from_state(self, state: str, **kwargs) -> Sequence[IndexedStringParser]:
        ...


class ParseContext(Protocol):
    """Holds references to the ResultHandler and ExpectedParsers"""

    result_handler: ResultHandler
    expected_parsers: ExpectedParsers
