# Лабораторна 4 — ООП у Python: перевантаження операторів і контейнерні методи

Десять класів, демонстрація та тести на `pytest`.

## Структура

```
oop-classes-lab4/
├── oop_tasks/
│   ├── _validators.py     # спільні перевірки → ValueError
│   ├── vector.py          # 4.1  Vector     — + - * (зліва/справа), -v, abs, ==, dot()
│   ├── fraction.py        # 4.2  Fraction   — скорочення, + - * /, total_ordering, float()
│   ├── time_value.py      # 4.3  Time       — нормалізація, + -, порівняння, hash, ГГ:ХХ:СС
│   ├── matrix.py          # 4.4  Matrix     — + * , m[i, j], ==, перевірка розмірів
│   ├── complex_number.py  # 4.5  Complex    — + - *, abs, conjugate, операції з дійсними
│   ├── polynomial.py      # 4.6  Polynomial — + *, __call__, str "1 + 2x^2", degree
│   ├── playlist.py        # 4.7  Playlist   — len, [i] і зрізи, in, for, bool, +, +=
│   ├── version.py         # 4.8  Version    — числове порівняння, hash, sorted()
│   ├── money.py           # 4.9  Money      — одна валюта, * число, sum() через __radd__
│   └── bag.py             # 4.10 Bag        — мультимножина: [], len, in, +, ==, обхід
├── tests/                 # по одному файлу на клас
├── demo.py
├── pytest.ini
└── .gitignore
```

## Запуск

```bash
pip install pytest
python demo.py
python -m pytest -v
```

## Рішення, які варто знати

- Оператори повертають нові об'єкти й не змінюють операндів. Виняток — `Playlist.__iadd__`,
  який за завданням додає пісню в той самий плейлист.
- Несумісний тип операнда → `return NotImplemented`, тому Python сам кидає `TypeError`.
- Некоректні дані в `__init__` → `ValueError`. Ділення на нульовий `Fraction` → `ZeroDivisionError`.
- Класи з `__eq__` мають узгоджений `__hash__` (`Fraction(3)` має той самий hash, що й `3`).
  Змінні `Playlist` і `Bag` — нехешовані (`__hash__ = None`).
- `Fraction`, `Complex`, `Polynomial` працюють також із числами: `Fraction(1, 2) + 1`, `2 * Complex(1, 2)`.
  `Fraction` приймає лише цілі, `Complex` і `Polynomial` — `int` та `float`.
- `Version`: кінцеві нулі не враховуються, тому `1.2 == 1.2.0`.
- `Money`: порівняння різних валют через `<`/`>` → `ValueError`, а `==` дає `False`.
  Множення на дробове число округлюється до копійки (half-up). `sum([])` повертає `0`.
- `Matrix` — незмінна; `m[i]` повертає рядок-кортеж, тож працює і `m[i][j]`, і `m[i, j]`.
- `Time`: години не обмежуються 23 (`Time(25)` → `25:00:00`); різниця не нижча за `00:00:00`.
- `Polynomial`: степінь нульового многочлена вважається 0.
