from calculator.core import add, sub

def divide(x, y):
    z = 0
    flag_not_done = True
    x_pos = abs(x)
    y_pos = abs(y)

    while 1:
        if x_pos >= y_pos:
            x_pos = sub(x_pos, y_pos)
            z = add(z, 1)
        else:
            break

    if x > 0 and y > 0:
        return z
    elif x < 0 and y < 0:
        return z
    elif x > 0 and y < 0:
        return -z
    elif x < 0 and y > 0:
        return -z
