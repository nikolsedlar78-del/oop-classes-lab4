"""Задача 4.2 — клас Fraction."""

import math
from functools import total_ordering

from ._validators import require_int


@total_ordering
class Fraction:
    """Звичайний дріб, що завжди зберігається скороченим (знаменник > 0).

    Операції працюють з іншими ``Fraction`` та цілими числами.
    """

    def __init__(self, numerator, denominator=1):
        """Створює дріб; знаменник не може бути нулем."""
        numerator = require_int(numerator, "Чисельник")
        denominator = require_int(denominator, "Знаменник")
        if denominator == 0:
            raise ValueError("Знаменник не може дорівнювати нулю")
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        g = math.gcd(numerator, denominator)
        self._num = numerator // g
        self._den = denominator // g

    @property
    def numerator(self):
        """Чисельник скороченого дробу."""
        return self._num

    @property
    def denominator(self):
        """Знаменник скороченого дробу (> 0)."""
        return self._den

    @staticmethod
    def _coerce(other):
        if isinstance(other, Fraction):
            return other
        if isinstance(other, int) and not isinstance(other, bool):
            return Fraction(other)
        return None

    def __add__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return Fraction(self._num * o._den + o._num * self._den, self._den * o._den)

    __radd__ = __add__

    def __sub__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return Fraction(self._num * o._den - o._num * self._den, self._den * o._den)

    def __rsub__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return o - self

    def __mul__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return Fraction(self._num * o._num, self._den * o._den)

    __rmul__ = __mul__

    def __truediv__(self, other):
        """Ділення; ділення на нуль — ``ZeroDivisionError``."""
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        if o._num == 0:
            raise ZeroDivisionError("Ділення на нульовий дріб")
        return Fraction(self._num * o._den, self._den * o._num)

    def __rtruediv__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return o / self

    def __neg__(self):
        return Fraction(-self._num, self._den)

    def __abs__(self):
        return Fraction(abs(self._num), self._den)

    def __eq__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return (self._num, self._den) == (o._num, o._den)

    def __lt__(self, other):
        """Менше; решту порівнянь дає ``total_ordering``."""
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return self._num * o._den < o._num * self._den

    def __float__(self):
        return self._num / self._den

    def __hash__(self):
        if self._den == 1:
            return hash(self._num)
        return hash((self._num, self._den))

    def __str__(self):
        if self._den == 1:
            return str(self._num)
        return f"{self._num}/{self._den}"

    def __repr__(self):
        return f"Fraction({self._num}, {self._den})"
