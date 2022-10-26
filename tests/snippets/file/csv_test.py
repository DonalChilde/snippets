from datetime import timedelta


class SubDelta(timedelta):
    pass


def test_type_output():
    sub = SubDelta(hours=1)
    delta = timedelta(hours=1)
    sub_type = type(sub)
    delta_type = type(delta)
    print("sub", sub_type)
    print("delta", delta_type)
    assert isinstance(sub, timedelta)
    assert sub_type != delta_type
    value = {sub_type: sub, delta_type: delta}
    print(value)
    assert False
