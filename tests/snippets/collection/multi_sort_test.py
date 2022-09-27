# pylint: disable=missing-docstring, empty-docstring
####################################################
#                                                  #
#   tests/snippets/collection/multi_sort_test.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T15:35:16-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
import logging
from dataclasses import dataclass

import pytest

from snippets.collection.multi_sort import (
    SortInstructionAttrgetter,
    SortInstructionItemgetter,
    sort_in_place,
    sort_to_new_list,
)

#### setting up logger ####
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


@dataclass
class SomeData:
    data_1: int
    data_2: str


list_1 = ["d", "e", "f", 1, 4]
list_2 = ["a", "b", "c", 2, 5]
list_3 = ["g", "h", "i", 3, 6]
list_4 = ["d", "e", "f", 4, 4]
list_5 = ["a", "b", "c", 5, 5]
list_6 = ["g", "h", "i", 6, 6]

obj_1 = SomeData(1, "a")
obj_2 = SomeData(2, "b")
obj_3 = SomeData(3, "c")
obj_4 = SomeData(1, "d")
obj_5 = SomeData(2, "e")
obj_6 = SomeData(3, "f")


def test_attrgetter_new_list_multiple():
    # only one test of sort to new list, as its a near duplicate of inplace sort.
    data = [obj_2, obj_3, obj_1, obj_5, obj_4, obj_6]
    print("data:\n", data)
    sort_instructions = [
        SortInstructionAttrgetter(sort_key="data_1", descending=False),
        SortInstructionAttrgetter(sort_key="data_2", descending=True),
    ]
    expected_result = [obj_4, obj_1, obj_5, obj_2, obj_6, obj_3]
    result = sort_to_new_list(data, sort_instructions)
    print("sorted data:\n", data)
    print("expected result:\n", expected_result)
    assert data != result
    assert result == expected_result


def test_attrgetter_in_place_multiple():
    data = [obj_2, obj_3, obj_1, obj_5, obj_4, obj_6]
    print("data:\n", data)
    sort_instructions = [
        SortInstructionAttrgetter(sort_key="data_1", descending=False),
        SortInstructionAttrgetter(sort_key="data_2", descending=True),
    ]
    expected_result = [obj_4, obj_1, obj_5, obj_2, obj_6, obj_3]
    sort_in_place(data, sort_instructions)
    print("sorted data:\n", data)
    print("expected result:\n", expected_result)
    assert data == expected_result


def test_attrgetter_in_place_ascending():
    data = [obj_2, obj_3, obj_1, obj_5, obj_4, obj_6]
    print("data:\n", data)
    sort_instructions = [
        SortInstructionAttrgetter(sort_key="data_2", descending=False),
    ]
    expected_result = [obj_1, obj_2, obj_3, obj_4, obj_5, obj_6]
    sort_in_place(data, sort_instructions)
    print("sorted data:\n", data)
    print("expected result:\n", expected_result)
    assert data == expected_result


def test_attrgetter_in_place_descending():
    data = [obj_2, obj_3, obj_1, obj_5, obj_4, obj_6]
    print("data:\n", data)
    sort_instructions = [
        SortInstructionAttrgetter(sort_key="data_2", descending=True),
    ]
    expected_result = [obj_6, obj_5, obj_4, obj_3, obj_2, obj_1]
    sort_in_place(data, sort_instructions)
    print("sorted data:\n", data)
    print("expected result:\n", expected_result)
    assert data == expected_result


def test_itemgetter_in_place_descending():
    data = [list_1, list_2, list_3]
    sort_instructions = [SortInstructionItemgetter(sort_key=0, descending=True)]
    expected_result = [list_3, list_1, list_2]
    sort_in_place(data, sort_instructions)
    print(data)
    print(expected_result)
    assert data == expected_result


def test_itemgetter_in_place_ascending():
    data = [list_1, list_2, list_3]
    sort_instructions = [SortInstructionItemgetter(sort_key=0, descending=False)]
    expected_result = [list_2, list_1, list_3]
    sort_in_place(data, sort_instructions)
    print(data)
    print(expected_result)
    assert data == expected_result


def test_itemgetter_in_place_multiple():
    data = [list_1, list_2, list_3, list_4, list_5, list_6]
    sort_instructions = [
        SortInstructionItemgetter(sort_key=0, descending=False),
        SortInstructionItemgetter(sort_key=3, descending=False),
    ]
    expected_result = [list_2, list_5, list_1, list_4, list_3, list_6]
    sort_in_place(data, sort_instructions)
    print(data)
    print(expected_result)
    assert data == expected_result


def test_itemgetter_in_place_multiple_descending():
    data = [list_1, list_2, list_3, list_4, list_5, list_6]
    print("data:\n", data)
    sort_instructions = [
        SortInstructionItemgetter(sort_key=0, descending=False),
        SortInstructionItemgetter(sort_key=3, descending=True),
    ]
    expected_result = [list_5, list_2, list_4, list_1, list_6, list_3]
    sort_in_place(data, sort_instructions)
    print("sorted data:\n", data)
    print("expected result:\n", expected_result)
    assert data == expected_result


def test_no_sort_method():

    with pytest.raises(AttributeError):
        no_sort = int
        primary_sort = SortInstructionAttrgetter(sort_key="data_2", descending=True)
        sort_in_place(no_sort, [primary_sort])
