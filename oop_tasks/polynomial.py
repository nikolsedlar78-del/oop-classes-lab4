"""Задача 4.6 — клас Polynomial."""

from itertools import zip_longest

from ._validators import format_number, is_number, require_number


class Polynomial:
    """Незмінний многочлен; коефіцієнти задаються від a₀ (``[1, 0, 2]`` → ``1 + 2x^2``)."""

    def __init__(self, coefficients):
        """Створює многочлен; старші нульові коефіцієнти відкидаються."""
        try:
            coeffs = list(coefficients)
        except TypeError:
            raise ValueError("Очікується послідовність коефіцієнтів") from None
        if not coeffs:
            raise ValueError("Потрібен щонайменше один коефіцієнт")
        coeffs = [require_number(c, "Коефіцієнт") for c in coeffs]
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        self._coeffs = tuple(coeffs)

    @property
    def coefficients(self):
        """Коефіцієнти від a₀ (кортеж)."""
        return self._coeffs

    @property
    def degree(self):
        """Степінь многочлена (для нульового — 0)."""
        return len(self._coeffs) - 1

    @staticmethod
    def _coerce(other):
        if isinstance(other, Polynomial):
            return other
        if is_number(other):
            return Polynomial([other])
        return None

    def __add__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return Polynomial([a + b for a, b in zip_longest(self._coeffs, o._coeffs, fillvalue=0)])

    __radd__ = __add__

    def __mul__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        result = [0] * (len(self._coeffs) + len(o._coeffs) - 1)
        for i, a in enumerate(self._coeffs):
            for j, b in enumerate(o._coeffs):
                result[i + j] += a * b
        return Polynomial(result)

    __rmul__ = __mul__

    def __call__(self, x):
        """Значення многочлена в точці ``x`` (схема Горнера)."""
        x = require_number(x, "x")
        result = 0
        for c in reversed(self._coeffs):
            result = result * x + c
        return result

    def __eq__(self, other):
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return self._coeffs == o._coeffs

    def __hash__(self):
        if len(self._coeffs) == 1:
            return hash(self._coeffs[0])
        return hash(self._coeffs)

    def __str__(self):
        terms = []
        for power, c in enumerate(self._coeffs):
            if c == 0:
                continue
            magnitude = format_number(abs(c))
            if power == 0:
                body = str(magnitude)
            else:
                coef = "" if magnitude == 1 else str(magnitude)
                body = f"{coef}x" if power == 1 else f"{coef}x^{power}"
            terms.append((c < 0, body))
        if not terms:
            return "0"
        text = ("-" if terms[0][0] else "") + terms[0][1]
        for negative, body in terms[1:]:
            text += (" - " if negative else " + ") + body
        return text

    def __repr__(self):
        return f"Polynomial({list(self._coeffs)!r})"
