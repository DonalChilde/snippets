import logging
from dataclasses import dataclass

from snippets.collection.iterable_to_dict import iterable_to_dict


@dataclass
class SomeData:
    data_1: int
    data_2: str


def test_index_objects(caplog):
    caplog.set_level(logging.DEBUG)
    data_1 = [[1, 2, 3], ["a", "b", "c"], [4, 5, 6]]
    data_2 = [
        {"arg1": 1, "arg2": 2, "arg3": 3},
        {"arg1": "a", "arg2": "b", "arg3": "c"},
        {"arg1": 4, "arg2": 5, "arg3": 6},
    ]
    obj_1 = SomeData(1, "a")
    obj_2 = SomeData(2, "b")
    obj_3 = SomeData(3, "c")
    obj_4 = SomeData(4, "b")
    data_3 = [obj_1, obj_2, obj_3, obj_4]

    result_1 = iterable_to_dict(data_1, 2)
    assert result_1["c"] == ["a", "b", "c"]
    assert result_1["3"] == [1, 2, 3]

    result_2 = iterable_to_dict(data_2, "arg2")
    assert result_2["2"] == {"arg1": 1, "arg2": 2, "arg3": 3}

    result_3 = iterable_to_dict(data_3, "data_2", use_itemgetter=False)
    assert result_3["a"] == SomeData(1, "a")
    assert len(result_3) == 3

    result_4 = iterable_to_dict(
        data_3, "data_2", use_itemgetter=False, preserve_multiple=True
    )
    logging.debug("result_4: %s", result_4)
    assert result_4["a"] == [SomeData(1, "a")]
    assert result_4["b"] == [SomeData(2, "b"), SomeData(4, "b")]
    assert len(result_4) == 3

    result_5 = iterable_to_dict(data_1, 2, cast_index=None)
    assert result_5[3] == [1, 2, 3]
    assert result_5["c"] == ["a", "b", "c"]
