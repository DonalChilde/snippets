from copy import copy
from datetime import datetime, timedelta

from snippets.collection.mutable_collection_caster import MutableCollectionCaster

TEST_LIST = ["value_1", datetime.now(), timedelta(hours=1), 3]
TEST_DICT = {
    "field_1": "value_1",
    "datetime_field": datetime.now(),
    "timedelta_field": timedelta(hours=1),
    "int_field": 3,
}


def cast_datetime(value: datetime) -> str:
    return "Formatted_datetime"


def cast_timedelta(value: timedelta) -> str:
    return "Formatted_timedelta"


def fullname(obj: object) -> str:
    """Return the full name of the given object using its module and qualified class names."""
    # Ref: https://stackoverflow.com/a/66508248/
    module_name, class_name = obj.__class__.__module__, obj.__class__.__qualname__
    if module_name in (None, str.__class__.__module__):
        return class_name
    return module_name + "." + class_name


CAST_MAP = {
    MutableCollectionCaster.type_signature(datetime): cast_datetime,
    MutableCollectionCaster.type_signature(timedelta()): cast_timedelta,
    MutableCollectionCaster.type_signature(3): float,
}


def test_list():
    collection = [copy(TEST_LIST), copy(TEST_LIST), copy(TEST_LIST)]
    for index, result in enumerate(MutableCollectionCaster(CAST_MAP, collection)):
        assert result[0] == "value_1"
        assert result[1] == "Formatted_datetime"
        assert result[2] == "Formatted_timedelta"
        assert result[3] == 3.0
        assert result is collection[index]


def test_dict():
    collection = [copy(TEST_DICT), copy(TEST_DICT), copy(TEST_DICT)]
    for index, result in enumerate(MutableCollectionCaster(CAST_MAP, collection)):
        assert result["field_1"] == "value_1"
        assert result["datetime_field"] == "Formatted_datetime"
        assert result["timedelta_field"] == "Formatted_timedelta"
        assert result["int_field"] == 3.0
        assert result is collection[index]
