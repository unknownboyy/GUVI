for _ in range(int(input())) :
    n,m,k,l=map(int,input().split())
    s=list(map(int,input().split()))
    s.sort()
    wait=10**15+1
    for i in range(n):
        if s[i]<=k:
            wait=min(wait,(m+i+1)*l-s[i])
    print(min(wait,(m+n+1)*l-k)) 