for _ in range(int(input())):
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b=map(int,input().split())
        x.append(a)
        y.append(b)
    k = list(map(int,input().split()))
    k.sort()
    dist = [0]*n
    for i in range(n):
        for j in range(n):
            dist[i]+=abs(x[i]-x[j])+abs(y[i]-y[j])
    dist.sort(reverse=True)
    count = 0
    for i in range(n):
        count+=k[i]*dist[i]
    print(count)