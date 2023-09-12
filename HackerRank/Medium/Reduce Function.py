from fractions import Fraction
from functools import reduce
from math import gcd
"""
 the Fraction class handles all the necessary arithmetic
 operations for fractions, including addition, subtraction,
 multiplication, and division, and it automatically simplifies
 the result to its simplest form.
 """
def mult(fracs):
    result = 1 # Fraction(1,1) = 1/1, Fraction is a class .
    for c in fracs:
        result*=c
    return result

def product(fracs):
    x = mult(fracs)
    return x.numerator, x.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)