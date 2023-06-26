####################################################
#                                                  #
#  src/snippets/indexed_string/dataclass/indexed_string.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-11-02T07:34:02-07:00            #
# Last Modified: 2023-06-26T22:54:24.730673+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from dataclasses import dataclass
from typing import Protocol


@dataclass
class IndexedString:
    idx: int
    txt: str

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f"{cls_name}(idx={self.idx}, txt={self.txt!r})"

    def __str__(self):
        return f"{self.idx}: {self.txt!r}"


class IndexedStringProtocol(Protocol):
    idx: int
    txt: str
