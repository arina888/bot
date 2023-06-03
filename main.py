import mpmath
import time

# Нахождение параметра k
def get_k(a, b):
    return mpmath.sqrt((a**2 - b**2)/a**2)

# Вычисление периметра эллипса по формуле Айвори-Бесселя
def ellipse_perimeter_ivory_bessel(a, b):
    t1 = time.time()
    k = get_k(a, b)
    p = 4 * a * mpmath.ellipk(k) if a > b else 4 * b * mpmath.ellipk(k)
    t2 = time.time()
    return p, t2 - t1

# Вычисление периметра эллипса по альтернативной формуле
def ellipse_perimeter_alternative(a, b):
    t1 = time.time()
    k = get_k(a, b)
    p = mpmath.pi * (3*(a + b) - mpmath.sqrt((3*a + b)*(a + 3*b)))
    t2 = time.time()
    return p, t2 - t1

# Вычисление периметра эллипса по формуле Айвори-Бесселя и альтернативной формуле с использованием mpmath
def ellipse_perimeter(a, b, dps):
    mpmath.mp.dps = dps
    return ellipse_perimeter_ivory_bessel(a, b), ellipse_perimeter_alternative(a, b)

a = mpmath.mpf(input("Введите значение полуоси a: "))
b = mpmath.mpf(input("Введите значение полуоси b: "))
dps = int(input("Введите количество знаков после запятой: "))

(p1, t1), (p2, t2) = ellipse_perimeter(a, b, dps)

print(f"Периметр эллипса с полуосями a={a} и b={b} по формуле Айвори-Бесселя: {p1}, время: {t1:.20f} секунд")
print(f"Периметр эллипса с полуосями a={a} и b={b} по альтернативной формуле: {p2}, время: {t2:.20f} секунд")