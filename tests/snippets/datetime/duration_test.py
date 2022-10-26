# ####################################################
# #                                                  #
# #  tests/snippets/datetime/duration_test.py
# #                                                  #
# ####################################################
# # Created by: Chad Lowe                            #
# # Created on: 2022-10-01T17:33:32-07:00            #
# # Last Modified: _iso_date_         #
# # Source: https://github.com/DonalChilde/snippets  #
# ####################################################

# from datetime import timedelta
# from decimal import Decimal

# from snippets.datetime.duration import DurationDict, factor_timedelta


# def test_factor_timedelta():
#     factored_delta: DurationDict = {
#         "years": 0,
#         "days": 5,
#         "hours": 12,
#         "minutes": 4,
#         "seconds": 35,
#         "fractional_seconds": 6,
#         "exponent": -6,
#     }
#     delta = timedelta(
#         days=factored_delta["days"],
#         hours=factored_delta["hours"],
#         minutes=factored_delta["minutes"],
#         seconds=factored_delta["seconds"],
#         microseconds=factored_delta["fractional_seconds"],
#     )
#     print(float(6e-6))
#     print(Decimal(6e-6))
#     print(Decimal(0.000006))
#     print(Decimal("0.000006"))
#     refactored_delta = factor_timedelta(delta)
#     assert factored_delta == refactored_delta
#     assert False


# def test_decimals():
#     print(float(6e-6))
#     print(Decimal(6e-6))
#     print(Decimal(0.000006))
#     print(Decimal("0.000006"))
