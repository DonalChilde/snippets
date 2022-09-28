# pylint: disable=missing-docstring, empty-docstring
####################################################
#                                                  #
# tests/snippets/collection/distance_in_wrapped_list_test.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-28T10:01:16-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
import logging
from dataclasses import dataclass
from typing import List

import pytest

from snippets.collection.distance_in_wrapped_list import (
    MatchDistance,
    NoMatchException,
    distance_in_wrapped_list,
)
from snippets.filter.filter import simple_filter

#### setting up logger ####
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


@dataclass
class TestInstruction:
    target: int
    start_idx: int
    dir: int
    expected: MatchDistance


def test_distance_in_list_int():
    list_data = list(range(10))
    # List_data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    instructions = [
        TestInstruction(target=5, start_idx=4, dir=1, expected=MatchDistance(1, 5)),
        TestInstruction(target=5, start_idx=5, dir=1, expected=MatchDistance(0, 5)),
        TestInstruction(target=5, start_idx=6, dir=1, expected=MatchDistance(9, 5)),
        TestInstruction(target=5, start_idx=7, dir=1, expected=MatchDistance(8, 5)),
        TestInstruction(target=5, start_idx=8, dir=1, expected=MatchDistance(7, 5)),
        TestInstruction(target=5, start_idx=9, dir=1, expected=MatchDistance(6, 5)),
        TestInstruction(target=5, start_idx=0, dir=1, expected=MatchDistance(5, 5)),
        TestInstruction(target=5, start_idx=1, dir=1, expected=MatchDistance(4, 5)),
        TestInstruction(target=5, start_idx=2, dir=1, expected=MatchDistance(3, 5)),
        TestInstruction(target=5, start_idx=3, dir=1, expected=MatchDistance(2, 5)),
        TestInstruction(target=5, start_idx=4, dir=-1, expected=MatchDistance(9, 5)),
        TestInstruction(target=5, start_idx=5, dir=-1, expected=MatchDistance(0, 5)),
        TestInstruction(target=5, start_idx=6, dir=-1, expected=MatchDistance(1, 5)),
        TestInstruction(target=5, start_idx=7, dir=-1, expected=MatchDistance(2, 5)),
        TestInstruction(target=5, start_idx=8, dir=-1, expected=MatchDistance(3, 5)),
        TestInstruction(target=5, start_idx=9, dir=-1, expected=MatchDistance(4, 5)),
        TestInstruction(target=5, start_idx=0, dir=-1, expected=MatchDistance(5, 5)),
        TestInstruction(target=5, start_idx=1, dir=-1, expected=MatchDistance(6, 5)),
        TestInstruction(target=5, start_idx=2, dir=-1, expected=MatchDistance(7, 5)),
        TestInstruction(target=5, start_idx=3, dir=-1, expected=MatchDistance(8, 5)),
    ]
    for instruction in instructions:
        do_the_test(test_data=list_data, instruction=instruction)


def test_distance_in_list_str():
    list_data = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
    ]
    instructions = [
        TestInstruction(
            target="five", start_idx=4, dir=1, expected=MatchDistance(0, 4)
        ),
        TestInstruction(
            target="five", start_idx=5, dir=1, expected=MatchDistance(9, 4)
        ),
        TestInstruction(
            target="five", start_idx=6, dir=1, expected=MatchDistance(8, 4)
        ),
        TestInstruction(
            target="five", start_idx=7, dir=1, expected=MatchDistance(7, 4)
        ),
        TestInstruction(
            target="five", start_idx=8, dir=1, expected=MatchDistance(6, 4)
        ),
        TestInstruction(
            target="five", start_idx=9, dir=1, expected=MatchDistance(5, 4)
        ),
        TestInstruction(
            target="five", start_idx=0, dir=1, expected=MatchDistance(4, 4)
        ),
        TestInstruction(
            target="five", start_idx=1, dir=1, expected=MatchDistance(3, 4)
        ),
        TestInstruction(
            target="five", start_idx=2, dir=1, expected=MatchDistance(2, 4)
        ),
        TestInstruction(
            target="five", start_idx=3, dir=1, expected=MatchDistance(1, 4)
        ),
        TestInstruction(
            target="five", start_idx=4, dir=-1, expected=MatchDistance(0, 4)
        ),
        TestInstruction(
            target="five", start_idx=5, dir=-1, expected=MatchDistance(1, 4)
        ),
        TestInstruction(
            target="five", start_idx=6, dir=-1, expected=MatchDistance(2, 4)
        ),
        TestInstruction(
            target="five", start_idx=7, dir=-1, expected=MatchDistance(3, 4)
        ),
        TestInstruction(
            target="five", start_idx=8, dir=-1, expected=MatchDistance(4, 4)
        ),
        TestInstruction(
            target="five", start_idx=9, dir=-1, expected=MatchDistance(5, 4)
        ),
        TestInstruction(
            target="five", start_idx=0, dir=-1, expected=MatchDistance(6, 4)
        ),
        TestInstruction(
            target="five", start_idx=1, dir=-1, expected=MatchDistance(7, 4)
        ),
        TestInstruction(
            target="five", start_idx=2, dir=-1, expected=MatchDistance(8, 4)
        ),
        TestInstruction(
            target="five", start_idx=3, dir=-1, expected=MatchDistance(9, 4)
        ),
    ]
    for instruction in instructions:
        do_the_test(test_data=list_data, instruction=instruction)


def test_fail_to_match():
    with pytest.raises(NoMatchException):
        _ = distance_in_wrapped_list([1, 2, 3, 4, 5], 4, 1, simple_filter("Not Here"))


def do_the_test(test_data: List, instruction: TestInstruction):
    match_distance = distance_in_wrapped_list(
        list_data=test_data,
        start_index=instruction.start_idx,
        direction=instruction.dir,
        filter_function=simple_filter(instruction.target),
    )
    assert match_distance == instruction.expected
