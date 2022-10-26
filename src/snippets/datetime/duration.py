# ####################################################
# #                                                  #
# # src/snippets/datetime/durations.py
# #                                                  #
# ####################################################
# # Created by: Chad Lowe                            #
# # Created on: 2022-09-28T16:46:27-07:00            #
# # Last Modified: _iso_date_         #
# # Source: https://github.com/DonalChilde/snippets  #
# ####################################################

# """
# Dear god. duration parsing and string output is such a pain in the butt.
# ISO durations are ambiguous, with variable month, year, and even hour lengths.
# https://en.wikipedia.org/wiki/ISO_8601#Durations

# use a subset, re: Java
# https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html#parse-java.lang.CharSequence-
# https://github.com/python/cpython/blob/3.10/Lib/datetime.py


# *************************************
#         STOP THE MADDNESS!!!!!

# Make a simple thing.
# Don't reinvent the wheel.
# Use timedelta for arithmatic, until a clear need for otherwise.

# *************************************


# As weird as timedelta looks, its actually one of the more reasonable ways to store a duration,
# though it dosnt support durations longer than about 2.8 million years.

# so, make a class to hold a duration, and write formatters against it?
# will Decimal format precision in a f string?

# Two strategies for parsing string durations,
# Pyparsing, and regular expressions.
# Maybe make both?

# then can output from timedelta to various formats.

# """

# from dataclasses import dataclass
# from datetime import timedelta
# from decimal import Decimal
# from typing import TypedDict

# from snippets.datetime.duration_dict import DurationDict
# from snippets.datetime.factor_timedelta import factor_timedelta

# # class Duration:
# #     def __init__(
# #         self, days: int = 0, seconds: int = 0, fractional_seconds: Decimal = Decimal(0)
# #     ) -> None:
# #         self.days = days
# #         self.seconds = seconds
# #         self.fractional_seconds = fractional_seconds
# #         # check for field overflow
# #         # make immutable
# #         # constructors from common sources, ie nanoseconds, timedelta
# #         # output to string, iso


# @dataclass(frozen=True)
# class Duration:
#     """
#     Hold a length of time.

#     SIMPLE IS BETTER!!!!
#     Ah, crap. Im part way to a timedelta replacement with arbitrary precision.
#     internally, could store as years, days, seconds, fractional seconds.
#     Change to regular class, to make it more clear what I'm doing?
#     Do testing on Deciaml to see actual precision, int and fractional values.

#     TODO immutable, iso format in/out
#     TODO support math
#     TODO interaction of precision, how and when to define.
#     TODO __str__ as iso
#     TODO fields as DurationDict, then can replace durationdict
#     TODO handle fractional leading and trailing zeros. send through Decimal?
#     """

#     years: int = 0
#     days: int = 0
#     hours: int = 0
#     minutes: int = 0
#     seconds: int = 0
#     fractional_seconds: int = 0
#     exponent: int = 0
#     precision: int = 9

#     def __post_init__(self):
#         self._check_overflow()

#     def _check_overflow(self):
#         # TODO check for overflow of fields, eg. days=400
#         # start at the bottom and get bigger.
#         # handle precision
#         pass

#     def to_seconds(self) -> Decimal:
#         day_seconds = ((self.years * 365) + self.days) * 24 * 60 * 60
#         hour_seconds = self.hours * 60 * 60
#         minute_seconds = self.minutes * 60
#         subtotal = Decimal(day_seconds + hour_seconds + minute_seconds)
#         return subtotal + self.seconds

#     def to_timedelta(self) -> timedelta:
#         days = (self.years * 365) + self.days
#         result = timedelta(
#             days=days,
#             hours=self.hours,
#             minutes=self.minutes,
#             seconds=float(self.seconds),
#         )
#         return result

#     def to_iso_format(self) -> str:
#         """
#         Get an iso string of the Duration.
#         https://en.wikipedia.org/wiki/ISO_8601#Durations
#         """
#         iso_string = (
#             f"P{self.years}Y{self.days}DT{self.hours}H{self.minutes}M{self.seconds}S"
#         )
#         return iso_string

