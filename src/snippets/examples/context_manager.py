####################################################
#                                                  #
#     src/snippets/examples/context_manager.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-06-30T15:36:54-07:00            #
# Last Modified: 2023-07-01T21:57:53.536433+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

from io import TextIOWrapper
from pathlib import Path
from typing import Any


class Example:
    def __init__(self, file_in: Path) -> None:
        self.file_in = file_in
        self.file_fp: TextIOWrapper | None = None

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __enter__(self) -> TextIOWrapper:
        self.file_fp = open(self.file_in, mode="rt", encoding="utf-8")
        return self.file_fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_fp is not None:
            self.file_fp.close()
