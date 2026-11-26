"""Демонстрація роботи всіх десяти класів лабораторної 4."""

from oop_tasks import (Vector, Fraction, Time, Matrix, Complex,
                       Polynomial, Playlist, Version, Money, Bag)


def header(title):
    print(f"\n=== {title} ===")


def attempt(label, action):
    """Виконує дію й показує результат або помилку."""
    try:
        result = action()
    except (ValueError, TypeError, ZeroDivisionError) as error:
        print(f"  ✗ {label}: {type(error).__name__}: {error}")
    else:
        print(f"  ✓ {label} = {result}")


def demo_vector():
    header("4.1 Vector")
    a, b, c = Vector(1, 2), Vector(3, 4), Vector(0, 0)
    print("a + b =", a + b, "| b - a =", b - a, "| -a =", -a)
    print("a * 3 =", a * 3, "| 3 * a =", 3 * a, "| |b| =", abs(b), "| a·b =", a.dot(b))
    print("Операнди не змінились:", a, b, c, "| repr:", repr(a))
    attempt("a + 5", lambda: a + 5)
    attempt("a * b", lambda: a * b)


def demo_fraction():
    header("4.2 Fraction")
    a, b, c = Fraction(1, 2), Fraction(1, 3), Fraction(6, -8)
    print("c = 6/-8 скорочено:", c)
    print("a + b =", a + b, "| a - b =", a - b, "| a * b =", a * b, "| a / b =", a / b)
    print("a > b:", a > b, "| float(b) =", float(b), "| 1 - a =", 1 - a)
    print("sorted:", [str(f) for f in sorted([a, b, c])])
    attempt("Fraction(1, 0)", lambda: Fraction(1, 0))
    attempt("a / Fraction(0)", lambda: a / Fraction(0))


def demo_time():
    header("4.3 Time")
    t1, t2, t3 = Time(1, 30), Time(0, 45, 30), Time(0, 90, 70)
    print("t3 = Time(0, 90, 70) нормалізується:", t3)
    print("t1 + t2 =", t1 + t2, "| t1 - t2 =", t1 - t2, "| t2 - t1 (не нижче 0) =", t2 - t1)
    print("sorted:", [str(t) for t in sorted([t1, t2, t3])], "| t3 == Time(1, 31, 10):",
          t3 == Time(1, 31, 10))
    attempt("Time(-1)", lambda: Time(-1))
    attempt("t1 + 5", lambda: t1 + 5)


def demo_matrix():
    header("4.4 Matrix")
    a, b = Matrix([[1, 2], [3, 4]]), Matrix([[5, 6], [7, 8]])
    print("a[0, 1] =", a[0, 1], "| a[1][0] =", a[1][0])
    print("a + b:\n" + str(a + b))
    print("a * 2:\n" + str(a * 2))
    print("a * b:\n" + str(a * b))
    attempt("a + Matrix([[1]])", lambda: a + Matrix([[1]]))
    attempt("Matrix([[1, 2], [3]])", lambda: Matrix([[1, 2], [3]]))


def demo_complex():
    header("4.5 Complex")
    a, b = Complex(1, 2), Complex(3, 4)
    print("a + b =", a + b, "| a - b =", a - b, "| a * b =", a * b)
    print("|b| =", abs(b), "| conj(b) =", b.conjugate(), "| b * conj(b) =", b * b.conjugate())
    print("a + 2 =", a + 2, "| 2 + a =", 2 + a, "| Complex(2, 0) == 2:", Complex(2, 0) == 2)
    attempt("a + 'x'", lambda: a + "x")


def demo_polynomial():
    header("4.6 Polynomial")
    p, q = Polynomial([1, 0, 2]), Polynomial([1, 1])
    print("p =", p, "| степінь:", p.degree, "| p(3) =", p(3))
    print("q =", q, "| p + q =", p + q, "| p * q =", p * q)
    print("(1+x)(1-x) =", Polynomial([1, 1]) * Polynomial([1, -1]))
    attempt("Polynomial([])", lambda: Polynomial([]))


def demo_playlist():
    header("4.7 Playlist")
    p1 = Playlist(["Song A", "Song B", "Song C"], "Ранок")
    p2 = Playlist(["Song D"], "Вечір")
    print(p1, "| довжина:", len(p1), "| p1[0] =", p1[0], "| p1[1:] =", list(p1[1:]))
    print("'Song B' in p1:", "Song B" in p1, "| bool(Playlist()):", bool(Playlist()))
    merged = p1 + p2
    print("p1 + p2:", merged, "| p1 не змінився:", len(p1))
    p2 += "Song E"
    print("p2 після += :", p2)
    for i, song in enumerate(merged, 1):
        print(f"  {i}. {song}")
    attempt("p1 + 'x'", lambda: p1 + "x")


def demo_version():
    header("4.8 Version")
    vs = [Version("1.10.0"), Version("1.2.9"), Version("1.2.10"), Version("1.2")]
    print("sorted:", [str(v) for v in sorted(vs)])
    print("1.2.10 > 1.2.9:", Version("1.2.10") > Version("1.2.9"),
          "| 1.2 == 1.2.0:", Version("1.2") == Version("1.2.0"),
          "| max:", max(vs))
    print("У множині:", len({Version("1.2"), Version("1.2.0")}), "елемент")
    attempt("Version('1..2')", lambda: Version("1..2"))


def demo_money():
    header("4.9 Money")
    a, b, usd = Money(1250), Money(300), Money(1000, "usd")
    print("a =", a, "| b =", b, "| usd =", usd)
    print("a + b =", a + b, "| a - b =", a - b, "| a * 1.5 =", a * 1.5, "| 2 * b =", 2 * b)
    print("sum([a, b, a]) =", sum([a, b, a]), "| sum([]) =", sum([]))
    print("a > b:", a > b, "| bool(Money(0)):", bool(Money(0)))
    attempt("a + usd", lambda: a + usd)
    attempt("a < usd", lambda: a < usd)


def demo_bag():
    header("4.10 Bag")
    a, b = Bag("abracadabra"), Bag(["x", "x", "y"])
    print(a, "| len =", len(a), "| a['a'] =", a["a"], "| a['z'] =", a["z"])
    a["z"] = 3
    print("Після a['z'] = 3:", a["z"], "| 'z' in a:", "z" in a)
    a["z"] = 0
    print("Після a['z'] = 0:", "z" in a)
    merged = a + b
    print("a + b:", merged, "| len =", len(merged), "| a не змінився:", len(a))
    print("Обхід b:", list(b), "| Bag('aab') == Bag('aba'):", Bag("aab") == Bag("aba"))
    attempt("a['a'] = -1", lambda: a.__setitem__("a", -1))


if __name__ == "__main__":
    for demo in (demo_vector, demo_fraction, demo_time, demo_matrix, demo_complex,
                 demo_polynomial, demo_playlist, demo_version, demo_money, demo_bag):
        demo()
