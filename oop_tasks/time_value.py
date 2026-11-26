"""Задача 4.3 — клас Time."""

from functools import total_ordering

from ._validators import require_int


@total_ordering
class Time:
    """Проміжок часу в годинах, хвилинах і секундах (нормалізується)."""

    def __init__(self, hours=0, minutes=0, seconds=0):
        """Створює час; значення — невід'ємні цілі, надлишок переноситься (90 хв → 1 год 30 хв)."""
        total = 0
        for value, name, factor in ((hours, "Години", 3600), (minutes, "Хвилини", 60),
                                    (seconds, "Секунди", 1)):
            value = require_int(value, name)
            if value < 0:
                raise ValueError(f"{name} не можуть бути від'ємними")
            total += value * factor
        self._total = total

    @classmethod
    def from_seconds(cls, total):
        """Створює час із загальної кількості секунд."""
        return cls(0, 0, total)

    @property
    def hours(self):
        """Години (можуть перевищувати 23)."""
        return self._total // 3600

    @property
    def minutes(self):
        """Хвилини (0–59)."""
        return self._total % 3600 // 60

    @property
    def seconds(self):
        """Секунди (0–59)."""
        return self._total % 60

    def total_seconds(self):
        """Загальна кількість секунд."""
        return self._total

    def __add__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return Time.from_seconds(self._total + other._total)

    def __sub__(self, other):
        """Різниця; результат не нижчий за 00:00:00."""
        if not isinstance(other, Time):
            return NotImplemented
        return Time.from_seconds(max(0, self._total - other._total))

    def __eq__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return self._total == other._total

    def __lt__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return self._total < other._total

    def __hash__(self):
        return hash(self._total)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __repr__(self):
        return f"Time({self.hours}, {self.minutes}, {self.seconds})"
