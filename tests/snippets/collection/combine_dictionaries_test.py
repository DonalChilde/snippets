# pylint: disable=missing-docstring, empty-docstring
####################################################
#                                                  #
# tests/snippets/collection/combine_dictionaries_test.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T15:39:43-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

from snippets.collection.combine_dictionaries import combine_dictionaries

dict_1 = {"a": 1, "b": 2}
dict_2 = {"c": 3, "d": 4}
dict_3 = {"a": 5, "d": 6}
dict_list = [dict_1, dict_2, dict_3]
expected_result = {"a": 5, "b": 2, "c": 3, "d": 6}


def test_combine_dictionaries_use_first():
    result = combine_dictionaries(dicts=dict_list, use_first_dict=True)
    assert dict_1 is result
    assert dict_1 == expected_result


def test_combine_dictionaries_new_dict():
    result = combine_dictionaries(dicts=dict_list)
    assert result == expected_result
    assert result is not dict_1
