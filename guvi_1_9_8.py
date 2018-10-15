def gcd(a,b):
    if b==0:
        return 1
    if a%b==0:
        return b
    return gcd(b,a%b)
n,m=map(int,input().split())
print((n*m)//gcd(n,m))