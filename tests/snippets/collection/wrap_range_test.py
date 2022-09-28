# pylint: disable=missing-docstring, empty-docstring
####################################################
#                                                  #
# tests/snippets/collection/wrap_range_test.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T11:06:40-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

"""

"""

import logging

import pytest

from snippets.collection.wrap_range import wrap_range

#### setting up logger ####
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def test_forward():
    range_gen = wrap_range(left_boundry=0, right_boundry=10, start_value=6, direction=1)
    as_list = list(range_gen)
    expected = [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
    assert as_list == expected


def test_backward():
    range_gen = wrap_range(
        left_boundry=0, right_boundry=10, start_value=6, direction=-1
    )
    as_list = list(range_gen)
    expected = [6, 5, 4, 3, 2, 1, 0, 9, 8, 7]
    assert as_list == expected


def test_negative_start_backward():
    wrap_range(left_boundry=-2, right_boundry=10, start_value=6, direction=-1)
    range_gen = wrap_range(-2, 10, 6, -1)
    as_list = list(range_gen)
    expected = [6, 5, 4, 3, 2, 1, 0, -1, -2, 9, 8, 7]
    assert as_list == expected


def test_non_zero_start_backward():
    range_gen = wrap_range(left_boundry=1, right_boundry=8, start_value=4, direction=-1)
    as_list = list(range_gen)
    expected = [4, 3, 2, 1, 7, 6, 5]
    assert as_list == expected


def test_zero_direction():
    # zero in direction
    with pytest.raises(ValueError):
        _ = wrap_range(1, 8, 4, 0)


def test_left_greater_than_right():
    # left bound greater than right bound
    with pytest.raises(ValueError):
        _ = wrap_range(8, 1, 4, 1)
