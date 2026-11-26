import pytest

from oop_tasks import Bag


def test_missing_item_has_zero_count():
    assert Bag()["a"] == 0


def test_construct_from_iterable():
    b = Bag("abca")
    assert (b["a"], b["b"], b["c"]) == (2, 1, 1)
    assert len(b) == 4


def test_setitem():
    b = Bag()
    b["a"] = 3
    assert b["a"] == 3
    b["a"] = 1
    assert b["a"] == 1


def test_setitem_zero_removes_item():
    b = Bag("aab")
    b["a"] = 0
    assert "a" not in b
    assert b["a"] == 0
    assert len(b) == 1


def test_setitem_invalid_values_rejected():
    b = Bag()
    for bad in (-1, 1.5, "2", None, True):
        with pytest.raises(ValueError):
            b["a"] = bad
    assert len(b) == 0


def test_len_is_sum_of_counts():
    b = Bag()
    b["a"] = 2
    b["b"] = 5
    assert len(b) == 7
    assert bool(Bag()) is False
    assert bool(b) is True


def test_getitem_does_not_add_item():
    b = Bag("a")
    b["zzz"]
    assert "zzz" not in b
    assert len(b) == 1


def test_contains():
    b = Bag("ab")
    assert "a" in b
    assert "z" not in b
    assert [] not in b


def test_iteration_with_repeats():
    assert sorted(Bag("aab")) == ["a", "a", "b"]
    assert len(list(Bag("aabbb"))) == 5
    assert list(Bag()) == []


def test_add_merges_into_new_bag():
    a, b = Bag("aab"), Bag("bcc")
    c = a + b
    assert (c["a"], c["b"], c["c"]) == (2, 2, 2)
    assert c is not a and c is not b
    assert a == Bag("aab") and b == Bag("bcc")


def test_equality_ignores_order():
    assert Bag("aab") == Bag("aba")
    assert Bag("aab") != Bag("ab")
    assert (Bag("a") == ["a"]) is False


def test_bag_is_unhashable():
    with pytest.raises(TypeError):
        hash(Bag())


def test_invalid_constructor_data():
    with pytest.raises(ValueError):
        Bag(5)
    with pytest.raises(ValueError):
        Bag([[1], [2]])


def test_incompatible_types_give_not_implemented():
    b = Bag("a")
    assert b.__add__(["a"]) is NotImplemented
    assert b.__eq__({"a": 1}) is NotImplemented
    with pytest.raises(TypeError):
        b + 5


def test_str_and_repr():
    assert str(Bag("aab")) == "Bag{a: 2, b: 1}"
    assert str(Bag()) == "Bag{}"
    assert repr(Bag("aab")) == "Bag(['a', 'a', 'b'])"
