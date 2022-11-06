import logging
from dataclasses import dataclass, fields
from datetime import datetime
from typing import List
from zoneinfo import ZoneInfo

from snippets.datetime.complete_partial_datetime import (
    complete_future_mdt,
    complete_future_time,
)

target_logger = logging.getLogger(complete_future_time.__module__)


@dataclass
class TestingData:
    start: datetime
    strf: str
    expected: datetime
    future: str

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
    test_data: List[TestingData] = []
    start = datetime(year=2022, month=12, day=31, hour=13, minute=00)
    strf = "%H:%M"
    future = "02:30"
    expected = datetime(year=2023, month=1, day=1, hour=2, minute=30)
    test_data.append(
        TestingData(
            start=start,
            strf=strf,
            expected=expected,
            future=future,
        )
    )
    do_fwd_time_tests(test_data)


def test_fwd_time_with_tz():
    test_data: List[TestingData] = []
    start_tz = ZoneInfo("America/Phoenix")
    expected_tz = ZoneInfo("America/New_York")
    start = datetime(year=2022, month=12, day=31, hour=13, minute=00, tzinfo=start_tz)
    strf = "%H:%M"
    future = "02:30"
    expected = datetime(
        year=2023, month=1, day=1, hour=2, minute=30, tzinfo=expected_tz
    )
    test_data.append(
        TestingData(
            start=start,
            strf=strf,
            expected=expected,
            future=future,
        )
    )
    do_fwd_time_tests(test_data)


def do_fwd_time_tests(test_values: List[TestingData]):
    for item in test_values:
        result = complete_future_time(
            start=item.start,
            future=item.future,
            tz_info=item.expected.tzinfo,
            strf=item.strf,
        )
        print("ref", item.start.isoformat())
        print("expected", item.expected.isoformat())
        print("result", result.isoformat())
        assert result == item.expected, f"\n{item!r}"
        # assert False


def do_fwd_mdt_tests(test_values: List[TestingData]):
    for item in test_values:
        result = complete_future_mdt(
            start=item.start,
            future=item.future,
            strf=item.strf,
            tz_info=item.expected.tzinfo,
        )
        print("ref", item.start.isoformat())
        print("expected", item.expected.isoformat())
        print("result", result.isoformat())
        assert result == item.expected, f"\n{item!r}"
        # assert False


def test_fwd_mdt_no_tz(logger: logging.Logger):
    for handler in logger.handlers:
        target_logger.addHandler(handler)
    test_data: List[TestingData] = []
    start = datetime(year=2022, month=12, day=31, hour=13, minute=00)
    strf = "%m/%d %H:%M"
    future = "01/01 02:30"
    expected = datetime(year=2023, month=1, day=1, hour=2, minute=30)
    test_data.append(
        TestingData(
            start=start,
            strf=strf,
            expected=expected,
            future=future,
        )
    )
    future = "02/29 02:30"
    expected = datetime(year=2024, month=2, day=29, hour=2, minute=30)
    test_data.append(
        TestingData(
            start=start,
            strf=strf,
            expected=expected,
            future=future,
        )
    )
    # Just short date no time
    strf = "%m/%d"
    future = "02/29"
    expected = datetime(year=2024, month=2, day=29)
    test_data.append(
        TestingData(
            start=start,
            strf=strf,
            expected=expected,
            future=future,
        )
    )
    do_fwd_mdt_tests(test_data)
    # assert False


def test_fwd_mdt_with_tz(logger: logging.Logger):
    for handler in logger.handlers:
        target_logger.addHandler(handler)
    test_data: List[TestingData] = []
    start_tz = ZoneInfo("America/Phoenix")
    expected_tz = ZoneInfo("America/New_York")
    start = datetime(year=2022, month=12, day=31, hour=13, minute=00, tzinfo=start_tz)
    strf = "%m/%d %H:%M"
    future = "01/01 02:30"
    expected = datetime(
        year=2023, month=1, day=1, hour=2, minute=30, tzinfo=expected_tz
    )
    test_data.append(
        TestingData(
            start=start,
            strf=strf,
            expected=expected,
            future=future,
        )
    )
    future = "02/29 02:30"
    expected = datetime(
        year=2024, month=2, day=29, hour=2, minute=30, tzinfo=expected_tz
    )
    test_data.append(
        TestingData(
            start=start,
            strf=strf,
            expected=expected,
            future=future,
        )
    )
    # Just short date no time
    strf = "%m/%d"
    future = "02/29"
    expected = datetime(year=2024, month=2, day=29, tzinfo=expected_tz)
    test_data.append(
        TestingData(
            start=start,
            strf=strf,
            expected=expected,
            future=future,
        )
    )
    do_fwd_mdt_tests(test_data)
