"""Спільні функції перевірки значень. Некоректні дані — ``ValueError``."""

import math


def is_number(value):
    """``True`` для ``int``/``float`` (але не ``bool``) — для перевірки операндів."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def require_number(value, name="Значення"):
    """Повертає ``value``, якщо це скінченне число, інакше ``ValueError``."""
    if not is_number(value) or not math.isfinite(value):
        raise ValueError(f"{name} має бути скінченним числом")
    return value


def require_int(value, name="Значення"):
    """Повертає ``value``, якщо це ціле число (не ``bool``), інакше ``ValueError``."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} має бути цілим числом")
    return value


def require_text(value, name="Значення"):
    """Повертає рядок без пробілів по краях; порожній або не-рядок — ``ValueError``."""
    if not isinstance(value, str):
        raise ValueError(f"{name} має бути рядком")
    value = value.strip()
    if not value:
        raise ValueError(f"{name} не може бути порожнім")
    return value


def format_number(value):
    """Показує ``2.0`` як ``2``, решту чисел — як є."""
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value
