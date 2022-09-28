# pylint: disable=missing-docstring, empty-docstring
####################################################
#                                                  #
# tests/snippets/collection/optional_object_test.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T11:04:15-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

"""

"""

from dataclasses import dataclass
from typing import Dict, List, Optional

from snippets.collection.optional_object import optional_object


@dataclass
class SomeData:
    data_1: int
    data_2: str


class TestClass:
    def __init__(
        self,
        int_field: int,
        list_field: Optional[List[str]] = None,
        dict_field: Optional[Dict[str, int]] = None,
        obj_field: Optional[SomeData] = None,
    ):
        default_somedata = {"data_1": 1, "data_2": "two"}
        self.int_field = int_field
        self.list_field: List[str] = optional_object(list_field, list, ["a", "b", "c"])
        self.dict_field: Dict[str, int] = optional_object(dict_field, dict)
        self.obj_field: SomeData = optional_object(
            obj_field, SomeData, **default_somedata
        )


def test_default_values():

    test_1 = TestClass(5)
    test_2 = TestClass(5)
    assert isinstance(test_1.list_field, list)
    assert isinstance(test_1.dict_field, dict)
    assert isinstance(test_1.obj_field, SomeData)
    assert test_1.obj_field == SomeData(data_1=1, data_2="two")
    assert test_1.list_field == ["a", "b", "c"]
    assert test_1.dict_field is not test_2.dict_field


def test_passed_in_mutables():
    muta_list = [1, 2, 3]
    muta_dict = {"a": 1, "b": 2}
    muta_obj = SomeData(2, "three")

    test_2 = TestClass(
        2, list_field=muta_list, dict_field=muta_dict, obj_field=muta_obj
    )
    assert isinstance(test_2.list_field, list)
    assert isinstance(test_2.obj_field, SomeData)
    assert test_2.list_field is muta_list
    assert test_2.obj_field is muta_obj
    assert test_2.dict_field is muta_dict
