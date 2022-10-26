# from dataclasses import dataclass
# from datetime import timedelta

# from snippets.datetime.duration_dict import DurationDict


# # @dataclass
# # class FactoredDuration:
# #     is_negative: bool = False
# #     years: int = 0
# #     days: int = 0
# #     hours: int = 0
# #     minutes: int = 0
# #     seconds: int = 0
# #     fractional_seconds: int = 0
# #     exponent: int = 0

# #     @classmethod
# #     def from_timedelta(cls, delta) -> "FactoredDuration":
# #         if delta.days < 0:
# #             is_negative = True
# #         else:
# #             is_negative = False
# #         abs_delta = abs(delta)
# #         years, rem = divmod(abs_delta, timedelta(days=365))
# #         days, rem = divmod(rem, timedelta(days=1))
# #         hours, rem = divmod(rem, timedelta(hours=1))
# #         minutes, rem = divmod(rem, timedelta(minutes=1))
# #         seconds = int(rem.total_seconds())
# #         return FactoredDuration(
# #             is_negative=is_negative,
# #             years=years,
# #             days=days,
# #             hours=hours,
# #             minutes=minutes,
# #             seconds=seconds,
# #             fractional_seconds=rem.microseconds,
# #             exponent=6,
# #         )

# # FIXME superseeded by FactoredDuration
# def factor_timedelta(delta: timedelta) -> DurationDict:
#     """
#     Split a time delta to a dict of years, days, hours, minutes, seconds, microseconds.

#     https://stackoverflow.com/a/17847006/105844

#     Args:
#         delta: The timedelta to split
#     Returns:
#         A dict of the times in the timedelta
#     """
#     if delta.days < 0:
#         is_negative = True
#     else:
#         is_negative = False
#     abs_delta = abs(delta)
#     years, rem = divmod(abs_delta, timedelta(days=365))
#     days, rem = divmod(rem, timedelta(days=1))
#     hours, rem = divmod(rem, timedelta(hours=1))
#     minutes, rem = divmod(rem, timedelta(minutes=1))
#     seconds = int(rem.total_seconds())
#     fractional_seconds = rem.microseconds
#     exponent = 6
#     return DurationDict(
#         is_negative=is_negative,
#         years=years,
#         days=days,
#         hours=hours,
#         minutes=minutes,
#         seconds=seconds,
#         fractional_seconds=fractional_seconds,
#         fractional_exponent=exponent,
#     )
