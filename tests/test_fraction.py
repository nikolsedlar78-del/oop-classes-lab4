import pytest

from oop_tasks import Fraction


def test_automatic_reduction():
    f = Fraction(2, 4)
    assert (f.numerator, f.denominator) == (1, 2)


def test_sign_moves_to_numerator():
    assert (Fraction(1, -2).numerator, Fraction(1, -2).denominator) == (-1, 2)
    assert Fraction(-3, -6) == Fraction(1, 2)


def test_zero_fraction():
    f = Fraction(0, 5)
    assert (f.numerator, f.denominator) == (0, 1)


def test_zero_denominator_rejected():
    with pytest.raises(ValueError):
        Fraction(1, 0)


def test_non_integer_arguments_rejected():
    for bad in (1.5, "1", None, True):
        with pytest.raises(ValueError):
            Fraction(bad, 2)
        with pytest.raises(ValueError):
            Fraction(1, bad)


def test_arithmetic():
    a, b = Fraction(1, 2), Fraction(1, 3)
    assert a + b == Fraction(5, 6)
    assert a - b == Fraction(1, 6)
    assert a * b == Fraction(1, 6)
    assert a / b == Fraction(3, 2)


def test_division_by_zero_fraction():
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 2) / Fraction(0)
    with pytest.raises(ZeroDivisionError):
        1 / Fraction(0)


def test_comparisons():
    a, b = Fraction(1, 3), Fraction(1, 2)
    assert a < b and a <= b and b > a and b >= a
    assert Fraction(1, 2) <= Fraction(2, 4) and Fraction(1, 2) >= Fraction(2, 4)
    assert sorted([Fraction(1, 2), Fraction(1, 3), Fraction(-1, 4)]) == [
        Fraction(-1, 4), Fraction(1, 3), Fraction(1, 2)]


def test_float_conversion():
    assert float(Fraction(1, 4)) == 0.25
    assert float(Fraction(-1, 2)) == -0.5


def test_integer_interoperability():
    assert Fraction(1, 2) + 1 == Fraction(3, 2)
    assert 1 + Fraction(1, 2) == Fraction(3, 2)
    assert 1 - Fraction(1, 4) == Fraction(3, 4)
    assert 3 * Fraction(1, 3) == 1
    assert 2 / Fraction(1, 2) == Fraction(4)


def test_operands_unchanged():
    a, b = Fraction(1, 2), Fraction(1, 3)
    c = a + b
    assert c is not a and c is not b
    assert (a, b) == (Fraction(1, 2), Fraction(1, 3))


def test_incompatible_types_give_not_implemented():
    f = Fraction(1, 2)
    assert f.__add__(0.5) is NotImplemented
    assert f.__mul__("a") is NotImplemented
    assert f.__lt__("a") is NotImplemented
    assert f.__eq__(0.5) is NotImplemented
    with pytest.raises(TypeError):
        f + 0.5
    with pytest.raises(TypeError):
        f < "a"
    assert (f == 0.5) is False


def test_hash_consistent_with_equality():
    assert hash(Fraction(1, 2)) == hash(Fraction(2, 4))
    assert hash(Fraction(3)) == hash(3)
    assert len({Fraction(1, 2), Fraction(2, 4)}) == 1


def test_str_and_repr():
    assert str(Fraction(1, 2)) == "1/2"
    assert str(Fraction(6, 3)) == "2"
    assert repr(Fraction(1, 2)) == "Fraction(1, 2)"
