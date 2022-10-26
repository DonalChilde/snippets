####################################################
#                                                  #
# tests/snippets/datetime/parse_duration_regex_test.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-01T18:49:56-07:00            #
# Last Modified: _iso_date_       #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
import pytest

from snippets.datetime.factored_duration import FactoredDuration
from snippets.datetime.parse_duration_regex import parse_duration, pattern_HHHMMSSFS

HHHMMSSFS_BASE_TESTS = [
    ("23:14:30", FactoredDuration(hours=23, minutes=14, seconds=30)),
    ("123:25:15", FactoredDuration(hours=123, minutes=25, seconds=15)),
    ("0:25:15", FactoredDuration(minutes=25, seconds=15)),
    ("0:05:05", FactoredDuration(minutes=5, seconds=5)),
    (
        "123:15:34.456",
        FactoredDuration(
            hours=123,
            minutes=15,
            seconds=34,
            fractional_seconds=456,
            fractional_exponent=3,
        ),
    ),
    # this one needs some pattern refinement, does not match
    # ("1,234,567:15:34.456", timedelta(hours=1234567, minutes=15, seconds=34.456)),
]


def test_parse():
    duration_string = "23:14:30"
    expected = FactoredDuration(hours=23, minutes=14, seconds=30)
    pattern = pattern_HHHMMSSFS()
    result = parse_duration(pattern=pattern, duration_string=duration_string)
    assert expected == result


@pytest.mark.parametrize("duration_string, expected", HHHMMSSFS_BASE_TESTS)
def test_HHHMMSSFS(duration_string: str, expected: FactoredDuration):
    pattern = pattern_HHHMMSSFS()
    result = parse_duration(pattern=pattern, duration_string=duration_string)
    assert expected == result


def test_none():
    pattern = pattern_HHHMMSSFS()
    try:
        result = parse_duration(pattern=pattern, duration_string=None)
    except Exception as error:
        print(error)
    assert False


# TODO parameterize tests, different separators etc.
# TODO check to see if separators that would normally be escaped can be sent as raw strings.


def test_different_separators():
    pass
