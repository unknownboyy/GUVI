# Code for ratios of items
from fractions import Fraction
x = int(input())
y = int(input())
z = int(input())
F = Fraction(y-z,z-x)
print(F.numerator,F.denominator,sep=':')