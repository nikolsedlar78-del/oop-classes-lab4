"""Задача 4.8 — клас Version."""

import re
from functools import total_ordering


@total_ordering
class Version:
    """Версія виду ``"1.2.10"``; порівнюється за числовими компонентами.

    Кінцеві нулі не враховуються: ``1.2 == 1.2.0``.
    """

    _PATTERN = re.compile(r"\d+(\.\d+)*")

    def __init__(self, text):
        """Створює версію з рядка; некоректний формат — ``ValueError``."""
        if not isinstance(text, str):
            raise ValueError("Версія має бути рядком")
        text = text.strip()
        if not self._PATTERN.fullmatch(text):
            raise ValueError("Формат версії: числа через крапку, напр. 1.2.10")
        self._text = text
        self._parts = tuple(int(p) for p in text.split("."))
        key = list(self._parts)
        while len(key) > 1 and key[-1] == 0:
            key.pop()
        self._key = tuple(key)

    @property
    def parts(self):
        """Числові компоненти версії."""
        return self._parts

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._key == other._key

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._key < other._key

    def __hash__(self):
        return hash(self._key)

    def __str__(self):
        return self._text

    def __repr__(self):
        return f"Version({self._text!r})"
