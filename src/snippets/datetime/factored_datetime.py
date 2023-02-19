import datetime as DT
import logging
import time
from calendar import isleap
from dataclasses import asdict, dataclass
from typing import Any

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

TIME_FORMAT_CODES: list[str] = []
DATE_FORMAT_CODES: list[str] = []

# Incomplete. Was working on this to support logbook and pairing parser,
# But realized that the only reliable way to calculate the forward times
# was by adding durations to a known date, due to cursed DST shifts.


class FactoredDatetimeError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class AmbiguousIntervalError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


@dataclass
class FactoredDatetime:
    # Intent is to be able to tell when data is missing, not just a zero value
    # useful when parsing partial date time information.
    year: int | None = None
    month: int | None = None
    day: int | None = None
    hour: int | None = None
    minute: int | None = None
    second: int | None = None
    microsecond: int | None = None
    tzinfo: DT.tzinfo | None = None
    fold: int | None = None
    tz_name: str | None = None
    utc_offset: str | None = None

    @classmethod
    def strptime(cls, date_string: str, strf: str) -> "FactoredDatetime":
        # https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime
        # try to parse with datetime.strptime to capture microseconds.
        # fallback to time.strptime when parsing partial dates with 02/29, as datetime.strptime will not parse.
        # time.strptime does not parse microseconds
        # https://docs.python.org/3/library/time.html#time.struct_time
        raise NotImplementedError

    def strftime(self, strf: str) -> str:
        temp_datetime = self.datetime()
        return temp_datetime.strftime(strf)

    def as_dict(self) -> dict[str, Any]:
        """Return a dict with the non None values."""
        result = {}
        for key, value in asdict(self).items():
            if value is not None:
                result[key] = value
        return result

    def highest_field(self) -> str:
        for key, value in asdict(self).items():
            # return the first key that has a non None value
            if value is not None:
                return key
        raise ValueError("No values found that were not None.")

    def increment_interval(
        self, reference_date: DT.datetime, highest_field: str
    ) -> DT.timedelta:
        """Returns a duration used to `wrap` the appropriate time field."""
        if highest_field == "year":
            return DT.timedelta()
        if highest_field == "month":
            if isleap(reference_date.year):
                return DT.timedelta(days=366)
            return DT.timedelta(days=365)
        if highest_field == "day":
            raise AmbiguousIntervalError(
                "Unable to guess the length of an arbitrary month."
            )
        if highest_field == "hour":
            return DT.timedelta(hours=24)
        if highest_field == "minute":
            return DT.timedelta(hours=1)
        if highest_field == "second":
            return DT.timedelta(seconds=60)
        if highest_field == "microsecond":
            return DT.timedelta(seconds=1)
        raise ValueError("Not a valid time field.")

    def increment_instant(
        self, instant: DT.datetime, highest_field: str
    ) -> DT.datetime:
        """Increment an instant based on the largest time field used to make it."""
        if highest_field == "year":
            # TODO handle leap years and feb 29th
            return instant
        if highest_field == "month":
            return instant.replace(year=instant.year + 1)
        if highest_field == "day":
            if instant.month == 12:
                return instant.replace(month=1, year=instant.year + 1)
        if highest_field == "hour":
            return instant + DT.timedelta(hours=24)
        if highest_field == "minute":
            return instant + DT.timedelta(hours=1)
        if highest_field == "second":
            return instant + DT.timedelta(seconds=60)
        if highest_field == "microsecond":
            return instant + DT.timedelta(seconds=1)
        raise ValueError(f"{highest_field} is not a valid time field.")

    @classmethod
    def from_datetime(
        cls, from_datetime: DT.datetime, strf: str = ""
    ) -> "FactoredDatetime":
        raise NotImplementedError

    @classmethod
    def from_time(cls, from_time: DT.time, strf: str = "") -> "FactoredDatetime":

        valid_fields: list[str] = []
        if [i for i in ["H", "I", "X"] if i in strf]:
            valid_fields.append("hour")

        raise NotImplementedError

    @classmethod
    def from_date(cls, from_date: DT.date, strf: str = "") -> "FactoredDatetime":
        raise NotImplementedError

    @classmethod
    def from_struct_time(cls, struct, strf: str = "") -> "FactoredDatetime":
        raise NotImplementedError

    def next_instant(self, reference_date: DT.datetime) -> DT.datetime:
        """find the next occurance of a datetime.

        Working forwards from a reference datetime, find the next occurance of a datetime
        using possibly partial data.

        Example:
            reference_date = datetime(year=2020,month=3,day=5)
            partial_data = FactoredDateTime(month=2,day=1)
            next_instant = partial_data.next_instant(reference_date)
            next_instant == datetime(year=2021,month=2,day=1)
        """

        highest_field = self.highest_field()
        time_fields = self.as_dict()
        # TODO handle leap years and feb 29th
        # special handling for month increment, as length varies.
        if highest_field == "day":
            if reference_date.month == 12:
                time_fields["month"] = 1
                time_fields["year"] = reference_date.year + 1
            else:
                time_fields["month"] = reference_date.month + 1
        try:
            next_instant = reference_date.replace(**time_fields)
        except ValueError as error:
            logger.warning(
                "Tried to make a datetime with invalid data. "
                "reference_date=%r, time_fields=%r",
                reference_date,
                time_fields,
                exc_info=error,
            )
            raise error
        if next_instant < reference_date:
            if highest_field == "day":
                raise ValueError(
                    f"next_instant was less than reference date, even after correction."
                    f"reference_date={reference_date!r}, next_instant={next_instant!r}, "
                    f"time_fields={time_fields!r}",
                )
            # next_instant = next_instant + self.increment_interval(
            #     reference_date=reference_date, highest_field=highest_field
            # )
            next_instant = self.increment_instant(next_instant, highest_field)
            if next_instant < reference_date:
                raise ValueError(
                    f"next_instant was less than reference date, even after correction."
                    f"reference_date={reference_date!r}, next_instant={next_instant!r}, "
                    f"time_fields={time_fields!r}",
                )
        return next_instant

    def is_date(self) -> bool:
        raise NotImplementedError

    def is_time(self) -> bool:
        raise NotImplementedError

    def is_datetime(self) -> bool:
        raise NotImplementedError

    def date(self) -> DT.date:
        raise NotImplementedError

    def time(self) -> DT.time:
        raise NotImplementedError

    def datetime(self) -> DT.datetime:
        raise NotImplementedError

    # def struct_time(self) -> time.struct_time:
    #     raise NotImplementedError


