import inspect
from datetime import datetime, timedelta

from snippets.inspection.full_name import fullname


class Foo:
    class Bar:
        pass


def test_fullname_instance():
    instance = timedelta(hours=1)
    expected = "datetime.timedelta"
    result = fullname(instance)
    assert expected == result

    instance = 3
    expected = "builtins.int"
    result = fullname(instance)
    assert expected == result


def test_fullname_not_instance():
    not_instance = datetime
    expected = "datetime.datetime"
    result = fullname(not_instance)
    assert expected == result

    not_instance = timedelta
    expected = "datetime.timedelta"
    result = fullname(not_instance)
    assert expected == result

    not_instance = Foo.Bar
    expected = "tests.snippets.inspection.fullname_test.Foo.Bar"
    result = fullname(not_instance)
    assert expected == result

    not_instance = int
    expected = "builtins.int"
    result = fullname(not_instance)
    assert expected == result


def print_module(obj):
    print("with join:", ".".join([obj.__module__, obj.__qualname__]))
    print("direct access", obj.__module__)


# def test_type_sig():
#     print("not instance type to str", type(datetime))
#     print("not instance type module", type(datetime).__module__)
#     print("not instance class name", type(datetime).__qualname__)
#     print("instance type to str", type(datetime.now()))
#     print("instance type module", type(datetime.now()).__module__)
#     print("instance class name", type(datetime.now()).__qualname__)
#     print("not instance type to str", type(timedelta))
#     print("not instance type module", type(timedelta).__module__)
#     print("not instance class name", type(timedelta).__qualname__)
#     print("instance type to str", type(timedelta(hours=1)))
#     print("instance type module", type(timedelta(hours=1)).__module__)
#     print("instance class name", type(timedelta(hours=1)).__qualname__)

#     assert False
