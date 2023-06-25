import json
from pathlib import Path
from typing import TypeVar

from snippets.file.validate_file_out import validate_file_out
from snippets.indexed_string.state_parser_3.state_parser_protocols import (
    ParseResult,
    ResultHandlerData,
)

T = TypeVar("T")


class SaveAsJson:
    def __init__(
        self, file_out: Path, overwrite: bool = False, indent: int = 2, **kwargs
    ) -> None:
        self.data: ResultHandlerData = {"kwargs": {}, "data": []}
        self.file_out = file_out
        self.overwrite = overwrite
        self.indent = indent
        self.data["kwargs"].update(kwargs)

    def __enter__(self):
        validate_file_out(file_path=self.file_out, overwrite=self.overwrite)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_out.write_text(json.dumps(self.data, indent=self.indent))

    def handle_result(
        self, parse_result: ParseResult, ctx: dict | None = None, **kwargs
    ):
        """
        Handle the result of a successful parse.

        Args:
            parse_result: The result of a successful parse.
        """
        _ = ctx, kwargs
        self.data["data"].append(parse_result)
