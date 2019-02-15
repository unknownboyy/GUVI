<<<<<<< HEAD
# Code for ratios of items
from fractions import Fraction
x = int(input())
y = int(input())
z = int(input())
F = Fraction(y-z,z-x)
print(F.numerator,F.denominator,sep=':')
=======
from functools import reduce
for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    prod = reduce((lambda x,y:x*y),s)
    ss=s.copy()
    for i in range(n):
        ss[i]=prod//ss[i]
    print(*ss) 
>>>>>>> 33f4cd762d4e4b8b825025741676af85251a142b
