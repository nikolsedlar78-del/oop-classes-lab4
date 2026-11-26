"""Задача 4.1 — клас Vector (2D)."""

import math

from ._validators import is_number, require_number


class Vector:
    """Незмінний двовимірний вектор."""

    def __init__(self, x, y):
        """Створює вектор із двох скінченних чисел."""
        self._x = require_number(x, "x")
        self._y = require_number(y, "y")

    @property
    def x(self):
        """Координата x."""
        return self._x

    @property
    def y(self):
        """Координата y."""
        return self._y

    def __add__(self, other):
        """Сума векторів (новий об'єкт)."""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        """Різниця векторів (новий об'єкт)."""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self._x - other._x, self._y - other._y)

    def __mul__(self, k):
        """Множення на число: ``v * k``."""
        if not is_number(k):
            return NotImplemented
        return Vector(self._x * k, self._y * k)

    def __rmul__(self, k):
        """Множення на число зліва: ``k * v``."""
        return self.__mul__(k)

    def __neg__(self):
        """Протилежний вектор."""
        return Vector(-self._x, -self._y)

    def __abs__(self):
        """Довжина вектора."""
        return math.hypot(self._x, self._y)

    def dot(self, other):
        """Скалярний добуток із іншим вектором."""
        if not isinstance(other, Vector):
            raise TypeError("dot() приймає лише Vector")
        return self._x * other._x + self._y * other._y

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self._x, self._y) == (other._x, other._y)

    def __hash__(self):
        return hash((self._x, self._y))

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return f"Vector({self._x!r}, {self._y!r})"
