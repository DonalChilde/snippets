####################################################
#                                                  #
#          src/snippets/indexed_string/indexed_string.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-06-26T14:26:13-07:00            #
# Last Modified: 2023-06-26T22:54:24.731566+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from dataclasses import dataclass
from typing import Protocol, TypedDict


@dataclass
class IndexedStringDC:
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


class IndexedString(TypedDict):
    idx: int
    txt: str


def foo(value: IndexedStringProtocol):
    return True


def bar():
    istd = IndexedString(idx=1, txt="loreipsum")
    isdc = IndexedStringDC(idx=1, txt="foobar")
    one = foo(istd)
    two = foo(isdc)
