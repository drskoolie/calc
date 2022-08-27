from calculator.core import add, sub
from calculator.divide import divide
from calculator.multiply import multiply

def quotient(x, y):
    # x - (x//y * y) 
    return sub(x, multiply(divide(x,y), y))
