"""Задача 4.10 — клас Bag (мультимножина)."""

from ._validators import require_int


class Bag:
    """Мультимножина: кожен елемент може траплятися кілька разів."""

    def __init__(self, items=None):
        """Створює мішок із ітерабельного набору хешованих елементів."""
        self._counts = {}
        if items is None:
            return
        try:
            iterator = iter(items)
        except TypeError:
            raise ValueError("Очікується ітерабельний набір елементів") from None
        for item in iterator:
            try:
                self._counts[item] = self._counts.get(item, 0) + 1
            except TypeError:
                raise ValueError("Елементи мають бути хешованими") from None

    def __getitem__(self, item):
        """Кількість елемента (0, якщо його немає). Не додає елемент до мішка."""
        return self._counts.get(item, 0)

    def __setitem__(self, item, count):
        """Задає кількість елемента; 0 видаляє його, від'ємне — ``ValueError``."""
        count = require_int(count, "Кількість")
        if count < 0:
            raise ValueError("Кількість не може бути від'ємною")
        if count == 0:
            self._counts.pop(item, None)
        else:
            self._counts[item] = count

    def __len__(self):
        """Сума кількостей усіх елементів."""
        return sum(self._counts.values())

    def __contains__(self, item):
        try:
            return item in self._counts
        except TypeError:
            return False

    def __iter__(self):
        """Обхід по елементах із повторами."""
        for item, count in self._counts.items():
            for _ in range(count):
                yield item

    def __add__(self, other):
        """Злиття двох мішків у новий."""
        if not isinstance(other, Bag):
            return NotImplemented
        result = Bag()
        result._counts = dict(self._counts)
        for item, count in other._counts.items():
            result._counts[item] = result._counts.get(item, 0) + count
        return result

    def __eq__(self, other):
        if not isinstance(other, Bag):
            return NotImplemented
        return self._counts == other._counts

    __hash__ = None

    def __str__(self):
        if not self._counts:
            return "Bag{}"
        return "Bag{" + ", ".join(f"{k}: {v}" for k, v in self._counts.items()) + "}"

    def __repr__(self):
        return f"Bag({list(self)!r})"