HOUR = ("H", "I", "c", "X")
MINUTE = ("M", "c", "X")
SECOND = ("S", "c", "X")
MICROSECOND = ("f",)
UTC_OFFSET = ("z",)
TZ_NAME = ("Z",)
YEAR = ("y", "Y", "c", "x")
MONTH = ("b", "B", "m", "c", "x", "j", "U")
DAY = ("d", "c", "x", "j", "W")


def parses_hour(strf: str) -> bool:
    if [i for i in HOUR if i in strf]:
        return True
    return False


def parses_minute(strf: str) -> bool:
    if [i for i in MINUTE if i in strf]:
        return True
    return False


def parses_second(strf: str) -> bool:
    if [i for i in SECOND if i in strf]:
        return True
    return False


def parses_microsecond(strf: str) -> bool:
    if [i for i in MICROSECOND if i in strf]:
        return True
    return False


def parses_utc_offset(strf: str) -> bool:
    if [i for i in UTC_OFFSET if i in strf]:
        return True
    return False


def parses_tz_name(strf: str) -> bool:
    if [i for i in TZ_NAME if i in strf]:
        return True
    return False


def parses_year(strf: str) -> bool:
    if [i for i in YEAR if i in strf]:
        return True
    return False


def parses_month(strf: str) -> bool:
    if [i for i in MONTH if i in strf]:
        return True
    return False


def parses_day(strf: str) -> bool:
    if [i for i in DAY if i in strf]:
        return True
    return False


def parses_fields(strf: str) -> list[str]:
    parsed_fields = []
    if parses_year(strf):
        parsed_fields.append("year")
    if parses_month(strf):
        parsed_fields.append("month")
    if parses_day(strf):
        parsed_fields.append("day")
    if parses_hour(strf):
        parsed_fields.append("hour")
    if parses_minute(strf):
        parsed_fields.append("minute")
    if parses_second(strf):
        parsed_fields.append("second")
    if parses_microsecond(strf):
        parsed_fields.append("microsecond")
    if parses_utc_offset(strf):
        parsed_fields.append("utc_offset")
    if parses_tz_name(strf):
        parsed_fields.append("tz_name")
    return parsed_fields
