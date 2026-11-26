import pytest

from oop_tasks import Version


def test_numeric_comparison():
    assert Version("1.2.10") > Version("1.2.9")
    assert Version("1.10") > Version("1.9")
    assert Version("2.0") > Version("1.99.99")


def test_sorted():
    raw = ["1.10.0", "1.2.0", "1.9.5", "1.2.10"]
    assert [str(v) for v in sorted(Version(s) for s in raw)] == [
        "1.2.0", "1.2.10", "1.9.5", "1.10.0"]


def test_trailing_zeros_equal_and_hash():
    assert Version("1.2") == Version("1.2.0")
    assert hash(Version("1.2")) == hash(Version("1.2.0"))
    assert len({Version("1.2"), Version("1.2.0"), Version("1.2.0.0")}) == 1


def test_prefix_is_smaller():
    assert Version("1.0") < Version("1.0.1")
    assert Version("1") < Version("1.0.1")


def test_comparison_operators():
    a, b = Version("1.0.0"), Version("1.0.1")
    assert a < b and a <= b and b > a and b >= a and a != b
    assert Version("1.0") <= Version("1.0.0") and Version("1.0") >= Version("1.0.0")


def test_min_max():
    versions = [Version("1.2"), Version("1.10"), Version("1.9")]
    assert str(max(versions)) == "1.10"
    assert str(min(versions)) == "1.2"


def test_str_repr_and_parts():
    v = Version("  1.2.10 ")
    assert str(v) == "1.2.10"
    assert repr(v) == "Version('1.2.10')"
    assert v.parts == (1, 2, 10)


def test_single_component():
    assert Version("3").parts == (3,)
    assert Version("3") < Version("3.1")


def test_invalid_data_rejected():
    for bad in ("", " ", "1..2", "1.", ".1", "1.a", "v1.2", "-1", "1.2-beta", None, 5, 1.2):
        with pytest.raises(ValueError):
            Version(bad)


def test_incompatible_types_give_not_implemented():
    v = Version("1.2")
    assert v.__eq__("1.2") is NotImplemented
    assert v.__lt__("1.3") is NotImplemented
    assert (v == "1.2") is False
    with pytest.raises(TypeError):
        v < "1.3"
