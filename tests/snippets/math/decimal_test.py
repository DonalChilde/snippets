from snippets.math.decimal import make_decimal_string


def test_make_decimal_string():
    expected = "0.003"
    result = make_decimal_string(fractional=3, exponent=3)
    assert expected == result

    expected = "56.003"
    result = make_decimal_string(whole=56, fractional=3, exponent=3)
    assert expected == result

    expected = "56.003"
    result = make_decimal_string(whole=56, fractional=3, exponent=-3)
    assert expected == result

    expected = "56.0"
    result = make_decimal_string(whole=56, fractional=0, exponent=1)
    assert expected == result

    expected = "56.0"
    result = make_decimal_string(whole=56, fractional=0)
    assert expected == result
