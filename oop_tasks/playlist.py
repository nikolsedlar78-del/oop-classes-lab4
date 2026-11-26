"""Задача 4.7 — клас Playlist."""

from ._validators import require_text


class Playlist:
    """Плейлист: впорядкований список назв пісень."""

    def __init__(self, songs=None, name="Без назви"):
        """Створює плейлист із назвою та (необов'язково) списком пісень."""
        self._name = require_text(name, "Назва плейлиста")
        if isinstance(songs, (str, bytes)):
            raise ValueError("Пісні мають бути списком рядків, а не одним рядком")
        try:
            self._songs = [require_text(s, "Назва пісні") for s in (songs or [])]
        except TypeError:
            raise ValueError("Пісні мають бути послідовністю рядків") from None

    @property
    def name(self):
        """Назва плейлиста."""
        return self._name

    def __len__(self):
        return len(self._songs)

    def __bool__(self):
        """``False`` для порожнього плейлиста."""
        return bool(self._songs)

    def __getitem__(self, index):
        """``p[i]`` — пісня; ``p[a:b]`` — новий плейлист зі зрізу."""
        result = self._songs[index]
        if isinstance(index, slice):
            return Playlist(result, self._name)
        return result

    def __contains__(self, song):
        return song in self._songs

    def __iter__(self):
        return iter(self._songs)

    def __add__(self, other):
        """Об'єднання двох плейлистів у новий (назва — з лівого)."""
        if not isinstance(other, Playlist):
            return NotImplemented
        return Playlist(self._songs + other._songs, self._name)

    def __iadd__(self, other):
        """``p += "пісня"`` додає пісню в цей самий плейлист."""
        if isinstance(other, str):
            self._songs.append(require_text(other, "Назва пісні"))
            return self
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        return (self._name, self._songs) == (other._name, other._songs)

    __hash__ = None

    def __str__(self):
        body = ", ".join(self._songs) if self._songs else "порожній"
        return f"{self._name}: {body}"

    def __repr__(self):
        return f"Playlist({self._songs!r}, name={self._name!r})"
