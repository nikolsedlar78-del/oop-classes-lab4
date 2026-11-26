"""Задача 4.4 — клас Matrix."""

from ._validators import is_number, require_number


class Matrix:
    """Незмінна прямокутна матриця чисел."""

    def __init__(self, rows):
        """Створює матрицю зі списку рядків; вона має бути непорожньою та прямокутною."""
        try:
            data = [tuple(row) for row in rows]
        except TypeError:
            raise ValueError("Очікується список рядків") from None
        if not data or not data[0]:
            raise ValueError("Матриця не може бути порожньою")
        width = len(data[0])
        if any(len(row) != width for row in data):
            raise ValueError("Усі рядки мають однакову довжину")
        self._rows = tuple(tuple(require_number(v, "Елемент") for v in row) for row in data)

    @property
    def shape(self):
        """Розмір ``(рядків, стовпців)``."""
        return len(self._rows), len(self._rows[0])

    def __getitem__(self, key):
        """``m[i, j]`` — елемент; ``m[i]`` — рядок (кортеж), тож працює й ``m[i][j]``."""
        if isinstance(key, tuple):
            if len(key) != 2:
                raise TypeError("Очікується m[i, j]")
            i, j = key
            return self._rows[i][j]
        return self._rows[key]

    def __add__(self, other):
        """Сума матриць однакового розміру."""
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.shape != other.shape:
            raise ValueError("Розміри матриць не збігаються")
        return Matrix([[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(self._rows, other._rows)])

    def __mul__(self, other):
        """Множення на число або на матрицю (стовпців лівої = рядків правої)."""
        if is_number(other):
            return Matrix([[v * other for v in row] for row in self._rows])
        if isinstance(other, Matrix):
            if self.shape[1] != other.shape[0]:
                raise ValueError("Кількість стовпців першої матриці має дорівнювати кількості рядків другої")
            cols = list(zip(*other._rows))
            return Matrix([[sum(a * b for a, b in zip(row, col)) for col in cols]
                           for row in self._rows])
        return NotImplemented

    def __rmul__(self, other):
        """Множення на число зліва."""
        if not is_number(other):
            return NotImplemented
        return self.__mul__(other)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        return self._rows == other._rows

    def __hash__(self):
        return hash(self._rows)

    def __str__(self):
        return "\n".join(" ".join(str(v) for v in row) for row in self._rows)

    def __repr__(self):
        return f"Matrix({[list(row) for row in self._rows]!r})"
