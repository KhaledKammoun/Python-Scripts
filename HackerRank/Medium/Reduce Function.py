from fractions import Fraction
from functools import reduce


def mult(fracs):
    x, y = 1, 1
    for c in fracs:
        x *= c.numerator
        y *= c.denominator
    maxVal = max(x, y)
    for i in range((maxVal // 2) + 1, 0, -1):
        if x % i == 0 and y % i == 0:
            return Fraction(x // i, y // i)
    return Fraction(x, y)

def product(fracs):
    x = mult(fracs)
    return x.numerator, x.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)