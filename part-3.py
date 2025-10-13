import random
from math import pi


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


print(factorial(5))
print(factorial(50))
print(factorial(random.randint(1, 10)))
print(pi)
