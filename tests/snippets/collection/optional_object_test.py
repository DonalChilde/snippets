from dataclasses import dataclass
from typing import Dict, List, Optional

from snippets.collection.optional_object import optional_object


@dataclass
class SomeData:
    data_1: int
    data_2: str


def test_optional_object():
    class MyClass:
        def __init__(
            self,
            arg1: int,
            arg2: Optional[List[str]] = None,
            arg3: Optional[Dict[str, int]] = None,
            arg4: Optional[SomeData] = None,
        ):
            default_somedata = {"data_1": 1, "data_2": "two"}
            self.arg1 = arg1
            self.arg2: List[str] = optional_object(arg2, list, ["a", "b", "c"])
            self.arg3: Dict[str, int] = optional_object(arg3, dict)
            self.arg4: SomeData = optional_object(arg4, SomeData, **default_somedata)

    test_1 = MyClass(5)
    assert isinstance(test_1.arg2, list)
    assert isinstance(test_1.arg3, dict)
    assert isinstance(test_1.arg4, SomeData)
    assert test_1.arg4.data_1 == 1
    assert test_1.arg2[0] == "a"

    test_2 = MyClass(2, [1, 2, 3], arg4=SomeData(2, "three"))
    assert isinstance(test_2.arg2, list)
    assert isinstance(test_2.arg4, SomeData)
    assert test_2.arg2[0] == 1
    assert test_2.arg4.data_1 == 2
