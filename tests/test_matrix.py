import pytest

from oop_tasks import Matrix


def test_creation_and_shape():
    m = Matrix([[1, 2, 3], [4, 5, 6]])
    assert m.shape == (2, 3)


def test_getitem_with_tuple_and_chained():
    m = Matrix([[1, 2], [3, 4]])
    assert m[0, 1] == 2
    assert m[1][0] == 3
    assert m[-1, -1] == 4


def test_add():
    a, b = Matrix([[1, 2], [3, 4]]), Matrix([[10, 20], [30, 40]])
    assert a + b == Matrix([[11, 22], [33, 44]])


def test_add_shape_mismatch_rejected():
    with pytest.raises(ValueError):
        Matrix([[1, 2]]) + Matrix([[1], [2]])


def test_multiply_by_number_both_sides():
    m = Matrix([[1, 2], [3, 4]])
    assert m * 2 == Matrix([[2, 4], [6, 8]])
    assert 2 * m == Matrix([[2, 4], [6, 8]])
    assert m * 0 == Matrix([[0, 0], [0, 0]])


def test_matrix_product():
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    assert a * b == Matrix([[19, 22], [43, 50]])
    c = Matrix([[1, 2, 3], [4, 5, 6]])
    d = Matrix([[1, 0], [0, 1], [1, 1]])
    assert (c * d).shape == (2, 2)
    assert c * d == Matrix([[4, 5], [10, 11]])


def test_product_shape_mismatch_rejected():
    with pytest.raises(ValueError):
        Matrix([[1, 2, 3]]) * Matrix([[1, 2, 3]])


def test_equality_and_hash():
    assert Matrix([[1, 2]]) == Matrix([[1, 2]])
    assert Matrix([[1, 2]]) != Matrix([[2, 1]])
    assert hash(Matrix([[1, 2]])) == hash(Matrix([[1, 2]]))


def test_str_and_repr():
    m = Matrix([[1, 2], [3, 4]])
    assert str(m) == "1 2\n3 4"
    assert repr(m) == "Matrix([[1, 2], [3, 4]])"


def test_invalid_data_rejected():
    for bad in ([], [[]], [[1, 2], [3]], [["a"]], [[True]], "abc", 5, None):
        with pytest.raises(ValueError):
            Matrix(bad)


def test_bad_indices():
    m = Matrix([[1, 2], [3, 4]])
    with pytest.raises(IndexError):
        m[5, 0]
    with pytest.raises(TypeError):
        m[0, 1, 2]


def test_operands_unchanged():
    a, b = Matrix([[1, 2]]), Matrix([[3, 4]])
    c = a + b
    d = a * 2
    assert c is not a and d is not a
    assert a == Matrix([[1, 2]]) and b == Matrix([[3, 4]])


def test_incompatible_types_give_not_implemented():
    m = Matrix([[1]])
    assert m.__add__(5) is NotImplemented
    assert m.__mul__("a") is NotImplemented
    assert m.__rmul__("a") is NotImplemented
    assert m.__eq__([[1]]) is NotImplemented
    with pytest.raises(TypeError):
        m + 5
