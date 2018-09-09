def factorial(n):
    if n==0 or n==1:    return 1
    return n*factorial(n-1)
def comb(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k))
def bino(n,k,p):
    return comb(n,k)*(p**k)*((1-p)**(n-k))
p,n=map(int,input().split())
p=p*0.01
ans=0
for i in range(3):
    ans+=bino(n,i,p)
print(round(ans,3))
ans=0
for i in range(2,11):
    ans+=bino(n,i,p)
print(round(ans,3))