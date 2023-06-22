####################################################
#                                                  #
#       src/snippets/file/list_file_open.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-06-20T19:00:01-07:00            #
# Last Modified: 2023-06-22T14:52:30.120732+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from pathlib import Path
from typing import IO, Any, Sequence

# Context manager to open a list of files, returned as a dict of file pointers.


class OpenFiles:
    def __init__(
        self, file_paths: Sequence[Path], mode: str, encoding: str = "utf-8"
    ) -> None:
        self.file_paths = file_paths
        self.mode = mode
        self.encoding = encoding
        self.file_p: dict[str, IO[Any]] = {}

    def __enter__(self):
        for file in self.file_paths:
            self.file_p[str(file)] = open(file, mode=self.mode, encoding=self.encoding)
        return self.file_p

    def __exit__(self, exc_type, exc_val, exc_tb):
        for file in self.file_p.values():
            file.close()
