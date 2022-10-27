import logging
from dataclasses import dataclass, fields
from datetime import datetime
from typing import List
from zoneinfo import ZoneInfo

from snippets.datetime.complete_partial_datetime import (
    complete_fwd_mdt,
    complete_fwd_time,
)

target_logger = logging.getLogger(complete_fwd_time.__module__)


@dataclass
class TestData:
    ref_datetime: datetime
    strf: str
    expected: datetime
    partial_string: str

    def __repr__(self):
        # enhanced from Fluent Python 2ed. p189
        cls = self.__class__
        cls_name = cls.__name__
        field_names = (field.name for field in fields(cls))
        indent = " " * 4
        rep = [f"{cls_name}("]
        for field in field_names:
            value = getattr(self, field)
            rep.append(f"{indent}{field} = {value!r}")
        rep.append(")")
        return "\n".join(rep)


def test_fwd_time_no_tz(logger: logging.Logger):
    for handler in logger.handlers:
        target_logger.addHandler(handler)
    ref_datetime = datetime(year=2022, month=12, day=31, hour=13, minute=00)
    expected = datetime(year=2023, month=1, day=1, hour=2, minute=30)
    test_data = TestData(
        ref_datetime=ref_datetime,
        strf="%H:%M",
        expected=expected,
        partial_string="02:30",
    )
    do_fwd_time_tests([test_data])


def test_fwd_time_with_tz():
    ref_tz = ZoneInfo("America/Phoenix")
    expected_tz = ZoneInfo("America/New_York")

    ref_datetime = datetime(
        year=2022, month=12, day=31, hour=13, minute=00, tzinfo=ref_tz
    )
    expected = datetime(
        year=2023, month=1, day=1, hour=2, minute=30, tzinfo=expected_tz
    )
    test_data = TestData(
        ref_datetime=ref_datetime,
        strf="%H:%M",
        expected=expected,
        partial_string="02:30",
    )
    do_fwd_time_tests([test_data])


def do_fwd_time_tests(test_values: List[TestData]):
    for item in test_values:
        result = complete_fwd_time(
            ref_datetime=item.ref_datetime,
            partial_string=item.partial_string,
            tz_info=item.expected.tzinfo,
            strf=item.strf,
        )
        print("ref", item.ref_datetime.isoformat())
        print("expected", item.expected.isoformat())
        print("result", result.isoformat())
        assert result == item.expected, f"\n{item!r}"
        # assert False


def do_fwd_mdt_tests(test_values: List[TestData]):
    for item in test_values:
        result = complete_fwd_mdt(
            ref_datetime=item.ref_datetime,
            partial_string=item.partial_string,
            tz_info=item.expected.tzinfo,
        )
        print("ref", item.ref_datetime.isoformat())
        print("expected", item.expected.isoformat())
        print("result", result.isoformat())
        assert result == item.expected, f"\n{item!r}"
        # assert False


def test_fwd_mdt_no_tz(logger: logging.Logger):
    for handler in logger.handlers:
        target_logger.addHandler(handler)
    ref_datetime = datetime(year=2022, month=12, day=31, hour=13, minute=00)
    expected = datetime(year=2023, month=1, day=1, hour=2, minute=30)
    test_data = TestData(
        ref_datetime=ref_datetime,
        strf="%m/%d %H:%M",
        expected=expected,
        partial_string="01/01 02:30",
    )
    do_fwd_mdt_tests([test_data])


def test_fwd_mdt_with_tz(logger: logging.Logger):
    for handler in logger.handlers:
        target_logger.addHandler(handler)
    ref_tz = ZoneInfo("America/Phoenix")
    expected_tz = ZoneInfo("America/New_York")
    ref_datetime = datetime(
        year=2022, month=12, day=31, hour=13, minute=00, tzinfo=ref_tz
    )
    expected = datetime(
        year=2023, month=1, day=1, hour=2, minute=30, tzinfo=expected_tz
    )
    test_data = TestData(
        ref_datetime=ref_datetime,
        strf="%m/%d %H:%M",
        expected=expected,
        partial_string="01/01 02:30",
    )
    do_fwd_mdt_tests([test_data])
