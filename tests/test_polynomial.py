import pytest

from oop_tasks import Polynomial


def test_str_examples():
    assert str(Polynomial([1, 0, 2])) == "1 + 2x^2"
    assert str(Polynomial([0, 1])) == "x"
    assert str(Polynomial([0, -1, 3])) == "-x + 3x^2"
    assert str(Polynomial([1, -2])) == "1 - 2x"
    assert str(Polynomial([0, 0, -1])) == "-x^2"
    assert str(Polynomial([2.0, 1.5])) == "2 + 1.5x"


def test_constant_and_zero_polynomials():
    assert str(Polynomial([5])) == "5"
    assert str(Polynomial([0])) == "0"
    assert Polynomial([0]).degree == 0


def test_degree_and_trailing_zeros_stripped():
    assert Polynomial([1, 2, 3]).degree == 2
    p = Polynomial([1, 2, 0, 0])
    assert p.degree == 1
    assert p.coefficients == (1, 2)


def test_call():
    p = Polynomial([1, 0, 2])
    assert p(3) == 19
    assert p(0) == 1
    assert p(-1) == 3
    assert p(0.5) == 1.5


def test_add():
    assert Polynomial([1, 2]) + Polynomial([3, 0, 4]) == Polynomial([4, 2, 4])


def test_add_can_cancel_leading_terms():
    assert (Polynomial([1, 2, 3]) + Polynomial([0, 0, -3])).degree == 1


def test_mul():
    assert Polynomial([1, 1]) * Polynomial([1, 1]) == Polynomial([1, 2, 1])
    assert (Polynomial([1, 1]) * Polynomial([1, -1])).coefficients == (1, 0, -1)
    assert (Polynomial([1, 1]) * Polynomial([0])).coefficients == (0,)


def test_operations_with_numbers():
    p = Polynomial([1, 2])
    assert p + 1 == Polynomial([2, 2])
    assert 1 + p == Polynomial([2, 2])
    assert 2 * p == Polynomial([2, 4])
    assert p * 3 == Polynomial([3, 6])


def test_equality_and_hash():
    assert Polynomial([1, 2]) == Polynomial([1, 2, 0])
    assert Polynomial([5]) == 5
    assert hash(Polynomial([5])) == hash(5)
    assert hash(Polynomial([1, 2])) == hash(Polynomial([1, 2, 0]))


def test_invalid_data_rejected():
    for bad in ([], ["a"], None, "12", [True], [1, float("nan")]):
        with pytest.raises(ValueError):
            Polynomial(bad)
    with pytest.raises(ValueError):
        Polynomial([1])("a")


def test_operands_unchanged():
    a, b = Polynomial([1, 2]), Polynomial([3, 4])
    c = a * b
    d = a + b
    assert c is not a and d is not a
    assert a.coefficients == (1, 2) and b.coefficients == (3, 4)


def test_incompatible_types_give_not_implemented():
    p = Polynomial([1, 2])
    assert p.__add__("a") is NotImplemented
    assert p.__mul__([1]) is NotImplemented
    assert p.__eq__("a") is NotImplemented
    with pytest.raises(TypeError):
        p + "a"


def test_repr():
    assert repr(Polynomial([1, 0, 2])) == "Polynomial([1, 0, 2])"
