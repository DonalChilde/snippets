####################################################
#                                                  #
#      src/snippets/indexed_string/filters.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-11-10T15:27:45-07:00            #
# Last Modified: 2023-04-15T23:08:58.643699+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Callable, Sequence

from snippets.indexed_string.indexed_string_protocol import IndexedStringProtocol


class SkipBlankLines:
    def __call__(self, indexed_string: IndexedStringProtocol) -> bool:
        return bool(indexed_string.txt.strip())


class SkipTillMatch:
    def __init__(self, matcher: Callable[[IndexedStringProtocol], bool]) -> None:
        self.matcher = matcher
        self.procede = False

    def __call__(self, indexed_string: IndexedStringProtocol) -> bool:
        if self.procede:
            return True
        if self.matcher(indexed_string):
            self.procede = True
            return True
        return False


class MultiTest:
    def __init__(
        self, testers: Sequence[Callable[[IndexedStringProtocol], bool]]
    ) -> None:
        self.testers: Sequence[Callable[[IndexedStringProtocol], bool]] = list(testers)

    def __call__(self, indexed_string: IndexedStringProtocol) -> bool:
        return all((tester(indexed_string) for tester in self.testers))


def isNumeric(indexed_string: IndexedStringProtocol) -> bool:
    return indexed_string.txt.isnumeric()


def isBlank(indexed_string: IndexedStringProtocol) -> bool:
    return bool(indexed_string.txt.strip())


def pass_through(indexed_string: IndexedStringProtocol) -> bool:
    _ = indexed_string
    return True
