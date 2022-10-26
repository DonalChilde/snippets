from dataclasses import dataclass

from snippets.collection.dataclasses_to_dicts import DataclassesToDicts


@dataclass
class TestValue:
    field_1: str
    field_2: str


def test_to_dicts():
    values = [TestValue(field_1="1", field_2="2"), TestValue(field_1="3", field_2="4")]
    gen = DataclassesToDicts(values)
    first = next(gen)
    second = next(gen)
    assert first == {"field_1": "1", "field_2": "2"}
    assert second == {"field_1": "3", "field_2": "4"}
    assert len(gen.failed) == 0
    assert gen.fail_count == 0

    values = [TestValue(field_1="1", field_2="2"), TestValue(field_1="3", field_2="4")]
    gen = DataclassesToDicts(values, stop_on_error=True, save_failed=True)
    values = list(gen)
    assert values == [
        {"field_1": "1", "field_2": "2"},
        {"field_1": "3", "field_2": "4"},
    ]
    assert len(gen.failed) == 0
    assert gen.fail_count == 0


def test_fail_stop_on_error_true_save_failed_true():
    values = [
        TestValue(field_1="1", field_2="2"),
        "foo",
        TestValue(field_1="3", field_2="4"),
    ]
    gen = DataclassesToDicts(values, stop_on_error=True, save_failed=True)
    values = list(gen)
    assert gen.failed[0] == "foo"
    assert gen.fail_count == 1
    assert values == [
        {"field_1": "1", "field_2": "2"},
    ]


def test_fail_stop_on_error_false_save_failed_true():
    values = [
        TestValue(field_1="1", field_2="2"),
        "foo",
        TestValue(field_1="3", field_2="4"),
    ]
    gen = DataclassesToDicts(values, stop_on_error=False, save_failed=True)
    values = list(gen)
    assert gen.failed[0] == "foo"
    assert gen.fail_count == 1
    assert len(values) == 2
    assert values == [
        {"field_1": "1", "field_2": "2"},
        {"field_1": "3", "field_2": "4"},
    ]


def test_fail_stop_on_error_false_save_failed_false():
    values = [
        TestValue(field_1="1", field_2="2"),
        "foo",
        TestValue(field_1="3", field_2="4"),
    ]
    gen = DataclassesToDicts(values, stop_on_error=False, save_failed=False)
    values = list(gen)
    assert not gen.failed
    assert gen.fail_count == 1
    assert len(values) == 2
    assert values == [
        {"field_1": "1", "field_2": "2"},
        {"field_1": "3", "field_2": "4"},
    ]
