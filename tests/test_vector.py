import pytest

from oop_tasks import Vector


def test_add_and_sub():
    assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)
    assert Vector(5, 5) - Vector(2, 3) == Vector(3, 2)


def test_multiply_by_number_both_sides():
    v = Vector(1, 2)
    assert v * 3 == Vector(3, 6)
    assert 3 * v == Vector(3, 6)
    assert v * 0.5 == Vector(0.5, 1.0)


def test_unary_minus():
    assert -Vector(1, -2) == Vector(-1, 2)


def test_abs():
    assert abs(Vector(3, 4)) == 5
    assert abs(Vector(0, 0)) == 0


def test_zero_boundaries():
    assert Vector(1, 2) * 0 == Vector(0, 0)
    assert Vector(1, 2) + Vector(0, 0) == Vector(1, 2)


def test_dot():
    assert Vector(1, 2).dot(Vector(3, 4)) == 11
    assert Vector(1, 0).dot(Vector(0, 1)) == 0
    with pytest.raises(TypeError):
        Vector(1, 2).dot((3, 4))


def test_operators_return_new_objects_and_keep_operands():
    a, b = Vector(1, 2), Vector(3, 4)
    c = a + b
    d = a * 2
    assert c is not a and c is not b and d is not a
    assert (a, b) == (Vector(1, 2), Vector(3, 4))


def test_equality_and_hash():
    assert Vector(1, 2) == Vector(1, 2)
    assert Vector(1, 2) != Vector(2, 1)
    assert Vector(1, 2) != (1, 2)
    assert hash(Vector(1, 2)) == hash(Vector(1, 2))


def test_incompatible_types_give_not_implemented():
    v = Vector(1, 2)
    assert v.__add__(5) is NotImplemented
    assert v.__sub__("a") is NotImplemented
    assert v.__mul__("a") is NotImplemented
    assert v.__mul__(v) is NotImplemented
    assert v.__eq__((1, 2)) is NotImplemented
    with pytest.raises(TypeError):
        v + 5
    with pytest.raises(TypeError):
        v * v
    with pytest.raises(TypeError):
        "a" * v


def test_str_and_repr():
    assert str(Vector(1, 2)) == "(1, 2)"
    assert repr(Vector(1, 2.5)) == "Vector(1, 2.5)"


def test_invalid_data_rejected():
    for bad in ("a", None, True, float("nan"), float("inf")):
        with pytest.raises(ValueError):
            Vector(bad, 1)
        with pytest.raises(ValueError):
            Vector(1, bad)
