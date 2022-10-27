import calendar
from datetime import datetime, timedelta


def increment_year(value: datetime) -> timedelta:
    # https://stackoverflow.com/questions/15741618/add-one-year-in-current-date-python
    # https://stackoverflow.com/a/63927498/105844
    one_year_delta = timedelta(
        days=366
        if (
            (value.month >= 3 and calendar.isleap(value.year + 1))
            or (value.month < 3 and calendar.isleap(value.year))
        )
        else 365
    )
    return one_year_delta
