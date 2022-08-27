from calculator.core import add, sub

def multiply(x, y):
    z = 0

    for _ in range(abs(x)):
        z = add(z, y)

    if x > 0:
        return z
    else:
        return -z

