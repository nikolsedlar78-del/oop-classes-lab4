import pytest

from oop_tasks import Money


def test_defaults_and_currency_normalization():
    m = Money(100)
    assert (m.kopecks, m.currency) == (100, "UAH")
    assert Money(100, "usd").currency == "USD"


def test_add_and_sub():
    assert Money(500) + Money(250) == Money(750)
    assert Money(500) - Money(200) == Money(300)
    assert Money(100) - Money(300) == Money(-200)


def test_different_currencies_rejected():
    with pytest.raises(ValueError):
        Money(100, "UAH") + Money(100, "USD")
    with pytest.raises(ValueError):
        Money(100, "UAH") - Money(100, "USD")


def test_multiply_by_number():
    assert Money(1000) * 2 == Money(2000)
    assert 2 * Money(1000) == Money(2000)
    assert Money(1000) * 0.5 == Money(500)
    assert Money(1000) * 0 == Money(0)


def test_multiply_rounds_half_up():
    assert Money(100) * 1.005 == Money(101)
    assert Money(1) * 0.5 == Money(1)
    assert Money(3) * 0.5 == Money(2)


def test_comparisons():
    assert Money(100) < Money(200)
    assert Money(200) >= Money(200)
    assert Money(200) > Money(100)
    assert sorted([Money(300), Money(100), Money(200)]) == [Money(100), Money(200), Money(300)]


def test_comparing_different_currencies():
    assert (Money(100, "UAH") == Money(100, "USD")) is False
    with pytest.raises(ValueError):
        Money(100, "UAH") < Money(100, "USD")


def test_bool():
    assert bool(Money(0)) is False
    assert bool(Money(1)) is True
    assert bool(Money(-1)) is True


def test_sum_of_list():
    assert sum([Money(100), Money(200), Money(300)]) == Money(600)
    assert sum([Money(100)]) == Money(100)
    assert sum([]) == 0


def test_sum_with_mixed_currencies_rejected():
    with pytest.raises(ValueError):
        sum([Money(100, "UAH"), Money(100, "USD")])


def test_radd_accepts_only_zero():
    m = Money(100)
    assert m.__radd__(0) == m
    assert m.__radd__(0) is not m
    assert m.__radd__(5) is NotImplemented
    assert m.__radd__(True) is NotImplemented
    with pytest.raises(TypeError):
        5 + m


def test_hash_and_set():
    assert hash(Money(100)) == hash(Money(100))
    assert len({Money(100), Money(100), Money(100, "USD")}) == 2


def test_str_and_repr():
    assert str(Money(1250)) == "12.50 UAH"
    assert str(Money(5)) == "0.05 UAH"
    assert str(Money(-320)) == "-3.20 UAH"
    assert str(Money(1000, "usd")) == "10.00 USD"
    assert repr(Money(1250)) == "Money(1250, 'UAH')"


def test_invalid_data_rejected():
    for bad in (1.5, "100", None, True):
        with pytest.raises(ValueError):
            Money(bad)
    for bad in ("", "UA", "UAHH", "U1H", "грн", 5, None):
        with pytest.raises(ValueError):
            Money(100, bad)


def test_operands_unchanged():
    a, b = Money(100), Money(50)
    c = a + b
    d = a * 2
    assert c is not a and d is not a
    assert (a, b) == (Money(100), Money(50))


def test_incompatible_types_give_not_implemented():
    m = Money(100)
    assert m.__add__(5) is NotImplemented
    assert m.__sub__("a") is NotImplemented
    assert m.__mul__("a") is NotImplemented
    assert m.__mul__(m) is NotImplemented
    assert m.__lt__(5) is NotImplemented
    assert m.__eq__(100) is NotImplemented
    with pytest.raises(TypeError):
        m * "a"
