import pytest

from oop_tasks import Playlist


def make():
    return Playlist(["a", "b", "c"], name="Тест")


def test_len_and_bool():
    assert len(make()) == 3
    assert bool(make()) is True
    assert bool(Playlist()) is False
    assert len(Playlist()) == 0


def test_indexing():
    p = make()
    assert p[0] == "a"
    assert p[-1] == "c"
    with pytest.raises(IndexError):
        p[3]


def test_slicing_returns_new_playlist():
    p = make()
    part = p[1:]
    assert isinstance(part, Playlist)
    assert list(part) == ["b", "c"]
    assert part.name == "Тест"
    assert part is not p
    assert list(p) == ["a", "b", "c"]


def test_empty_slice():
    assert len(make()[5:]) == 0


def test_in_and_for():
    p = make()
    assert "b" in p
    assert "z" not in p
    assert [song for song in p] == ["a", "b", "c"]
    assert list(p) == ["a", "b", "c"]


def test_add_creates_new_playlist():
    a, b = Playlist(["x"], "A"), Playlist(["y", "z"], "B")
    c = a + b
    assert list(c) == ["x", "y", "z"]
    assert c.name == "A"
    assert c is not a and c is not b
    assert list(a) == ["x"] and list(b) == ["y", "z"]


def test_iadd_song_modifies_in_place():
    p = Playlist(["a"])
    same = p
    p += "b"
    assert p is same
    assert list(p) == ["a", "b"]


def test_iadd_playlist_falls_back_to_add():
    a, b = Playlist(["a"]), Playlist(["b"])
    original = a
    a += b
    assert list(a) == ["a", "b"]
    assert a is not original
    assert list(original) == ["a"]


def test_iadd_invalid_values():
    p = Playlist(["a"])
    with pytest.raises(ValueError):
        p += "   "
    with pytest.raises(TypeError):
        p += 5
    assert list(p) == ["a"]


def test_invalid_constructor_data():
    for bad in ("abc", [1], [""], 5):
        with pytest.raises(ValueError):
            Playlist(bad)
    with pytest.raises(ValueError):
        Playlist([], name="  ")


def test_incompatible_types_give_not_implemented():
    p = make()
    assert p.__add__(["a"]) is NotImplemented
    assert p.__iadd__(5) is NotImplemented
    assert p.__eq__(["a", "b", "c"]) is NotImplemented
    with pytest.raises(TypeError):
        p + "x"


def test_equality_and_unhashable():
    assert make() == make()
    assert make() != Playlist(["a"], "Тест")
    with pytest.raises(TypeError):
        hash(make())


def test_str_and_repr():
    assert str(make()) == "Тест: a, b, c"
    assert str(Playlist(name="Порожній")) == "Порожній: порожній"
    assert repr(Playlist(["a"], "X")) == "Playlist(['a'], name='X')"
