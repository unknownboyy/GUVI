fact=[1,1]
for i in range(2,10**5):
    fact.append((i*fact[-1]%(10**9+7)))
def comb(n,r):
    return fact[n]//(fact[r]*fact[n-r])
for target_list in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    c=[0]*(10**6+1)
    for i in s:
        c[i]+=1
    count=1
    i=10**6
    while i>=0 and c[i]==0:
        i-=1
    remain=c[i]
    i-=1
    while i>=0:
        if c[i]>0:
            cn,cr=min(remain,c[i]),max(remain,c[i])
            count*=comb(cr,cn)%(10**9+7)
            remain=cr-cn
        i-=1
    print(count%(10**9+7))
"""
    d=[]
    for i in range(10**6+1):
        if c[i]>0:
            d.append(i)
    d.sort(reverse=True)
    remain=c[d.pop(0)]
    count=1
    for i in d:
        cn,cr=min(remain,c[i]),max(remain,c[i])
        count*=comb(cr,cn)
        remain=cr-cn
    print(count)
"""