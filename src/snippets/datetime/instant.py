####################################################
#                                                  #
#       src/snippets/datetime/instant.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-04-30T10:41:37-07:00            #
# Last Modified: 2023-04-30T18:49:04.951161+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import UUID, uuid5
from zoneinfo import ZoneInfo


@dataclass(frozen=True)
class Instant:
    """Represents an instant in time.

    The datetime should be an aware datetime with a timezone of timezone.utc
    The tz_name field can store the local time zone name for conversions.
    Addition and subtraction of timedeltas is supported.
    Enforced use of utc time should prevent ambiguous math.
    """

    utc_date: datetime
    tz_name: str

    def local(self, tz_name: str | None = None) -> datetime:
        """Get the local datetime, or the local datetime in a new tz."""
        if tz_name is None:
            return self.utc_date.astimezone(tz=ZoneInfo(self.tz_name))
        return self.utc_date.astimezone(tz=ZoneInfo(tz_name))

    def new_tz(self, tz_name: str) -> "Instant":
        return Instant(utc_date=self.utc_date, tz_name=tz_name)

    def __copy__(self) -> "Instant":
        return Instant(utc_date=self.utc_date, tz_name=self.tz_name)

    def __add__(self, other: timedelta) -> "Instant":
        if not isinstance(other, timedelta):
            return NotImplemented
        new_instant = Instant(utc_date=self.utc_date + other, tz_name=self.tz_name)
        return new_instant

    def __sub__(self, other: timedelta) -> "Instant":
        if not isinstance(other, timedelta):
            return NotImplemented
        new_instant = Instant(utc_date=self.utc_date - other, tz_name=self.tz_name)
        return new_instant

    def uuid5(self, uuid: UUID) -> UUID:
        return uuid5(uuid, f"{self}")

    def __str__(self) -> str:
        return f"utc_date={self.utc_date.isoformat()}, tz_name={self.tz_name}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__qualname__}("
            f"utc_date={self.utc_date!r}, tz_name={self.tz_name!r}"
            ")"
        )
