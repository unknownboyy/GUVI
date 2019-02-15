from fractions import Fraction
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
        other=Fraction(1,1)
        while m>0:
            if n>k and m>1:
                if n%k==0:
                    n=k
                else:
                    n=n%k
            else:
                if f is None:
                    f = other*Fraction(1,n)
                else:
                    f = f + other*Fraction(1,n)
                other = Fraction(f.denominator-f.numerator,f.denominator)
                n+=k
            m-=1
        print(generatesol(f.numerator,f.denominator))