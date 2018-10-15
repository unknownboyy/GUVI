def gcd(a,b):
    if b==0 or a%b==0:
        return b
    return gcd(b,a%b)
n,m=map(int,input().split())
print(gcd(n,m))