# This is an example of higher order function using the calculator program


def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, func):
    return func(n1, n2)


result = calculator(5, 7, add)
print(result)