def func(s,k):
    d=dict()
    for i in range(k):
        if s[i] in d:
            return True
        else:
            d[s[i]]=1
    for i in range(k,n):
        if s[i] in d:
            return True
        else:
            d[s[i]]=1
        del d[s[i-k]]
    return False
for _ in range(int(input())) :
    k,n=map(int,input().split())
    s=list(map(int,input().split()))
    print(func(s,k))
