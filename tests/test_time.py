import pytest

from oop_tasks import Time


def test_normalization():
    t = Time(0, 90, 70)
    assert (t.hours, t.minutes, t.seconds) == (1, 31, 10)


def test_str_format():
    assert str(Time()) == "00:00:00"
    assert str(Time(1, 5, 9)) == "01:05:09"
    assert str(Time(25)) == "25:00:00"


def test_add_with_carry():
    assert Time(1, 30, 0) + Time(0, 45, 30) == Time(2, 15, 30)
    assert str(Time(0, 59, 59) + Time(0, 0, 1)) == "01:00:00"


def test_sub():
    assert Time(2, 0, 0) - Time(0, 30, 0) == Time(1, 30, 0)


def test_sub_never_below_zero():
    assert Time(0, 1, 0) - Time(0, 2, 0) == Time()
    assert Time(1) - Time(1) == Time()


def test_comparisons():
    a, b = Time(0, 59, 59), Time(1, 0, 0)
    assert a < b and a <= b and b > a and b >= a
    assert Time(0, 60, 0) == Time(1)
    assert sorted([Time(2), Time(0, 5), Time(1)]) == [Time(0, 5), Time(1), Time(2)]


def test_hash_consistent_with_equality():
    assert hash(Time(1, 0, 0)) == hash(Time(0, 60, 0))
    assert len({Time(1), Time(0, 60), Time(0, 0, 3600)}) == 1


def test_invalid_data_rejected():
    for bad in (-1, 1.5, "1", None, True):
        with pytest.raises(ValueError):
            Time(bad)
        with pytest.raises(ValueError):
            Time(0, bad)
        with pytest.raises(ValueError):
            Time(0, 0, bad)


def test_operands_unchanged():
    a, b = Time(1), Time(0, 30)
    c = a + b
    d = a - b
    assert c is not a and d is not a
    assert (a, b) == (Time(1), Time(0, 30))


def test_incompatible_types_give_not_implemented():
    t = Time(1)
    assert t.__add__(5) is NotImplemented
    assert t.__sub__("a") is NotImplemented
    assert t.__lt__(5) is NotImplemented
    assert t.__eq__(3600) is NotImplemented
    with pytest.raises(TypeError):
        t + 5
    with pytest.raises(TypeError):
        t < 5
    assert (t == 3600) is False


def test_total_seconds_from_seconds_and_repr():
    assert Time(1, 1, 1).total_seconds() == 3661
    assert Time.from_seconds(3661) == Time(1, 1, 1)
    assert repr(Time(1, 30, 0)) == "Time(1, 30, 0)"
