"""Задача 4.5 — клас Complex."""

import math

from ._validators import is_number, require_number


class Complex:
    """Незмінне комплексне число; операції працюють і з дійсними числами."""

    def __init__(self, real=0, imag=0):
        """Створює число ``real + imag·i``."""
        self._real = require_number(real, "Дійсна частина")
        self._imag = require_number(imag, "Уявна частина")

    @property
    def real(self):
        """Дійсна частина."""
        return self._real

    @property
    def imag(self):
        """Уявна частина."""
        return self._imag

    @staticmethod
    def _coerce(other):
        if isinstance(other, Complex):
            return other
        if is_number(other):
            return Complex(other, 0)
        return None

    def __add__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return Complex(self._real + o._real, self._imag + o._imag)

    __radd__ = __add__

    def __sub__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return Complex(self._real - o._real, self._imag - o._imag)

    def __rsub__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return o - self

    def __mul__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return Complex(self._real * o._real - self._imag * o._imag,
                       self._real * o._imag + self._imag * o._real)

    __rmul__ = __mul__

    def __abs__(self):
        """Модуль числа."""
        return math.hypot(self._real, self._imag)

    def conjugate(self):
        """Спряжене число."""
        return Complex(self._real, -self._imag)

    def __eq__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return (self._real, self._imag) == (o._real, o._imag)

    def __hash__(self):
        if self._imag == 0:
            return hash(self._real)
        return hash((self._real, self._imag))

    def __str__(self):
        sign = "-" if self._imag < 0 else "+"
        return f"{self._real}{sign}{abs(self._imag)}i"

    def __repr__(self):
        return f"Complex({self._real!r}, {self._imag!r})"
