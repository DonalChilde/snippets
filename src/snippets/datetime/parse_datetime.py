# parse a string containing datetime information.
# use time.strptime to get struct_time
# fields not parsed get a None in returned value
import time
from dataclasses import dataclass
from typing import TypedDict


class AwareStructTimeDict(TypedDict):
    tm_year: int | None
    tm_mon: int | None
    tm_mday: int | None
    tm_hour: int | None
    tm_min: int | None
    tm_sec: int | None
    tm_wday: int | None
    tm_yday: int | None
    tm_isdst: int | None
    tm_zone: str | None
    tm_gmtoff: int | None


@dataclass
class AwareStructTime:
    struct: time.struct_time
    fmt_str: str

    def to_dict(self) -> AwareStructTimeDict:
        return {
            "tm_year": self.tm_year(),
            "tm_mon": self.tm_mon(),
            "tm_mday": self.tm_mday(),
            "tm_hour": self.tm_hour(),
            "tm_min": self.tm_min(),
            "tm_sec": self.tm_sec(),
            "tm_wday": self.tm_wday(),
            "tm_yday": self.tm_yday(),
            "tm_isdst": self.tm_isdst(),
            "tm_zone": self.tm_zone(),
            "tm_gmtoff": self.tm_gmtoff(),
        }

    def tm_year(self) -> int | None:
        if any((x in self.fmt_str for x in ["%y", "%Y", "%c", "%x"])):
            return self.struct.tm_year
        return None

    def tm_mon(self) -> int | None:
        pass

    def tm_mday(self) -> int | None:
        pass

    def tm_hour(self) -> int | None:
        pass

    def tm_min(self) -> int | None:
        pass

    def tm_sec(self) -> int | None:
        pass

    def tm_wday(self) -> int | None:
        pass

    def tm_yday(self) -> int | None:
        pass

    def tm_isdst(self) -> int | None:
        pass

    def tm_zone(self) -> str | None:
        pass

    def tm_gmtoff(self) -> int | None:
        pass


def parse_time(value: str, fmt_str: str) -> AwareStructTime:
    """Parse a string to AwareStructTime using time.strptime."""
    struct = time.strptime(string=value, format=fmt_str)
    return AwareStructTime(struct=struct, fmt_str=fmt_str)