#     @classmethod
#     def from_iso(cls, iso_string: str) -> "Duration":
#         """
#         Make a Duration from an iso string.

#         ISO Duration strings are ambiguous. This function assumes 365 days in a year,
#         30 days in a month, 7 days in a week, 24 hours in a day, 60 minutes an hour,
#         and 60 seconds in a minute. To allow greatest precision for fractional values,
#         all fields will be converted to seconds before the fraction is applied.
#         For example, 1 day = 86400 seconds. P.34D would be calulated as
#         86400 * .34 = 29376 seconds. Duration(seconds = 29376)

#         Args:
#             iso_string: _description_

#         Returns:
#             _description_
#         """
#         raise NotImplementedError

#     @classmethod
#     def from_seconds(cls, seconds: float | Decimal | int) -> "Duration":
#         # TODO rework to allow decimal, keep precision
#         raise NotImplementedError
#         # delta = timedelta(seconds=seconds)
#         # return Duration.from_timedelta(delta=delta)

#     @classmethod
#     def from_nanoseconds(cls, nanos: int) -> "Duration":
#         raise NotImplementedError

#     @classmethod
#     def from_timedelta(cls, delta: timedelta) -> "Duration":
#         split = factor_timedelta(delta=delta)
#         return cls(
#             years=split["years"],
#             days=split["days"],
#             hours=split["hours"],
#             minutes=split["minutes"],
#             seconds=split["seconds"],
#         )

#     @classmethod
#     def from_duration_dict(cls, duration_dict: DurationDict) -> "Duration":
#         raise NotImplementedError


# def duration_to_HHMMSS(
#     duration: Duration,
#     hm_separator: str = ":",
#     ms_separator: str = ":",
#     timespec=None,
#     float_precision: int = 6,
# ) -> str:
#     total_hours = (duration.years * 365 * 24) + (duration.days * 24) + duration.hours
#     if timespec == "M":
#         return f"{total_hours}{hm_separator}{duration.minutes:02d}"
#     return (
#         f"{total_hours}{hm_separator}{duration.minutes:02d}{ms_separator}"
#         f"{duration.seconds:02d.{float_precision}f}"
#     )


# # def timedelta_To_isoformat(timeDelta: timedelta, strict=True) -> str:
# #     """
# #     FIXME move this to duration and drop timedelta, as it already uses duration internally
# #     if strict then limit output fields to PddDThhHmmMss.sS # Not implemeted
# #     """
# #     # int_seconds = 0
# #     # if timeDelta.days:
# #     #     int_seconds = int_seconds + (abs(timeDelta.days)*86400)
# #     # if timeDelta.seconds:
# #     #     int_seconds = int_seconds + timeDelta.seconds
# #     # minutes, seconds = divmod(int_seconds, 60)
# #     # hours, minutes = divmod(minutes, 60)
# #     # days, hours = divmod(hours, 24)
# #     # microseconds = timeDelta.microseconds

# #     time_split = Duration.from_timedelta(timeDelta)
# #     daystext = hourstext = minutestext = secondstext = microtext = ""
# #     if time_split.days:
# #         daystext = f"{time_split.days}D"
# #     if time_split.hours:
# #         hourstext = f"{time_split.hours}H"
# #     if time_split.minutes:
# #         minutestext = f"{time_split.minutes}M"
# #     if time_split.microseconds:
# #         if not time_split.seconds:
# #             time_split.seconds = 0
# #         microtext = f".{time_split.microseconds:06d}"
# #     if time_split.seconds or time_split.microseconds:
# #         secondstext = f"{time_split.seconds}{microtext}S"
# #     if not (
# #         time_split.hours
# #         or time_split.minutes
# #         or time_split.seconds
# #         or time_split.microseconds
# #     ):
# #         secondstext = f"{time_split.seconds}S"
# #     isoString = f"P{daystext}T{hourstext}{minutestext}{secondstext}"
# #     return isoString
