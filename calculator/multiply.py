from calculator.core import add


def multiply(x, y):
    if x != x or y != y:
        return float("nan")

    z = 0

    for _ in range(abs(x)):
        z = add(z, y)

    if x > 0:
        return z
    else:
        return -z

