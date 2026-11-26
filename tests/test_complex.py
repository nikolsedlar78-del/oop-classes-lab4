import pytest

from oop_tasks import Complex


def test_add_sub_mul():
    a, b = Complex(1, 2), Complex(3, 4)
    assert a + b == Complex(4, 6)
    assert b - a == Complex(2, 2)
    assert a * b == Complex(-5, 10)


def test_abs():
    assert abs(Complex(3, 4)) == 5
    assert abs(Complex(0, 0)) == 0


def test_conjugate():
    assert Complex(1, 2).conjugate() == Complex(1, -2)
    assert Complex(3, 4) * Complex(3, 4).conjugate() == 25


def test_operations_with_real_numbers():
    c = Complex(1, 2)
    assert c + 2 == Complex(3, 2)
    assert 2 + c == Complex(3, 2)
    assert c - 2 == Complex(-1, 2)
    assert 2 - c == Complex(1, -2)
    assert c * 2 == Complex(2, 4)
    assert 2 * c == Complex(2, 4)
    assert c + 0.5 == Complex(1.5, 2)


def test_equality_with_real_and_hash():
    assert Complex(2, 0) == 2
    assert Complex(2, 1) != 2
    assert hash(Complex(2, 0)) == hash(2)
    assert hash(Complex(1, 2)) == hash(Complex(1, 2))


def test_imaginary_unit_squared():
    i = Complex(0, 1)
    assert i * i == Complex(-1, 0)
    assert i * i == -1


def test_str_and_repr():
    assert str(Complex(1, 2)) == "1+2i"
    assert str(Complex(1.5, -2)) == "1.5-2i"
    assert str(Complex()) == "0+0i"
    assert repr(Complex(1, 2)) == "Complex(1, 2)"


def test_invalid_data_rejected():
    for bad in ("a", None, True, float("nan")):
        with pytest.raises(ValueError):
            Complex(bad, 0)
        with pytest.raises(ValueError):
            Complex(0, bad)


def test_operands_unchanged():
    a, b = Complex(1, 2), Complex(3, 4)
    c = a * b
    assert c is not a and c is not b
    assert (a, b) == (Complex(1, 2), Complex(3, 4))


def test_incompatible_types_give_not_implemented():
    c = Complex(1, 2)
    assert c.__add__("a") is NotImplemented
    assert c.__sub__(None) is NotImplemented
    assert c.__mul__([1]) is NotImplemented
    assert c.__radd__("a") is NotImplemented
    assert c.__eq__("a") is NotImplemented
    with pytest.raises(TypeError):
        c + "a"
    with pytest.raises(TypeError):
        "a" * c
