# pylint: disable=missing-docstring, empty-docstring
####################################################
#                                                  #
# tests/snippets/collection/iterable_to_dict_test.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-28T10:52:22-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from dataclasses import dataclass
from operator import attrgetter, itemgetter

from snippets.collection.iterable_to_dict import (
    iterable_to_dict,
    iterable_to_dict_of_lists,
)


@dataclass
class SomeData:
    data_1: int
    data_2: str


def test_iterable_to_dict_list_data():
    list_data = [[1, 2, 3], ["a", "b", "c"], [4, 5, 6]]
    expected_result = {"1": [1, 2, 3], "a": ["a", "b", "c"], "4": [4, 5, 6]}
    key_getter = itemgetter(0)
    result = iterable_to_dict(data=list_data, key_getter=key_getter)
    assert result == expected_result


def test_iterable_to_dict_dict_data():
    dict_data = [
        {"arg1": 1, "arg2": 2, "arg3": 3},
        {"arg1": "a", "arg2": "b", "arg3": "c"},
        {"arg1": 4, "arg2": 5, "arg3": 6},
    ]
    expected_result = {
        "2": {"arg1": 1, "arg2": 2, "arg3": 3},
        "b": {"arg1": "a", "arg2": "b", "arg3": "c"},
        "5": {"arg1": 4, "arg2": 5, "arg3": 6},
    }
    key_getter = itemgetter("arg2")
    result = iterable_to_dict(data=dict_data, key_getter=key_getter)
    assert result == expected_result


def test_iterable_to_dict_obj_data():
    obj_data = [SomeData(1, "a"), SomeData(2, "b"), SomeData(3, "c")]
    expected_result = {
        "1": SomeData(1, "a"),
        "2": SomeData(2, "b"),
        "3": SomeData(3, "c"),
    }
    key_getter = attrgetter("data_1")
    result = iterable_to_dict(data=obj_data, key_getter=key_getter)
    assert result == expected_result


def test_iterable_to_dict_of_lists_list_data():
    list_data = [[1, 2, 3], ["a", "b", "c"], [4, 5, 6], [4, 5, 6]]
    expected_result = {
        "1": [[1, 2, 3]],
        "a": [["a", "b", "c"]],
        "4": [[4, 5, 6], [4, 5, 6]],
    }
    key_getter = itemgetter(0)
    result = iterable_to_dict_of_lists(data=list_data, key_getter=key_getter)
    assert result == expected_result


def test_iterable_to_dict_of_lists_dict_data():
    dict_data = [
        {"arg1": 1, "arg2": 2, "arg3": 3},
        {"arg1": "a", "arg2": "b", "arg3": "c"},
        {"arg1": 4, "arg2": 5, "arg3": 6},
        {"arg1": 4, "arg2": 5, "arg3": 6},
    ]
    expected_result = {
        "2": [{"arg1": 1, "arg2": 2, "arg3": 3}],
        "b": [{"arg1": "a", "arg2": "b", "arg3": "c"}],
        "5": [{"arg1": 4, "arg2": 5, "arg3": 6}, {"arg1": 4, "arg2": 5, "arg3": 6}],
    }
    key_getter = itemgetter("arg2")
    result = iterable_to_dict_of_lists(data=dict_data, key_getter=key_getter)
    assert result == expected_result


def test_iterable_to_dict_of_lists_obj_data():
    obj_data = [SomeData(1, "a"), SomeData(2, "b"), SomeData(3, "c"), SomeData(3, "c")]
    expected_result = {
        "1": [SomeData(1, "a")],
        "2": [SomeData(2, "b")],
        "3": [SomeData(3, "c"), SomeData(3, "c")],
    }
    key_getter = attrgetter("data_1")
    result = iterable_to_dict_of_lists(data=obj_data, key_getter=key_getter)
    assert result == expected_result
