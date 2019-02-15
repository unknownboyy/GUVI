from fractions import Fraction
from math import ceil
def power(x, y, m):	
	if (y == 0) : 
		return 1
	p = power(x, y // 2, m) % m 
	p = (p * p) % m 
	if(y % 2 == 0) : 
		return p 
	else : 
		return ((x * p) % m) 
def gcd(a, b): 
	if (a == 0):
		return b
	return gcd(b % a, a)
def generatesol(x,y):
    q = power(y,10**9+5,10**9+7)
    return (x*q)%(10**9+7)
for _ in range(int(input())):
    n,k,m=map(int,input().split())
    f = None
    if m==1:
        print(generatesol(1,n))
    else:
        if m%2==1:
            mpower = ceil(m/2)
            q = pow(n,mpower,10**9+7)
            p = q - pow(n-1,mpower,10**9+7)
            print(generatesol(p,q))
        else:
            mpower = m//2
            q = pow(n,mpower,10**9+7)
            p = q - pow(n-1,mpower,10**9+7)
            f1 = Fraction(p,q)
            f2 = Fraction(pow(n-1,mpower,10**9+7),pow(n,mpower,10**9+7)*(n+k))
            f = f1+f2
            print(generatesol(f.numerator,f.denominator))