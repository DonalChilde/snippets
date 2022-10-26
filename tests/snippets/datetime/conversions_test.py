####################################################
#                                                  #
#  tests/snippets/datetime/conversions_test.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-01T17:28:57-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

from datetime import timedelta

from snippets.datetime.conversions import (
    build_iso_duration,
    duration_to_seconds_int,
    nanoseconds_to_seconds,
    seconds_to_nanoseconds,
    timedelta_to_HHHMMSS,
    timedelta_to_iso,
)


def test_write_the_tests():
    assert False, "Write The Tests!"


def test_timedelta_to_HHHMMSS():
    delta = timedelta(days=-1, seconds=68400)
    expected = "-5:00:00"
    assert expected == timedelta_to_HHHMMSS(delta)

    delta = timedelta(days=-1, seconds=68400) * -1
    expected = "5:00:00"
    assert expected == timedelta_to_HHHMMSS(delta)

    delta = timedelta(hours=5, microseconds=6)
    expected = "5:00:00.000006"
    assert expected == timedelta_to_HHHMMSS(delta)

    delta = timedelta(hours=5, microseconds=6) * -1
    expected = "-5:00:00.000006"
    assert expected == timedelta_to_HHHMMSS(delta)

    delta = timedelta(minutes=5)
    expected = "0:05:00"
    assert expected == timedelta_to_HHHMMSS(delta)

    delta = timedelta(seconds=5)
    expected = "0:00:05"
    assert expected == timedelta_to_HHHMMSS(delta)


def test_timedelta_to_iso():
    delta = timedelta(days=-1, seconds=68400)
    expected = "-PT5H"
    assert expected == timedelta_to_iso(delta)

    delta = timedelta(days=-1, seconds=68400) * -1
    expected = "PT5H"
    assert expected == timedelta_to_iso(delta)

    delta = timedelta(hours=5, microseconds=6)
    expected = "PT5H0.000006S"
    assert expected == timedelta_to_iso(delta)

    delta = timedelta(hours=5, microseconds=6) * -1
    expected = "-PT5H0.000006S"
    assert expected == timedelta_to_iso(delta)

    delta = timedelta(minutes=5)
    expected = "PT5M"
    assert expected == timedelta_to_iso(delta)

    delta = timedelta(seconds=5)
    expected = "PT5S"
    assert expected == timedelta_to_iso(delta)


def test_build_iso_duration():
    expected = "PT5S"
    assert expected == build_iso_duration(seconds=5)

    expected = "-PT5H0.000006S"
    assert expected == build_iso_duration(
        sign="-", hours=5, fractional_seconds=6, exponent=6
    )
