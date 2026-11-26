"""Задача 4.9 — клас Money."""

from decimal import Decimal, ROUND_HALF_UP
from functools import total_ordering

from ._validators import is_number, require_int


@total_ordering
class Money:
    """Сума в копійках із валютою. Арифметика — лише в межах однієї валюти."""

    def __init__(self, kopecks, currency="UAH"):
        """Створює суму: ``kopecks`` — ціле, ``currency`` — три латинські літери."""
        self._kopecks = require_int(kopecks, "Сума")
        if not isinstance(currency, str):
            raise ValueError("Валюта має бути рядком")
        currency = currency.strip()
        if len(currency) != 3 or not (currency.isascii() and currency.isalpha()):
            raise ValueError("Валюта — три латинські літери, напр. UAH")
        self._currency = currency.upper()

    @property
    def kopecks(self):
        """Сума в копійках."""
        return self._kopecks

    @property
    def currency(self):
        """Код валюти."""
        return self._currency

    def _same_currency(self, other):
        if self._currency != other._currency:
            raise ValueError(f"Різні валюти: {self._currency} і {other._currency}")

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._same_currency(other)
        return Money(self._kopecks + other._kopecks, self._currency)

    def __radd__(self, other):
        """Підтримка ``sum()``: ``0 + Money`` повертає копію ``Money``."""
        if isinstance(other, int) and not isinstance(other, bool) and other == 0:
            return Money(self._kopecks, self._currency)
        return NotImplemented

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._same_currency(other)
        return Money(self._kopecks - other._kopecks, self._currency)

    def __mul__(self, factor):
        """Множення на число з округленням до копійки (half-up)."""
        if not is_number(factor):
            return NotImplemented
        value = (Decimal(self._kopecks) * Decimal(str(factor))).quantize(
            Decimal(1), rounding=ROUND_HALF_UP)
        return Money(int(value), self._currency)

    __rmul__ = __mul__

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return (self._kopecks, self._currency) == (other._kopecks, other._currency)

    def __lt__(self, other):
        """Менше; порівняння різних валют — ``ValueError``."""
        if not isinstance(other, Money):
            return NotImplemented
        self._same_currency(other)
        return self._kopecks < other._kopecks

    def __hash__(self):
        return hash((self._kopecks, self._currency))

    def __bool__(self):
        """``True``, якщо сума ненульова."""
        return self._kopecks != 0

    def __str__(self):
        sign = "-" if self._kopecks < 0 else ""
        whole, cents = divmod(abs(self._kopecks), 100)
        return f"{sign}{whole}.{cents:02d} {self._currency}"

    def __repr__(self):
        return f"Money({self._kopecks}, {self._currency!r})"
