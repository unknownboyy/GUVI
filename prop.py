def solve(l,n,cc):
    if len(l)==0:   return cc
    p=l[0]
    for i in range(1,len(l)):
        p=p^l[i]
    if p==n:
        return cc
    dd=n
    ll=l.copy()
    for i in ll:
        l.remove(i)
        dd=min(dd,solve(l,n,cc+1))
        l.append(i)
    return dd
for _ in range(int(input())):
    n=int(input())
    l=[(i+1) for i in range(n)]
    dd=n
    for i in range(n):
        l.remove(i+1)
        dd=min(dd,solve(l,n,1))
        l.append(i+1)
    print(dd)